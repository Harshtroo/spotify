
$(document).ready(function () {
    // all chackbox select
    $("#all_select").change(function () {
        $(".select_row").prop('checked', $(this).prop('checked'));
        getSelectedIDs();
        handleEditButton();
    });
    // if user one checkbox unselectd then all sectbox unselected.
    
    $(".select_row").on('click', function () {

        if ($(".select_row").length === $(".select_row:checked").length) {
            $("#all_select").prop("checked", true);
        } else {
            $("#all_select").prop("checked", false);
        }
        getSelectedIDs()
        handleEditButton()
       
       
    })
    function getSelectedIDs() {
        var select_id = [];
        $(".select_row:checked").each(function () {
            select_id.push($(this).val());
        });
        console.log("select_id", select_id);
        sendDeleteRequest(select_id);
    }

    function sendDeleteRequest(selectedIDs) {
        $.ajax({
            url: 'song_list/',
            type: 'POST',
            headers: { "X-CSRFToken": csrf_token },
            data: {checkbox_ids: selectedIDs},
            success: function(response) {
                // Handle the response from Django here
                console.log(response);
            },
            error: function(error) {
                // Handle any error that occurs during the AJAX request
                console.log(error);
            }
        });
    }
    function handleEditButton() {
        var selectedCount = $(".select_row:checked").length;
        if (selectedCount > 1) {
            $(".btn_edit").prop("disabled", true);
        } else {
            $(".btn_edit").prop("disabled", false);
        }
    }
    
})