// JavaScript script that adds, removes and clears LI elements from a list when the user clicks
$(document).ready(() => {
  $('#add_item').click(() => {
    // Add a new <li> element to the list
    $('.my_list').append('<li>Item</li>');
  });

  $('#remove_item').click(() => {
    // Remove the last <li> element from the list
    $('.my_list li:last').remove();
  });

  $('#clear_list').click(() => {
    // Clear all <li> elements from the list
    $('.my_list').empty();
  });
});
