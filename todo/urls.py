from django.urls import path

from .views import (HomePageView,
                    StudyListView,
                    StudyDetailView,
                    StudyCreateView,
                    StudyUpdateView,
                    StudyDeleteView,
                    AboutTemplateView,
                    StudyCommentCreateView)

urlpatterns = [
    path('about/', AboutTemplateView.as_view(), name='about'),
    # path('todo/<int:pk>/comment/', StudyCommentCreateView.as_view(), name='comment_new'),
    path('todo/delete/<int:pk>', StudyDeleteView.as_view(), name='todo_delete'),
    path('todo/edit/<int:pk>', StudyUpdateView.as_view(), name='todo_edit'),
    path('todo/new', StudyCreateView.as_view(), name='todo_new'),
    path('todo/<int:pk>/', StudyDetailView.as_view(), name='todo_detail'),
    path('todo/', StudyListView.as_view(), name='todo_list'),
    path('', HomePageView.as_view(), name='home'),
]