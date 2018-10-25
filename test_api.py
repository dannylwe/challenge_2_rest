from unittest import TestCase
import app

class Test(TestCase):

	def setUp(self):
		#self.app = storemanager_api.app.test_client()
		self.app = app.app.test_client()  

	def test_hello_world(self):
		response = self.app.get('/hello')
		self.assertEqual(response.status_code, 200)
	
	def test_get_all_products(self):
		response = self.app.get('/api/v1/products')
		self.assertEqual(response.status_code, 200)

	def test_attendants(self):
		response = self.app.get('/api/v1/attendants')
		self.assertEqual(response.status_code, 200)

	#endpoint with jwt
	def test_sale_order(self):
		response = self.app.get('/api/v1/g/sale_order/')
		self.assertEqual(response.status_code, 500)

	def test_get_one_products(self):
		response = self.app.get('/api/v1/products/1')
		self.assertEqual(response.status_code, 200)

	def test_delete_one_attendants(self):
		response = self.app.delete('/api/v1/attendants/1')
		self.assertEqual(response.status_code, 204)

	def test_delete_one_product(self):
		response = self.app.delete('/api/v1/products/1')
		self.assertEqual(response.status_code, 204)

	def test_login(self):
		response = self.app.delete('/login')
		self.assertEqual(response.status_code, 405)

	def test_login_refresh(self):
		response = self.app.delete('/token/refresh')
		self.assertEqual(response.status_code, 405)

	def test_login_logout(self):
		response = self.app.delete('/logout')
		self.assertEqual(response.status_code, 405)