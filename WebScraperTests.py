from unittest import TestCase, mock
import unittest

from WebScraper import get_reviews
import test_fixtures


class Response:
    def __init__(self, status_code, content=''):
        self.status_code = status_code
        self.content = content


base_url = ''


class TestWebScraper(TestCase):

    @mock.patch('WebScraper.get')
    def test_error_response(self, mock_get):
        mock_get.return_value = Response(300, '')
        data = get_reviews(base_url)
        self.assertEqual(data, [])

    @mock.patch('WebScraper.get')
    def test_should_return_empty(self, mock_get):
        mock_get.return_value = Response(200, '')
        data = get_reviews(base_url)
        self.assertEqual(data, [])
    
    @mock.patch('WebScraper.get')
    def test_should_return_10_rows(self, mock_get):
        mock_get.return_value = Response(200, content=test_fixtures.content)
        data = get_reviews(base_url)
        self.assertNotEqual(data, [])
        self.assertEqual(len(data), 10)


if __name__ == '__main__':
    unittest.main()
