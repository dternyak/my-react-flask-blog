import json
import requests

__author__ = 'agosto'

import unittest

class TestMainHandler(unittest.TestCase):

    def test_request(self):
        api_key = "AIzaSyBPauhbnepUR9Ir8YaycIApPazAwKiKvJ4"
        r = requests.get("https://maps.googleapis.com/maps/api/timezone/json?location=39.6034810,-119.6822510&timestamp=1331161200&key=" + api_key)
        json_payload = json.loads(r.text)
        # print str(json_payload)
