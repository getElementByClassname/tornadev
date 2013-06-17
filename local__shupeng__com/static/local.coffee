$ ->
  node = $('#main > *')
  location = window.location
  i = parseInt(location.hash.replace('#', '')) or 0
  last_i = 0

  toggle_node = ()->
    el = node.eq(i)
    if el.prop('tagName') is 'H1'
      node.hide()
    el.toggle()
    last_i = i
    # $(document).scrollTop($('#main').height())

  $(document).on 'keyup', (e)->
    kc = e.keyCode
    if kc == 39
      i = if (i >= node.length) then 0 else i+1
    if kc == 37
      i = if (i == 0) then node.length else i-1
    location.hash = i

  $(window).on 'hashchange load', ()->
    toggle_node()
    #console.log location.hash
