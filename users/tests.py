from django.test import TestCase

class TemplateTestCases(TestCase):
	
	def test_login_template(self):
		response = self.client.get("/login/")
		self.assertTemplateUsed(response, 'users/login.html')

	def test_register_template(self):
		response = self.client.get("/register/")
		self.assertTemplateUsed(response, 'users/register.html')

	def test_logout_template(self):
		response = self.client.get('/logout/')
		self.assertTemplateUsed(response, "users/logout.html")

	def tests_profile_template(self):
		# Failing probably it requires login that's why!
		# Why not working!!!
		response = self.client.get('/profile/')
		self.assertTemplateUsed(response, 'users/profile.html')