from django.urls import path

from .views import (HomePageView,
                    BlogListView,
                    BlogDetailView,
                    BlogCreateView,
                    BlogUpdateView,
                    BlogDeleteView)

urlpatterns = [
    path('post/delete/<int:pk>', BlogDeleteView.as_view(), name='post_delete'),
    path('post/edit/<int:pk>', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('post/', BlogListView.as_view(), name='post_list'),
    path('', HomePageView.as_view(), name='home'),
]