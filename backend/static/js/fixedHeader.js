const navbar = $("#fixed-navbar");
const offsetTopNavbar = navbar.offset().top;
const header = $(".header");

$(window).scroll(function () {
  if ($(window).scrollTop() > offsetTopNavbar) {
    navbar.addClass("fixed");
    header.css('margin-bottom', '93px');
  } else {
    navbar.removeClass("fixed");
    header.css('margin-bottom', '16px');
  }
});