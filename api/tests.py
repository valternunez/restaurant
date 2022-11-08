from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Order


class OrderTests(APITestCase):

    def test_create_order(self):
        """
        Ensure we can create a new Order object.
        """
        url = reverse('orders')
        data = {
            "client_name": "Test Name",
            "client_phone": "+554422471344",
            "client_order": "test order",
            "client_address": "Test Address",
        }
        response = self.client.post(url, data, format="json")
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().client_name, 'Test Name')


    def test_get_order_list(self):
        """
        Ensure we can get a list of Order object.
        """
        url = reverse('orders')
        data = {
            "client_name": "Test Name",
            "client_phone": "+554422471344",
            "client_order": "test order",
            "client_address": "Test Address",
        }
        self.client.post(url, data, format="json")
        response = self.client.get(url, format="json")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().client_name, 'Test Name')


    def test_update_order(self):
        """
        Ensure we can update an Order object.
        """
        original_url = reverse('orders')
        original_data = {
            "client_name": "Test Name",
            "client_phone": "+554422471344",
            "client_order": "test order",
            "client_address": "Test Address",
        }
        new_data = {
            "client_name": "New Name",
            "client_phone": "+554422778899",
            "client_order": "new order",
            "client_address": "new address",
        }
        self.client.post(original_url, original_data, format="json")
        order = Order.objects.get(client_name="Test Name")
        
        new_url = reverse('order_detail', kwargs={'id': order.id})
        response = self.client.put(new_url, new_data, format="json")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().client_name, 'New Name')
    
    def test_delete_order(self):
        """
        Ensure we can delete an Order object.
        """
        url = reverse('orders')
        data = {
            "client_name": "Test Name",
            "client_phone": "+554422471344",
            "client_order": "test order",
            "client_address": "Test Address",
        }
        self.client.post(url, data, format="json")
        order = Order.objects.get(client_name="Test Name")
        
        new_url = reverse('order_detail', kwargs={'id': order.id})
        response = self.client.delete(new_url, format="json")
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Order.objects.count(), 0)
