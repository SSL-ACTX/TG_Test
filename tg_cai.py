import telebot
import websockets
from characterai import PyCAI

bot = telebot.TeleBot('tg_token')
client = PyCAI('characterai_token') # see https://github.com/kramcat/CharacterAI if ever... :)

char = "EEI6sjnddRIJTVC59MODiYjL0-JyDIVI2IEGLkPx2Jk"
# Example: https://beta.character.ai/chat?char=EEI6sjnddRIJTVC59MODiYjL0-JyDIVI2IEGLkPx2Jk&source=category-carousel&category=Featured
# You can see the 'char=' right? Copy its value :)
# Remember, most characters doesn't work at all

chat = client.chat.get_chat(char)
participants = chat['participants']

if not participants[0]['is_human']:
    tgt_username = participants[0]['user']['username']
else:
    tgt_username = participants[1]['user']['username']

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    data = client.chat.send_message(chat['external_id'], tgt_username, message.text)

    name = data['src_char']['participant']['name']
    text = data['replies'][0]['text']

    bot.reply_to(message, f"{name}: {text}")

bot.polling()
