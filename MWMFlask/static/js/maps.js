function initMap() {
    var mpls = {lat: 45.000, lng: -93.265};
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 13,
        center: mpls,
        disableDefaultUI: true
    });
    // var marker = new google.maps.Marker({
    //     position: mpls,
    //     map: map
    // });


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
    map.controls[google.maps.ControlPosition.RIGHT_BOTTOM].push(weatherMenuDiv);
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

function do_search() {
    alert("search");
}


function searchBar() {
    
}