from django.http import HttpResponse

# Create your views here.
# holds the business logic for the attendance app

def greetings(request):
    return HttpResponse('Hi, Moise!')
  
def greetings2(request):
    return HttpResponse('Hi, Benise!')
  
def greetings3(request):
    return HttpResponse('Hi, Delice!')