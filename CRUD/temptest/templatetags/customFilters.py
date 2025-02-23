from django import template

register = template.Library()

@register.filter
def add_prefix(value, prefix):
    """Adds a prefix to a string."""
    return f"{prefix}{value}"
