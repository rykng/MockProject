
from app.facebook import Facebook
from app.google import Google

class HumanScreeningService():

    @classmethod
    def get_credit_score(cls,ssn:str):
        score = 0

        id = int(ssn)

        fb_result = Facebook.check_seller_rating(fb_id=id)
        gg_result = Google.get_reputation_score(g_id=id)

        score = (fb_result.get('rating') * 100) + gg_result.get('reputation')

        json = {
            'ssn': ssn,
            'fb_rating': fb_result.get("rating"),
            'g_reputation' : gg_result.get("reputation"),
            'score': score,
        }

        return json






