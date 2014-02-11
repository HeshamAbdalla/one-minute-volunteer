import urllib
import urllib2
import time
import json

class ChangeOrgRequest(object):
    """
    A simple class to sign requests to the Change.org API. They use some
    crappy signing, so this thing is a damn hack.
    """

    def __init__(self, key=None, secret=None, base_url=None):
        if not key:
            key = Change_Org.KEY

        if not secret:
            secret = Change_Org.SECRET

        if not base_url:
            base_url = "https://api.change.org"

        self.api_key = key
        self.api_secret = secret
        self.base_url = base_url


    def get(self, url, params={}):
        params['api_key'] = self.api_key
        url = url + "?" + urllib.urlencode(params)
        try:
            resp = urllib2.urlopen(url)
            return self.json_parse(resp.read())
        except urllib2.HTTPError, e:
            return self.json_parse(e.read())

    def json_parse(self, content):
        try:
            data = json.loads(content)
        except:
            data = {'error': { 'desc': 'Malformed Content' }}
        return data


    def post(self, url, query_params={}, post_params={}, auth_key=""):
        if query_params:
            url = url + "?" + urllib.urlencode(query_params)

        params = dict(query_params, **post_params)
        ts = datetime.datetime.utcnow().replace(microsecond=0).isoformat() + 'Z'
        params['timestamp'] = ts
        signing_string = "".join([urllib.urlencode(params), self.secret, auth_key])
        h = hashlib.sha256()
        rsig = h.update(signing_string).hexdigest()
        post_params['timestamp'] = ts
        post_params['rsig'] = rsig

        try:
            resp = urllib2.urlopen(url, post_params)
            return self.json_parse(resp.read())
        except urllib2.HTTPError, e:
            return self.json_parse(e.read())


