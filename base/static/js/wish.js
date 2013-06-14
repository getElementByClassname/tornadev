$(document).ready(function(){

  var resize = function(el){
    var doc = document,
      doce = doc.documentElement;
    el.find('.popup-mask')
			.css('height', document.height + 'px');
    el.find('.popup-content')
			.css('top', (doc.body.scrollTop || doce.scrollTop) + window.innerHeight/2 - 25 + 'px').show();
  }

  $(window).resize(function(){
    resize($('.popup'));
  })

  var popup = function(content){
    var el = $('<div class="popup"><div class="popup-content">'+content+'</div><div class="popup-mask"></div></div>')
      .appendTo(document.body);
    resize(el);
    return el
  }

  var set_name = function(fn){
    if (!guest || guest == 'null') {
      var pop = new popup('<form><input type="text" placeholder="不能为空" /><button>名字?</button></form>');
      pop.find('input').focus();
      pop.find('form').submit(function(e){
        e.preventDefault();
        guest = pop.find('input').val();
        if (guest && guest != 'None' && guest != 'null' && guest != '') {
          $.get('/name/'+guest, function(){
            pop.hide().remove();
            $('.item').each(function(idx, el){
              var el = $(el);
              if (el.data('mark') == guest) {
                el.find('button').removeAttr('disabled').text('官人，不要..')
              }
            })
            if (fn) fn();
          });
        }
      })
    } else {
      if (fn) fn();
    }
  }
  /*set_name()*/

  var notify = function(trigger, msg, fn){
    var el = $('<notify>'+ msg +'</notify>').appendTo(trigger || document.body);
    if (fn) fn(el)
  }

  // mark item
  $('.item button').click(function(e){
    e.preventDefault()
    var el = $(this);
    set_name(function(){
      el.text('loading...');
      $.get('/mark/'+el.attr('id')+'/'+guest, function(data){
        var o = jQuery.parseJSON(data);
        var li = el.parents('li');
        el.text(o.msg)
        if (o.ok == 2) el.attr('disabled', '');
        if (o.ok == 1) li.data('mark', guest);
        if (o.ok == 0) li.data('mark', '');
        if (o.ok == 1 || o.ok == 0) li.toggleClass('marked');
      })
    })
  })
})
