from django.test import TestCase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import lxml.html


class FunctionalTestCases(TestCase):

	def setUp(self):
		self.required_form_fields = sorted(['csrfmiddlewaretoken', 'first_name', 'last_name', 'username', 'email', 'password1', 'password2'])
		self.required_form_fields_type = sorted(['hidden', 'text', 'text', 'text', 'email', 'password', 'password'])
		self.driver = webdriver.Chrome(ChromeDriverManager().install())


	def test_there_is_a_Djang_Blog_on_home_page(self):
		self.driver.get('http://localhost:8000/')
		self.assertIn("Django Blog", self.driver.page_source)


	def test_register_form_fields(self):
		self.driver.get("http://localhost:8000/register/")
		page_source = self.driver.page_source
		tree = lxml.html.fromstring(page_source)
		form_input_fields = tree.cssselect("form input")
		form_input_fields = sorted([x.name for x in form_input_fields])
		self.assertEqual(form_input_fields, self.required_form_fields)

	def test_register_form_fields_type(self):
		self.driver.get("http://localhost:8000/register/")
		page_source = self.driver.page_source
		tree = lxml.html.fromstring(page_source)
		form_input_fields_type = tree.cssselect("form input")
		form_input_fields_type = sorted([x.type for x in form_input_fields_type])
		self.assertEqual(form_input_fields_type, self.required_form_fields_type)

	def test_register_user(self):
		self.driver.get("http://localhost:8000/register/")
		self.driver.find_element_by_name('first_name').send_keys("Mohsin")
		self.driver.find_element_by_name('last_name').send_keys("Ashraf")
		self.driver.find_element_by_name('username').send_keys("mohsin.ashraf12")
		self.driver.find_element_by_name('email').send_keys("mohsinashraf@gmail.com")
		self.driver.find_element_by_name('password1').send_keys("testing12345")
		self.driver.find_element_by_name('password2').send_keys("testing12345")
		self.driver.find_element_by_css_selector('body > main > div > div.col-md-8 > div > form > div > button').click()
		page_source = self.driver.page_source
		self.assertIn("Account created for mohsin.ashraf12!", self.driver.page_source)

	def tearDown(self):
		self.driver.quit()


class TemplatesTestCases(TestCase):

	def test_homepage_template(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'blog/home.html')

	def test_aboutpage_template(self):
		response = self.client.get('/about/')
		self.assertTemplateUsed(response, 'blog/about.html')

	def test_post_detail_template(self):
		response = self.client.get('/post/1/')
		self.assertTemplateUsed(response, 'blog/post_detail.html')

	def test_post_create_template(self):
		response = self.client.get('/post/new/')
		self.assertTemplateUsed(response, 'blog/post_form.html')