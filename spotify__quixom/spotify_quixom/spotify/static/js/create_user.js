function createUser() {
    var username = document.getElementById("id_username").value
    var email = document.getElementById("id_email").value
    var role = document.getElementById("id_role").value;
    var mobile_number = document.getElementById("id_mobile_number").value
    var password = document.getElementById("id_password1").value

    var data = {
        "username": username,
        "email": email,
        "role": role,
        "mobile_number":mobile_number,
        "password":password,
    }

    $.ajax({
        url: createuser,
        type: "POST",
        headers: { "X-CSRFToken": csrf_token },
        data: data,
        success: function (data) {
            if (data.messages == "success") {
                window.location.href = "/"
            }
        },
        error: function (data, error) {

        },

    });

}