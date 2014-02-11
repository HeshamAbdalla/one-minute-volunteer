from . import request
from . import keys

CALLBACK_ENDPOINT = 'http://ec2-54-193-39-226.us-west-1.compute.amazonaws.com/callback'

class ChangeOrgApi(object):
    def __init__(self, request_obj=None):
        self.base_url = 'http://api.change.org'
        if not request_obj:
            request_obj = request.ChangeOrgRequest(keys.API_KEY, keys.API_SECRET)

        self.request = request_obj

    def petition_info(self, petition_url=None, petition_id=None):
        if petition_url:
            resp = self.request.get(self.base_url + '/v1/petitions/get_id',
                                          {'petition_url': petition_url})
            petition_id = resp.get('petition_id')

        if not petition_id:
            raise ValueError("petition_id was not a valid number")

        return self.request.get("".join([self.base_url, '/v1/petitions/']), str(petition_id))

    def sign_petition(self, petition_id, signature_data):
        url = "".join([self.base_url, "/v1/petitions/", str(petition_id), "auth_keys"])
        data = {
            'source_description': "1 Minute Volunteer",
            'source': 'http://ec2-54-193-39-226.us-west-1.compute.amazonaws.com/',
            'requester_email': email,
            'callback_endpoint': CALLBACK_ENDPOINT
        }
