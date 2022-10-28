from unittest import mock, TestCase

from app import facebook, google, data

class TestApiClass(TestCase):

    def setUp(self):
        self.patcher = mock.patch('app.google.get_data', return_value="data.mock")
        self.patcher.start()

    def tearDown(self) -> None:
        self.patcher.stop()

    def test_external_api_with_class(self):
        self.assertEqual(google.call_google_api(), "gdata.mock", msg="should be gdata.mock")