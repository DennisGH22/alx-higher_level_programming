$(document).ready(function () {
	$('INPUT#btn_translate').click(function () {
		let languageCode = $('INPUT#language_code').val();
		
		function sayHello (translate) {
			$('DIV#hello').text(translate);
		}

		$.get(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`, function (data, displayTranslation) {
			let translate = data.hello;
			displayTranslation = sayHello(translate);
		});
	});
});
