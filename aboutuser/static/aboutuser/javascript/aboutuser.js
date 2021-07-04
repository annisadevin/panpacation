$(document).ready(function(){
    // var readURL = function(input) {
    //     if (input.files && input.files[0]) {
    //         var reader = new FileReader();

    //         reader.onload = function (e) {
    //             $('.avatar').attr('src', e.target.result);
    //         }
    
    //         reader.readAsDataURL(input.files[0]);
    //     }
    // }
    

    // $(".file-upload").on('change', function(){
    //     readURL(this);
    // });
    
    // $("input[type='radio']").click(function(){
    //     var sim = $("input[type='radio']:checked").val();
    //     //alert(sim);
    //     if (sim<3) { 
    //         $('.myratings').css('color','red'); 
    //         $(".myratings").text(sim); 
    //     }else{ 
    //         $('.myratings').css('color','green'); 
    //         $(".myratings").text(sim); 
    //     } 
    // });

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

    $(".button-review.mt-5.btn.btn-light").click(function(){
        var id_transaksi = $(this).val()
        console.log(id_transaksi)
        $.ajax({
            url : "/data/myreview/",
            type : "POST",
            dataType: 'json',
            data : {
                'id_transaksi' :  id_transaksi,
            },
            headers: {
                "X-CSRFToken": csrftoken,
            },  
            success : function(data){
                console.log("sukses");
                listMyReview = data.listMyReview;

                $(".collapse.my-review").empty();
                for (var i=0; i<listMyReview.length; i++){
                    var isi = listMyReview[i][0];
                    var rate = listMyReview[i][1];

                    var changedHTML1 = '<p class="text-left">' + isi + '</p>';
                    var changedHTML2;
                    if (rate=='0'){
                        changedHTML2 = '<label id="star"></label>'; 
                    }
                    else if(rate=='1'){
                        changedHTML2 = '<label id="star">★☆☆☆☆</label>';    
                    }
                    else if(rate=='2'){
                        changedHTML2 = '<label id="star">★★☆☆☆</label>';    
                    }
                    else if(rate=='3'){
                        changedHTML2 = '<label id="star">★★★☆☆</label>';    
                    }
                    else if(rate=='4'){
                        changedHTML2 = '<label id="star">★★★★☆</label>';    
                    }
                    else{
                        changedHTML2 = '<label id="star">★★★★★</label>' ;       
                    }
                    $(".collapse.my-review").append(changedHTML1 + changedHTML2);
                }
            }
        });
    });
});