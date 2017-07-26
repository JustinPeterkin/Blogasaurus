function greeting() {
  var userName = $('#username').val();
  alert("Hi " + userName);
  var header = $("h2");
  header.text("Welcome " + userName);
}


function setup() {
  $("body").append("<div></div>");
  $("#ok_button").click(greeting);
  $
}

$(document).ready(setup);
