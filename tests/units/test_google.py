import unittest

from app.google import Google
'''
We test the funcationality of the Google API
'''
class GoogleUnitTest(unittest.TestCase):
    '''
    Pretend that We created Google Service in-house so we can unittest our Google.get_reputation_scoreg API
    no mocking. We are testing the actual functionality
    '''

    def test_good_reputation(self):

        gid = 899
        expected_result = Google.get_reputation_score(g_id=gid)
        self.assertEqual(expected_result.get("gid"),gid, msg="google ID should be the same")
        self.assertTrue(expected_result.get("reputation") > 90, msg="User reputation should be greater than 90")


    def test_bad_reputation(self):
        gid = 3021
        expected_result = Google.get_reputation_score(g_id=gid)
        self.assertEqual(expected_result.get("gid"), gid, msg="google ID should be the same")
        self.assertTrue(expected_result.get("reputation") < 25, msg="User reputation should be under 25")

