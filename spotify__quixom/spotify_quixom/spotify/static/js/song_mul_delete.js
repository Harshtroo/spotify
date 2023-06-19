
$(document).ready(function () {
    var select_ids = [];
    // all chackbox select
    $("#all_select").change(function () {
        $(".select_row").prop('checked', $(this).prop('checked'));
        getSelectedIDs();
        handleEditButton();
        deleteDisable()
        addToPlayListDisable()
        removeToPlayListDisable()
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
        addToPlayListDisable()
        removeToPlayListDisable()
    })

    function getSelectedIDs() {
        select_ids = []
        $(".select_row:checked").each(function () {
            select_ids.push($(this).val());
        });
    }

    function sendDeleteRequest(select_ids) {
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



    //handle edit button
    function handleEditButton() {
        var selectedCount = $(".select_row:checked").length
        if (selectedCount > 0 ) {
            $(".btn_edit").prop("disabled", true);
            if (selectedCount == 1 ){
                $("#btn_edit_"+select_ids[0]).prop("disabled", false);
            }
        } else {
            $(".btn_edit").prop("disabled", false);
        }
    }
    $(document).on("click", ".btn_edit", function () {
        window.location = $(this).attr('href')
    })

    //user click close button inn modal
    $(".close_btn").on("click",function(){
        $(".modal").modal("hide")
    })

    //multiple select song and add to playlist
    $("#add_playlist").on("click",function(){
    console.log("==============",$("#id_playlist").val())
        $.ajax({
            url: addtoPlaylistURL,
            type: 'POST',
            headers: { "X-CSRFToken": csrf_token },
            data: { "selected_ids": select_ids,
                    "id_playlist": $("#id_playlist").val()},
            success: function (response) {

                window.location.reload()
            },
            error: function (error) {
//                alert("places select any one playlist")
                console.log(error);

            }
        })
    })

    // multiple song remove to playlist
    $("#remove_playlist_submit").on("click",function(event) {
       console.log("select_ids",select_ids)
       event.preventDefault()
//       debugger
       $.ajax({
            url: mulSongRemovePlaylist,
            type: "POST",
            headers: { "X-CSRFToken": csrf_token },
            data: { "selected_ids": select_ids,
                    "id_playlist": $("#id_playlist").val()},
            success: function (response) {
                window.location.reload()
            },
            error:function (error){
                console.log(error)
            }
       })
    })

//    multiple song select and create playlist and add song that playlist function
    $("#create_playlist").on("click",function(){
        console.log("select_ids==",select_ids);
        $.ajax({
            url: mulSongCreatePlaylist,
            type: 'POST',
            headers: { "X-CSRFToken": csrf_token },
            data: { "selected_ids": select_ids,
                      "form":$("#id_name").val()},
            success: function (response) {
                window.location.reload()
            },
            error: function (error){
                console.log(error)
            }
        })
    })
})

function addFav(song_id,obj) {
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

//add to playlist button event
$(".btn-playlist").prop("disabled", true);
    function addToPlayListDisable(){
        var selectedCount = $(".select_row:checked").length;
        console.log("selectedCount",selectedCount)
            if (selectedCount == 0) {
                $(".btn-playlist").prop("disabled", true);
            } else {
                $(".btn-playlist").prop("disabled", false);
            }
    }

//show add playlist modal open
$(".btn-playlist").on("click",function(){
    $("#staticBackdrop").modal("show")
})

$('#close').on('click', function () {
    $('.center').hide();
    $('#show').show();
})

// show multiple song and that create playlist
$(".create_btn").on("click",function(){
    $("#create_playlist_modal").modal("show")
    $("#create_playlist_modal").css('zIndex', '2000')
})

//show remove to playlist button on click open the modal
$(".btn-remove-playlist").on("click",function(){
    $("#remove_playlist").modal("show")
})

//
$(".btn-remove-playlist").prop("disabled", true);
   function removeToPlayListDisable(){
       var selectedCount = $(".select_row:checked").length;
           if (selectedCount == 0) {
               $(".btn-remove-playlist").prop("disabled", true);
           } else {
               $(".btn-remove-playlist").prop("disabled", false);
           }
   }

// if user click on add to playlist button and user not select any playlist that time show error

// document.getElementById("add_playlist").addEventListener("click",function(){
//     // var playlistname = $("#play_list").val()
//     if (!document.getElementById("play_list").value){
//         document.getElementById("error-message").innerHTML = "please select any playlist."
//         document.getElementById("error-message").style.display= "block"
//         return
//     }else {
//         document.getElementById("add_playlist_form").submit()
//         // $("#add_playlist_form").submit()
//     }
// })



