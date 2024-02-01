import logging
import random

from django.contrib import messages
# from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import Ai_chat_botForm
from .models import Chat
from django.views.generic import FormView
from django.core import serializers
from .ai_chat_bot import AiChatBot

logger = logging.getLogger(__name__)

# ai_chat_bot
class Ai_chat_botView(FormView):
    template_name = "ai_chat_bot.html"
    form_class = Ai_chat_botForm
    success_url = "/ai_chat_bot/"

    def form_valid(self, form):
        # ユーザーのチャットを取得する
        chats = Chat.objects.all()

        # チャットが3つ以上なら最古のものを削除
        if len(chats) >= 3:
            chats[0].delete()

        message = form.send_message()
        emoji = random.choice(["✌️", "♫", "✨", "❄️"])
        response = AiChatBot(f"DJ AI {emoji} : ", message)  # AIチャットボット
        chat = Chat(message=message, response=response)
        chat.save()
        data = serializers.serialize('json', [chat])
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Invalid form")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['chats'] = Chat.objects.all()
        return context