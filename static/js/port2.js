
function initMap() {
    var seoul = { lat: 37.5642135 ,lng: 127.0016985 };
    var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 5,
          center: seoul
        });
    new google.maps.Marker({
        position: seoul,
        map,
        title: "Hello seoul!",
    });
    addMarker(map);

    let infoWindow = new google.maps.InfoWindow({
        content: "Click the map to get Lat/Lng!",
        position: seoul,
    });

    infoWindow.open(map);
    // Configure the click listener.
    map.addListener("click", (mapsMouseEvent) => {
    // Close the current InfoWindow.
        infoWindow.close();
        // Create a new InfoWindow.
        infoWindow = new google.maps.InfoWindow({
            position: mapsMouseEvent.latLng,
        });
        infoWindow.setContent(
            JSON.stringify(mapsMouseEvent.latLng.toJSON(), null, 2)
        );
        infoWindow.open(map);
    });

}


function addMarker(map) {
  //  var ship_locations ={{ship_locations|safe }}  <!-- receive data  string -->
    var ship_locations = global_variable_ship_locations;

    let location_ports = []

    for (i=0; i < ship_locations.length; i++) {
       var location_port = ship_locations[i][4]
       location_ports.push(location_port)
    }
    const result = location_ports.reduce((accu,curr)=> {
        accu.set(curr, (accu.get(curr)||0) +1) ;
        return accu;
    },new Map());

    for (let [key, value] of result.entries()) {
        console.log(key + ' : ' + value + '<br>');
    }

    for (i = 0; i < ship_locations.length; i++) {

        function get_port_ship_list(){
            const port = ship_locations[i][4]
            $.ajax({
              url:"{% url 'port' %}",
              type:'GET',
              data:allData
            })return global_variable_port_ship_list
        }

        var titles = get_port_ship_list();
        port_ul.innerHTML = '';

        var title3 = "<div><table border='1'>";
            for ( k = 0 ; k < titleStr.length ; k++ ) {
                title3 += "<tr><td style='border:1px solid;'>"+titles"</td></tr>";
             //   port_ul.innerHTML += "<li><a href=\"#\">"+title3[i]+"</a></li>";
            }
        title3 += "</table></div>";

        createMarker(title3);

        function createMarker(titles){
            new google.maps.Marker({
            position: new google.maps.LatLng(ship_locations[i][6], ship_locations[i][7]),
            map: map,

            title: `${i + 1}. ${titles}`,
         //   snippet:'${title}',
            label: `${result.get(location_ports[i])}`,
            })
        }


    }
}

initMap();
//window.initMap = initMap;