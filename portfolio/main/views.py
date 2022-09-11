from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.http import Http404
from django.template import TemplateDoesNotExist


# Create your views here.
def about(request):
    return render(request, 'main/about.html')

def index(request):
    return render(request, 'main/index.html')


def other_page(request, page):
    try:
        template = get_template('main/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))
    
