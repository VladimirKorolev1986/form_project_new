from django.contrib import admin
from django.urls import path
from .views import FeedBackView, UpdateFeedBack, DoneView, ListFeedBack

urlpatterns = [
    path('done', DoneView.as_view()),
    path('list', ListFeedBack.as_view()),
    path('', FeedBackView.as_view()),
    path('<int:id_feedback>', UpdateFeedBack.as_view()),
]
