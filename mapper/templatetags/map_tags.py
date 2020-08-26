from django import template
from django.utils.html import escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag(takes_context=True)
def tooltip(context, x, y):
    if 'names' in context:
        names = context['names']
        titles=[]
        for i in names:
            if i['x'] == x and i['y'] == y:
                titles.append(escape(i['name']))
        if titles:
            return mark_safe("<br>".join(titles))
    return None
