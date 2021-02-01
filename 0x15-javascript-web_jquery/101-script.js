$(document).ready(function () {
  $('DIV#add_item').click(function () {
    $('ul.my_list').append('<LI>Item</LI>');
  });

  $('DIV#remove_item').click(function () {
    $('ul.my_list li').first().remove();
  });

  $('DIV#clear_list').click(function () {
    $('ul.my_list').empty();
  });
});
