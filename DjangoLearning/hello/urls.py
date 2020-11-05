from django.urls import path
from .views import *

urlpatterns = [
    path('', UserView.as_view(), name="index"),
    path("create", CreateView.as_view(), name="create"),
    path('edit/<int:num>', EditView.as_view(), name='edit'),
    path('delete/<int:num>', DeleteView.as_view(), name='delete'),
]
