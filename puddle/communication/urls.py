from django.urls import path

from . import views

app_name = 'communication'

urlpatterns = [
    path('send/', views.send, name='send'),
    path('send/<str:to>/', views.send, name='send'),
    path('', views.inbox, name='inbox'),
    path('message/<int:message_id>/', views.message_detail, name='message_detail'),
    path('delete/<int:message_id>/', views.delete_message, name='delete_message'),
]