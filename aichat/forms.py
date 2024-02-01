import os

from django import forms

class Ai_chat_botForm(forms.Form):
    message = forms.CharField(label="メッセージ", widget=forms.Textarea, max_length=200)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["message"].widget.attrs["class"] = "form-control"
        self.fields["message"].widget.attrs["placeholder"] = "メッセージをここに入力してください。"

    def send_message(self):
        message = self.cleaned_data['message']
        return message