function locationList(){
   // let data = {{ship_locations|safe }};
    let data = global_variable_ship_locations;
    let container = document.getElementById("ship_list");
    for(let i=0; i<data.length; i++){
        let tr = document.createElement("tr");
        container.appendChild(tr);
        let columnCount = data[i].length;

        for (let j=0; j<columnCount-4; j++){
            let td = document.createElement("td");
            td.innerHTML = data[i][j];
            tr.appendChild(td);
        }
    }
}


locationList();