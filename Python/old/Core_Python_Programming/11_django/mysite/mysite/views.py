from django.http import HttpResponse


def favicon(request):
    image = open('./static/favicon.ico', 'rb')
    data = image.read()
    image.close()

    return HttpResponse(data, content_type='image/png')
