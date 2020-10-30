import json
import requests

from datetime import datetime
from khayyam import JalaliDatetime
from config import url, rules
from mail import send_smtp_email
from notification import send_sms


def get_rates():
    """
    get the rates from the site
    :return: json form of the rates
    """
    response = requests.get(url)
    if response.status_code == 200:
        return json.loads(response.text)
    return None


def archive(filename, rates):
    """
    archive the rates in the json format
    :param filename: unic timestamps
    :param rates: rates
    :return: none
    """
    with open(f'archive/{filename}.json', 'w') as f:
        f.write(json.dumps(rates))


def send_mail(timestamps, rates):
    """
    contain subject and body of the email and will send it
    :param timestamps: time of rates
    :param rates: rates
    :return: none
    """
    now = JalaliDatetime(datetime.now()).strftime('%y-%B-%d  %A  %H:%M')
    subject = f'{timestamps} - {now} rates'

    if rules['email']['preferred'] is not None:
        tmp = {}
        for exc in rules['email']['preferred']:
            tmp[exc] = rates[exc]
        rates = tmp
    text = json.dumps(rates)
    send_smtp_email(subject, text)


def check_notification_rules(rates):
    """
    check whether its necessary to send sms or not
    :param rates: rates
    :return:body of message
    """
    preferred = rules['notification']['preferred']
    msg = ''
    for exc in preferred.keys():
        if rates[exc] <= preferred[exc]['min']:
            msg += f'{exc} reached min : {rates[exc]}\n'
        if rates[exc] >= preferred[exc]['max']:
            msg += f'{exc} reached max : {rates[exc]}\n'
    return msg


def send_notification(msg):
    """
    send message and jalalidate time
    :param msg: body of sms
    :return: none
    """
    now = JalaliDatetime(datetime.now()).strftime('%y-%B-%d  %A  %H:%M')
    msg += now
    send_sms(msg)


if __name__ == '__main__':
    rqt = get_rates()
    if rules['archive']:
        archive(rqt['timestamp'], rqt['rates'])
    if rules['email']['activate']:
        send_mail(rqt['timestamp'], rqt['rates'])
    if rules['notification']['activate']:
        notification_msg = check_notification_rules(rqt['rates'])
        if notification_msg:
            send_notification(notification_msg)
