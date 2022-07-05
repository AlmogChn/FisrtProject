from flask import Flask
import db_connector

app = Flask(__name__)


@app.route('/users/<user_id>')
def get_user_name(user_id):
    get_name = db_connector.Msql(table='users', user_id=user_id)
    if not db_connector.Msql.check_id(get_name):
        return "<H1 id='error'>" + "no such user:" +user_id+ "</H1>"
    user_name = db_connector.Msql.select_name(get_name)
    return "<H1 id='user'>" + user_name + "</H1>", 200


app.run(host='127.0.0.1', debug=True, port=5001)
