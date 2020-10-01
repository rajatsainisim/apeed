
(function($) {

   'use strict'

    $(document).ready(function()
  {

   $(window).scroll(function(){
        if($(window).scrollTop() > $(window).height()){
              $(".myheader").css({"background-color":"white"});
        }
        else{
            
             $(".myheader").css({"background-color":"transparent"});
        }

    })
  });

  var num = 200; //number of pixels before modifying styles

$(window).bind('scroll', function () {
    if ($(window).scrollTop() > num) {
        $('.myheader').addClass('sticky');
    } else {
        $('.myheader').removeClass('sticky');
    }
});


 //HamBurger
  var forEach=function(t,o,r){if("[object Object]"===Object.prototype.toString.call(t))for(var c in t)Object.prototype.hasOwnProperty.call(t,c)&&o.call(r,t[c],c,t);else for(var e=0,l=t.length;l>e;e++)o.call(r,t[e],e,t)};
  var hamburgers = document.querySelectorAll(".hamburger");
  if (hamburgers.length > 0) {
    forEach(hamburgers, function(hamburger) {
      hamburger.addEventListener("click", function() {
        this.classList.toggle("is-active");
      }, false);
    });
  }

  $('.navbar-toggler').click(function(){
    $('#navbarNav').toggleClass('menu-show');
    $(this).toggleClass('collapsed');
    $('body').toggleClass('menu-open');
  });

/*------------------------------------------------------------------------------*/
/* TopSearch
/*------------------------------------------------------------------------------*/

    
    jQuery( ".ttm-header-search-link a" ).addClass('sclose');   
    
    jQuery( ".ttm-header-search-link a" ).on('click', function(event ) {  
  
        jQuery(".field.searchform-s").focus();  
        
        if (jQuery('.ttm-header-search-link a').hasClass('sclose')) {   
            jQuery( ".ttm-header-search-link a i" ).removeClass('ti-search').addClass('ti-close');
            jQuery(this).removeClass('sclose').addClass('open');    
            jQuery(".ttm-search-overlay").addClass('st-show');                  
        } else {
            jQuery(this).removeClass('open').addClass('sclose');
            jQuery( ".ttm-header-search-link a i" ).removeClass('ti-close').addClass('ti-search');  
            jQuery(".ttm-search-overlay").removeClass('st-show');   
        }   
        event.preventDefault(); 
    });


/*------------------------------------------------------------------------------*/
/* Fixed-header
/*------------------------------------------------------------------------------*/


$(window).scroll(function(){
    if ( matchMedia( 'only screen and (min-width: 1200px)' ).matches ) 
    {
        if ($(window).scrollTop() >= 50 ) {
            $('.ttm-stickable-header').addClass('fixed-header');
            $('.ttm-stickable-header').addClass('visible-title');
        }
        else {

            $('.ttm-stickable-header').removeClass('fixed-header');
            $('ttm-stickable-header').removeClass('visible-title');
            }
    }
});


/*------------------------------------------------------------------------------*/
/* Menu
/*------------------------------------------------------------------------------*/

    $('ul li:has(ul)').addClass('has-submenu');
    $('ul li ul').addClass('sub-menu');


    $("ul.dropdown li").on({

        mouseover: function(){
           $(this).addClass("hover");
        },  
        mouseout: function(){
           $(this).removeClass("hover");
        }, 

    });
    
    var $menu = $('#menu'), $menulink = $('#menu-toggle-form'), $menuTrigger = $('.has-submenu > a');
    $menulink.on('click',function (e) {

        $menulink.toggleClass('active');
        $menu.toggleClass('active');
    });

    $menuTrigger.on('click',function (e) {
        e.preventDefault();
        var t = $(this);
        t.toggleClass('active').next('ul').toggleClass('active');
    });

    $('ul li:has(ul)');

   

/*------------------------------------------------------------------------------*/
/* owlCarousel
/*------------------------------------------------------------------------------*/
// ===== 6-Portfolio-slide ==== 

$(".portfolio-slide").owlCarousel({ 
    margin: 0,
    loop:true,
    nav: $('.portfolio-slide').data('nav'),
    dots: $('.portfolio-slide').data('dots'),                     
    autoplay: $('.portfolio-slide').data('auto'),
    smartSpeed: 3000,
    responsive:{
        0:{
            items:1
        },
        576:{
            items:2
        },
        991:{
            items:2
        },
         1024:{
            items:3
        },
           1200 : {
                    items :3
                },
                1500 : {
                    items : 4
                }
    }    
});
    /*====================================
            Slider Active JS
        ======================================*/ 
        $('.slider-active').owlCarousel({
            autoplay:true,
            autoplayTimeout:3500,
            autoplayHoverPause:true,
            items:1,
            smartSpeed: 600,
            loop:true,
            merge:true,
            touchDrag  : false,
            mouseDrag  : false,
            nav:true,
            dots:true,
           responsive:{
                300: {
                    nav:false,
                },
                768: {
                    nav:false,
                },
                1170: {
                    nav:true,
                },
            }
        });
        
// =====7- Testimonial slide ==== 

    $(".testimonial-slide2").owlCarousel({  
        loop:true,
        margin:10,
        smartSpeed: 1000,
        nav: false,
        dots:true,
        autoplay: true,
        items:3,
        dotsEach: true ,
        responsive:{
            0:{
                items:1,
            },
            576:{
                items:1,
            },
            768:{
                items:2,
            },
            991:{
                items:2,
            },
            1368:{
                items: 3
            }
        }


    });

 $(".employee-carousel").owlCarousel({  
        loop:true,
        margin:10,
        mouseDrag: false,
        touchDrag: false,
        nav: false,
        dots:false,
        autoplay: true,
        items:1,
        autoplayHoverPause: true,
        animateOut: 'slideOutUp',
        animateIn: 'slideInUp',
        dotsEach: false ,
      

    });
/*------------**** match height----------------------------------------------*/
//Match title height
var matchHeight = function () {
    
    function init() {
        eventListeners();
        matchHeight();
    }
    
    function eventListeners(){
        $(window).on('resize', function() {
            matchHeight();
        });
    }
    
    function matchHeight(){
        var groupName = $('[data-match-height]');
        var groupHeights = [];
        
        groupName.css('min-height', 'auto');
        
        groupName.each(function() {
            groupHeights.push($(this).outerHeight());
        });
        
        var maxHeight = Math.max.apply(null, groupHeights);
        groupName.css('min-height', maxHeight);
    };
    
    return {
        init: init
    };
    
} ();
jQuery(window).load(function($){
  matchHeight.init();
});


/*------------------------------------------------------------------------------*/
/* Back to top
/*------------------------------------------------------------------------------*/

// ===== Scroll to Top ==== 
jQuery('#totop').hide();
jQuery(window).scroll(function() {
    "use strict";
    if (jQuery(this).scrollTop() >= 100) {        // If page is scrolled more than 50px
        jQuery('#totop').fadeIn(200);    // Fade in the arrow
        jQuery('#totop').addClass('top-visible');
    } else {
        jQuery('#totop').fadeOut(200);   // Else fade out the arrow
        jQuery('#totop').removeClass('top-visible');
    }
});
jQuery('#totop').on('click', function() {      // When arrow is clicked
    jQuery('body,html').animate({
        scrollTop : 0                       // Scroll to top of body
    }, 500);
    return false;
});


 $(function() {
    
    });

//==============================


// Responsive dropdown menu with submenu
 $('.dropdown-menu a.dropdown-toggle').on('click', function(e) {
            if (!$(this).next().hasClass('show')) {
              $(this).parents('.dropdown-menu').first().find('.show').removeClass("show");
            }
            var $subMenu = $(this).next(".dropdown-menu");
            $subMenu.toggleClass('show');


            $(this).parents('li.nav-item.dropdown.show').on('hidden.bs.dropdown', function(e) {
              $('.dropdown-submenu .show').removeClass("show");
            });


            return false;
          });


})(jQuery);