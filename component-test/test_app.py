#!/usr/bin/env python

import unittest
import os
import requests
import re
import time

class TestName(unittest.TestCase):
    # Base URL for the service (default localhost)
    url = os.getenv('SERVICE_URL', 'http://127.0.0.1:8000')
    
    # Delay to simulate service startup
    time.sleep(10)

    # ---------- BROKEN TEST ----------
    def test_status_broken(self):
        """
        This test is intentionally broken to fail CI:
        - Expects status code 500 instead of 200
        - Expects text 'Service down' instead of 'Up and running'
        """
        url = self.url + "/status"
        response = requests.get(url, timeout=1)
        self.assertEqual(response.status_code, 500)  # intentionally wrong
        self.assertEqual(response.encoding, 'ISO-8859-1')
        self.assertTrue(re.match('Service down', response.text))  # intentionally wrong

    # ---------- SAFE TEST ----------
    def test_always_pass(self):
        """
        This test is safe and always passes.
        """
        self.assertEqual(1 + 1, 2)

if __name__ == '__main__':
    unittest.main()
