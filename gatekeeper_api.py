import requests
import json


def generate_header(auth_token):

    header = {
        'Authorization': 'Bearer {0}'.format(auth_token)
    }
    return header


def get_suppliers(auth_token, region):

    response = requests.get('https://{0}.gatekeeperhq.com/api/suppliers'.format(region),
                            headers=generate_header(auth_token))
    return response.json()


def get_supplier_by_id(auth_token, region, supplier_id):

    response = requests.get('https://{0}.gatekeeperhq.com/api/suppliers/{1}'.format(region, supplier_id),
                            headers=generate_header(auth_token))
    return response.json()


def update_supplier(auth_token, region, supplier_id,data):

    update_response = requests.put('https://{0}.gatekeeperhq.com/api/suppliers/{1}'.format(region, supplier_id),
                                   headers=generate_header(auth_token), data=json.dumps(data))
    return update_response.content
