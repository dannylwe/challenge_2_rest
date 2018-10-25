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

@api.response(204, 'successfully deleted.')
@api.route(base_url + '/del_one_attendant/<int:id>')
class delete_attendant(Resource):

	def delete(self, id):
		"Delete one attendant by Id"

		attendant.pop(id)

		return {"attendant": attendant}, 204

@api.route(base_url + '/all_products')
class All_products(Resource):
	@api.doc('Method that returns all products')
	def get(self):
		"Get all products"

		return {"products": products}, 200

@api.route(base_url + '/one_product/<int:id>')
class One_product(Resource):

	def get(self, id):
		"Get one product by Id"

		return {"product": products[id]}, 200

#@api.response(204, 'successfully deleted.')
@api.route(base_url + '/del_one_product/<int:id>')
class Del_product(Resource):

	def delete(self, id):
		"Delete one product by Id"

		"""
		for index, prod in enumerate(products):
            if prod['id'] == id:
                del products[index]
                return {"response": "product deleted"}, 204
        return None, 404
        """

		products.pop(id)
		return {"products": products}, 204

@api.expect(a_product)
@api.route(base_url + '/add_product/')
class post_product(Resource):

	def post(self):
		"Add a single product"

		new_product = api.payload
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
		sale_order.append(new_sale_order)
		return {"successfully added new sale order": new_sale_order}, 201
