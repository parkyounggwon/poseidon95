
function order_locationList(){
    let data = global_variable_order_locations;
    let container = document.getElementById("order_list");
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

order_locationList();