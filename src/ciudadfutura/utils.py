from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginate(params, qs, per_page=25, param_name='page'):

    paginator = Paginator(qs, per_page)

    page = params.get(param_name)
    try:
        results = paginator.page(page)
    except PageNotAnInteger:
        results = paginator.page(1)
    except EmptyPage:
        results = paginator.page(paginator.num_pages)

    return results
