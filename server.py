from flask import Flask, jsonify, render_template, request
from pymongo import MongoClient
server = Flask(__name__)
import datetime
client = MongoClient(port=27017)
db=client.paquetes

@server.route('/')
def index():
    return render_template('home.html')

@server.route('/data', methods=['GET', 'POST'])
def data():
    try:
        id_device = request.args.get('id_device')
        fecha_desde = request.args.get('fecha_desde')
        fecha_desde = fecha_desde.replace('%3A',':')
        fecha_hasta = request.args.get('fecha_hasta')
        fecha_hasta = fecha_hasta.replace('%3A',':') 
        date_desde = datetime.datetime.strptime(fecha_desde, '%Y-%m-%dT%H:%M')
        date_hasta = datetime.datetime.strptime(fecha_hasta, '%Y-%m-%dT%H:%M')
        items = list(db[str(id_device)].find({"fecha": {"$gte": date_desde, "$lt": date_hasta}},{"fecha":1,"ip":1,"puerto":1,"datos":1,"_id":False}).limit(3000))
        cuenta = len(items)
        return render_template("index.html", items = items, id_device = str(id_device), cuenta = cuenta, fecha_desde = fecha_desde, fecha_hasta = fecha_hasta)
    except Exception as ex:
        return jsonify({"error" : "Error interno en el servidor"}), 500    
    
if __name__ == '__main__':
    server.run(host='0.0.0.0', port=8000)