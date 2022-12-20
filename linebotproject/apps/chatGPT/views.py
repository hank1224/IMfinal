from django.shortcuts import render

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, TextMessage, QuickReply, QuickReplyButton, MessageAction

import openai

Line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

from chatGPT.models import lineUser
from CWBdata.models import hazards, rain

#Line_bot_api.push_message('Uf496dcee2f5c542148d67e7a2a418a22', TextSendMessage(text=tt.sPhenomena))

def rain_reply(event): #即時時雨量
    message=""
    try:
        lineUserSet = lineUser.objects.filter(sLineID = event.source.user_id).values('sCity')
        userCity = str(lineUserSet[0]['sCity'])
        try:
            if userCity == "None":
                    message = "您尚未完成綁定\n請輸入: 綁定地區"
            else:
                queryset = rain.objects.filter(sCity = userCity).values()                
                message = userCity+" 即時雨量如下(毫米)：\n10分鐘: "+str(queryset[0]['sMIN_10'])+"\n1小時: "\
                    +str(queryset[0]['sRAIN'])+"\n3小時: "+str(queryset[0]['sHOUR_3'])+"\n6小時: "\
                    +str(queryset[0]['sHOUR_6'])+"\n12小時: "+str(queryset[0]['sHOUR_12'])+"\n24小時: "\
                    +str(queryset[0]['sHOUR_24'])+"\n截至現在今日雨量為： "+str(queryset[0]['sNOW'])
        except:
            message = "CWBdata sql err"
    except:
        message = "lineUser sql err"

    Line_bot_api.reply_message(event.reply_token, TextSendMessage(text=message))

def bind_N_city(event): #北部地區
    try:
        replyhead = "設定用戶地區通知為"
        message = TextSendMessage(
            text= "請選擇一個想收到的縣市通知",
            quick_reply=QuickReply(
                items=[ 
                    QuickReplyButton(action=MessageAction(label="臺北市", text= replyhead + "臺北市")),
                    QuickReplyButton(action=MessageAction(label="基隆市", text= replyhead + "基隆市")),
                    QuickReplyButton(action=MessageAction(label="新北市", text= replyhead + "新北市")),
                    QuickReplyButton(action=MessageAction(label="桃園市", text= replyhead + "桃園市")),
                    QuickReplyButton(action=MessageAction(label="新竹縣", text= replyhead + "新竹縣")),
                    QuickReplyButton(action=MessageAction(label="新竹市", text= replyhead + "新竹市"))
                ]
            )
        )
        Line_bot_api.reply_message(event.reply_token, message)
    except:
        Line_bot_api.reply_message(event.reply_token, TextSendMessage(text="choseCity err"))

def bind_W_city(event): #西部、中部地區
    try:
        replyhead = "設定用戶地區通知為"
        message = TextSendMessage(
            text= "請選擇一個想收到的縣市通知",
            quick_reply=QuickReply(
                items=[ 
                    QuickReplyButton(action=MessageAction(label="苗栗縣", text= replyhead + "苗栗縣")),
                    QuickReplyButton(action=MessageAction(label="臺中市", text= replyhead + "臺中市")),
                    QuickReplyButton(action=MessageAction(label="彰化縣", text= replyhead + "彰化縣")),
                    QuickReplyButton(action=MessageAction(label="南投縣", text= replyhead + "南投縣")),
                    QuickReplyButton(action=MessageAction(label="雲林縣", text= replyhead + "雲林縣")),
                ]
            )
        )
        Line_bot_api.reply_message(event.reply_token, message)
    except:
        Line_bot_api.reply_message(event.reply_token, TextSendMessage(text="choseCity err"))
        
def bind_E_city(event): #東部地區
    try:
        replyhead = "設定用戶地區通知為"
        message = TextSendMessage(
            text= "請選擇一個想收到的縣市通知",
            quick_reply=QuickReply(
                items=[ 
                    QuickReplyButton(action=MessageAction(label="宜蘭縣", text= replyhead + "宜蘭縣")),
                    QuickReplyButton(action=MessageAction(label="花蓮縣", text= replyhead + "花蓮縣")),
                    QuickReplyButton(action=MessageAction(label="臺東縣", text= replyhead + "臺東縣")),
                ]
            )
        )
        Line_bot_api.reply_message(event.reply_token, message)
    except:
        Line_bot_api.reply_message(event.reply_token, TextSendMessage(text="choseCity err"))

def bind_S_city(event): #南部地區
    try:
        replyhead = "設定用戶地區通知為"
        message = TextSendMessage(
            text= "請選擇一個想收到的縣市通知",
            quick_reply=QuickReply(
                items=[ 
                    QuickReplyButton(action=MessageAction(label="嘉義縣", text= replyhead + "嘉義縣")),
                    QuickReplyButton(action=MessageAction(label="嘉義市", text= replyhead + "嘉義市")),
                    QuickReplyButton(action=MessageAction(label="臺南市", text= replyhead + "臺南市")),
                    QuickReplyButton(action=MessageAction(label="高雄市", text= replyhead + "高雄市")),
                    QuickReplyButton(action=MessageAction(label="屏東縣", text= replyhead + "屏東縣"))
                ]
            )
        )
        Line_bot_api.reply_message(event.reply_token, message)
    except:
        Line_bot_api.reply_message(event.reply_token, TextSendMessage(text="choseCity err"))

def bind_Outer_city(event): #離島地區
    try:
        replyhead = "設定用戶地區通知為"
        message = TextSendMessage(
            text= "請選擇一個想收到的縣市通知",
            quick_reply=QuickReply(
                items=[ 
                    QuickReplyButton(action=MessageAction(label="澎湖縣", text= replyhead + "澎湖縣")),
                    QuickReplyButton(action=MessageAction(label="金門縣", text= replyhead + "金門縣")),
                    QuickReplyButton(action=MessageAction(label="連江縣", text= replyhead + "連江縣"))
                ]
            )
        )
        Line_bot_api.reply_message(event.reply_token, message)
    except:
        Line_bot_api.reply_message(event.reply_token, TextSendMessage(text="choseCity err"))

