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
import re


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
    ### 抓到顧客的資料 ###
    profile = line_bot_api.get_profile(event.source.user_id)
    uid = profile.user_id #使用者ID
    usespeak = str(event.message.text) #使用者講的話
    
    #read db
    #stat = mongodb.test_connect()
    #line_bot_api.push_message(uid, TextSendMessage(stat))

    # 先判斷是否是使用者要用來存股票的
    #if re.match('[+][0-9]{4}',usespeak):
    #    line_bot_api.push_message(uid, TextSendMessage('很熱'))
    #elif re.match('[-][0-9]{4}',usespeak): # 刪除存在資料庫裡面的股票
    #    line_bot_api.push_message(uid, TextSendMessage('很冷'))
    #else:
    #    data = mongodb.get_data()
    #   for i in data:
    #        temp = i['temp']
    #        humi = i['humi']
    #        line_bot_api.push_message(uid, TextSendMessage('目前溫度：' + str(temp) + ', 目前濕度：' + str(humi)))
    
    temp_22 = '葡萄酒要變酸拉'
    temp_21 = '溫室效應沒酒喝'
    temp_20 = '預計3年6個月發酵完成'
    temp_19 = '發酵趨緩'
    temp_18 = '冷到不想發笑'

    humi_76 = '這濕度會發霉'
    humi_73 = '除濕機自動運轉'
    humi_70 = '完美濕度'
    humi_67 = '地球暖化濕度不足'
    humi_64 = '水分不足'

    send_str = ''

    #get temp an humi
    data = mongodb.get_data()
    for i in data:
        temp = i['temp']
        humi = i['humi']
        line_bot_api.push_message(uid, TextSendMessage('目前溫度：' + str(temp) + ', 目前濕度：' + str(humi)))
    
    if temp >= 22.0:
        send_str = temp_22
    elif temp >= 21.0:
        send_str = temp_21
    elif temp >= 20.0:
        send_str = temp_20
    elif temp >= 19.0:
        send_str = temp_19
    else:
        send_str = temp_18

    send_str += ', '

    if humi >= 76.0:
        send_str += humi_76
    elif temp >= 73.0:
        send_str += humi_73
    elif temp >= 70.0:
        send_str += humi_70
    elif temp >= 67.0:
        send_str += humi_67
    else:
        send_str += humi_64

    #print(send_str)
    ine_bot_api.push_message(uid, TextSendMessage(send_str))

    return 0


#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

