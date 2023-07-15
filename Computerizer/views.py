from django.http import HttpResponse
from django.views.decorators.http import require_GET

from django.urls import path

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
path('sentry-debug/', trigger_error),
# ...
]


@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: googlebot",
        "Disallow: /admin",
        "Disallow: /blog",
        "Disallow: /auth",
        "Disallow: /TPA",
        " ",
        "User-Agent: Mediapartners-Google",
        "Disallow: /admin",
        "Disallow: /blog",
        "Disallow: /auth",
        "Disallow: /TPA",
        " ",
        "Sitemap: https://computerizr.com/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")