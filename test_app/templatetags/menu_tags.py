from django import template
from django.db.models import Prefetch
from ..models import (Menu,
                     InnerMenu,
                     )


register = template.Library()


@register.inclusion_tag('test_app/menu.html', 
                        takes_context = True,
                        )
def menutag(context, menuname):
    url = context['request'].path
    menu = Menu.objects.prefetch_related(
        Prefetch('item', 
                 queryset = InnerMenu.objects.all())
    ).get(name = menuname)

    return {
        'menu': menu,
        'url':url,
    }