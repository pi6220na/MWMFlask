var map;

function initMap() {
    var mpls = {lat: 45.000, lng: -93.265};
    map = new google.maps.Map(document.getElementById('map'), {
        zoom: 13,
        center: mpls,
        disableDefaultUI: true,
        styles: style
    });
    // var marker = new google.maps.Marker({
    //     position: mpls,
    //     map: map
    // });

    // alert("test");

    // alert(style.toString());



    // Create the DIV to hold the control and call the CenterControl()
    // constructor passing in this DIV.
    var userIconDiv = document.createElement('div');
    var sideMenuDiv = document.createElement('div');
    var userIcon = new UserIcon(userIconDiv, map);
    var sideMenu = new SideMenu(sideMenuDiv, map);

    userIconDiv.index = 1;
    sideMenuDiv.index = 2;
    map.controls[google.maps.ControlPosition.TOP_RIGHT].push(userIconDiv);
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(sideMenuDiv);


    var infoWindow = new google.maps.InfoWindow;

    // getGeolocarion(infoWindow, map)

        if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
        var pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
        };

        infoWindow.setPosition(pos);
        infoWindow.setContent('Location found.');
        infoWindow.open(map);
        map.setCenter(pos);
        }, function() {
            handleLocationError(true, infoWindow, map.getCenter());
        });
    } else {
        // Browser doesn't support Geolocation
        handleLocationError(false, infoWindow, map.getCenter());
    }


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

    // var iconText = document.createElement('div');
    // iconText.innerHTML = "<i class=\"far fa-user\"></i>";
    // iconText.classList.add("userIconText");
    // iconUI.appendChild(iconText)

}

function SideMenu(controlDiv, map) {
    var menuUI = document.getElementById("side-menu");
    controlDiv.appendChild(menuUI)
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

function do_search() {
    alert("search");
}


function searchBar() {
    
}


// adapted from https://developers.google.com/maps/documentation/javascript/examples/map-geolocation
function getGeolocarion(infoWindow, map) {
    // Try HTML5 geolocation.
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
        var pos = {
            lat: position.coords.latitude,
            lng: position.coords.longitude
        };

        infoWindow.setPosition(pos);
        infoWindow.setContent('Location found.');
        infoWindow.open(map);
        map.setCenter(pos);
        }, function() {
            handleLocationError(true, infoWindow, map.getCenter());
        });
    } else {
        // Browser doesn't support Geolocation
        handleLocationError(false, infoWindow, map.getCenter());
    }
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
    infoWindow.setPosition(pos);
    infoWindow.setContent(browserHasGeolocation ?
                      'Error: The Geolocation service failed.' :
                      'Error: Your browser doesn\'t support geolocation.');
    infoWindow.open(map);
}

function updateMapPins() {
    var places_list = getCheckedPlacesList();

    var loc = [45.020459, -93.241592];

    var key = "AIzaSyBnoAOkefgBP2J5_pHYLqrZIbmdLWM1dHc";

    getPlacesOfType("restaurant", loc, 500, key);

    // alert(places_list);
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

function getPlacesOfType(type, loc, rad, key) {

    var query_string = `json?location=${loc[0]},${loc[1]}&radius=${rad}&type=${type}&key=${key}`;

    var api_url = `https://maps.googleapis.com/maps/api/place/nearbysearch/${query_string}`;

    alert("in new get pl");

    // alert(query_string);
    alert(api_url);

}

// var lattitude = 45.020459;
// var longetude = -93.241592;
//
// var type = "restaurant";
// var radius = 500;
// var key = "AIzaSyBnoAOkefgBP2J5_pHYLqrZIbmdLWM1dHc";


