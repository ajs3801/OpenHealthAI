const coordinate_value = document.getElementById("coordinate_value").value;
const Coordinate_btn = document.getElementById("Run");

function onClick() {
  const dict_values = {coordinate_value} //Pass the javascript variables to a dictionary.
  const s = JSON.stringify(dict_values); // Stringify converts a JavaScript object or value to a JSON string

  console.log(s); // Prints the variables to console window, which are in the JSON format
  window.alert(s)
  $.ajax({
      url:"/test",
      type:"POST",
      contentType: "application/json",
      data: JSON.stringify(s)});
}

Coordinate_btn.addEventListener('click', () => {
  onClick();
});
