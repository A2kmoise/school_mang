from django.http import HttpResponse

# Create your views here.
def ispaid(request):
    return HttpResponse('Moise you have already paid the service!')
  
def remainingmoney(request):
    return HttpResponse('Moise you have remaining money!')
  
def grosspayment(request):
    return HttpResponse('Moise you have gross payment!')