# myapp/views/test_view.py
from django.http import HttpResponse

def test(request):
    return HttpResponse("Hello World")
