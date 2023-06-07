from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'main/main.html')

def first_page(request):
    return render(request, 'main/first_page.html')

def about(request):
    return render(request, 'main/about.html')

def second_page(request):
    return render(request, 'main/second_page.html')

