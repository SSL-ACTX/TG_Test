from characterai import PyCAI

client = PyCAI('characterai_token') # see https://github.com/kramcat/CharacterAI if ever... :)

char = "EEI6sjnddRIJTVC59MODiYjL0-JyDIVI2IEGLkPx2Jk"  
# Example: https://beta.character.ai/chat?char=EEI6sjnddRIJTVC59MODiYjL0-JyDIVI2IEGLkPx2Jk&source=category-carousel&category=Featured
# You can see ther 'char=' right? Copy its value :)
# Remember, most characters doesn't work at all

chat = client.chat.get_chat(char)

participants = chat['participants']

if not participants[0]['is_human']:
    tgt = participants[0]['user']['username']
else:
    tgt = participants[1]['user']['username']

while True:
    message = input('You: ')

    data = client.chat.send_message(
        chat['external_id'], tgt, message
    )

    name = data['src_char']['participant']['name']
    text = data['replies'][0]['text']

    print(f"{name}: {text}")