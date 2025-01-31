$("document").ready(function(){



//On Hover to zoom img
$("#zoom-03").elevateZoom({
  constrainType: "height",
  zoomType: "lens",
  zoomWindowWidth: 300,
  zoomWindowHeight: 300,
  containLensZoom: true,
  gallery: 'thumbnail-gall',
  cursor: 'pointer',
  galleryActiveClass: "active"

});

// Zoom gallery Carousel
$('#thumbnail-gall').owlCarousel({
  items: 4,
  nav: true,
  dots: false,
  navText: ['<i class="fas fa-angle-double-left"></i>',
      '<i class="fas fa-angle-double-right"></i>'
  ],
  loop: false,
  margin: 0,
  autoplay: false,
  responsive: {
      0: {

          items: 2,

      },

      450: {
          items: 3,
      },

      768: {
          items: 4,
      }
  }
});



});


$("document").ready(function () {


    

  // OwlCarousel
  $(".carouser-slider").owlCarousel({
    nav: true,
    dots: true,
    loop: true,
    autoplay: false,
    navText: [
      '<i class="fas fa-arrow-left"></i>',
      '<i class="fas fa-arrow-right"></i>',
    ],
    responsive: {
      0: {
        items: 1,
      },
    },
  });

  // OwlCarousel
  $(".").owlCarousel({
    nav: true,
    dots: true,
    loop: true,
    autoplay: true,
    responsive: {
      0: {
        items: 1,
      },
      575: {
        items: 2,
      },

      768: {
        items: 2,
      },

      992: {
        items: 1,
      },
    },
  });

  // end carosel




});


