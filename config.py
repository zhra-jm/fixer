
BASE_URL = "http://data.fixer.io/api/latest?access_key="
API_KEY = "29265649dca3774ba982e56091619cb6"
url = BASE_URL + API_KEY

API = "6C48763447394C336C55616747516F2B576F354855" \
      "445741642F756533633772732F704B566F6A46376E553D "

rules = {
    'archive': True,
    'email': {
        'receiver': 'zahrajam1999@gmail.com',
        'activate': True,
        'preferred': ['BTC', 'IRR', "IQD", "USD", "CAD", "AED"]
    },
    'notification': {
        'receiver': '09302828801',
        'activate': False,
        'preferred': {
            'BTC': {'min': 0.000101, 'max': 0.000110},
            'IRR': {'min': 45000, 'max': 50000}
        }
    }
}
