virtualenv(wrapper)
===

[tutorial][virtualenvwrapper]

auto switch python environment

    source /usr/local/bin/virtualenvwrapper.sh
    mkvirtualenv --no-site-packages --distribute -p /usr/local/bin/python3 tornadev
    pip install -r requirements.txt


    #!/bin/bash
    VENV=$1
    if [ -z $VENV ]; then
        echo "usage: runinenv [virtualenv_path] CMDS"
        exit 1
    fi
    . ${VENV}/bin/activate
    shift 1
    echo "Executing $@ in ${VENV}"
    exec "$@"
    deactivate


    # /etc/supervisord.conf
    [program:app]
    command=sh path/to/run.sh ./.venv python boot.py
    directory=/path/to/Project
    autostart=true
    autorestart=true
    startsecs=10


[virtualfish](https://github.com/adambrenecki/virtualfish)


dnsmasq
===

[dnsmasq][] set up *.dev domain to localhost

    # /etc/dnsmasq.conf
    listen-address=127.0.0.1
    address=/.dev/127.0.0.1


tornado
===

- multi-domain with add_handlers
- auto reload browser by websocket


mongodb
===

- schemeless
- bson


fontend
===

## javascript
  - [coffeescript.org][coffee]
  - type-script

example

    # Assignment:
    number   = 42
    opposite = true

    # Conditions:
    number = -42 if opposite

    # Functions:
    square = (x) -> x - x

    # Arrays:
    list = [1, 2, 3, 4, 5]

`source.map`


## oocss    
- [stylus][]
- lesscss.org
- sacss, compass


example

    // styl
    select
      foo1 bar1
      sub
        foo2 bar2

    // less
    select {
      foo1: bar1;
      sub {
        foo2: bar2;
      }
    }
    
    /* css */
    select { foo1: bar1; }
    select sub { foo2: bar2; }

## template

- [jade][] / [pyjade][]
- [handlebars][]
- mustache.js

example

    !!! 5
    html(class=html_cls(__name__))
      head
        meta(chaset='utf-8')
        meta(name="viewport", content="width=device-width, initial-scale=1.0")
        link(rel="stylesheet", type="text/css", href=static_url('build/build.css'))
        link(rel="stylesheet", type="text/css", href=static_url('pure-min.css'))
        link(rel="stylesheet", type="text/css", href=static_url('pure.css'))
        script(type="text/javascript", src=static_url("build/build.js"))
      body
        .pure-g-r#layout
          header.pure-u#menu
            .pure-menu.pure-menu-open
              a.pure-menu-heading(href="/")= _('Dashboard')
              ul
                each name in ['issue', 'index', 'article', 'analyze']
                  li
                    a(href="/"+name+"/", class=name)= name

            - var user = handler.current_user
            if user
              p= user.split('@')[0]
              a(href="/auth/logout")= 'Sign Out'

          div.pure-u#main
            block content


## componets

- [componet][] [wiki][componet wiki]
  - purecss.io
  - d3.js
- [twitter flight][flight]
- bower.io


##  mvc

- [backbone][]
- [meteor][]
- AngularJS
- Ember

`router`, `data`, `event`, `sync`


tool
===

[yanyao's dotfile][dotfile]


## tmux

[tutorial][tmux]

- more than screen
- split panel
- session
- vi/emacs keybind
- copy/paste buffer (mouse support)


## fishshell

[tutorial][fishshell]

- Syntax Highlighting
- Autosuggestions
- Tab Completions


## vim

    Bundle 'gmarik/vundle'
    Bundle 'scrooloose/syntastic'
    Bundle 'majutsushi/tagbar'

    Bundle "groenewege/vim-less"
    Bundle "wavded/vim-stylus"
    Bundle "kchmck/vim-coffee-script"
    Bundle 'jade.vim'

    au bufwritepost *.less silent execute '!lessc % > %:t:r.css'
    au bufwritepost *.styl silent execute '!stylus --compress < % > %:t:r.css'
    au bufwritepost *.coffee silent execute '!coffee -cm %'


## vagrant

[tutorial][vagrant]

    vagrant init precise32 http://files.vagrantup.com/precise32.box
    vagrant up
    vagrant ssh


# subscribe

- [coder weekly](http://feeds.feedburner.com/CoderWeeklyArchiveFeed)
- [python weekly](http://www.pycoders.com)
- [devops weekly](http://devopsweekly.com)
- [hacknews daily](http://hnsummaries.com)


[dotfile]: https://github.com/yanyaoer/dotfile
[dnsmasq]: http://blog.evan.pro/how-to-set-up-dynamic-virtual-hosts-for-web-development
[tmux]: http://linuxtoy.org/archives/from-screen-to-tmux.html
[virtualenvwrapper]: http://virtualenvwrapper.readthedocs.org
[fishshell]: http://fishshell.com/tutorial.html
[vagrant]: http://docs.vagrantup.com/v2/getting-started/index.html

[componet]: http://component.io
[componet wiki]: https://github.com/component/component/wiki/Components
[backbone]: http://backbonejs.org
[meteor]: http://meteor.com
[flight]: http://twitter.github.io/flight
[jade]: http://jade-lang.com
[pyjade]: https://github.com/SyrusAkbary/pyjade
[coffee]: http://coffeescript.org
[stylus]: http://learnboost.github.io/stylus/
[handlebars]: http://handlebarsjs.com
