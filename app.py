import os
import requests
from flask import Flask, request
app = Flask(__name__)

token = os.getenv('TELEGRAM_BOT_TOKEN')

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route(f"/{token}", methods=['POST'])
def telegram():
    
    #1. 구조 확인하기
    from_telegram = request.get_json()
    print(from_telegram)
    
    #2. 그대로 돌려보내기(메아리)
    #['message'] #=> 키없으면 에러 발생
    #.get('message') #=> 키가없으면, None
    if from_telegram.get('message') is not None:
        chat_id = from_telegram['message']['chat']['id']
        text = from_telegram['message']['text']
        requests.get(f'https://api.hphk.io/telegram/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    
    return '', 200
    
if __name__== '__main__':
    app.run(host=os.getenv('IP','0.0.0.0'),port=int(os.getenv('PORT',8080)))
    {'update_id': 285263312, 
    'message': {'message_id': 25, 
    'from': {'id': 706120014, 'is_bot': False, 'first_name': 'MinJae', 'last_name': 'Gwon', 'language_code': 'ko'}, 
    'chat': {'id': 706120014, 'first_name': 'MinJae', 'last_name': 'Gwon', 'type': 'private'}, 'date': 1545372140, 'text': '오태식이 돌아왔구나'}}