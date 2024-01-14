$(document).ready(function () {
  const headerElement = $('header');
  $('DIV#toggle_header').click(function () {
    if (!headerElement.hasClass('red')) {
      headerElement.removeClass('green').addClass('red');
    } else {
      headerElement.removeClass('red').addClass('green');
    }
  });
});
