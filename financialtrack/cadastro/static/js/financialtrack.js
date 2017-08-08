$(document).ready(function(){
    $('#delete_confirm_modal').modal('show');
    $('#save').click(function(){
        var valor = $('#valor').val();
        valor = valor.replace(',','.');
        $('#valor').val(valor);
    });

    var repeat_checkbox = document.getElementById('repeat').value;
    if (repeat_checkbox == 'True'){
        $("#repeat").prop('checked', true);
    }


});
