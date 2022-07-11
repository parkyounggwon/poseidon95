
  document.querySelector('#ship_size [value="' + global_variable_ship_size + '"]').selected = true;
  document.querySelector('#ship_built [value="' + global_variable_ship_built + '"]').selected = true;
  document.querySelector('#ship_area [value="' + global_variable_ship_area + '"]').selected = true;

  document.querySelector('#cargo_size [value="' + global_variable_cargo_size + '"]').selected = true;
  document.querySelector('#cargo_area [value="' + global_variable_cargo_area + '"]').selected = true;

  document.querySelector('#cargo_size [value="' + global_variable_order_size + '"]').selected = true;
  document.querySelector('#cargo_area [value="' + global_variable_order_area + '"]').selected = true;

<!--    $('#ship_size option:contains(' + global_variable_ship_size + ')').prop({selected: true});-->

<!--    $('#ship_size').on('click', function() {-->
<!--        $('#sel').val(global_variable_ship_size)-->
<!--        cosole.log(' selection excute ' ,global_variable_ship_size)-->
<!--    })-->

<!--    var sel = document.getElementById('ship_size');-->
<!--    var opts = sel.options;-->
<!--    for (var opt, j = 0; opt = opts[j]; j++) {-->
<!--        if (opt.value == global_variable_ship_size) {-->
<!--            sel.selectedIndex = j;-->
<!--            break;-->
<!--            }-->
<!--        }-->
