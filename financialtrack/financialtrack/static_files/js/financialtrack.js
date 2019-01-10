$(document).ready(function(){
    $('#delete_confirm_modal').modal('show');
    $('#save').click(function(){
        var valor = $('#valor').val();
        valor = valor.replace(',','.');
        $('#valor').val(valor);
    });
    
    var click_count = 0;
    $('#future_title').click(function(){
        click_count ++;
        if (click_count % 2 == 0){
            $("#show_future_trans").removeClass('glyphicon-menu-up');
            $("#show_future_trans").addClass('glyphicon-menu-down');
        }
        else{
            $("#show_future_trans").removeClass('glyphicon-menu-down');
            $("#show_future_trans").addClass('glyphicon-menu-up');
        }
    });

    var repeat_checkbox = document.getElementById('repeat').value;
    if (repeat_checkbox == 'True'){
        $("#repeat").prop('checked', true);
    }


});
