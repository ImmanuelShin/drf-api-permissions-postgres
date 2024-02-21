from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from .models import Integer  


class IntegerTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.superuser = get_user_model().objects.create_superuser(
            username='admin1', password='pass123', email='admin1@admin.com'
        )

        test_integer = Integer.objects.create(
            name="10",
            owner=cls.superuser,
            description="Out of 10",
        )
        test_integer.save()

    def setUp(self):
        self.client.login(username='admin1', password='pass123')

    def test_Integer_model(self):
        thing = Integer.objects.get(id=1)
        actual_owner = str(thing.owner)
        actual_name = str(thing.name)
        actual_description = str(thing.description)
        self.assertEqual(actual_owner, "admin1")
        self.assertEqual(actual_name, "10")
        self.assertEqual(
            actual_description, "Out of 10"
        )

    def test_get_Integer_list(self):
        url = reverse("integer_list")  
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        things = response.data
        self.assertEqual(len(things), 1)
        self.assertEqual(things[0]["name"], "10")

    def test_get_Integer_by_id(self):
        url = reverse("integer_detail", args=(1,)) 
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        thing = response.data
        self.assertEqual(thing["name"], "10")

    def test_create_Integer(self):
        url = reverse("integer_list") 
        data = {"owner": 1, "name": "11", "description": "Up to eleven"}

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        things = Integer.objects.all()
        self.assertEqual(len(things), 2)
        self.assertEqual(Integer.objects.get(id=2).name, "11")

    def test_update_Integer(self):
        url = reverse("integer_detail", args=(1,))  
        data = {
            "owner": 1,
            "name": "10",
            "description": "Out of 10",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        thing = Integer.objects.get(id=1)
        self.assertEqual(thing.name, data["name"])
        self.assertEqual(thing.owner.id, data["owner"])
        self.assertEqual(thing.description, data["description"])

    def test_delete_Integer(self):
        url = reverse("integer_detail", args=(1,))  
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        things = Integer.objects.all()
        self.assertEqual(len(things), 0)
