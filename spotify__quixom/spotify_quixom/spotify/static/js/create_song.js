
function createUser() {
    // var form = document.querySelector('#my-form');
    // for (let i=0;i<form.elements.length; i++) {
    //    if(form.elements[i].value){
        
    //    }
    // }
    // console.log(form.elements[0].value)
    // console.log(form.elements[1].value)
    // console.log(form.elements[2].value)
    // console.log(form.elements[3].value)

    // var data = document.getElementById("my-form")
    // console.log("data",data);

    var name = document.getElementById("id_name").value
    var singername = document.getElementById("id_singer_name").value
    var category = document.getElementById("id_category").value

    var data= {
        name:name,
        singername:singername,
        category:category,
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