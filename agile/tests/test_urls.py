# from django.urls import reverse
# from rest_framework.test import APITestCase
# from rest_framework import status


# class TestUrls(APITestCase):
#     content_url = reverse('api-root')

#     def test_api_availability(self):
#         response = self.client.get(self.content_url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_data_value(self):
#         response = self.client.get(reverse('category-list'))
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data, {'name': 'Values'})
