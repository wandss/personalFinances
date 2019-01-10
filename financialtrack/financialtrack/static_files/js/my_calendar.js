$(document).ready(function(){
    $("#data").change(function(){
        var data = document.getElementById('data').value;
        var dia, mes, ano;

        if (data.split('/').length == 1){
            dia = data.slice(0,2);
            mes = data.slice(2,4);
            ano = data.slice(4, data[-1]);
        }
        else if (data.split('/').length == 3){
            dia = data.split('/')[0];
            mes = data.split('/')[1];
            ano = data.split('/')[2];
        }
        var date = new Date(ano, parseInt(mes)-1, dia, 6);
        dia = date.getDate();
        mes = date.getMonth()+1;
        ano = date.getFullYear().toString();

        if (dia < 10){
            dia = '0'+dia.toString();
        }
        if (mes < 10){
            mes = '0'+mes.toString();
        }
        $('#data').val(dia+'/'+mes.toString()+'/'+ano.toString());
    })
});
