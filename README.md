# Simple HTML remade language

> __First, you can enter the type of document like this:__
``DOCTYPE: html!``
> __The syntax is simple, to write a _TAG_, write this:__
```txt
tag{
  •••
}tag
```
### A disadvantage is that TAGS with text between them cannot occupy just one line, they have to be in between.
> __The "_tag{_" represents the opening _TAG_ in _HTML_,__
> __and "_}tag_" represents the closing _TAG_ in _HTML_.__

__It is important to know, that all code written is transforming into _HTML_ code through a _Python_ program.__

> __To create only opening _TAGS_ empty, write this:__
```txt
tag{}
```

> __To give a attribute for a _TAG_, make this:__
```txt
tag{<attr1:"value">, <attr2:"value">, (how many you want)...
  •••
}tag
```
> __In some situations, this same _TAG_ syntax can match _CSS_ syntax. But I thought of everything!__
> __A example:__
```CSS
button{
   color: Blue;
}
```
__and...__
```txt
button{
   •••
}button
```
> __To fix this, you can put a dollar sign ($) which here represents STYLE OBJECT, before the TAG name, class name, id, name, and other identifiers and after the closing key.__
> __Example:__
```txt
DOCTYPE: html!

html{
  head{
    meta{<charset:"UTF-8">}
    title{
      My WebPage!
    }title
    style{
      $button{
        color: Blue;
      }$
    }style
  }head
  body{
    button{
      Click-me!
    }button
  }body
}html
```

> __That's it, you do it like this:__
```bash
$ python main.py <file you wrote this.>
```
