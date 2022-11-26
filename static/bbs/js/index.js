window.addEventListener("load" , function (){


    $(document).on("click","#submit",function(){ send(this); });


});
function send(elem){

    let form_elem   = $(elem).parents("form");

    let data        = new FormData( $(form_elem).get(0) );

    //TODO:timeを追加する。
    data.set("time" , Number(data.get("hours"))*3600 + Number(data.get("minutes"))*60 + Number(data.get("seconds")) );

    let url     = $(form_elem).prop("action");
    let method  = $(form_elem).prop("method");

    $.ajax({
        url: url,
        type: method,
        data: data,
        processData: false,
        contentType: false,
        dataType: 'json'
    }).done( function(data, status, xhr ) { 
        window.location.replace("");
    }).fail( function(xhr, status, error) {
        console.log(status + ":" + error );
        window.location.replace("");
    }); 

}
