function createSong() {
    var name = document.getElementById("id_name").value
    var singername = document.getElementById("id_singer_name").value
    var category = document.getElementById("id_category").value

    var data = {
        "name": name,
        "singername": singername,
        "category": category,
    }

    $.ajax({
        url: createsong,
        method: "POST",
        headers: { "X-CSRFToken": csrf_token },
        data: data,
        success: function (data) {
            if (data.messages == "success") {
                window.location.href = data.redirect
                document.getElementById("message").innerHTML = "successfully create song"
            }
        },
        error: function (data, error) {

        },
    });
}

function editSong() {
    $.ajax({
        url: editurl,
        method: "POST",
        headers: { "X-CSRFToken": csrf_token },
        data: data,
        success: function (data) {
            if (data.messages == "success") {
                window.location.href = '/aong_list/'
            }
        }
    })
}