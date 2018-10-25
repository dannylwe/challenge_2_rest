from models import *

base_url= "/api/v1"

@api.route('/hello')
class HelloWorld(Resource):

    def get(self):
    	"sanity check"

        return {'hello': 'world'}, 200

@api.route(base_url + '/attendants')
class get_attendants(Resource):

	def get(self):
		"Get all records of attendants"

		return {"attendants": attendant}, 200

@api.route(base_url + '/del_one_attendant/<int:id>')
class delete_attendant(Resource):

	def find_one(self, id):
		return next((b for b in attendant if b['id'] == id), None)

	@api.marshal_with(a_attendant, envelope= 'data')
	def delete(self, id):
		"Delete one product by Id"

		global attendant

		match= self.find_one(id)
		attendant= list(filter(lambda b: b['id'] != id, attendant))

		return match, 204

		"""
		attendant.pop(id)
		return {"attendant": attendant}, 204
		"""

@api.route(base_url + '/all_products')
class All_products(Resource):
	@api.doc('Method that returns all products')
	def get(self):
		"Get all products"

		return {"products": products}, 200

@api.route(base_url + '/one_product/<int:id>')
class One_product(Resource):

	@api.marshal_with(a_product, envelope= 'data')
	def get(self, id):
		"Get one product by Id"

		result = [prod for prod in products if prod['id'] == id]

		return result
		#return {"product": products[id]}, 200

#@api.response(204, 'successfully deleted.')
@api.route(base_url + '/del_one_product/<int:id>')
class Del_product(Resource):

	def find_one(self, id):
		return next((b for b in products if b['id'] == id), None)

	@api.marshal_with(a_product, envelope= 'data')
	def delete(self, id):
		"Delete one product by Id"

		global products

		match= self.find_one(id)
		products= list(filter(lambda b: b['id'] != id, products))

		return match, 204

		"""
		for index, prod in enumerate(products):
            if prod['id'] == id:
                del products[index]
                return {"response": "product deleted"}, 204
        return None, 404
        """
		"""
		products.pop(id)
		return {"products": products}, 204
		"""

@api.expect(a_product)
@api.route(base_url + '/add_product/')
class post_product(Resource):

	def post(self):
		"Add a single product"

		new_product = api.payload
		new_product['id'] = products[-1]['id'] + 1 if len(products) > 0 else 0
		products.append(new_product)
		return {"successfully added product": new_product}, 201


@api.route(base_url + '/g/sale_order/')
class Sale_order(Resource):

	def get(self):
		"Get all records of sale orders"

		return {"sale_orders": sale_order}, 200

@api.route(base_url + '/sale_order')	
@api.expect(a_sale_order)
class Sale_order_post(Resource):
	def post(self):
		"Post a sale order"

		new_sale_order = api.payload
		new_sale_order['id'] = sale_order[-1]['id'] + 1 if len(Sale_order) > 0 else 0
		sale_order.append(new_sale_order)
		return {"successfully added new sale order": new_sale_order}, 201