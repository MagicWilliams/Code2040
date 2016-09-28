import json
import urllib2

data = {
        'token': "b445cce28b1d51745774db40e999c4ea",
        'github':
}

req = urllib2.Request('http://example.com/api/posts/create')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))

