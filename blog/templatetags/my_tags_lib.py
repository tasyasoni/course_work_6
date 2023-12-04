from django import template

register = template.Library()


@register.filter()
def media_pic(val):
    if val:
        return f'media/{val}'
    return"#"




