function initMap() {
    var mpls = {lat: 45.000, lng: -93.265};
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 13,
        center: mpls
    });
    var marker = new google.maps.Marker({
        position: mpls,
        map: map
    });
}
