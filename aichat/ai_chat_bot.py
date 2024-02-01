import openai
import os
import random

# import langchain

openai.api_type = os.getenv('OPENAI_API_TYPE')
openai.api_base = os.getenv('OPENAI_API_BASE')
openai.api_version = os.getenv('OPENAI_API_VERSION')
openai.api_key = os.getenv('OPENAI_API_KEY')


def AiChatBot(name, prompt):

    messages = [{
    'role': 'system', 
    'content': 'あなたは日本で有名なラッパーです。「ユーザーの質問」に100文字程度のバースで回答してください。 \
        文章は可能な限り「回答例」のように語尾に韻を踏んでください。 \
        回答例: しかと見ときな格の違い キッズとキングの箔の違い お前殺すぜ覚悟しな ここに転がるカスの死体 \
        ユーザーの質問：'
    }]

    messages.append({'role': 'user', 'content': prompt})
    ai_response = openai.ChatCompletion.create(messages = messages, engine='{Model Name}')
    return name + ai_response.choices[0].message.content + "\n"