# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, FlexSendMessage, TextSendMessage

# 建立 Flask 應用程式
app = Flask(__name__)

# 設定 Line Bot API 和 Webhook Handler
line_bot_api = LineBotApi('v8Enq4ZezmDT5zEDeZvTc7L8z2ydo3ihjyZjL/oDCVcn29ZNThlmxFAjmHRNZ3CMHcaZSe8hh0K+itGHZWjWYFjIj0EEjRizFHQFVA+bYINb4MBNxuc5AWcFfmjB6Or+LeRyDzxq6JucIwjgC238+AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('756e1f0671b2abad37750f48b590eae0')

# 定義 /callback 路由，處理 Line Webhook 請求
@app.route("/callback", methods=['POST'])
def callback():
    # 獲取 X-Line-Signature 標頭
    signature = request.headers['X-Line-Signature']

    # 獲取請求的主體
    body = request.get_data(as_text=True)
    try:
        # 處理 webhook 主體與簽名
        handler.handle(body, signature)
    except InvalidSignatureError:
        # 簽名無效時回傳 400 錯誤
        abort(400)
    return 'OK'

# 處理文本消息的函數
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    mtext = event.message.text
    if mtext == '關於我們':
        sendFlex(event)
    elif mtext == '預約資訊':
        sendmessage(event)
    elif mtext == '預約':
        sendMessage(event)
        
# 發送預約資訊消息的函數
def sendMessage(event):
    try:
        message = TextSendMessage(
            text=(
                "本店提供「線上預約」及現場候位。\n"
                "每月20號前，公告次月班表並開放預約。\n\n"
                "恕不接受當日取消預約。\n"
                "爽約三次(含以上)者，取消預約資格。\n\n"
                "為顧及其他顧客時間權益，「遲到者」理髮師將可能無法為您服務。\n\n"
                "剪髮價格依理髮師而有所不同，可指名理髮師，指名不加價。\n\n"
                "--------------------------------\n\n"
                "如要預約，請輸入以下資訊並回傳!\n\n"
                "姓名:\n"
                "電話:\n"
                "服務項目:\n"
                "預約日期:"
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=f'發生錯誤！{str(e)}'))


       
# 發送預約資訊消息的函數
def sendmessage(event):
    try:
        message = TextSendMessage(
            text=(
                "本店提供「線上預約」及現場候位。\n\n"
                "每月20號前，公告次月班表並開放預約。\n\n"
                "恕不接受當日取消預約。\n\n"
                "爽約三次(含以上)者，取消預約資格。\n\n"
                "為顧及其他顧客時間權益，「遲到者」理髮師將可能無法為您服務。\n\n"
                "剪髮價格依理髮師而有所不同，可指名理髮師，指名不加價。\n\n"
                "--------------------------------\n\n"
                "如要預約，請輸入以下資訊並回傳!\n\n"
                "姓名:\n\n"
                "電話:\n\n"
                "服務項目:\n\n"
                "預約日期:"
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=f'發生錯誤！{str(e)}'))


# 送出彈性消息的函數
def sendFlex(event):
    try:
        bubble = {
            "type": "bubble",
            "hero": {
                "type": "image",
                "url": "https://lh3.googleusercontent.com/p/AF1QipPW2YUnL6NzXKUtZiUOCp4GWtQQVI9gnphdQ7-u=s680-w680-h510",
                "size": "full",
                "aspectRatio": "20:13",
                "aspectMode": "cover",
                "action": {
                    "type": "uri",
                    "uri": "https://line.me/"
                }
            },
            "body": {
                "type": "box",
                "layout": "vertical",
                "contents": [
                    {
                        "type": "text",
                        "text": "G.A Hair Salon",
                        "weight": "bold",
                        "size": "xl",
                        "style": "italic"
                    },
                    {
                        "type": "box",
                        "layout": "baseline",
                        "margin": "md",
                        "contents": [
                            {
                                "type": "icon",
                                "size": "sm",
                                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                            },
                            {
                                "type": "icon",
                                "size": "sm",
                                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                            },
                            {
                                "type": "icon",
                                "size": "sm",
                                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                            },
                            {
                                "type": "icon",
                                "size": "sm",
                                "url": "https://developers-resource.landpress.line.me/fx/img/review_gold_star_28.png"
                            },
                            {
                                "type": "icon",
                                "size": "sm",
                                "url": "https://static-00.iconduck.com/assets.00/star-half-icon-512x512-9vvvuf2x.png"
                            },
                            {
                                "type": "text",
                                "text": "4.5",
                                "size": "sm",
                                "color": "#999999",
                                "margin": "md",
                                "flex": 0
                            }
                        ]
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "margin": "lg",
                        "spacing": "sm",
                        "contents": [
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Place",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 1
                                    },
                                    {
                                        "type": "text",
                                        "text": "106台北市大安區忠孝東路四段216巷40弄7-1號1樓",
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 5
                                    }
                                ]
                            },
                            {
                                "type": "box",
                                "layout": "baseline",
                                "spacing": "sm",
                                "contents": [
                                    {
                                        "type": "text",
                                        "text": "Time",
                                        "color": "#aaaaaa",
                                        "size": "sm",
                                        "flex": 1
                                    },
                                    {
                                        "type": "text",
                                        "text": "11:00-19:00 每週一公休",
                                        "wrap": True,
                                        "color": "#666666",
                                        "size": "sm",
                                        "flex": 5
                                    }
                                ]
                            }
                        ]
                    }
                ],
                "backgroundColor": "#f0ebe5"
            },
            "footer": {
                "type": "box",
                "layout": "vertical",
                "spacing": "sm",
                "contents": [
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                            "type": "message",
                            "label": "CALL",
                            "text": "02 8773 0567"
                        }
                    },
                    {
                        "type": "button",
                        "style": "link",
                        "height": "sm",
                        "action": {
                            "type": "uri",
                            "label": "WEBSITE",
                            "uri": "https://www.google.com/search?gs_ssp=eJzj4tVP1zc0TDKrKkrPMcoxYLRSNagwNjExSkxKNrUwMzQ0sUwxtTKosDQ2TkwztjSyNDU2SzIzS_HiS9dLVMhIzCxSKE7Myc8DAKLmE6g&q=g.a+hair+salon&rlz=1C1GCEU_zh-HKTW1113&oq=G.A+&gs_lcrp=EgZjaHJvbWUqEAgFEC4YrwEYxwEYgAQYjgUyBggAEEUYOTIHCAEQABiABDIHCAIQABiABDIHCAMQABiABDINCAQQLhivARjHARiABDIQCAUQLhivARjHARiABBiOBTIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCTc4ODRqMGoxNagCBLACAQ&sourceid=chrome&ie=UTF-8#ip=1&lrd=0x3442abc5861149d5:0x933af3929536b66d,1,,,,"
                        }
                    },
                    {
                        "type": "box",
                        "layout": "vertical",
                        "contents": [],
                        "margin": "sm"
                    }
                ],
                "flex": 0,
                "backgroundColor": "#E3D0CC"
            }
        }

        message = FlexSendMessage(alt_text="關於我們範例", contents=bubble)
        line_bot_api.reply_message(event.reply_token, message)
    except Exception as e:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=f'發生錯誤！{str(e)}'))

if __name__ == '__main__':
    app.run()