def bindCity(event): #用戶綁定縣市
    try:
        replyhead = "選擇"
        message = TextSendMessage(
            text= "請選擇地區",
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(action=MessageAction(label="北部地區", text= replyhead + "北部地區")),
                    QuickReplyButton(action=MessageAction(label="中部地區", text= replyhead + "中部地區")),
                    QuickReplyButton(action=MessageAction(label="南部地區", text= replyhead + "南部地區")),
                    QuickReplyButton(action=MessageAction(label="東部地區", text= replyhead + "東部地區")),
                    QuickReplyButton(action=MessageAction(label="離島地區", text= replyhead + "離島地區")),
                ]
            )
        )
        Line_bot_api.reply_message(event.reply_token, message)
    except:
        Line_bot_api.reply_message(event.reply_token, TextSendMessage(text="choseCity err"))

def insertCity(event): #寫入City到sql
    try:
        Ccity = event.message.text[9:12]
        profile = Line_bot_api.get_profile(event.source.user_id)
        try:
            a=""
            if lineUser.objects.update_or_create(sLineID = event.source.user_id)[1] == False: #如果已存在
                lineUser.objects.filter(sLineID = event.source.user_id).update(sName = profile.display_name, sCity=Ccity)
                a="更新"
            else:
                lineUser.objects.filter(sLineID = event.source.user_id).update(sName = profile.display_name, sCity=Ccity)
                a="創建"
            wrcheck = lineUser.objects.get(sLineID = event.source.user_id)
            message = TextSendMessage("已"+ a + wrcheck.sName + "的地區綁定為"+ Ccity)
            Line_bot_api.reply_message(event.reply_token, message)
        except:
            Line_bot_api.reply_message(event.reply_token, TextSendMessage(text="insertCity sql err"))
    except:
        Line_bot_api.reply_message(event.reply_token, TextSendMessage(text="insertCity err"))

def setCityBlank(event): #解除綁定縣市通知
    try:
        profile = Line_bot_api.get_profile(event.source.user_id)
        try:
            a="移除"
            if lineUser.objects.update_or_create(sLineID = event.source.user_id)[1] == False: #如果已存在
                lineUser.objects.filter(sLineID = event.source.user_id).update(sName = profile.display_name, sCity=None)
                a="更新"
            else:
                lineUser.objects.filter(sLineID = event.source.user_id).update(sName = profile.display_name, sCity=None)
            wrcheck = lineUser.objects.get(sLineID = event.source.user_id)
            message = TextSendMessage("已"+ a + wrcheck.sName + "的地區綁定")
            Line_bot_api.reply_message(event.reply_token, message)
        except:
            Line_bot_api.reply_message(event.reply_token, TextSendMessage(text="setCityBlank sql err"))
    except:
        Line_bot_api.reply_message(event.reply_token, TextSendMessage(text="setCityBlank err"))

def chatGPT(event):
    try:
        openai.api_key = settings.CHAT_GPT_TOKEN
        ans = openai.Completion.create(
            model="text-davinci-003",
            prompt= event.message.text,
            max_tokens=700,
            temperature=0.8
        )
        message = ans['choices'][0]['text']

        # if str(message).startswith("\n",beg=1,end=10):
        # 需要刪除開頭空格
        Line_bot_api.reply_message(event.reply_token, TextSendMessage(text= message))
    except:
        Line_bot_api.reply_message(event.reply_token, TextSendMessage(text='chatGPT err'))


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    mtext = event.message.text

                    if mtext == '@即時時雨量':
                        rain_reply(event)

                    if mtext == '@降水預測':
                        Line_bot_api.reply_message(event.reply_token, TextSendMessage(text="1"))
                    if mtext == '@未來兩日預報':
                        Line_bot_api.reply_message(event.reply_token, TextSendMessage(text="2"))
                    if mtext == '@資料來源':
                        Line_bot_api.reply_message(event.reply_token, TextSendMessage(text='中央氣象局提供'))
                    if mtext == '@網站':
                        Line_bot_api.reply_message(event.reply_token, TextSendMessage(text='網站'))
                    if mtext == '@歷年淹水範圍':
                        Line_bot_api.reply_message(event.reply_token, TextSendMessage(text='淹水'))

                    if mtext == '綁定地區':
                        bindCity(event)

                    if mtext == '解除綁定':
                        setCityBlank(event)

                    if mtext.startswith('設定用戶地區通知為') == True:
                        insertCity(event)

                    if mtext == '選擇北部地區':
                        bind_N_city(event)

                    if mtext == '選擇中部地區':
                        bind_W_city(event)

                    if mtext == '選擇南部地區':
                        bind_S_city(event)

                    if mtext == '選擇東部地區':
                        bind_E_city(event)

                    if mtext == '選擇離島地區':
                        bind_Outer_city(event)

                    if mtext == '我的ID':
                        try:
                            Line_bot_api.reply_message(event.reply_token, TextSendMessage(text=event.source.user_id))
                        except:
                            Line_bot_api.reply_message(event.reply_token, TextSendMessage(text="Get user_id err"))
                    
                    if mtext.startswith('我想問') == True:
                        chatGPT(event)

                    else:
                        #Line_bot_api.reply_message(event.reply_token, TextSendMessage(text="all else"))
                        pass #掛上去就500 "message": "Invalid reply token"

        return HttpResponse()
    else:
        return HttpResponseBadRequest()

    

# Create your views here.