// Generated by CoffeeScript 1.6.3
(function() {
  $(function() {
    var i, location, node, toggle_node;
    node = $('#main > *');
    location = window.location;
    i = parseInt(location.hash.replace('#', '')) || 0;
    toggle_node = function() {
      var el;
      el = node.eq(i);
      if (el.prop('tagName') === 'H1') {
        node.hide();
      }
      el.toggle();
      console.log($('#main').height());
      return $(document).scrollTop($('#main').height());
    };
    $(document).on('keyup', function(e) {
      var kc;
      kc = e.keyCode;
      if (kc === 39) {
        i = i >= node.length ? 0 : i + 1;
      }
      if (kc === 37) {
        i = i === 0 ? node.length : i - 1;
      }
      return location.hash = i;
    });
    return $(window).on('hashchange load', function() {
      return console.log(location.hash);
    });
  });

}).call(this);

/*
//@ sourceMappingURL=local.map
*/