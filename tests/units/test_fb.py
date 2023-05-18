import unittest

from app.facebook import Facebook
'''
Pretend that We created Facebook Service in-house so we can unittest our Facebook.check_seller_rating API
no mocking. We are testing the actual functionality
'''
class FacebookUnitTest(unittest.TestCase):


    def test_good_rating(self):

        fb_id = 899
        expected_result = Facebook.check_seller_rating(fb_id=fb_id)
        self.assertEqual(expected_result.get("fb_id"),fb_id, msg="FB ID should be the same")
        self.assertTrue(expected_result.get("rating") >= 4, msg="User rating should be 4")


    def test_bad_rating(self):
        fb_id = 7
        expected_result = Facebook.check_seller_rating(fb_id=fb_id)
        self.assertEqual(expected_result.get("fb_id"), fb_id, msg="FB ID should be the same")
        self.assertTrue(expected_result.get("rating") == 1, msg="User rating should be 1")