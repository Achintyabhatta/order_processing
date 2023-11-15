from django.urls import path
from . import views
from .views import *

urlpatterns = [

    path('place-new-order', PlaceNewOrder.as_view(), name='customer'),
    path('update-order', UpdateExistingOrder.as_view(), name='customer'),
    path('get-order', GetOrders.as_view(), name='customer'),
    path('cancel-order', CancelOrder.as_view(), name='customer')

]
