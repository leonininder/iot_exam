#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

#self
import mongodb
#import re


app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('/YdOJvjT4og6YuQowSzdJEZDYd9b2mJ3pbfnw1lPcnhyBKL/uCtSihzpmWYWfQz73UIlxxmojN5KPhGzsLdAN8v5CDXV3lGtqFzBYuwr4rCabiQTQUNsPjRdv+YmDsDG/9ClwwKmBTdyun+IKWyNWQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('535b63b5ac03898a88ad322cca64f395')
# User id
line_bot_api.push_message('U34ec65fa99a75eac948509e49894839a', TextSendMessage(text='start, yo~'))

# listening to /callback Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


#訊息傳遞區塊
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #message = TextSendMessage(text=event.message.text)
    #line_bot_api.reply_message(event.reply_token,message)
    
    #read db
    stat = mongodb.test_connect()
    line_bot_api.push_message(uid, TextSendMessage('test'))


#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

