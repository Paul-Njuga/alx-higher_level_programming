/* Displays value of hello from fetch in DIV#hello */
$.get('https://fourtonfish.com/hellosalut/?lang=fr', (data) => {
  $('DIV#hello').text(data.hello);
});
