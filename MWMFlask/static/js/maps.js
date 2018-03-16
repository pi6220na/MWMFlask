var map;

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
    var userIcon = new UserIcon(userIconDiv, map);
    var sideMenu = new SideMenu(sideMenuDiv, map);

    userIconDiv.index = 1;
    sideMenuDiv.index = 2;
    map.controls[google.maps.ControlPosition.TOP_RIGHT].push(userIconDiv);
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(sideMenuDiv);


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


// function searchBar() {
//
// }


// adapted from https://developers.google.com/maps/documentation/javascript/examples/map-geolocation
function getGeolocation(infoWindow, map, callback=null) {
    let mpls = {lat: 45.000, lng: -93.265};

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
        if (callback !== null) {
            callback(pos, map);
        }
        }, function() {
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
    infoWindow.setPosition(pos);
    infoWindow.setContent(browserHasGeolocation ?
                      'Error: The Geolocation service failed.' :
                      'Error: Your browser doesn\'t support geolocation.');
    infoWindow.open(map);
}

function updateMapPins() {
    var places_list = getCheckedPlacesList();

    var loc = [45.020459, -93.241592];

    var key = document.getElementById("map_key").classList[0];

    getPlacesOfType("restaurant", loc, 500, key);
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
    // alert("in getInitialPins: ");
    // alert(location["lat"]);

    var lat = location["lat"];
    var lng = location["lng"];

    var types = ["bar", "restaurant"];

    getPlacesFromCache(lat, lng, 10000, types, map, addPinsToMapFromJSON)

}

function getPlacesOfType(type, loc, rad, key) {

    var query_string = `json?location=${loc[0]},${loc[1]}&radius=${rad}&type=${type}&key=${key}`;

    var api_url = `https://maps.googleapis.com/maps/api/place/nearbysearch/${query_string}`;

    alert("in new get pl");

    // alert(query_string);
    alert(api_url);

}



// adapted from:
// https://stackoverflow.com/questions/247483/http-get-request-in-javascript
function getPlacesFromCache(lat, lng, rad, types, map, callback)
{
    var xmlHttp = new XMLHttpRequest();

    var theUrl = "http://localhost:5000/cache?lat=" + lat + "&lng=" + lng + "&radius=" + rad;
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

    // alert(theUrl);

    xmlHttp.onreadystatechange = function() {
        if (xmlHttp.readyState === 4 && xmlHttp.status === 200)
            // alert("in async - if ");
            callback(xmlHttp.responseText, map);
    };
    xmlHttp.open("GET", theUrl, true); // true for asynchronous
    xmlHttp.send(null);
}

function addPinsToMapFromJSON(json_str, map_obj) {
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

        marker.addListener('click', function() {
            infowindow.open(map, marker);
        });
    }


    // var marker = new google.maps.Marker({
    //     position: mpls,
    //     map: map
    // });



}