//  Star wars character 
$.ajax({
  type: 'GET',
  url: 'https://swapi-api.hbtn.io/api/people/5/?format=json',
  success: (r) => {
    $('DIV#character').text(r.name);
  }
});
