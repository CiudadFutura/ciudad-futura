from django.template import Library

register = Library()


@register.inclusion_tag('site/_pagination.html')
def pagination(results):
    return {
        'results': results,
    }
