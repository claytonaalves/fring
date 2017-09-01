function readImageURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#imagem')
                .attr('src', e.target.result)
                .height(200);
        };

        reader.readAsDataURL(input.files[0]);
    }
}

$(document).ready(function () {
    $("#imagem").click(function () {
        $("#file_upload").trigger("click");
    });
});
