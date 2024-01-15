$(document).ready(function () {
  function character (name) {
    $('DIV#character').text(name);
  }

  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data, displayName) {
    const characterName = data.name;
    displayName = character(characterName);
  });
});
