$(function () {
    $("#image_up").change(function(){
      readImage( this );
    });
    $('#submit_pic').click(function () {
        event.preventDefault();
        var form_data = new FormData($('#upload-image')[0]);
        $.ajax({
            type: 'POST',
            url: '/prediction',
            data: form_data,
            contentType: false,
            processData: false,
            dataType: 'json'
        }).done(function (data, textStatus, jqXHR) {
            console.log(data);
            console.log(textStatus);
            console.log(jqXHR);
            console.log('Success!');
            $("#facelandmark").text(JSON.stringify(data, null, 2));
        }).fail(function (data) {
            alert('error!');
        });
    });
});

function readImage(input) {
    if (input.files && input.files[0]) {
        var FR = new FileReader();
        FR.onload = function (e) {
            //e.target.result = base64 format picture
            $('#preview').attr("src", e.target.result);
        };
        FR.readAsDataURL(input.files[0]);
    }
}