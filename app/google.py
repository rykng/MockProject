from app.data import get_data


def call_google_api():
    data = get_data()
    return "g" + data


class Google():

    @classmethod
    def get_reputation_score(cls, g_id:int):
        reputation = g_id % 100
        json = {
            'gid': g_id,
            'reputation': reputation
        }
        return json
