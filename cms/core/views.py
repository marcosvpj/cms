from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse


# Create your views here.
def index(request):
    from cms.core.models import Content

    content = get_list_or_404(Content)

    return render(request, 'core/index.html', {'content': content})
