$('#detail-form').sortable({
  axis: 'y'
});

$('form').submit(function () {
  $('#detail-form').find('tr:visible').each(function (index) {
    // This should target the order field within the row
    if ($(this).find('input[type="hidden"]')[2].hasAttribute('value')) {
      console.log('aqui jue');
      $(this).find('input[type="hidden"]')[0].value = index;
    } else {
      $(this).find('input[type="hidden"]')[0].removeAttribute('value');
    }
  });
})