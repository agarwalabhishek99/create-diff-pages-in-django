from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Hello page</h1>')

def about(request):
    return HttpResponse('<h1>About page</h1>')

def contact(request):
    return HttpResponse('<h1>Contact page</h1>')

def address(request):
    return HttpResponse('<h1>Address page</h1>')

def technology(request):
    return HttpResponse('<h1>Technology page</h1>')

def web(request):
    return HttpResponse('<h1>Web page</h1>')

def mobile(request):
    return HttpResponse('<h1>Mobile page</h1>')

def desktop(request):
    return HttpResponse('<h1>Desktop page</h1>')
