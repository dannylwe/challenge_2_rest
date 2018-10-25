from flask_restplus import Api, Resource, fields
from flask import Flask

app = Flask(__name__)

api = Api(app, version='1.1', title='Store Manager Api', 
	description='An Api that supplies data to the store manager app')

attendant = [
	{
	"id": 1,
	"name": "Tony Stark",
	"email": "tony@gmail.com",
	"password": "iamironman",
	"contact": "1800-TONY-STARK",
	},

	{
	"id": 2,
	"name": "Peter Parker",
	"email": "peter@gmail.com",
	"password": "auntmay",
	"contact": "0758123456",
	},

	{
	"id": 3,
	"name": "Hulk",
	"email": "hulk@gmail.com",
	"password": "banner",
	"contact": None,
	},
]

products = [
	
	{
	"id": 1, "name": "Kitchen towels", "quantity": 15, "price": 4000
	},

	{
	"id": 2, "name": "blue band", "quantity": 5, "price": 1000
	},
]

"""should use OOP to create these"""

sale_order = [
	{
	"order_id": 123456,
	"name": ['Kitchen towels', 'blue band'],
	"quantity": 3,
	"price": 6000,
	"attendant": "Tony Stark",
	"attendant_id": 1,
	"category": "Households"
	},
]

#Products.append(products)

"""for i in attendant:
	print(i['id'])
"""
#print(products[0])

a_product = api.model('product', {	
	"name": fields.String('name of product'), 
	"quantity": fields.Integer('Number of products'),
	"price": fields.Integer('Retail price'),
	})

a_sale_order = api.model('sale_order', {
	"name": fields.String('Name of product(s)'),
	"quantity": fields.Integer('Numerical quantity of products'),
	"price": fields.Integer('Cumulative price'),
	"attendant": fields.String('Name of attendant'),
	"attendant_id": fields.String('Unique Id of attendant'),
	"category": fields.String('category of product if any'),
	})

a_attendant = api.model('attendant', {
	"name": fields.String('Name of attendant'),
	"email": fields.String("Email for attendant"),
	"password": fields.String("password for attendant account"),
	"contact": fields.Integer("Handphone contact number")
	})