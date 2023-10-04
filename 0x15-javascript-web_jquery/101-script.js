/* Adds <li> element to list when DIV#add_item is clicked */
$('DIV#add_item')click(() => {
  $('UL.my_list').append($('<li>Item</li>'));
});

/* Rmvs last <li> element frm list when DIV#remove_item is clicked */
$('DIV#remove_item')click(() => {
  $('UL.my_list li').last().remove();
});

/* Clears <li> elements frm list when DIV#clear_list is clicked */
$('DIV#clear_list')click(() => {
  $('UL.my_list').empty();
});
