import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage,ImageSendMessage,FlexSendMessage,VideoSendMessage


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_image_url(reply_token, img_url):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, ImageSendMessage(original_content_url=img_url, preview_image_url=img_url))
    return "OK"

def send_video_url(reply_token, img_url):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, VideoSendMessage(original_content_url=img_url, preview_image_url='https://i.imgur.com/R9BAHi3.jpg'))
    return "OK"

def send_flex_message(reply_token, flex_msg):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, FlexSendMessage("menu", flex_msg))

    return "OK"
    