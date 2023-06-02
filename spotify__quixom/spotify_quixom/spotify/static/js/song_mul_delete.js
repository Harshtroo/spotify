
$(document).ready(function () {
    // all chackbox select
    $("#all_select").change(function () {
        $(".select_row").each(function () {
            this.checked = $("#all_select").prop('checked');
        })
    })
    // if user one checkbox unselectd then all sectbox unselected.
    
    $(".select_row").on('click', function () {
        console.log($(".select_row:checked"));

        // console.log("dfvdfv",(".select_row").length);
        // console.log($(".select_row").id);

        if ($(".select_row").length == $(".select_row:checked").length) {
            $("#all_select").prop("checked", true)
        }
        else if ($(".select_row").length - 1 == $(".select_row:checked").length) {
            $("#all_select").prop("checked", false)
        }

        var select_id = []
        // var select_checkbox = document.getElementById("select_row").value
        // console.log("select========",select_checkbox);
        // // select_id.append(select_checkbox)
        // // console.log("kncsdv",select_id);
        // if ($(this).is(":checked")){
        //     select_id.push($(this).attr('id'))
        // }
        // console.log("select_id",select_id);
        // var row =$(this)
        // console.log(row);
        // console.log(row.find('input[type="checkout]').is(':checked'));

        var chek = document.querySelectorAll('input[name="checkbox"]:checked')
        chek.array.forEach(checkbox => {
            select_id.push(checkbox.value)
        }); 
        console.log("select_id",select_id);
    })
})