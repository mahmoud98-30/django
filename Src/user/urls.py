from django.urls import path
from . import views
app_name='user'
urlpatterns={
    path('about/', views.about, name='about'),
}