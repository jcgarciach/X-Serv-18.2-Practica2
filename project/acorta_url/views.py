
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from acorta_url.models import urls

# Create your views here.

@csrf_exempt

def pag(request):
    lista_urls = urls.objects.all()
    if request.method == "GET":
        response = ("<form method = 'POST'>" +
                    "Introduce la URL que quieres acortar: " +
                    "<input type='text' name='url'><br>" +
                    "<input type='submit' value='Enviar'></form>")
        if len(lista_urls) == 0:
            response += "<br>Lista de urls vacia"
        else:
            for url in lista_urls:
                url_short = "http://localhost:1234/" + str(url.id)
                response += ("<br>URL: " + url.url_large + "URL acortada" + "<a href=" + url_short + ">" + "</a>")
    elif request.method == "POST":
        url_large = request.POST['url']
        if (url_large[0:7] != "http://" and url_large[0:8] != "https://"):
            url_large = "http://" + url_large
            try:
                url_short = urls.objects.get(url_large=url_large)
            except urls.DoesNotExist:
                url = lista_urls(url_large=url_large)
                url.save()
                url_short = urls.objects.get(url_large=url_large)
            url_short = "http://localhost:1234/" + str(url_short.id)
            response = ("<br>URL: " + url.url_large + "URL acortada" + "<a href=" + url_short + ">" + "</a>")
    else:
        return HttpResponse("Method not allowed", code = 405)
    return HttpResponse(response, code = 200)


def redir(request, resource):
    try:
        url_large = urls.objects.get(id = resource).url_large
        return HttpResponseRedirect(url_large)
    except urls.DoesNotExist:
        response = "Not Found"
        return HttpResponse(response, code = 404) 
        
