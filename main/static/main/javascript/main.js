$(document).ready(function(){
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');
    
    $('select#select-reservasi').on('change', function(){
        console.log("Select Terpilih");
        console.log( $("#select-reservasi option:selected").val());
        selected_reservasi = $("#select-reservasi option:selected").val();
        $.ajax({
            url : "/data/basedOnReservasi/",
            type : "POST",
            dataType: 'json',
            data : {
                'selected_reservasi' :  selected_reservasi,
            },
            headers: {
                "X-CSRFToken": csrftoken,
            },  
            success : function(data){
                console.log("sukses");
                var listKota = data.listKota;

                $('select#select-lokasi').empty();

                for (var i=0; i<listKota.length; i++){
                    var kota = listKota[i][0];
                    var changedHTML = '<option value="' + kota + '">' + kota + '</option>';
                    console.log(changedHTML);
                    $('select#select-lokasi').append(changedHTML);
                }
            }
        });
    });

    $("#button-check-ketersediaan").click(function(){
        var check_in = new Date($("input[name='check_in']").val());
        var check_out = new Date($("input[name='check_out']").val());

        if(check_in > check_out){
            alert("Waktu check out harus lebih besar dari waktu check in");
        }
    });

    $(".img-diklik").click(function(){
        console.log($(".img-diklik").attr('src'));
        var src = $(".img-diklik").attr('src');
        var res = src.substring(25, 26);
        console.log(res)
        
        $("#keep-random-no").val(res);
    });
});