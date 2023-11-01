// JavaScript script that fetches and prints how to say “Hello” depending on the language
$(document).ready(() => {
  $('#btn_translate').click(() => {
    const languageCode = $('#language_code').val();

    $.ajax({
      url: `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`,
      method: 'GET',
      dataType: 'json',
      success: function (data) {
        $('#hello').text(data.hello);
      },
      error: function (error) {
        $('#hello').text('Translation not found.');
      }
    });
  });
});
