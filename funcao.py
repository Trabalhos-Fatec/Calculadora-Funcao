from flask import Flask, request, jsonify
from flask_cors import CORS
from urllib import parse
import math


app = Flask(__name__)
CORS(app)

@app.route('/cosseno', methods=['POST'])
def cosseno():
    try:
        data_request = request.get_data()
        data_request = dict(parse.parse_qsl(data_request.decode('utf8')))
        value = data_request['data']
        value = math.cos(int(value))
        if value:
            argumento = 'cos(' + data_request['data'] + ')'
            return jsonify({ 'argumento': argumento, 'resultado': round(value, 2) })
        
        else: 
            return jsonify({ 'erro': 'os campos v1 e v2 sao obrigatorios' }), 400

    except Exception as error:
        res = {'error': str(error)}
        return jsonify(res), 500

@app.route('/cossecante', methods=['POST'])
def cossecante():
    try:
        data_request = request.get_data()
        data_request = dict(parse.parse_qsl(data_request.decode('utf8')))
        value = data_request['data']
        value = 1/math.sin(int(value))
        if value:
            argumento = 'cosTan(' + data_request['data'] + ')'
            return jsonify({ 'argumento': argumento, 'resultado': round(value, 2) })
        
        else: 
            return jsonify({ 'erro': 'os campos v1 e v2 sao obrigatorios' }), 400

    except Exception as error:
        res = {'error': str(error)}
        return jsonify(res), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)