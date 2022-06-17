from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import *

class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(username='Tester', email='testing@gmail.com', password='testing0485')
        self.post = Post.objects.create(author=self.user, title='title', text='body body')

    def test_post(self):
        post = self.post
        self.assertEquals(str(post), post.title)
        self.assertEqual(post.author, self.user)
        self.assertEqual(post.title, 'title')
        self.assertEqual(post.text, 'body body')


    def test_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'BlogApp/home.html')
        self.assertContains(response, 'title')


    def test_post_page(self):
        response = self.client.get('/post/1/')
        wrong_response = self.client.get('post/wrong/')
        self.assertEquals(response.status_code, 200)
        self.assertEquals(wrong_response.status_code, 404)
        self.assertTemplateUsed(response, 'BlogApp/post.html')
        self.assertContains(response, 'title')

