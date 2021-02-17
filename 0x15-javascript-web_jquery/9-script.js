// Say Hello! : The translation of “hello” must be displayed in the HTML tag
const $ = window.$;
$(function () {
  $.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('DIV#hello').text(data.hello);
  });
});
