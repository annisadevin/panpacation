$(document).ready(function () {
    var silder = $(".owl-carousel");
      silder.owlCarousel({
      autoPlay: true,
      items: 1,
      center: false,
      nav: true,
      margin: 30,
    dots: false,
    loop: true,
    navText: ["<i class='fa fa-arrow-left' aria-hidden='true'></i>", "<i class='fa fa-arrow-right' aria-hidden='true'></i>"],
    responsive: {
    0: {
    items: 1,
    },
    575: { items: 1 },
    768: { items: 2 },
    991: { items: 3 },
    1200: { items: 4 }
    }
    });
});
var myCenter = new google.maps.LatLng(37.422230, -122.084058);
function initialize(){
    var mapProp = {
        center:myCenter,
        zoom:12,
        mapTypeId:google.maps.MapTypeId.ROADMAP
    };

    var map = new google.maps.Map(document.getElementById("map"),mapProp);

    var marker = new google.maps.Marker({
        position:myCenter,
    });

    marker.setMap(map);
}
google.maps.event.addDomListener(window, 'load', initialize);