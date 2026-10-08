from django.urls import path
from .views import ispaid, remainingmoney, grosspayment


urlpatterns = [
    path('ispaid/', ispaid, name='ispaid'),
    path('remainingmoney/', remainingmoney, name='remainingmoney'),
    path('grosspayment/', grosspayment, name='grosspayment'),
]
