function standardModal(text){
  // initialize modal element
  var $modalEl = $('<div/>');

  // set style
  $modalEl.css({
    width: '400px',
    height: '400px',
    margin: '100px auto',
    padding: '10px 20px',
    backgroundColor: '#f2f2f2'
  });

  // add content
  var $content = $(text);
  $modalEl.append($content);

  // show modal
  mui.overlay('on', $modalEl.get(0));
}
