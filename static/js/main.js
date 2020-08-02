$('.recent-items').slick({
    infinite: true,
    speed: 300,
    slidesToShow: 6,
    slidesToScroll: 6,
    prevArrow: ".recent-list .slider-btn .pre",
    nextArrow: ".recent-list .slider-btn .next",
    dots:false,
  
    responsive: [
      {
        breakpoint: 1440,
        settings: {
          slidesToShow: 5,
          slidesToScroll: 5,
        }
      },
  
      {
        breakpoint: 1124,
        settings: {
          slidesToShow: 4,
          slidesToScroll: 4,
        }
      },
      {
        breakpoint: 900,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 3,
        }
      },
      {
        breakpoint: 650,
        settings: {
          slidesToShow: 2,
          slidesToScroll: 2,
        }
      },
    //   {
    //     breakpoint: 480,
    //     settings: {
    //       slidesToShow: 1,
    //       slidesToScroll: 1
    //     }
    //   }
      // You can unslick at a given breakpoint now by adding:
      // settings: "unslick"
      // instead of a settings object
    ]
  });
       
    $('.recomended-items').slick({
        infinite: true,
      speed: 300,
      slidesToShow: 6,
      slidesToScroll: 6,
      prevArrow: ".recomended-list .slider-btn .pre",
      nextArrow: ".recomended-list .slider-btn .next",
      dots:false,
  
      responsive: [
        {
          breakpoint: 1440,
          settings: {
            slidesToShow: 5,
            slidesToScroll: 5,
          }
        },
  
        {
          breakpoint: 1124,
          settings: {
            slidesToShow: 4,
            slidesToScroll: 4,
          }
        },
        {
          breakpoint: 900,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 3,
          }
        },
        {
          breakpoint: 650,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 2,
          }
        },
      //   {
      //     breakpoint: 480,
      //     settings: {
      //       slidesToShow: 1,
      //       slidesToScroll: 1
      //     }
      //   }
        // You can unslick at a given breakpoint now by adding:
        // settings: "unslick"
        // instead of a settings object
      ]
    });
  
    $('.deal-items').slick({
      infinite: true,
      speed: 300,
      slidesToShow: 6,
      slidesToScroll: 6,
      prevArrow: ".deal-list .slider-btn .pre",
      nextArrow: ".deal-list .slider-btn .next",
      dots:false,
  
      responsive: [
        {
          breakpoint: 1440,
          settings: {
            slidesToShow: 5,
            slidesToScroll: 5,
          }
        },
  
        {
          breakpoint: 1124,
          settings: {
            slidesToShow: 4,
            slidesToScroll: 4,
          }
        },
        {
          breakpoint: 900,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 3,
          }
        },
        {
          breakpoint: 650,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 2,
          }
        },
      //   {
      //     breakpoint: 480,
      //     settings: {
      //       slidesToShow: 1,
      //       slidesToScroll: 1
      //     }
      //   }
        // You can unslick at a given breakpoint now by adding:
        // settings: "unslick"
        // instead of a settings object
      ]
    });
  
  
  
    $('.banner').slick({
      autoplay: true,
      autoplaySpeed: 3000,
      infinite: true,
      dots:true,
      prevArrow: ".banner-head .slider-btn .pre",
      nextArrow: ".banner-head .slider-btn .next",
      
    });
  
    $('.pro_photos').slick({
      infinite: true,
      dots:true,
      prevArrow: ".pro_head .slider-btn .pre",
      nextArrow: ".pro_head .slider-btn .next",
    });