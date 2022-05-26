from flask import Flask, request, jsonify
from flask_cors import CORS
from db import create_table
import news_models

app = Flask(__name__)
CORS(app)

@app.route('/news', methods=['GET']) ###############
def get_news():
    try:
        result = news_models.get_news()
        data = {
                'status': 200,
                'data': result
            }
        resp = jsonify(data)
        resp.status_code = 200
        return resp

    except:
        data = {
                'status': 404,
                'message': "Data Not Found!"
            }
        resp = jsonify(data)
        resp.status_code = 404
        return resp

@app.route('/news/<news_id>', methods=['GET']) #############
def get_news_by_id(news_id):
    try:
        result = news_models.get_news_by_id(news_id)
        data = {
                'status': 200,
                'data': result
            }
        
        resp = jsonify(data)
        resp.status_code = 200
        return resp

    except:
        data = {
                'status': 404,
                'message': "Data Not Found!"
            }
        resp = jsonify(data)
        resp.status_code = 404
        return resp
           
@app.route('/news', methods=['POST']) ##############
def insert_news():
    news_details = request.json
    title = news_details['title']
    content = news_details['content']
    datetime = news_details['datetime']
    flag = news_details['flag']

    try:
        result = news_models.insert_news(title, content, datetime, flag)
        data = {
                'status': 201,
                'message': 'Success!'
            }
        resp = jsonify(data)
        resp.status_code = 201
        return resp

    except:
        data = {
                'status': 404,
                'message': "Data Not Found!"
            }
        resp = jsonify(data)
        resp.status_code = 404
        return resp

@app.route('/news/<news_id>', methods=['PUT']) ############
def update_news(news_id):
    news_details = request.json
    news_id =  news_details['news_id']
    title =  news_details['title']
    content =  news_details['content']
    datetime =  news_details['datetime']
    flag =  news_details['flag']

    try:
        result = news_models.update_news(news_id, title, content, datetime, flag)
        data = {
                'status': 200,
                'message': 'Success!'
            }
        resp = jsonify(data)
        resp.status_code = 200
        return resp

    except:
        data = {
                'status': 404,
                'message': "Data Not Found!"
            }
        resp = jsonify(data)
        resp.status_code = 404
        return resp

@app.route('/news/<news_id>', methods=['PATCH'])
def patch_news(news_id):
    news_details = request.json
    news_id =  news_details['news_id']
    flag =  news_details['flag']

    try:
        result = news_models.patch_news(news_id, flag)
        data = {
                'status': 200,
                'message': 'Success!'
            }
        
        resp = jsonify(data)
        resp.status_code = 200
        return resp

    except:
        data = {
                'status': 404,
                'message': "Data Not Found!"
            }
        resp = jsonify(data)
        resp.status_code = 404
        return resp

@app.route('/news/<news_id>', methods=['DELETE']) ############
def delete_news(news_id):
    try:
        result = news_models.delete_news(news_id)
        data = {
                'status': 200,
                'message': "Success!"
            }
        resp = jsonify(data)
        resp.status_code = 200
        return resp

    except:
        data = {
                'status': 404,
                'message': "Data Not Found!"
            }
        resp = jsonify(data)
        resp.status_code = 404
        return resp


################ ERROR HANDLER ################
    
@app.errorhandler(404)
def not_found(error=None):
    message = {
                'status': 404,
                'message': 'Not Found: ' + request.url
            }
    resp = jsonify(message)
    resp.status_code = 404
    return resp

###############################################

if __name__ == "__main__":
    create_table()
    #print(get_data())
    app.run(debug=True)

