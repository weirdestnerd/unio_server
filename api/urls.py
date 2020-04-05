from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:username>/chat_history', views.get_user_chats,
         name='chats-for-username'),
    path('<str:username>/bot_response', views.generate_response_to_message,
         name='response-to-message'),
]
