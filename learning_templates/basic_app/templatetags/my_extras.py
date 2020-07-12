from django import template

register=template.Library()

# writing the same code written down using a decorator
@register.filter(name='cut') #or just @register.filter('cut')
def cut(value,arg):
    """
    This cuts out all values of "arg" from the passed string

    """
    return value.replace(arg,'')

# without decorator
# first arg is name you want to call it, second is the actual filter
# register.filter('cut',cut)