from django.urls import path
from ar import views

urlpatterns=[
    path('ar',views.losar),
]