
from django.conf import settings
import requests
def send_message_telebot(text):
    text = text.replace('_', '-')
    send_text = 'https://api.telegram.org/bot' + settings.TELEGRAM_BOT_TOKEN + '/sendMessage?chat_id=' + settings.CHAT_ID + '&parse_mode=Markdown&text=' + text
    requests.get(send_text)