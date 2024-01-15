$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const languageCode = $('INPUT#language_code').val();

    function sayHello (translate) {
      $('DIV#hello').text(translate);
    }

    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`, function (data, displayTranslation) {
      const translate = data.hello;
      displayTranslation = sayHello(translate);
    });
  });
});
