function utilizouhoraextra(pk, boolean){
    token = document.getElementsByName('csrfmiddlewaretoken')[0].value;

    $.ajax({
        type: 'POST',
        url: '/horaextra/utilizouhoraextra/' + pk + '/',
        data: {
            csrfmiddlewaretoken: token,
            'boolean': boolean,
        }
    })
    .done(function (result){
            $('.mensagem').text(result.mensagem);
            $('#total_hora_extra').text(result.horas);
            if (boolean == 'True'){
                $('input[name="horas"]').addClass('text-danger text-bold');
            }
            else{
                $('input[name="horas"]').removeClass('text-danger text-bold');
            }
    });
}