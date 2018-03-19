var map;
var markers = [];
var user_location;

function initMap() {
    var mpls = {lat: 45.000, lng: -93.265};
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 13,
        center: mpls,
        disableDefaultUI: true,
        styles: style
    });

    // Create the DIV to hold the control and call the CenterControl()
    // constructor passing in this DIV.
    var userIconDiv = document.createElement('div');
    var sideMenuDiv = document.createElement('div');
    var weatherMenuDiv = document.createElement('div');
    var userIcon = new UserIcon(userIconDiv, map);
    var sideMenu = new SideMenu(sideMenuDiv, map);
    var weatherMenu = new WeatherMenu(weatherMenuDiv, map);

    userIconDiv.index = 1;
    sideMenuDiv.index = 2;
    weatherMenuDiv.index = 3;
    map.controls[google.maps.ControlPosition.TOP_RIGHT].push(userIconDiv);
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(sideMenuDiv);
    map.controls[google.maps.ControlPosition.RIGHT_CENTER].push(weatherMenuDiv);

    var infoWindow = new google.maps.InfoWindow;
    getGeolocation(infoWindow, map, getInitialPins);

}

function UserIcon(controlDiv, map) {
    // Set CSS for the control border.
    // var iconUI = document.createElement('div');
    // iconUI.classList.add("userIcon");
    var iconUI = document.getElementById("userIcon");
    // var login = document.getElementById("login_modal");
    // var signup = document.getElementById("signup_modal");
    controlDiv.appendChild(iconUI);
    // controlDiv.appendChild(login)


}

function SideMenu(controlDiv, map) {
    var menuUI = document.getElementById("side-menu");
    controlDiv.appendChild(menuUI)
}

function WeatherMenu(controlDiv, map) {
    var weatherUI = document.getElementById("weather-menu");
    controlDiv.appendChild(weatherUI)
}

function expand_menu() {
    toggle_collapsed();
}

function toggle_collapsed() {
    var expandable = document.getElementById("expandable");
    expandable.classList.toggle("collapsed");

    var header = document.getElementById("side-menu-header");
    header.classList.toggle("opaque");

    var side = document.getElementById("side-menu");
    side.classList.toggle("side-menu-border");
}

// adapted from https://developers.google.com/maps/documentation/javascript/examples/map-geolocation
function getGeolocation(infoWindow = null, map = null, callback = null) {
    let mpls = {lat: 45.000, lng: -93.265};

    // Try HTML5 geolocation.
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
            var pos = {
                lat: position.coords.latitude,
                lng: position.coords.longitude
            };

            if (infoWindow !== null) {
                infoWindow.setPosition(pos);
                infoWindow.setContent('Location found.');
                infoWindow.open(map);
            }
            map.setCenter(pos);

            user_location = pos;

            alert("user_location in get geo: ");
            alert(user_location.latitude);
            alert(user_location.longitude);

            if (callback !== null) {
                callback(pos, map);
            }
        }, function () {
            callback(mpls, map);
            handleLocationError(true, infoWindow, map.getCenter());
        });
    } else {
        // Browser doesn't support Geolocation
        callback(mpls, map);
        handleLocationError(false, infoWindow, map.getCenter());
    }
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
    if (infoWindow !== null) {
        infoWindow.setPosition(pos);
        infoWindow.setContent(browserHasGeolocation ?
            'Error: The Geolocation service failed.' :
            'Error: Your browser doesn\'t support geolocation.');
        infoWindow.open(map);
    }
}

function updateMapPins() {
    getGeolocation(null, map, refreshMap());
}

function getCheckedPlacesList() {
    var place_types = [];
    var inputs = document.getElementsByTagName("input");

    for (var i = 0; i < inputs.length; i++) {
        if (inputs[i].type === "checkbox") {
            if (inputs[i].checked) {
                place_types.push(inputs[i].name)
            }
        }
    }

    return place_types;
}

function placePin(obj) {
}

function getInitialPins(location, map) {
    var lat = location["lat"];
    var lng = location["lng"];

    var types = ["church", "hindu_temple", "mosque", "synagogue", "amusement_park", "aquarium", "park",
        "zoo", "night_club", "bar", "art_gallery", "movie_theater", "museum", "bakery", "restaurant",
        "cafe", "meal_takeaway", "bowling_alley", "stadium", "parking", "bus_station", "subway_station"];

    updateCache(lat, lng, 1000,
    getPlacesFromCache(lat, lng, 1000, types, map, addPinsToMapFromJSON));
}


// adapted from:
// https://stackoverflow.com/questions/247483/http-get-request-in-javascript
function getPlacesFromCache(lat, lng, rad, types, map, callback) {
    var xmlHttp = new XMLHttpRequest();

    // alert("places from cache");

    var theUrl = "http://127.0.0.1:5000/cache?lat=" + lat + "&lng=" + lng + "&radius=" + rad;
    var types_qry = "";
    if (types.length > 1) {
        types_qry = "&types=" + types[0];
        for (var i = 1; i < types.length; i++) {
            types_qry += "-" + types[i]
        }
    } else if (types.length === 1) {
        types_qry = "&types=" + types[0];
    }

    theUrl += types_qry;

    alert(theUrl);

    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState === 4 && xmlHttp.status === 200)
        // alert("in async - if ");
            callback(xmlHttp.responseText, map);
    };
    xmlHttp.open("GET", theUrl, true); // true for asynchronous
    xmlHttp.send(null);
}

function updateCache(lat, lng, rad, callback) {
    var xmlHttp = new XMLHttpRequest();

    // alert("update cache");

    var url = "http://127.0.0.1:5000/cache/update?lat=" + lat + "&lng=" + lng + "&radius=" + rad * 2;

    // alert(url);

    xmlHttp.onreadystatechange = function () {
        if (xmlHttp.readyState === 4 && xmlHttp.status === 200)
            callback();
    };

    xmlHttp.open("GET", url, true);
    xmlHttp.send(null);
}

function addPinsToMapFromJSON(json_str, map) {
    var json_obj = JSON.parse(json_str);

    for (var i = 0; i < json_obj.length; i++) {

        var mkr = json_obj[i];

        // alert(JSON.stringify(mkr));

        var contentString = mkr.name;

        var infowindow = new google.maps.InfoWindow({
            content: contentString
        });

        var marker = new google.maps.Marker({
            position: mkr.location,
            map: map,
            title: mkr.name
        });

        marker.addListener('click', function () {
            infowindow.open(map, marker);
        });

        markers.push(marker)
    }
}

function refreshMap(location, map_obj) {
    var places_list = getCheckedPlacesList();
    clearAllMapPins();
    getPlacesFromCache(location[0], location[1], 1000, places_list, map, addPinsToMapFromJSON)
}

function clearAllMapPins() {
    clearMarkers();
    markers = [];
}

function addPlaceListToMap(loc, map, places) {

}

// Sets the map on all markers in the array.
function setMapOnAll(map) {
    for (var i = 0; i < markers.length; i++) {
        markers[i].setMap(map);
    }
}

// Removes the markers from the map, but keeps them in the array.
function clearMarkers() {
    setMapOnAll(null);
}