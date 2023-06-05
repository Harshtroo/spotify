
$(document).ready(function () {
    console.log("Document Ready")
    var select_ids = [];
    // all chackbox select
    $("#all_select").change(function () {
        $(".select_row").prop('checked', $(this).prop('checked'));
        console.log("fvnfvfn");
        getSelectedIDs();
        handleEditButton();
    });

    $("#delete_master").on("click", function(){

        sendDeleteRequest()

    })

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
        select_ids = []
        $(".select_row:checked").each(function () {
            select_ids.push($(this).val());

        });
        
    }
    
    function sendDeleteRequest() {
        console.log("inside delete===",select_ids);
        $.ajax({
            url: songListURL, 
            type: 'POST',
            headers: { "X-CSRFToken": csrf_token },
            data: {checkbox_ids: select_ids},
            success: function(response) {
                // Handle the response from Django here
                location.reload(true);

                // window.location.href = "song_list/"

            },
            error: function(error) {
                // Handle any error that occurs during the AJAX request
                console.log(error);
            }
        });
      }

    function handleEditButton() {
        var selectedCount = $(".select_row:checked").length;
        console.log("selectedCount",selectedCount);
        if (selectedCount > 1) {
            $(".btn_edit").prop("disabled", true);
        } else {
            $(".btn_edit").prop("disabled", false);
        }
    }


    $(document).on("click", "#btn_edit", function()
    {
        window.location = $(this).attr('href')
    })

    $(document).on("click", "#favourite", function(){
        let song_id = $(this).attr("value")
        $.ajax({
            url: favSongURL, 
            type: 'POST',
            headers: { "X-CSRFToken": csrf_token },
            data: { "song_id": song_id },
            success: function(response) {
                if (response.status == true)
                {
                    window.location.reload()
                }
            }
        })
    })

    $(document).on("click", "#unfavourite", function(){
        let song_id = $(this).attr("value")
        $.ajax({
            url: favSongURL, 
            type: 'POST',
            headers: { "X-CSRFToken": csrf_token },
            data: { "song_id": song_id },
            success: function(response) {
                if (response.status == true)
                {
                    window.location.reload()
                }
            }
        })
    })
})



// function addFavorite(){
//     ad_fav = document.getElementById("favourite").value
//     console.log(ad_fav)
//     $.ajax({
//         url: songListURL, 
//         type: 'POST',
//         headers: { "X-CSRFToken": csrf_token },
//         data: { "song_id": songId },
//         success: function(response) {
//             console.log(response);
//         }
//     })
// }