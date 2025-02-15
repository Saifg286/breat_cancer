# prediction/urls.py
from django.urls import path
from .views import predict_view

urlpatterns = [
    path('', predict_view, name='predict'),  # Empty path to call the predict_view function
]
