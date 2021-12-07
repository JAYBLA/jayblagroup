// ==================================================
// Project Name  :  Printem - HTML5 Template
// File          :  JS Base
// Version       :  1.0.0
// Last change   :  05 Octobar 2020
// Author        :  BDevs (https://themeforest.net/user/bdevs)
// Developer:    :  Rakibul Islam Dewan
// ==================================================


(function($) {
    "use strict";
  
  
    // back to top - start
    // --------------------------------------------------
    $(window).scroll(function() {
      if ($(this).scrollTop() > 200) {
        $('#backtotop:hidden').stop(true, true).fadeIn();
      } else {
        $('#backtotop').stop(true, true).fadeOut();
      }
    });
    $(function() {
      $("#scroll").on('click', function() {
        $("html,body").animate({
          scrollTop: $("#thetop").offset().top
        }, "slow");
        return false
      })
    });
    // back to top - end
    // --------------------------------------------------
  
  
    // preloader - start
    // --------------------------------------------------
    $(window).on('load', function() {
      $('.preloader').addClass('loaded');
      if ($('.preloader').hasClass('loaded')) {
        $('.spinner').delay(1000).queue(function () {
          $(this).remove();
        });
      }
    });
    // preloader - end
    // --------------------------------------------------
  
  

  
    // background image - start
    // --------------------------------------------------
    $('[data-background]').each(function() {
      $(this).css('background-image', 'url('+ $(this).attr('data-background') + ')');
    });
    // background image - end
    // --------------------------------------------------
  
  

  
  
    // sidebar mobile menu - start
    // --------------------------------------------------
    $(document).ready(function () {
      $('.close_btn, .overlay').on('click', function () {
        $('.sidebar_mobile_menu').removeClass('active');
        $('.overlay').removeClass('active');
      });
  
      $('.mobile_menu_btn').on('click', function () {
        $('.sidebar_mobile_menu').addClass('active');
        $('.overlay').addClass('active');
      });
    });
  
    // 3rd level dropdown menu
    $('.dropdown > a').addClass('dropdown-toggle');
    $('.dropdown-menu .dropdown > a').on('click', function(e) {
      if (!$(this).next().hasClass('show')) {
        $(this).parents('.dropdown-menu').first().find('.show').removeClass("show");
      }
      var $subMenu = $(this).next(".dropdown-menu");
      $subMenu.toggleClass('show');
      $(this).parents('li.dropdown.show').on('.dropdown', function(e) {
        $('.dropdown-menu > .dropdown .show').removeClass("show");
      });
      $('.dropdown-menu li a.dropdown-toggle').removeClass("show_dropdown");
      if ($(this).next().hasClass('show')) {
        $(this).addClass("show_dropdown");
      }
      return false;
    });
    // sidebar mobile menu - end
    // --------------------------------------------------
  
  
    // sticky header - start
    // --------------------------------------------------
    $(window).on('scroll', function () {
      if ($(this).scrollTop() > 120) {
        $('.sticky_header').addClass("stuck")
      } else {
        $('.sticky_header').removeClass("stuck")
      }
    });
    // sticky header - end
    // --------------------------------------------------
  
    
    // masonry layout - start
    // --------------------------------------------------
    var $grid = $('.grid').imagesLoaded( function() {
      $grid.masonry({
        itemSelector: '.grid-item',
        percentPosition: true,
        columnWidth: '.grid-sizer'
      }); 
    });
    // masonry layout - end
    // --------------------------------------------------

  
  
    // columns of carousel - start
    // --------------------------------------------------
    $('.main_slider').owlCarousel({
      items:1,
      margin:0,
      nav:false,
      loop:true,
      dots:true,
      autoplay:true,
      smartSpeed:1000,
      autoplayTimeout:6000
      // autoplayHoverPause:true,
    });
    // columns of carousel - end
    // -------------------------------------------------- 


    // parallax - start
    // --------------------------------------------------
    if ($('.scene').length > 0 ) {
      $('.scene').parallax({
        scalarX: 10.0,
        scalarY: 10.0,
      }); 
    }
    // parallax - end
    // --------------------------------------------------
  
  
    // wow animation - start
    // --------------------------------------------------
    function wowAnimation() {
      new WOW({
        offset: 100,
        mobile: true
      }).init()
    }
    wowAnimation();
    // wow animation - end
    // --------------------------------------------------
  })(jQuery);