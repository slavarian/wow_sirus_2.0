function updateFileName() {
    var fileName = $('#id_file').val().split('\\').pop();
    $('#selected-file-name').text('Выбранный файл: ' + fileName);
}

function validateFile() {
    var fileName = $('#id_file').val();
    if (!fileName) {
        alert('Выберите файл для загрузки.');
        return false;
    }

    $('#upload-notification').show();

    return true;
}

$(document).ready(function () {
    $("#id_avatar").change(function () {
        readURL(this);
    });

    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('#avatar-preview').attr('src', e.target.result);
                $('#id_file').prop('required', true);
                $('#id_file').toggleClass('hidden-file-input');
            };

            reader.readAsDataURL(input.files[0]);
        }
    }
});