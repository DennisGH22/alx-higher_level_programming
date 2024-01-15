$(document).ready(function () {
  function hello (sayHello) {
    $('DIV#hello').text(sayHello);
  }

  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (data, displayHello) {
    const sayHello = data.hello;
    displayHello = hello(sayHello);
  });
});
