from flask import Flask,request
from flask_restful import Resource,Api,reqparse
from flask_jwt import JWT,jwt_required

from security import authenticate,identity

app = Flask(__name__)
api = Api(app)
app.secret_key = 'jeevi'
jwt = JWT(app,authenticate,identity)

items = []

class Item(Resource):
    parser = reqparse.RequestParser()
    @jwt_required()
    def get(self,name):
        item = next(filter(lambda x: x['name'] == name,items),None)
        return item
        return {'item': None}, 200 if item else 404
        
    def post(self,name):
        if next(filter(lambda x: x['name'] == name,items),None):
            return {'message': "Am item with name {} already exist.".format(name)}, 400
        data = request.get_json(force=True)
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201
    
    def put(self,name):
        parser = Item.parser
        parser.add_argument('price',
        type=float,
        required=True,
        help='Field is required'
        )
        # data = request.get_json(force=True)
        data = parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, items),None)
        if item is None:
            item = {"name": name,"price": data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

    def delete(self,name):
        global items
        items = filter(lambda x: x['name'] != name,items)
        return {"message": "Items deelted"},200

class ItemsList(Resource):
    def get(self):
        return {'items':items}

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemsList,'/items')
app.run(port=5000,debug=True)