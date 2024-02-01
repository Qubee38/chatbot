from django.db import models

class Chat(models.Model):
    message = models.TextField()
    response = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, **kwargs):
        # データベース内の Chat インスタンス数を確認
        chats = Chat.object.all()
        if chats.count() >= 3:
            # 古いものから削除
            oldest_chat = chats.order_by('created_at').first()
            oldest_chat.delete()
        
        # インスタンスを作成
        chat = cls(**kwargs)
        chat.save()
        return chat