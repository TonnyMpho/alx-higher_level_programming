//  JavaScript script that fetches and prints how to say “Hello” depending on the language
$(document).ready(function () {
  function translateLang () {
    const lang = $('INPUT#language_code').val();

    const url = `https://www.fourtonfish.com/hellosalut/hello/?lang=${lang}`;
    $.get(url, function (data, textStatus) {
      $('DIV#hello').text(data.hello);
    });
  }
});

$('INPUT#btn_translate').click(translateLang);

$('INPUT#btn_translate').on('keypress', function (e) {
  if (e.which === 13) {
    translateLang();
  }
});
