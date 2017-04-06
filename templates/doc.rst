## template for doc
## Date   : 04.06.2017
## Author : Jay Zhao 
## Email  : zq496547199@126.com

{% macro list(l)%}
{%for i in l%}
  #. {{i}}
{%endfor%}
{%endmacro%}

{% macro para(p) %}
{{p.title}}
{{p.sep[p.depth]*p.title.__len__()}}
{{p.des}}
{%for item in p.articles %} {%if item.type  == 'para'%} {{para(item)}} {%elif item.type == 'list'%} {{ list(item.entity) }} {%else%} FIXME {%endif%}
{%endfor%}
{% endmacro %}

{{doc.topic}}
{{doc.sep[doc.depth]*doc.topic.__len__()}}
{{doc.des}}

{%for p in doc.paras%}
{{para(p)}}
{%endfor%}
