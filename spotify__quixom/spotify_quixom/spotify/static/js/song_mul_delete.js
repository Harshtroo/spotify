
$(document).ready(function () {
    var select_ids = [];
    // all chackbox select
    $("#all_select").change(function () {
        $(".select_row").prop('checked', $(this).prop('checked'));
        getSelectedIDs();
        handleEditButton();
        deleteDisable()

    });

    $(".delete_master").on("click", function () {
        sendDeleteRequest(select_ids)
    })

    // if user one checkbox unselectd then all checkbox unselected.

    $(".select_row").on('click', function () {
        if ($(".select_row").length === $(".select_row:checked").length) {
            $("#all_select").prop("checked", true);
        } else {
            $("#all_select").prop("checked", false);
        }
        getSelectedIDs()
        handleEditButton()
        deleteDisable()
    })


    function getSelectedIDs() {
        select_ids = []
        $(".select_row:checked").each(function () {
            select_ids.push($(this).val());
        });
    }

        function sendDeleteRequest(select_ids) {
        
        console.log("songDeleteURL",songDeleteURL);
        $.ajax({
            url: songDeleteURL,
            type: 'POST',
            headers: { "X-CSRFToken": csrf_token },
            data: { checkbox_ids: select_ids },
            success: function (response) {
                window.location.reload()

            },
            error: function (error) {
                console.log(error);
            }
        });
    }

    $(".btn_delete").prop("disabled", true);
    function deleteDisable() {
        var selectedCount = $(".select_row:checked").length;
        if (selectedCount == 0) {
            $(".btn_delete").prop("disabled", true);
        } else {
            $(".btn_delete").prop("disabled", false);
        }
    }

    function handleEditButton() {
        var selectedCount = $(".select_row:checked").length;
        if (selectedCount > 1) {
            $(".btn_edit").prop("disabled", true);
        } else {
            $(".btn_edit").prop("disabled", false);
        }
    }


    $(document).on("click", "#btn_edit", function () {
        window.location = $(this).attr('href')
    })
})
function addFav(song_id,obj) {
    const table = $("#song-table")
    const tBody = table.find('tbody > tr')
    console.log("this",obj.children[0].style.color)
    $.ajax({
        url: favSongURL,
        type: 'POST',
        headers: { "X-CSRFToken": csrf_token },
        data: { "song_id": song_id },
        success: function (response) {
            if (obj.children[0].style.color){
                obj.innerHTML ='<i class="fa fa-heart-o fa-2x" aria-hidden="true"></i>'

            }else{
                obj.innerHTML ='<i class="fa fa-heart fa-2x fav" style="color:red;" aria-hidden="true" ></i>'

            }
            
        
        }
    })
}