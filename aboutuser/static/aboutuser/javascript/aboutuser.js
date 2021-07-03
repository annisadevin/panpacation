$(document).ready(function(){
    var readURL = function(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();

            reader.onload = function (e) {
                $('.avatar').attr('src', e.target.result);
            }
    
            reader.readAsDataURL(input.files[0]);
        }
    }
    

    $(".file-upload").on('change', function(){
        readURL(this);
    });
    
    $("input[type='radio']").click(function(){
        var sim = $("input[type='radio']:checked").val();
        //alert(sim);
        if (sim<3) { 
            $('.myratings').css('color','red'); 
            $(".myratings").text(sim); 
        }else{ 
            $('.myratings').css('color','green'); 
            $(".myratings").text(sim); 
        } 
    });
});