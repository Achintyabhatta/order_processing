from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status
from .models import Orders
from .helper import NewAuthenticateJWTtoken

class PlaceNewOrderTestCase(TestCase):
    def test_place_new_order(self):
        # TODO: Add your test case for PlaceNewOrder view
        pass

class UpdateExistingOrderTestCase(TestCase):
    def test_update_existing_order(self):
        # TODO: Add your test case for UpdateExistingOrder view
        pass

class GetOrdersTestCase(TestCase):
    def test_get_orders(self):
        # TODO: Add your test case for GetOrders view
        pass

class CancelOrderTestCase(TestCase):
    def test_cancel_order(self):
        # TODO: Add your test case for CancelOrder view
        pass

class HelperFunctionsTestCase(TestCase):
    def test_new_authenticate_jwt_token_valid(self):
        # TODO: Add your test case for a valid JWT token
        pass

    def test_new_authenticate_jwt_token_invalid(self):
        # TODO: Add your test case for an invalid JWT token
        pass

    def test_get_inventory_detail_for_order(self):
        # TODO: Add your test case for getInventoryDetailForOrder function
        pass

    def test_increment_inventory_count(self):
        # TODO: Add your test case for IncrementInventoryCount function
        pass

    def test_decrement_inventory_count(self):
        # TODO: Add your test case for DecrementInventoryCount function
        pass

class OrdersModelTestCase(TestCase):
    def test_orders_model_str(self):
        order = Orders(item_name="Test Item", customer_id=123, count=2)
        self.assertEqual(str(order), "Test Item")
