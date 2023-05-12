// Hamburger responsive navbar

$(".menu-toggle").click(function () {
  $(".site-nav").toggleClass("site-nav--open", 500);
  $(this).toggleClass("open");
});
