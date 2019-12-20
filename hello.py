from flask import Flask, escape, request, render_template
import random
import requests
import json

app = Flask(__name__)

@app.route('/')                               # '/'는 root를 의미
def hello():
    name = request.args.get("name", "웹서버에 입장하셨습니다.")
    return f'반갑습니다. {escape(name)}!'

@app.route('/myname')                             
def myname():                                
    return '이경호입니다.'

# 랜덤으로 점심메뉴 추천해주는 서버
@app.route('/lunch')
def lunch():
    menus = ['양자강','김밥까페','20층','순남시래기']
    lunch = random.choice(menus)
    return lunch

@app.route('/idol')
def idol():
    idols = {
        'bts':{'RM':25,
             '진':25,
             '슈가':25,
             '제이홉':25,
             '지민':25,
             '뷔정국':25
             },
        'rv':'레드벨벳',
        'pinkle':{
            '이효리': '꺼꾸로해도 이효리',
            '옥주현': '35'
                 },
        'ses':['유진','바다','슈']
        }
    return idols


@app.route ('/post/<int:num>')
def post(num):
    posts = ['0번 포스트','1번 포스트','2번 포스트']
    return posts[num]

# 실습 cube 뒤에 전달된 수의 세제곱수를 화면에 보여주세요.
# 1 -> 1
# 2 -> 8
# 3 -> 27
# str(): 숫자를 문자로 바꿔주는 함수

@app.route('/cube/<int:num>')
def cube(num):
    cubed = num * num * num
    return str(cubed)

# 클라이언트에게 html 파일을 주고 싶어요!
@app.route('/index')
def html():
    return render_template('hello.html')


@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age = request.args.get('age')

    return render_template('pong.html',age_in_html=age)


# lotto 번호를 가져와서 보여주는 서버
# https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=회차번호

@app.route('/lotto_result/<int:round>')
def lotto_result(round):
    url = f'https://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo={round}' 
    result = requests.get(url).json()

    winner = []
    for i in range (1,7):
        winner.append(result.get(f'drwtNo{i}'))
        # winner.append(result[f'drwtNo{i}'])

    winner.append(result.get('bnusNo'))    

    return json.dumps(winner)



    
app.run(debug=True)           # Python 에서 서버 실행하기