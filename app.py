from flask import Flask, request
import json
import requests

# ตรง YOURSECRETKEY ต้องนำมาใส่เองครับจะกล่าวถึงในขั้นตอนต่อๆ ไป
global LINE_API_KEY
# ห้ามลบคำว่า Bearer ออกนะครับเมื่อนำ access token มาใส่
LINE_API_KEY = 'Bearer N6X69KGY7TijrIGma2FFUm/2Z+bTjUS65QkZCcZ3LlpT2EI7JUpnNLaUopxehDCf5KOuDAOSV/GtEsX9eL63P1k53Zuo3bVyErr3MqImIuTB22DKzrTdIcu0B2Xw7ykvWsbsanseA2OFt9lN3AqX1wdB04t89/1O/w1cDnyilFU= '

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is chatbot server'
@app.route('/bot', methods=['POST'])

def bot():
    # ข้อความที่ต้องการส่งกลับ
    replyQueue = list()

    # ข้อความที่ได้รับมา
    msg_in_json = request.get_json()
    msg_in_string = json.dumps(msg_in_json)
    text = msg_in_json["events"][0]['message']['text'].lower().strip()
    print(msg_in_json["events"][0]['message']['text'].lower().strip())
    # Token สำหรับตอบกลับ (จำเป็นต้องใช้ในการตอบกลับ)
    replyToken = msg_in_json["events"][0]['replyToken']

    # ส่วนนี้ดึงข้อมูลพื้นฐานออกมาจาก json (เผื่อ)
    userID =  msg_in_json["events"][0]['source']['userId']
    msgType =  msg_in_json["events"][0]['message']['type']







    # ตรวจสอบว่า ที่ส่งเข้ามาเป็น text รึป่าว (อาจเป็น รูป, location อะไรแบบนี้ได้ครับ)
    # แต่ก็สามารถประมวลผลข้อมูลประเภทอื่นได้นะครับ
    # เช่น ถ้าส่งมาเป็น location ทำการดึง lat long ออกมาทำบางอย่าง เป็นต้น
    if(text == "สวัสดีค่ะ"):
         print('in if')
         replyQueue.append("อยากทราบวันลงทะเบียนใช่ไหมคะ")
         replyQueue.append("กรุณาพิมพ์รหัสนักศึกษาค่ะ")
         reply(replyToken, replyQueue[:5])
         return 'OK', 200

    if(text == "มีค่ะ"):
         print('in if')
         replyQueue.append("อยากรหัสอะไรเพิ่มเติมอีกดีค่ะ")
         replyQueue.append("สามารถพิมพ์รหัสนักศึกษาได้เลยค่ะ")
         reply(replyToken, replyQueue[:5])
         return 'OK', 200
    
    if(text == "ไม่มีค่ะ"):
         print('in if')
         replyQueue.append("ทางเรายินดีให้บริการค่ะ")
         replyQueue.append("ขอบคุณค่ะ")
         reply(replyToken, replyQueue[:5])
         return 'OK', 200

    if(text <= "5405000017"):
         print('in if')
         replyQueue.append("ขออภัยค่ะรหัสหมายเลขนี้ไม่มีในระบบค่ะ")
         replyQueue.append("กรุณาตรวจสอบหมายเลยรหัสใหม่อีกครั้งค่ะ")
         reply(replyToken, replyQueue[:5])
         return 'OK', 200
    if(text >= "6005004641"):
         print('in if')
         replyQueue.append("29 มีนาคม 2562")
         replyQueue.append("มีความต้องการอยากทราบรหัสอื่นเพิ่มเติมอีกไหมคะ?")  
         reply(replyToken, replyQueue[:5])
         return 'OK', 200

    if(text <= "6005004640"):
         print('in if')
         replyQueue.append("30 มีนาคม 2562")
         replyQueue.append("มีความต้องการอยากทราบรหัสอื่นเพิ่มเติมอีกไหมคะ?")    
         reply(replyToken, replyQueue[:5])
         return 'OK', 200

    if(text >= "5805002441"):
         print('in if')
         replyQueue.append("30 มีนาคม 2562")
         replyQueue.append("มีความต้องการอยากทราบรหัสอื่นเพิ่มเติมอีกไหมคะ?")    
         reply(replyToken, replyQueue[:5])
         return 'OK', 200

    if(text <= "5805002440"):
         print('in if')
         replyQueue.append("31 มีนาคม 2562")
         replyQueue.append("มีความต้องการอยากทราบรหัสอื่นเพิ่มเติมอีกไหมคะ?")    
         reply(replyToken, replyQueue[:5])
         return 'OK', 200

    if(text >= "5405000018"):
         print('in if')
         replyQueue.append("31 มีนาคม 2562")
         replyQueue.append("มีความต้องการอยากทราบรหัสอื่นเพิ่มเติมอีกไหมคะ?")    
         reply(replyToken, replyQueue[:5])
         return 'OK', 200
    
   
    


    # ตัวอย่างการทำให้ bot ถาม-ตอบได้ แบบ exact match
    # response_dict = {'สวัสดี':'สวัสดีครับ'}
    # if text in response_dict:
    #     replyQueue.append(reponse_dict[text])
    # else:
    #     replyQueue.append('ไม่รู้ว่าจะตอบอะไรดี TT')

    # ตัวอย่างการทำให้ bot ถาม-ตอบได้ แบบ non-exact match
    # โดยที่มี method ชื่อ find_closest_sentence ที่ใช้การเปรียบเทียบประโยค
    # เพื่อค้นหาประโยคที่ใกล้เคียงที่สุด อาจใช้เรื่องของ word embedding มาใช้งานได้ครับ
    # simple sentence embeddings --> https://openreview.net/pdf?id=SyK00v5xx
    # response_dict = {'สวัสดี':'สวัสดีครับ'}
    # closest = find_closest_sentence(response_dict, text)
    # replyQueue.append(reponse_dict[closest])

    # ตอบข้อความ "นี่คือรูปแบบข้อความที่รับส่ง" กลับไป
    replyQueue.append()

    # ทดลอง Echo ข้อความกลับไปในรูปแบบที่ส่งไปมา (แบบ json)
    replyQueue.append(msg_in_string)
    reply(replyToken, replyQueue[:5])

    return 'OK', 200

def reply(replyToken, textList):

    # Method สำหรับตอบกลับข้อความประเภท text กลับครับ เขียนแบบนี้เลยก็ได้ครับ

    LINE_API = 'https://api.line.me/v2/bot/message/reply'

    headers = {

        'Content-Type': 'application/json; charset=UTF-8',

        'Authorization': LINE_API_KEY

    }

    msgs = []

    for text in textList:

        msgs.append({

            "type":"text",

            "text":text

        })

    data = json.dumps({

        "replyToken":replyToken,

        "messages":msgs

    })

    requests.post(LINE_API, headers=headers, data=data)

    return



if __name__ == '__main__':

    app.run()
