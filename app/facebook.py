from app.data import get_data

from shared.random_util import RandomGenUtil


def call_facebook_api():
    data = get_data()
    return "fb" + data


class Facebook():
    '''
    if you have a fb_id, you can check if that person has a 5-star rating
    for simplicity, 0,1,2,3,4,5
    '''
    @classmethod
    def check_seller_rating(cls, fb_id:int=0):
        rating = fb_id % 6

        json = {
            'fb_id': fb_id,
            'first_name': RandomGenUtil.get_random_alphabets(length=10),
            'rating': rating,
        }
        return json

