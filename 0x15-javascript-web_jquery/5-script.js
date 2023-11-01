// JavaScript script that adds a <li> element to a
// list when the user clicks on the tag DIV#add_item
$(document).ready(() => {
  $('DIV#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
});
