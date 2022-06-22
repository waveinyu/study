# jinja와 mogoDB를 이용해서 index 페이지가 렌더링되면 DB정보에 따라 정보가 나올 수 있게 app.py를 만들어주세요
# index에는 렌더링 되자마자 실행되는 함수에 url:"/info"로 되어있으니 app.py에서 api를 그것에 맞추어 크롤링하여 DB에 데이터를 먼저 넣어야 합니다
# !!!저희가 클론하고 있는 여행프로젝트를 참고하시면 수월합니다.(여기서는 jinja와 DB의 흐름을 알아볼것이기에)!!!
from flask import Flask, render_template
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.sis7sux.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


app = Flask(__name__)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5500, debug=True)
    
    