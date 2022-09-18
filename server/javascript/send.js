const Coordinate_btn = document.getElementById("Run");

Coordinate_btn.addEventListener('click', () => {
  const coordinate_value = document.getElementById("coordinate_value").value;
  console.log(coordinate_value)
  const dict_values = {'data' : coordinate_value} //Pass the javascript variables to a dictionary.
  const send = JSON.stringify(dict_values); // Stringify converts a JavaScript object or value to a JSON string
  $.ajax({
    type:"POST",
    url : 'http://192.168.2.5:8000',
    data: send,
    dataType : 'JSON',
    contentType: "application/json",
    success : function(data){
      alert('success');
    },
    error : function(request,status,error) {
      alert("ERROR");
    }
  })
})
