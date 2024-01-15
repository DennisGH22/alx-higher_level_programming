$(document).ready(function () {
  function enterClicked () {
    $('INPUT#language_code').keypress(function (e) {
      if (e.key === 'Enter') {
        e.preventDefault();
        $('INPUT#btn_translate').trigger('click');
      }
    });
  }

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

  enterClicked();
});
