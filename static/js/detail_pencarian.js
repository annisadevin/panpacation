$(document).ready(function(){

  $('.items').slick({
  infinite: true,
  slidesToShow: 2,
  slidesToScroll: 2
  });
  });


$(document).ready(function () {
  var id = document.getElementById("kode").textContent;
  var checkin = $("#checkin").val();  
  var checkout = $("#checkout").val(); 
  var jumlah = $("#jml").val(); 

  $.ajax({                       
    dataType: "json",
    url: '/detail/getkodefromcheckin/' + id + '/' +checkin +'/' + checkout + '/' + jumlah + '/',
    cache: false,
    success: function (data) {
      console.log(data)
      data.forEach(function (data) {
        let  judul='';
        let  all='';
        let  cb='';
        let  kanan='';

        judul = '#judul'+ `${data.status}`
        console.log(judul)
        all = '#all'+ `${data.status}`
        cb = '#cb'+ `${data.status}`
        kanan = '#kanan'+ `${data.status}`
        $(judul).html(`<h5>${data.kode_room}</h5>`);
        $(all).append(`<span class="fa fa-user"></span><span class="faci"> ${data.kapasitas} Dewasa</span><br>`);
        $(all).append(`<span class="fa fa-bed"></span><span class="faci"> ${data.kasur} </span><br>`);



        if(`${data.is_there_bathtube}` == 1){
          $(all).append(`<span class="fa fa-bath"></span><span class="faci"> Bathtub </span><br>`);
        }
        if(`${data.isac}` == 1){
          $(all).append(`<span class="fa fa-fan"></span><span class="faci"> Air Conditioner </span><br>`);
        }
        if(`${data.is_there_airhangat}` == 1){
          $(all).append(`<span class="fa fa-bath"></span><span class="faci"> Air Hangat </span><br>`);
        }

        $(cb).html(`<input type="checkbox" name=${data.status} value=${data.kode_room}>`);

        $(kanan).html(`<h4>Rp ${data.harga}</h4> `);
      });
    } 
  });

  $("#checkin").change(function () {
    var id = document.getElementById("kode").textContent;
    var checkin = $(this).val();  
    var checkout = $("#checkout").val(); 
    var jumlah = $("#jml").val(); 
    
    $.ajax({                       
      dataType: "json",
      url: '/detail/getkodefromcheckin/' + id + '/' +checkin +'/' + checkout + '/' + jumlah + '/',
      success: function (data) {
        for( i = 0; i<=data.length ; i++){
          $("#all" + i).empty();

        }
        
        data.forEach(function (data) {
          let  judul='';
          let  all='';
          let  cb='';
          let  kanan='';

          judul = '#judul'+ `${data.status}`
          all = '#all'+ `${data.status}`
          cb = '#cb'+ `${data.status}`
          kanan = '#kanan'+ `${data.status}`

          $(judul).html(`<h5>${data.kode_room}</h5>`);
          $(all).append(`<span class="fa fa-user"></span><span class="faci"> ${data.kapasitas} Dewasa</span><br>`);
          $(all).append(`<span class="fa fa-bed"></span><span class="faci"> ${data.kasur} </span><br>`);

          if(`${data.is_there_bathtube}` == 1){
            $(all).append(`<span class="fa fa-bath"></span><span class="faci"> Bathtub </span><br>`);
          }
          if(`${data.isac}` == 1){
            $(all).append(`<span class="fa fa-fan"></span><span class="faci"> Air Conditioner </span><br>`);
          }
          if(`${data.is_there_airhangat}` == 1){
            $(all).append(`<span class="fa fa-bath"></span><span class="faci"> Air Hangat </span><br>`);
          }

          $(cb).html(`<input type="checkbox" name=${data.status} value=${data.kode_room}>`);
          $(kanan).html(`<h4 style="text-align: right;">Rp ${data.harga} </h4> `);

        });
      } 
    });
  });

  $("#checkout").change(function () {
    var id = document.getElementById("kode").textContent;
    var checkout = $(this).val();  
    var checkin = $("#checkin").val(); 
    var jumlah = $("#jml").val(); 
    
    $.ajax({                       
      dataType: "json",
      url: '/detail/getkodefromcheckin/' + id + '/' +checkin +'/' + checkout + '/' + jumlah + '/',
      success: function (data) {
        for( i = 0; i<=data.length ; i++){
          $("#all" + i).empty();
        }
        data.forEach(function (data) {
          let  judul='';
          let  all='';
          let  cb='';
          let  kanan='';

          judul = '#judul'+ `${data.status}`
          all = '#all'+ `${data.status}`
          cb = '#cb'+ `${data.status}`
          kanan = '#kanan'+ `${data.status}`

          $(judul).html(`<h5>${data.kode_room}</h5>`);
          $(all).append(`<span class="fa fa-user"></span><span class="faci"> ${data.kapasitas} Dewasa</span><br>`);
          $(all).append(`<span class="fa fa-bed"></span><span class="faci"> ${data.kasur} </span><br>`);


          if(`${data.is_there_bathtube}` == 1){
            $(all).append(`<span class="fa fa-bath"></span><span class="faci"> Bathtub </span><br>`);
          }
          if(`${data.isac}` == 1){
            $(all).append(`<span class="fa fa-fan"></span><span class="faci"> Air Conditioner </span><br>`);
          }
          if(`${data.is_there_airhangat}` == 1){
            $(all).append(`<span class="fa fa-bath"></span><span class="faci"> Air Hangat </span><br>`);
          }

          $(cb).html(`<input type="checkbox" name=${data.status} value=${data.kode_room}>`);
          $(kanan).html(`<h4 style="text-align: right;">Rp ${data.harga} </h4> `);

        });
      } 
    });
  });

  $("#jml").change(function () {
    var id = document.getElementById("kode").textContent;
    var checkout = $("#checkout").val();  
    var checkin = $("#checkin").val(); 
    var jumlah = $(this).val(); 
    
    $.ajax({                       
      dataType: "json",
      url: '/detail/getkodefromcheckin/' + id + '/' +checkin +'/' + checkout + '/' + jumlah + '/',
      success: function (data) {
        for( i = 0; i<=data.length ; i++){
          $("#all" + i).empty();
        }
        data.forEach(function (data) {
          let  judul='';
          let  all='';
          let  cb='';
          let  kanan='';
          judul = '#judul'+ `${data.status}`
          all = '#all'+ `${data.status}`
          cb = '#cb'+ `${data.status}`
          kanan = '#kanan'+ `${data.status}`


          $(judul).html(`<h5>${data.kode_room}</h5>`);
          $(all).append(`<span class="fa fa-user"></span><span class="faci"> ${data.kapasitas} Dewasa</span><br>`);
          $(all).append(`<span class="fa fa-bed"></span><span class="faci"> ${data.kasur} </span><br>`);

          if(`${data.is_there_bathtube}` == 1){
            $(all).append(`<span class="fa fa-bath"></span><span class="faci"> Bathtub </span><br>`);
          }
          if(`${data.isac}` == 1){
            $(all).append(`<span class="fa fa-fan"></span><span class="faci"> Air Conditioner </span><br>`);
          }
          if(`${data.is_there_airhangat}` == 1){
            $(all).append(`<span class="fa fa-bath"></span><span class="faci"> Air Hangat </span><br>`);
          }

          $(cb).html(`<input type="checkbox" name=${data.status} value=${data.kode_room}>`);
          $(kanan).html(`<h4 style="text-align: right;">Rp ${data.harga} </h4> `);

        });
      } 
    });
  });

  // $('.button').click( function() { 
  //   var checkout = $("#checkout").val();
  //   var checkin = $("#checkin").val();

  //   if(checkin>checkout){
  //     alert('Data yang dimasukkan salah');
  //   }
  // });

  $(".button").click(function(){
    var check_in = $("#checkin").val();
    var check_out = $("#checkout").val();

    if(check_in > check_out){
        alert("Waktu check out harus lebih besar dari waktu check in");
    }
});

});
