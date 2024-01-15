$(document).ready(function () {
  const liElement = '<li>Item</li>';
  const ulElement = $('UL.my_list');

  (function addItem () {
    $('DIV#add_item').click(function () {
      ulElement.append(liElement);
    });
  }());

  (function removeItem () {
    $('DIV#remove_item').click(function () {
      ulElement.children().last().remove();
    });
  }());

  (function clearList () {
    $('DIV#clear_list').click(function () {
      ulElement.empty();
    });
  }());
});
