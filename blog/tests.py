from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
# Create your tests here.
from .models import Post

class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = "aditya",
            password = "la,loli",
            email = "lake@lake.com",
        )
        self.post = Post.objects.create(
            title = "test",
            author = self.user,
            body = "test defined",
        )
    
    def test_string_representation(self):
        post = Post(title = "a title")
        self.assertEqual(str(post), post.title)
    
    def test_post_content(self):
        self.assertEqual(f"{self.post.title}", "test")
        self.assertEqual(f"{self.post.author}", "aditya")
        self.assertEqual(f"{self.post.body}", "test defined")

    def test_post_list_view(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test defined")
        self.assertTemplateUsed(response, "home.html")
    
    def test_post_detail_view(self):
        response = self.client.get('/post/1/')
        no_response = self.client.get("/post/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "test")
        self.assertTemplateUsed(response, "post_detail.html")
