from http import HTTPStatus
import requests


class InstagramRequester:
    @staticmethod
    def make_request(request_url: str, cookie: str):
        headers = {
            'cookie': cookie,
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                          'like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; '
                          'scale=2.00; 828x1792; 165586599)'
        }
        try:
            res = requests.get(request_url, headers=headers)
            if res.status_code != HTTPStatus.OK:
                raise Exception("Not successful status code")
            return res.json()
        except Exception as e:
            print("getting user failed, due to '{}'".format(e))
