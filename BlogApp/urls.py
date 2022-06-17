from django.urls import path
from .views import *

urlpatterns = [
    path('post/<slug:pk>/', PostDetailView.as_view(), name='detail_post'),
    path('', HomeView.as_view(), name='home'),
]
