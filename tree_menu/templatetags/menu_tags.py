from django import template
from tree_menu.models import Menu


register = template.Library()


@register.inclusion_tag('tree_menu/menu.html', takes_context=True)
def draw_menu(context, menu: str | Menu):
    if isinstance(menu, str):
        try:
            context['selected_menu'] = context.get('selected_menu', menu)
            menu = Menu.objects.filter(name=menu)[0].root
        except IndexError:
            return {
                'to_draw': False
            }

    return {
        'menu': menu,
        'selected_menu': context.get('selected_menu', menu.name),
        'before_selected': context.get('before_selected', True),
        'to_draw': True,
        'parent_context': context,
    }


@register.simple_tag(takes_context=True)
def change_context(context, attr: str, new_value):
    context[attr] = new_value
    cur = context.get('parent_context', None)
    while cur is not None:
        context = cur
        context[attr] = new_value
        cur = context.get('parent_context', None)
    return ''