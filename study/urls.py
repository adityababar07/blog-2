from django.urls import path

from .views import (HomePageView,
                    StudyListView,
                    StudyDetailView,
                    StudyCreateView,
                    StudyUpdateView,
                    StudyDeleteView,
                    AboutTemplateView,)

urlpatterns = [
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('post/delete/<int:pk>', StudyDeleteView.as_view(), name='post_delete'),
    path('post/edit/<int:pk>', StudyUpdateView.as_view(), name='post_edit'),
    path('post/new', StudyCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', StudyDetailView.as_view(), name='post_detail'),
    path('post/', StudyListView.as_view(), name='post_list'),
    path('', HomePageView.as_view(), name='home'),
]