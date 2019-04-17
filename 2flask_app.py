from flask import Flask, jsonify, request

#create object of Flask with unique name
app = Flask(__name__)

#For Browser
# POST - used to receive data
# GET - used to send data back only

#list of stores having items with name and price
stores = [
          {'name' : "My store",
           'items' : [
                     {'name' : "My item",
                      'price' : 15.99
                     }
                    ]
          }
         ]

#Creating endpoints

# POST /store data: {name:}
@app.route('/store', methods = ['POST'])
def create_store():
        request_data = request.get_json()
        new_store = {
                        'name' : request_data['name'],
                        'items' : []
                    }
        stores.append(new_store)
        return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
        #Iterate over stores
        #if match return store
        #else return error
	for s in stores:
		if s['name'] == name:
			return jsonify(s)
	return ({"'message" : 'Store not found'})

# GET /store/
@app.route('/store/')
def get_stores():
	return jsonify({'Stores':stores})


# POST /store/<string:name>/item  {name:, price:}
@app.route('/store/<string:name>/item' , methods = ['POST'])
def create_item_in_store(name):
	request_data = request.get_json()
	for s in stores:
		if s['name'] == name:
			new_item = {
					'name' : request_data['name'],
					'price' : request_data['price']
				   }
		s['items'].append(new_item)
		return jsonify(new_item)
	return ({"'message" : 'Store not found'})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
	for s in stores:
		if s['name'] == name:
			return jsonify({'Items' : s['items']})
	return ({"'message" : 'Store not found'})


app.run(port=5000)
