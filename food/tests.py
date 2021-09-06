from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Dish

class PostModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='tester',password='pass')
        test_user.save()

        test_post = Dish.objects.create(
            customer = test_user,
            type = 'Title of Blog',
            description = 'Words about the blog'
        )
        test_post.save()

    def test_blog_content(self):
        post = Dish.objects.get(id=1)

        self.assertEqual(str(post.customer), 'tester')
        self.assertEqual(post.type, 'Title of Blog')
        self.assertEqual(post.description, 'Words about the blog')