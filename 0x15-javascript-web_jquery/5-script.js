$(document).ready(function () {
  $('DIV#add_item').click(function () {
    const listElement = $('<li>Item</li>');
    $('UL.my_list').append(listElement);
  });
});
