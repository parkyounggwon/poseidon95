
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
        content: "Click to get ship_list!",
        position: seoul,
    });

    infoWindow.open(map);
    // Configure the click listener.
    map.addListener("click", (mapsMouseEvent) => {
    // Close the current InfoWindow.
        map.setZoom(6);
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

//    for (i = 0; i < ship_locations.length; i++) {
//        var ship_built = ship_locations[i][2]
//        console.log('ship_built', ship_built)
//        let d = new Date(ship_built)
//    console.log("년 : "+d.getFullYear())
//    console.log("월 : "+parseInt(d.getMonth()+1))
//    console.log("일 : "+d.getDate())
//    }-->

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
        const image ="https://developers.google.com/maps/documentation/javascript/examples/full/images/beachflag.png";

//        var ship_built = locations[i][2]
//        var ship_date = locations[i][3]
//        var ship_built_year = ship_built.slice(2,4)
//        var ship_built_month_date = ship_date.slice(5,10)
//        var title = (locations[i][0]+' '+locations[i][1]+' '+ship_built_year+'  '+ship_built_month_date)
//
//        titles.push(title)
//        var title2 = Array.from(new Set(titles));  // data deduplication
     //   console.log('title :' + title )

        const cri_port_name = ship_locations[i][4];
        var titles = new Set();
        for( let j = 0 ; j < ship_locations.length; j++) {

            if(cri_port_name == ship_locations[j][4]) {    // ship's position = 4번째인덱스는 port name
                //기준이 되는 항구이름이   현재반복문을 돌고있는 항구의 이름이면 마커 생성
                //한번의 기준이 끝나면 다음 항구이름으로 검사

                var ship_built = ship_locations[j][2]
                var ship_date = ship_locations[j][3]
                var ship_built_year = ship_built.slice(2,4)
                var ship_built_month_date = ship_date.slice(5,10)
                var title = (ship_locations[j][0]+' '+ship_locations[j][1]+' '+ship_built_year+'  '+ship_built_month_date)
                //핀클릭하면 보이는 것 = 배이름, 배크기, 선령, 날짜

                titles.add(title)
//                console.log('titles :',titles);
//                for (let [key, value] of titles.entries())
//                    console.log('value',value);

                let titleStr = Array.from(titles)  // string array
           //     console.log('i행 j열 titleStr  :', i, j, titleStr);

                const result = titleStr.reduce((accu,curr)=> {
                    accu.set(curr, (accu.get(curr)||0) +1) ;
                    return accu;
                },new Map());

                const title4 = []
                for (let [key, value] of result.entries()) {
           //        console.log( 'key present :'+ key + ' : ' + 'value :' + value + '<br>');
                   title4.push(key);
                }

              //  port_ul.innerHTML = " ";

              //  console.log('title4 :', title4 );

              //  var title5 = "<div><table border='1'>";
                var title5 = "";
                    //var port_ul = document.createElement('li')
                    for ( k = 0 ; k < title4.length ; k++ ) {
                       title5 += k+1  + ' '+ title4[k] + '\n';
                       //port_ul.innerHTML += "<li><a href=\"#\">"+title4[k]+"</a></li>";
                     //   title3+= "<tr><td style='border:1px solid;'>"+titleStr+"</td></tr>";
                    }
              //  title5 += "</table></div>";

                createMarker(title5);
              //  console.log("마커만들기 끝");

            }
        }

//         let infoWindow = new google.maps.InfoWindow({
//            content: "Click to get ship_list!",
//            position: new google.maps.LatLng(ship_locations[i][6], ship_locations[i][7]),
//        });

//        infoWindow.open(map);
//        // Configure the click listener.
//        map.addListener("click", (mapsMouseEvent) => {
//        // Close the current InfoWindow.
//            map.setZoom(6);
//            infoWindow.close();
//            // Create a new InfoWindow.
//            infoWindow = new google.maps.InfoWindow({
//                position: mapsMouseEvent.latLng(ship_locations[i][6], ship_locations[i][7]),
//            });
//            infoWindow.setContent(title5);
//            infoWindow.open(map);
//        });


        function createMarker(titles){
            new google.maps.Marker({
            position: new google.maps.LatLng(ship_locations[i][6], ship_locations[i][7]),
            map: map,

            title: `${titles}`,
         //   title: `${i + 1}. ${titles}`,
         //   snippet:'${title}',
            label: `${result.get(location_ports[i])}`,
            })
        }


    }
}

initMap();

//window.initMap = initMap;
