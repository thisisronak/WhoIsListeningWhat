function getData(){
  var user = document.getElementById("userName").value;
  var request = new XMLHttpRequest();
  request.onreadystatechange=function(){
    if(request.readyState==4 && request.status==200){
      addDiv(request.responseText);
    }
  };
  request.open('GET', "render/topTracks/" + user, true);
  request.onreadystatechange = function()
  {
    if(request.readyState == 4 && request.status == 200) {
      var response = JSON.parse(request.responseText);
      changeButtonState('btn-success');
      if(response.status === '!ok') {
        var html = htmlToAppend('alert-danger', 'red', response.data, response.whose, response.error);
        document.getElementById('wrapper').innerHTML += html;
      }
      else {
        var html = htmlToAppend('alert-success', 'green', response.data, response.whose, response.error);
        document.getElementById('wrapper').innerHTML += html;
      }
    }
  }
  request.send();
}

function htmlToAppend(alertType, colorType, url, whose, error) {
  var html = "<div role = 'alert' class = 'alert " + alertType + " urlbox'>";
  html += "<a class = '" + colorType + "' href = '" + url + "'>";
  html += whose;
  if(error !== '') {
    html += ": " + error;
  } else {
    html += "'s solution :)"
  }
  html += "</a></div>"
  return html;
}

function changeButtonState(btnState) {
  document.getElementById('button').className = "btn " + btnState;
}