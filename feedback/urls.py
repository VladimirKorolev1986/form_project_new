from django.contrib import admin
from django.urls import path
from .views import done, FeedBackView, UpdateFeedBack, DoneView

urlpatterns = [
    path('done', DoneView.as_view()),
    path('', FeedBackView.as_view()),
    path('<int:id_feedback>', UpdateFeedBack.as_view()),
]
