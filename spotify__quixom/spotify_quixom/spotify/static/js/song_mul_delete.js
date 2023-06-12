
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
        sendDeleteRequest()
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


    function sendDeleteRequest() {
        console.log("+=================", select_ids)
        $.ajax({
            url: songListURL,
            type: 'POST',
            headers: { "X-CSRFToken": csrf_token },
            data: { checkbox_ids: select_ids },
            success: function (response) {
                location.reload(true);

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
function addFav(song_id) {
    const table = $("#song-table")
    const tBody = table.find('tbody > tr')
    $.ajax({
        url: favSongURL,
        type: 'POST',
        headers: { "X-CSRFToken": csrf_token },
        data: { "song_id": song_id },
        success: function (response) {
            tBody.each((index, tr) => {
                console.log("+++++++++++",tr)
//                s_id = tr.attr("song_id")
//                if (response.is_added) {
//                    if (response.song_id == s_id) {
//
//                    }
//                } else {
//
//                }
            })
        }
    })
}