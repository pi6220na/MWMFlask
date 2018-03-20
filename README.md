# MWMFlask Web Application
## MCTC Software Development Capstone 2905-01
### Aaron Souer, Jeremy Wolfe, Reed Armstrong


Project Overview: This is a basic Flask web application that utilizes three APIs, Google Places (and Maps), Google Heatmap, and Wunderground Weather API.

The basic premise is to provide a list of selectable cultural/entertainment places and display them visually on a map of Minneapolis. Each place will be located with a marker that shows the location name and address when clicked on. If the user is logged on to the server, they can save a location to their favorites places. The information can also be displayed via a heatmap (work in progress). Additionally, the current weather conditions, forecast, and a current radar animation are available as an aide to planning activities in Minneapolis.

User signon,favorites, and session data is saved in a SQLite Database.

Project dependencies are listed in the "requirements.txt" file.

Two API keys are required: One for [Google Maps/Places/Heatmap](https://developers.google.com/maps/documentation/javascript/get-api-key) and one for [Wunderground Weather API](https://www.wunderground.com/weather/api/d/docs?MR=1)

## Example Screen Shots:
[text](http://./Screenshots/MWMFlask Main page.png)
