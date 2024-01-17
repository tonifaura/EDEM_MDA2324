import unittest
import requests

class APITestCase(unittest.TestCase):
    def test_successful_request(self):
        url = "https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest?CMC_PRO_API_KEY=0c58c479-77a7-40d6-a7cd-21eeb593f831"
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("data", data)
        self.assertIn("quote", data["data"])
        self.assertIn("USD", data["data"]["quote"])
        self.assertIn("total_market_cap", data["data"]["quote"]["USD"])

    def test_failed_request(self):
        url = "https://pro-api.coinmarketcap.com/v1/global-metrics/quotes/latest?CMC_PRO_API_KEY=invalid_api_key"
        response = requests.get(url)
        self.assertEqual(response.status_code, 401)
        data = response.json()
        self.assertIn("status", data)
        self.assertIn("error_message", data["status"])
        self.assertEqual(data["status"]["error_message"], "This API Key is invalid.")

if __name__ == "__main__":
    unittest.main()

