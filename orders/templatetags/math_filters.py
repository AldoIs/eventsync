from django import template

register = template.Library()

@register.filter
def mul(value, arg):
    """
    Multiplica value * arg.
    Útil para hacer price * quantity en plantillas.
    """
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return ''
