from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Customer, HealthRecord, Order
from .helper import *
from .imports import *
from .response_handlers import *

# Allows for Customer to place new order
class PlaceNewOrder(APIView):
    def post(self, request):

        jwtResponse = NewAuthenticateJWTtoken(request)
        validToken = jwtResponse["isValid"]
        if not validToken:
            return WriteErrorMessageBadRequest("Invalid Token passed")
        
        mobileNumber = jwtResponse["mobileNumber"]

        itemID = request.data["itemID"]
        count = request.data["count"]

        availableItem = getInventoryDetailForOrder(itemID)
        if count > availableItem["count"]:
            return WriteErrorMessageBadRequest("that many items not available in inventory")
        
        if not DecrementInventoryCount(itemID, count):
            return WriteErrorMessageInternalServerError("failed to create order")
        
        order = Orders.objects.create(
            item_name  = availableItem["name"],
            customer_id  = mobileNumber,
            count  =availableItem["count"]
        )

        return WriteSuccessMessage("order placed")
    
# Allows for Customer to update existing customer order | Order Count
class UpdateExistingOrder(APIView):
    @transaction.atomic
    def post(self, request):

        jwtResponse = NewAuthenticateJWTtoken(request)
        validToken = jwtResponse["isValid"]
        if not validToken:
            return WriteErrorMessageBadRequest("Invalid Token passed")
        
        mobileNumber = jwtResponse["mobileNumber"]
        orderID = request.data["orderID"]
        newcount = request.data["newcount"]

        try:
            order = Orders.objects.get(id = orderID, customer_id = mobileNumber)
        except Orders.DoesNotExist:
            return WriteErrorMessageBadRequest("order not found")
        except Exception as e:
            return WriteErrorMessageInternalServerError(str(e))
        
        order.count = newcount
        order.save()

        return WriteSuccessMessage("order updated")
    
# Allows for Customer to Fetch all ordered Items
class GetOrders(APIView):
    def get(self, request):

        jwtResponse = NewAuthenticateJWTtoken(request)
        validToken = jwtResponse["isValid"]
        if not validToken:
            return WriteErrorMessageBadRequest("Invalid Token passed")
        
        mobileNumber = jwtResponse["mobileNumber"]

        try:
            order = Orders.objects.filter(customer_id = mobileNumber)
        except Orders.DoesNotExist:
            order = None
        except Exception as e: # There some other Issue in accessing the database
            return WriteErrorMessageInternalServerError(str(e))
        
        return WriteSuccessMessageWithData(list(order.values()))
    
# Allows for Customer to Cancel existing order    
class CancelOrder(APIView):
    @transaction.atomic
    def post(self, request):

        jwtResponse = NewAuthenticateJWTtoken(request)
        validToken = jwtResponse["isValid"]
        if not validToken:
            return WriteErrorMessageBadRequest("Invalid Token passed")
        
        mobileNumber = jwtResponse["mobileNumber"]
        orderID = request.data["orderID"]

        try:
            order = Orders.objects.get(id = orderID, customer_id = mobileNumber)
        except Orders.DoesNotExist:
            return WriteErrorMessageBadRequest("order not found")
        except Exception as e:
            return WriteErrorMessageInternalServerError(str(e))
        
        order.delete()

        return WriteSuccessMessage("order cancelled")