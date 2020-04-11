import json

from django.urls import reverse
from agile.models import Category, Content

from rest_framework.test import APITestCase
from rest_framework import status


class TestCategory(APITestCase):
    
    def setUp(self):
        self.category_url = reverse('category-list')
        self.test_category = Category.objects.create(name="TestName")
    
    def test_list_all_category(self):
        response = self.client.get(self.category_url, format='json')
        expected_data = [{
            "name": self.test_category.name,
            "content": []
        }]
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), expected_data)
    
    def test_create_category(self):
        test_name = "TestCreation"
        data = {
            "name": test_name
        }
        response = self.client.post(self.category_url, data, format='json')
        
        expected_data = {
            "name": test_name,
            "content": []
        }
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, expected_data)
    
    def test_category_details(self):
        response = self.client.get(reverse('category-detail', kwargs={'pk':self.test_category.id}))
        data = {
            "name": self.test_category.name,
            "content": []
        }
        
        self.assertEqual(response.data, data)
    
    def test_delete_category(self):
        response = self.client.delete(reverse('category-detail', kwargs={'pk':self.test_category.id}))
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class TestContent(APITestCase):

    def setUp(self):
        self.content_url = reverse('content-list')
        self.test_category = Category.objects.create(name="TestName")
        self.test_content = Content.objects.create(category = self.test_category, order = 1,
                                                  item = "Content Item", details = "Content sample details")
        

    def test_list_all_content(self):
        response = self.client.get(self.content_url, format='json')
        expected_data = [{
            'order': self.test_content.order,
            'item': self.test_content.item,
            'details': self.test_content.details
        }]
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), expected_data)
    
    def test_create_content(self):
        data = {
            'category':self.test_category.id,
            'order': 1,
            'item': 'Test Content Item',
            'details': 'Test Content Detail'
        }
        response = self.client.post(self.content_url, data, format='json')
        
        
        expected_data = {
            'order': 1,
            'item': 'Test Content Item',
            'details': 'Test Content Detail'
        }
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, expected_data)
    
    def test_content_details(self):
        response = self.client.get(reverse('content-detail', kwargs={'pk':self.test_content.id}))
        expected_data = {
            'order': self.test_content.order,
            'item': self.test_content.item,
            'details': self.test_content.details
        }
        
        self.assertEqual(response.data, expected_data)
        
    
    def test_delete_content(self):
        response = self.client.delete(reverse('category-detail', kwargs={'pk':self.test_content.id}))
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    
    # This is a custom model function test
    def test_get_category_name(self):
        assert self.test_category.name == self.test_content.category_name()

    