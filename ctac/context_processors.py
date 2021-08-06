from .models import Chapel


def menu_links(request):
    links = Chapel.objects.all()
    return dict(links=links)
