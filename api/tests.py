from .data_gouv_helpers import build_json_instruction
from django.test import TestCase
from django.test import Client


class TestApiEndpoint(TestCase):
    def setUp(self):
        self.client = Client()

    def test_address_with_full_params_should_be_redirected_to_provider(self):
        """
        If the address is full, the client is redirected to our endpoint:
        provider/coordinate/
        """
        response = self.client.get("/api/address/?q=1 allée de faneurs 77185 Lognes")
        right_redirect_url = "provider/coordinate/" in response.url

        self.assertEqual(response.status_code, 302)
        self.assertEqual(right_redirect_url, True)

    def test_address_with_few_param_should_be_redirect_to_failed_url(self):
        """
        If address has too few params, data.gouv response with nothing
        """
        response = self.client.get("/api/address/?q=10")
        right_redirect_url = "failed-endpoint" in response.url
        right_error_response = "Your+address+is+not+precise+enough" in response.url

        self.assertEqual(response.status_code, 302)
        self.assertEqual(right_redirect_url, True)
        self.assertEqual(right_error_response, True)

    def test_address_without_cities_and_postal_code(self):
        """
        If address has few params but enough, data.gouv response with a list
        """
        response = self.client.get("/api/address/?q=1 allée des faneurs")
        self.assertEqual(response.status_code, 200)

    def test_address_without_param(self):

        response = self.client.get("/api/address/")
        right_redirect_url = "failed-endpoint" in response.url
        right_error_response = "Please+put+an+address+as+a+parameter" in response.url

        self.assertEqual(response.status_code, 302)
        self.assertEqual(right_redirect_url, True)
        self.assertEqual(right_error_response, True)

        # Check that the rendered context contains 5 customers.
        # self.assertEqual(len(response.context['customers']), 5)


#####################
# INTEGRATION TESTS #
#####################
"""
c = Client()
response = c.post('/login/', {'username': 'john', 'password': 'smith'})
response.status_code
response = c.get('/customer/details/')
response.content
"""
