from unittest import mock, TestCase

from app import facebook, google, data


class TestApi(TestCase):

    def test_external_api_with_real(self):
        self.assertEqual(google.call_google_api(), "gdata.1", msg="should get gdata.1")
        self.assertEqual(facebook.call_facebook_api(), 'fbdata.1', msg="should get fbdata.1")

    @mock.patch('app.facebook.get_data', return_value='data.mock')
    @mock.patch('app.google.get_data', return_value='data.mock.g')
    def test_external_api_decorator_mock(self, goo, fb):
        #it mock inside call_google_api()'s get_data. that one return "data.mock"
        #order of 1st paramater 'goo', matches with nearest decorator 'app.google.get_data'
        #order of 2nd parameter 'fb', matches with next nearest decorator 'app.facebook.get_data'
        self.assertEqual(google.call_google_api(), "gdata.mock.g", msg="should get gdata.mock.g")
        self.assertEqual(facebook.call_facebook_api(), 'fbdata.mock', msg="should get fbdata.mock")


    def test_external_api_with_mock(self):
        with mock.patch('app.google.get_data', return_value='data.mock.g'):
            self.assertEqual(google.call_google_api(), 'gdata.mock.g', msg="should get gdata.mock.g")
        with mock.patch('app.facebook.get_data', return_value='data.mock'):
            self.assertEqual(facebook.call_facebook_api(), 'fbdata.mock', msg="should get fbdata.mock")