// function go_search(){
//        console.log("go search")
//        $("select[name=ship_size]").val("{{ id_ship_size_text }}")
//        $('select[name=ship_size]').change(function () {
//            console.log($('select[name=ship_size]').val())
//            ship_size = $('select[name=ship_size]').val()
//            $('.form').submit()
//        })
//    }

let today = new Date()

const min_date = new Date(today)
const max_date = new Date(today)
console.log('const min_date :',min_date )
min_date.setDate(today.getDate() - 90)
max_date.setDate(today.getDate() + 180)
console.log('min_date :',  min_date)
console.log('max_date :',  max_date)

if (ship_date_start = null) {
    document.getElementById('ship_date_start').value = new Date().toISOString().slice(0, 10)
    document.getElementById('ship_date_end').value = new Date().toISOString().slice(0, 10)
    }else{
        document.getElementById('ship_date_start').value = global_variable_ship_date_start
        document.getElementById('ship_date_end').value = global_variable_ship_date_end
        console.log('global_variable_ship_date_start : ',global_variable_ship_date_start)
    }

if (cargo_date_start = null) {
    document.getElementById('cargo_date_start').value = new Date().toISOString().slice(0, 10)
    document.getElementById('cargo_date_end').value = new Date().toISOString().slice(0, 10)
    }else{
        document.getElementById('cargo_date_start').value = global_variable_cargo_date_start
        document.getElementById('cargo_date_end').value = global_variable_cargo_date_end
    }


if (order_date_start = null) {
    document.getElementById('order_date_start').value = new Date().toISOString().slice(0, 10)
    document.getElementById('order_date_end').value = new Date().toISOString().slice(0, 10)
    }else{
        document.getElementById('order_date_start').value = global_variable_order_date_start
        document.getElementById('order_date_end').value = global_variable_order_date_end
    }
