from kavenegar import *
from config import rules, API


def send_sms(text):
    """
    send sms by kavenegar
    :param text: text of message
    :return: none
    """
    try:
        api = KavenegarAPI(API)
        params = {
            'sender': '10004346',
            'receptor': rules['notification']['receiver'],
            'message': text,
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
