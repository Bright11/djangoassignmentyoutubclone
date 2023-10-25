

$(document).ready(function(){
    $('.categoryslider').owlCarousel({
        autoplay:false,
        loop:true,
        margin:10,
        responsiveClass:true,
        nav:true,
        autoWidth:true,
        autoHeight:true,
        freeDrag:true,
        pullDrag:true,
        touchDrag:true,
        mouseDrag:true,
        navText:['<i class="fa-solid fa-chevron-right"></i>'],
        responsive:{
            0:{
                items:3,
            },
            600:{
                items:3,
               
            },
            1000:{
                items:5,
               
            }
        }
    })
  });