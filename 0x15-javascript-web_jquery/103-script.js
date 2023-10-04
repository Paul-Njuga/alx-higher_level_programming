/* Displays value of hello from fetch in DIV#hello */
document.addEventListener('DOMContentLoaded', () => {
  /* When ENTER is clicked when the focus is on INPUT#language_code */
  $('INPUT#language_code').keypress((event) => {
    if (event.which === 13) {
      const lang = $('INPUT#language_code').val();
      $.get('https://hellosalut.stefanbohacek.dev/?lang=' + lang, (data) => {
        $('DIV#hello').text(data.hello);
      });
    }
  });
  /* When user clicks on INPUT#btn_translate */
  $('INPUT#btn_translate').click(() => {
    const lang = $('INPUT#language_code').val();
    $.get('https://hellosalut.stefanbohacek.dev/?lang=' + lang, (data) => {
      $('DIV#hello').text(data.hello);
    });
  });
});
