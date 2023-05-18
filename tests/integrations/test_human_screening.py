from unittest import mock, TestCase

from app.google import Google
from app.facebook import Facebook

from services.screening import HumanScreeningService

class TestHumanScreeningService(TestCase):
    '''
    This is the integration test that depends on other 2 external services: Google and FB services.
    Since HumanScreeningService.get_credit_score() requires Google.get_reputation_score and
    Facebook.check_seller_rating, we have to mock the results for those 2 calls, so we can test
    our Services business logic and get it right.
    '''

    fb_mock_json = {
        'fb_id': 9989,
        'first_name': "2 Star Baby",
        'rating': 2,
    }

    gg_mock_json = {
        'gid': 10,
        'reputation': 25
    }


    @mock.patch('app.facebook.Facebook.check_seller_rating', return_value= fb_mock_json)
    @mock.patch('app.google.Google.get_reputation_score', return_value= gg_mock_json)
    def test_human_screening(self, fb, gg):
        ssn = "10021290"
        expected_result = HumanScreeningService.get_credit_score(ssn=ssn)

        self.assertEqual(expected_result.get("ssn"), ssn,msg="SSN should be the same")
        self.assertEqual(expected_result.get("fb_rating"), 2,msg="fb rating should be same as mock")
        self.assertEqual(expected_result.get("g_reputation"), 25,msg="google reputation should be same as mock")
        self.assertEqual(expected_result.get('score'),225,msg="should be 325")

