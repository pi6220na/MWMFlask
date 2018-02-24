function initMap() {
    var mpls = {lat: 45.000, lng: -93.265};
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 13,
        center: mpls,
        disableDefaultUI: true
    });
    var marker = new google.maps.Marker({
        position: mpls,
        map: map
    });

    // Create the DIV to hold the control and call the CenterControl()
    // constructor passing in this DIV.
    var userIconDiv = document.createElement('div');
    var userIcon = new UserIcon(userIconDiv, map);


    userIconDiv.index = 1;
    map.controls[google.maps.ControlPosition.TOP_RIGHT].push(userIconDiv);

}


function UserIcon(controlDiv, map) {
    // Set CSS for the control border.
    // var iconUI = document.createElement('div');
    // iconUI.classList.add("userIcon");
    var iconUI = document.getElementById("userIcon");
    var login = document.getElementById("login_modal");
    var signup = document.getElementById("signup_modal");
    controlDiv.appendChild(iconUI);
    controlDiv.appendChild(login)

    // var iconText = document.createElement('div');
    // iconText.innerHTML = "<i class=\"far fa-user\"></i>";
    // iconText.classList.add("userIconText");
    // iconUI.appendChild(iconText)

}

function searchBar() {
    
}