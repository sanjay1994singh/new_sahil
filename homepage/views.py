from django.shortcuts import render


# Create your views here.
def homepage(request):
    print('============@@@@@@@@@@@@@@@@@@')
    return render(request, 'home.html')
