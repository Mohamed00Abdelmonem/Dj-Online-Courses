/***************************************************
==================== JS INDEX ======================
****************************************************
01. PreLoader Js


****************************************************/

(function ($) {
  "use strict";

  var windowOn = $(window);
  ////////////////////////////////////////////////////
  // 01. PreLoader Js
  windowOn.on("load", function () {
    $("#loading").fadeOut(500);
  });

  ////////////////////////////////////////////////////
  // 02. Mobile Menu Js
  $("#mobile-menu").meanmenu({
    meanMenuContainer: ".mobile-menu",
    meanScreenWidth: "1199",
    meanExpand: ['<i class="fal fa-plus"></i>'],
  });

  ////////////////////////////////////////////////////
  // 03. Sidebar Js
  $(".tp-menu-toggle").on("click", function () {
    $(".tp-sidebar-menu").addClass("sidebar-opened");
    $(".body-overlay").addClass("opened");
  });
  $(".sidebar-close").on("click", function () {
    $(".tp-sidebar-menu").removeClass("sidebar-opened");
    $(".body-overlay").removeClass("opened");
  });
  $(".body-overlay").on("click", function () {
    $(".tp-sidebar-menu").removeClass("sidebar-opened");
  });

  ////////////////////////////////////////////////////
  // 04. Body overlay Js
  $(".body-overlay").on("click", function () {
    $(".offcanvas__area").removeClass("opened");
    $(".body-overlay").removeClass("opened");
  });

  ////////////////////////////////////////////////////
  // 05. Search Js
  $(".search-toggle").on("click", function () {
    $(".search__area").addClass("opened");
  });
  $(".search-close-btn").on("click", function () {
    $(".search__area").removeClass("opened");
  });

  ////////////////////////////////////////////////////
  // 06. Sticky Header Js
  windowOn.on("scroll", function () {
    var scroll = $(window).scrollTop();
    if (scroll < 100) {
      $("#header-sticky,#header-mob-sticky").removeClass("header-sticky");
    } else {
      $("#header-sticky,#header-mob-sticky").addClass("header-sticky");
    }
  });

  ////////////////////////////////////////////////////
  // 07. Data CSS Js
  $("[data-background").each(function () {
    $(this).css(
      "background-image",
      "url( " + $(this).attr("data-background") + "  )"
    );
  });

  $("[data-width]").each(function () {
    $(this).css("width", $(this).attr("data-width"));
  });

  $("[data-bg-color]").each(function () {
    $(this).css("background-color", $(this).attr("data-bg-color"));
  });

  ////////////////////////////////////////////////////
  // 08. Nice Select Js
  $("select").niceSelect();

  // mainSlider
  function mainSlider() {
    var BasicSlider = $(".slider-active");
    BasicSlider.on("init", function (e, slick) {
      var $firstAnimatingElements = $(".single-slider:first-child").find(
        "[data-animation]"
      );
      doAnimations($firstAnimatingElements);
    });
    BasicSlider.on(
      "beforeChange",
      function (e, slick, currentSlide, nextSlide) {
        var $animatingElements = $(
          '.single-slider[data-slick-index="' + nextSlide + '"]'
        ).find("[data-animation]");
        doAnimations($animatingElements);
      }
    );
    BasicSlider.slick({
      autoplay: false,
      autoplaySpeed: 4000,
      dots: false,
      fade: true,
      arrows: true,
      slidesToShow: 1,
      slidesToScroll: 1,
      prevArrow:
        '<button type="button" class="slick-prev"><i class="fi fi-ss-angle-left"></i></button>',
      nextArrow:
        '<button type="button" class="slick-next"><i class="fi fi-ss-angle-right"></i></button>',
      responsive: [
        {
          breakpoint: 767,
          settings: {
            dots: false,
            arrows: true,
          },
        },
      ],
    });

    function doAnimations(elements) {
      var animationEndEvents =
        "webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend";
      elements.each(function () {
        var $this = $(this);
        var $animationDelay = $this.data("delay");
        var $animationType = "animated " + $this.data("animation");
        $this.css({
          "animation-delay": $animationDelay,
          "-webkit-animation-delay": $animationDelay,
        });
        $this.addClass($animationType).one(animationEndEvents, function () {
          $this.removeClass($animationType);
        });
      });
    }
  }
  mainSlider();

  ////////////////////////////////////////////////////
  // 09. brand-active

  $(".tp-brand-active").slick({
    dots: false,
    infinite: true,
    autoplaySpeed: 2000,
    slidesToShow: 5,
    slidesToScroll: 1,
    autoplay: true,
    arrows: false,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1,
          infinite: true,
        },
      },
      {
        breakpoint: 600,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1,
        },
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        },
      },
    ],
  });

  ////////////////////////////////////////////////////
  // 10. testimonial-active
  $(".testimonial-active").slick({
    infinite: true,
    slidesToShow: 3,
    slidesToScroll: 1,
    prevArrow:
      '<button type="button" class="slick-prev"><i class="arrow_carrot-left"></i></button>',
    nextArrow:
      '<button type="button" class="slick-next"><i class="arrow_carrot-right"></i></button>',
    arrows: true,
    appendArrows: $(".tp-section-arrow"),
    dots: false,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2,
        },
      },
      {
        breakpoint: 992,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 2,
        },
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        },
      },
      {
        breakpoint: 576,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        },
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        },
      },
    ],
  });

  ////////////////////////////////////////////////////
  // 10. testimonial-active

  $(".testimonial--active").slick({
    infinite: true,
    slidesToShow: 2,
    slidesToScroll: 1,
    prevArrow:
      '<button type="button" class="slick-prev"><i class="arrow_carrot-left"></i></button>',
    nextArrow:
      '<button type="button" class="slick-next"><i class="arrow_carrot-right"></i></button>',
    arrows: true,
    appendArrows: $(".tp-section-arrow"),
    dots: false,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2,
        },
      },
      {
        breakpoint: 992,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 2,
        },
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        },
      },
      {
        breakpoint: 576,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        },
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        },
      },
    ],
  });

  $(".testimonial-active-box").slick({
    infinite: true,
    autoplay: true,
    slidesToShow: 2,
    slidesToScroll: 1,
    prevArrow:
      '<button type="button" class="slick-prev"><i class="arrow_carrot-left"></i></button>',
    nextArrow:
      '<button type="button" class="slick-next"><i class="arrow_carrot-right"></i></button>',
    arrows: false,
    appendArrows: $(".tp-section-arrow"),
    dots: false,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2,
        },
      },
      {
        breakpoint: 992,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 2,
        },
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        },
      },
      {
        breakpoint: 576,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        },
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        },
      },
    ],
  });

  ////////////////////////////////////////////////////
  // 11. instructor-active

  $(".intruc-active").slick({
    infinite: true,
    slidesToShow: 3,
    slidesToScroll: 1,
    prevArrow:
      '<button type="button" class="slick-prev"><i class="arrow_carrot-left"></i></button>',
    nextArrow:
      '<button type="button" class="slick-next"><i class="arrow_carrot-right"></i></button>',
    arrows: true,
    appendArrows: $(".tp-instruc-arrow"),
    dots: false,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3,
        },
      },
      {
        breakpoint: 992,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2,
        },
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        },
      },
      {
        breakpoint: 576,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        },
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        },
      },
    ],
  });

  $(".intruc-active-two").slick({
    infinite: true,
    slidesToShow: 3,
    slidesToScroll: 1,
    prevArrow:
      '<button type="button" class="slick-prev"><i class="arrow_carrot-left"></i></button>',
    nextArrow:
      '<button type="button" class="slick-next"><i class="arrow_carrot-right"></i></button>',
    arrows: false,
    appendArrows: $(".tp-instruc-arrow"),
    dots: false,
    autoplay: true,
    responsive: [
      {
        breakpoint: 1024,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3,
        },
      },
      {
        breakpoint: 992,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2,
        },
      },
      {
        breakpoint: 480,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        },
      },
      {
        breakpoint: 576,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        },
      },
      {
        breakpoint: 768,
        settings: {
          slidesToShow: 1,
          slidesToScroll: 1,
        },
      },
    ],
  });

  ////////////////////////////////////////////////////
  // 12. Masonary Js
  $(".grid").imagesLoaded(function () {
    // init Isotope
    var $grid = $(".grid").isotope({
      itemSelector: ".grid-item",
      percentPosition: true,
      masonry: {
        // use outer width of grid-sizer for columnWidth
        columnWidth: ".grid-item",
      },
    });

    // filter items on button click
    $(".masonary-menu").on("click", "button", function () {
      var filterValue = $(this).attr("data-filter");
      $grid.isotope({ filter: filterValue });
    });

    //for menu active class
    $(".masonary-menu button").on("click", function (event) {
      $(this).siblings(".active").removeClass("active");
      $(this).addClass("active");
      event.preventDefault();
    });
  });

  /* magnificPopup img view */
  $(".popup-image").magnificPopup({
    type: "image",
    gallery: {
      enabled: true,
    },
  });

  /* magnificPopup video view */
  $(".popup-video").magnificPopup({
    type: "iframe",
  });

  ////////////////////////////////////////////////////
  // 13. Wow Js
  new WOW().init();

  ////////////////////////////////////////////////////
  // 14. Cart Quantity Js
  $(".cart-minus").click(function () {
    var $input = $(this).parent().find("input");
    var count = parseInt($input.val()) - 1;
    count = count < 1 ? 1 : count;
    $input.val(count);
    $input.change();
    return false;
  });
  $(".cart-plus").click(function () {
    var $input = $(this).parent().find("input");
    $input.val(parseInt($input.val()) + 1);
    $input.change();
    return false;
  });

  ////////////////////////////////////////////////////
  // 15. Show Login Toggle Js
  $("#showlogin").on("click", function () {
    $("#checkout-login").slideToggle(900);
  });

  ////////////////////////////////////////////////////
  // 16. Show Coupon Toggle Js
  $("#showcoupon").on("click", function () {
    $("#checkout_coupon").slideToggle(900);
  });

  ////////////////////////////////////////////////////
  // 17. Create An Account Toggle Js
  $("#cbox").on("click", function () {
    $("#cbox_info").slideToggle(900);
  });

  ////////////////////////////////////////////////////
  // 18. Shipping Box Toggle Js
  $("#ship-box").on("click", function () {
    $("#ship-box-info").slideToggle(1000);
  });

  ////////////////////////////////////////////////////
  // 19. Counter Js
  $(".counter").counterUp({
    delay: 10,
    time: 1000,
  });

  ////////////////////////////////////////////////////
  // 20. Parallax Js
  if ($(".scene").length > 0) {
    $(".scene").parallax({
      scalarX: 10.0,
      scalarY: 15.0,
    });
  }

  ////////////////////////////////////////////////////
  // 21. InHover Active Js
  $(".hover__active").on("mouseenter", function () {
    $(this)
      .addClass("active")
      .parent()
      .siblings()
      .find(".hover__active")
      .removeClass("active");
  });

  ////////////////////////////////////////////////////
  // 22. Blog Active Js

  $(".blog-item-active").slick({
    infinite: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    prevArrow:
      '<button type="button" class="slick-prev"><i class="fi fi-rr-arrow-small-left"></i></button>',
    nextArrow:
      '<button type="button" class="slick-next"><i class="fi fi-rr-arrow-small-right"></i></button>',
    arrows: true,
  });
})(jQuery);
