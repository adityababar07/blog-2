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
    
    def test_get_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(), '/post/1/') 
    
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

    def test_post_create_view(self):
        response = self.client.post(reverse('post_new'), {
            'title': 'new_title',
            'author': self.user,
            'body': 'this is a test',
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'new_title')
        self.assertContains(response, 'this is a test')

    def test_post_update_view(self):
        response = self.client.post(reverse('post_edit', args='1'), {
            'title': 'update_title',
            'body': 'new content',
        })
        self.assertEqual(response.status_code, 302)

    def test_post_delete_view(self):
        response = self.client.post(reverse('post_delete', args='1'))
        self.assertEqual(response.status_code, 302)

class SignUpPageTests(TestCase):
    
    username = 'newuser'
    email = 'newuser@django.com'

    def test_signup_pages_status_code(self):
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.staus_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_users_correct_template(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_form(self):
        newuser = get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all() [0].username, self.username)
        self.assertEqual(get_user_model().objects.all() [0].email, self.email)

