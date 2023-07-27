from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Snack
from django.urls import reverse
# Create your tests here.

class SnackTest(TestCase):
    def test_status_code(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


    def test_home_page_templates(self):
        url = reverse('snacks')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='random',email='random@random.com',
            password='random@12345'
        )
        self.snack = Snack.objects.create(
            title = 'test',
            purchaser = self.user,
            description='good',
        )

    def test_str_method(self):
        self.assertEqual(str(self.snack),'test')

    def test_title_field(self):
        self.assertEqual(str(self.snack.title),'test')
    
    def test_purchaser_field(self):
        self.assertEqual(str(self.snack.purchaser),'random')
    
    def test_description_field(self):
        self.assertEqual(str(self.snack.description),'good')

    def test_create_view(self):
        url = reverse('snack_create')
        data={
            "title":"test",
            "purchaser":self.user.id,
            "description":"perfect"
        }
        response = self.client.post(url,data=data,follow=True)
        self.assertTemplateUsed(response,'snack_detail.html')
        self.assertEqual(len(Snack.objects.all()),2)
        self.assertRedirects(response,reverse('snack_detail',args=[2]))

    def test_update_view(self):
        url = reverse('snack_update',args=[1])
        data={
            "title":"test",
            "purchaser":self.user.id,
            "description":"good"
        }
        response = self.client.post(url,data=data,follow=True)
        self.assertTemplateUsed(response,'snack_detail.html')
        self.assertEqual(len(Snack.objects.all()),1)
        self.assertRedirects(response,reverse('snack_detail',args=[1]))

    def test_delete_view(self):
        url = reverse('snack_delete',args=[1])
        response = self.client.post(url,follow=True)
        self.assertTemplateUsed(response,'snack_list.html')
        self.assertEqual(len(Snack.objects.all()),0)
        self.assertRedirects(response,reverse('snacks'))
    