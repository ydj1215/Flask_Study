from flask import Flask
from routes.data import get_data
from routes.weather import get_weather
from routes.movie import get_movie
from flask_cors import CORS

# __name__ 은 파이썬에서 사용되는 특별한 변수로 현재 모듈의 이름을 의미하며,
# 위와 같이 선언하면 app 객체가 현재 모듈에서 생성된다.
# 즉 다른 모듈에서 이 코드를 import할 때는 내장 서버가 실행되지 않는다.
app = Flask(__name__) # 해당 Flask 앱은 "app.py"에 존재한다
CORS(app, origins=['http://localhost:3000'])

# @app.route를 사용하지 않는 방식
# rule : url
# endpoint : 일반적으로 View 함수의 이름을 정의
app.add_url_rule('/api/data/', 'get_data', get_data, methods=['GET'])
app.add_url_rule('/api/movie/', 'get_movie', get_movie, methods=['GET'])
app.add_url_rule('/api/weather/', 'get_weather', get_weather, methods=['GET'])
# app.add_url_rule('/api/weather2', 'get_weather2', get_weather2, methods=['GET'])
# app.add_url_rule('/api/query', 'get_query', get_query, methods=['GET'])
# app.add_url_rule('/api/item/<item_id>', 'get_path_item', get_path_item, methods=['GET'])

if __name__ == '__main__': # 해당 앱에서 Flask 앱이 실행될 때,
    app.run(debug=True)
# else : 다른 파일에서 "app.py"를 import 한 후에 실행 할 때의 작동 방식을 정의