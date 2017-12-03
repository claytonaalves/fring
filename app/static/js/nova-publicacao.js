function readImageURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#' + input.name)
                .attr('src', e.target.result)
                .height(200);
        };

        reader.readAsDataURL(input.files[0]);
    }
}

$(function () {
    $("#imagem1").click(function () {
        $("#file_upload1").trigger("click");
    });

    $("#imagem2").click(function () {
        $("#file_upload2").trigger("click");
    });
 
    $("#imagem3").click(function () {
        $("#file_upload3").trigger("click");
    });
 
    $("#imagem4").click(function () {
        $("#file_upload4").trigger("click");
    });
 
    $("#data_validade").datepicker({dateFormat: "dd/mm/yy"});
});
