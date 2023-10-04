/* Adds <li> element to list when DIV#add_item is clicked */
$('#add_item')click(() => {
  $('UL.my_list').append($('<li>Item</li>'));
});
