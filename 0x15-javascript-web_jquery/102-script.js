/* Displays value of hello from fetch in DIV#hello */
document.addEventListener('DOMContentLoaded', () => {
  $('INPUT#btn_translate').click(() => {
    const lang = $('INPUT#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + lang, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
