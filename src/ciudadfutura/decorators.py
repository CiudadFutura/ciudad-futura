from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import REDIRECT_FIELD_NAME


def staff_required(function, **kwargs):
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated() and (u.is_admin or u.is_staff),
        login_url=kwargs.get('login_url', None),
        redirect_field_name=kwargs.get(
            'redirect_field_name', REDIRECT_FIELD_NAME
        )
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def admin_required(function, **kwargs):
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated() and u.is_admin,
        login_url=kwargs.get('login_url', None),
        redirect_field_name=kwargs.get(
            'redirect_field_name', REDIRECT_FIELD_NAME
        )
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def user_required(function=None, **kwargs):
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated(),
        login_url=kwargs.get('login_url', None),
        redirect_field_name=kwargs.get(
            'redirect_field_name', REDIRECT_FIELD_NAME
        )
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
