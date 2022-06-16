from django.shortcuts import render

# Create your views here.
def BlogName(request):
    return render(request, template_name='index.html')

def IndexPage(request):
    return render(request, template_name='index.html')