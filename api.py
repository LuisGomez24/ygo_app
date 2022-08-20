"""Libraries"""
import requests

URL = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'


def confirm_request(request):
    """_summary_

    Args:
        request (function): function to decorate
    """
    def wrap(*args, **kwargs):

        response = request(*args, **kwargs)

        match response.status_code:
            case 200:
                print('Card successfully found...')
                return (True, response)
            case 400:
                print('Error 400: Card was not found...')
            case 404:
                print('Error 404: REST API is not working...')
            case _:
                print('Unidentified error...')
        return (False, response)

    return wrap

@confirm_request
def get_request(url):
    """_summary_

    Args:
        url (string): URL to get data from API

    Returns:
        json: Data from API request
    """

    return requests.get(url)
