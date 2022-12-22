from django.http import HttpResponse
from django.views.decorators.http import require_GET


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
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")