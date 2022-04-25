$('tbody').sortable({
  axis: 'y',
  handle: '.fa-grip-vertical',
});


// update order when form is saved
$('form').submit(function () {
  $('#detail-form').find('tr:visible').each(function (index) {
    // This should target the order field within the row
    if ($(this).find('input[type="hidden"]')[2].hasAttribute('value')) {
      $(this).find('input[type="hidden"]')[0].value = index;
    } else {
      $(this).find('input[type="hidden"]')[0].removeAttribute('value');
    }
  });
})
