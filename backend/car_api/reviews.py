import json, requests

from .models import YouTubeModel, ExternalReviewsModel, YouTubePlaylistsModel, YouTubeVideosModel
from googleapiclient.discovery import build

def gis_reviews() -> dict:
    '''
    Получение информации по 2GIS
    ERROR: может падать в длительный таймаут или возвращать биты json

    :param id:
    :param api_key:
    :return:
    '''
    two_gis_obj = ExternalReviewsModel.objects.get(title='2GIS')
    id = two_gis_obj.company_id
    api_key = two_gis_obj.api_id

    url = f"https://public-api.reviews.2gis.com/2.0/branches/{id}/reviews?fields=meta.branch_rating,meta.branch_reviews_count&rated=false&key={api_key}"
    response = json.loads(
        requests.get(url).text
    )

    return {
        "rating": response["meta"]["branch_rating"],
        "count": response["meta"]["branch_reviews_count"],
    }

def vl_reviews() -> dict:
    '''
    :param id:
    :return:
    '''
    vl_obj = ExternalReviewsModel.objects.get(title='VL.RU')
    id = vl_obj.company_id

    url = f"https://www.vl.ru/ajax/company-history-votes?companyId={id}"
    response = json.loads(
        requests.get(url).text
    )
    rating = [response["history"][i] for i in response["history"].keys()][0]

    url = f"https://www.vl.ru/commentsgate/ajax/thread/company/batarejka25rus/embedded"
    response = requests.get(
        url,
        headers={
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "Referer": "https://www.vl.ru/batarejka25rus"
        }
    ).text
    count = json.loads(response)["total"]

    return {
        "rating": rating,
        "count": count,
    }

def get_playlists(channel_id: str="UCpNF-TmeXabe8FX3v26i36g", max_results: int=5, youtube=None) -> dict:
    '''
    Получение плейлистов канала
    :param channel_id:
    :param max_results:
    :return:
    '''
    request = youtube.playlists().list(part="snippet", channelId=channel_id, maxResults=max_results)
    response = request.execute()

    return {
        item["snippet"]["title"] : item["id"] for item in response["items"]
    }


def get_video_from_playlist(playlist_id: str, max_results: int=5, youtube=None) -> dict:
    '''
    Получение информацию о видео по плейлисту
    :param playlist_id:
    :param max_results:
    :return:
    '''
    request = youtube.playlistItems().list(part="snippet", playlistId=playlist_id, maxResults=max_results)
    response = json.loads(
        json.dumps(
            request.execute()
        )
    )

    return {
        item["snippet"]["resourceId"]["videoId"] : {
            "publish_date": item["snippet"]["publishedAt"],
            "title": item["snippet"]["title"],
            "cover_url": "/".join(
                item["snippet"]["thumbnails"]["default"]["url"].split("/")[:-1]
            ) + "/"
        }
        for item in response["items"]
        if item["snippet"]["title"] != "Private video"
    }

def parse_youtube():
    yt_obj = YouTubeModel.objects.get(id=1)
    api_key = yt_obj.api_key
    channel_id = yt_obj.channel_id

    youtube = build("youtube", "v3", developerKey=api_key)

    for name, playlist_id in get_playlists(channel_id=channel_id, youtube=youtube).items():
        if name == 'Курс по Нейросетям':
            continue
        yt_play_obj, _ = YouTubePlaylistsModel.objects.get_or_create(name=name, playlist_id=playlist_id)

        for video_id, value in get_video_from_playlist(playlist_id=playlist_id, youtube=youtube).items():
            video, _ = YouTubeVideosModel.objects.get_or_create(title=value.get('title'),
                                                        video_id=video_id,
                                                        cover_url=value.get('cover_url'))
            if video not in yt_play_obj.videos.all():
                yt_play_obj.videos.add(video)

        yt_play_obj.save()
