from django.urls import path
from . import views

app_name = 'aichat'
urlpatterns = [
    path('ai_chat_bot/', views.Ai_chat_botView.as_view(), name="ai_chat_bot")
]