$(document).ready(function () {
	$('DIV#add_item').click(function () {
		let listElement = $('<li>Item</li>');
		$('UL.my_list').append(listElement);
	});
});