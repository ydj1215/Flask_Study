from flask import Response, json

data = {
    'stations': ['강남역', '역삼역', '서울역'],
    'ridership': [1000, 800, 1200]
}

def get_data():
    response = Response(
        json.dumps(data, ensure_ascii=False),
        mimetype='application/json; charset=utf-8'
    )
    return response
