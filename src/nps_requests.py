import requests
import json


'''
Ideally these constants should be loaded from config file
'''
SERVER = "localhost"
PORT = "58001"
FIXTURES = "fixtures"

'''
Ideally methods should have docstrings
Also we could use psycopg2 to check db values in asserts. 
Then we could drop db state in teardown method after each test and prepare it in setup method before each test.
'''
class NpsRequsests:
    def send_request(self, endpoint, user_agent, case_name, valid=True):
        url = "http://{}:{}/{}".format(SERVER, PORT, endpoint)
        print(url)
        data = self.load_fixture(case_name, valid=valid)

        headers = {
            'User-Agent': user_agent,
            'Content-Type': 'application/json'
        }

        # There is should be more correct way of initializing instance attributes in pytest
        self.response = requests.post(url, json=data, headers=headers)

    # Ideally this method should be loaded from special data driver class outside this module
    def load_fixture(self, name, valid=True):
        if valid:
            return json.load(open("{}/data_{}.json".format(FIXTURES, name)))
        else:
            fixture_lines = open("{}/data_{}.txt".format(FIXTURES, name)).readlines()
            return "\n".join(fixture_lines)

    def assert_response_code(self, code):
        assert(int(self.response.status_code) == int(code))

    def assert_response_status(self):
        server_status_response = json.loads(self.response.text)
        assert(server_status_response.get("status") == "ok")

    def assert_has_error(self):
        server_status_response = json.loads(self.response.text)
        assert(server_status_response.get("status") == "error")

    def assert_errors_not_empty(self):
        server_status_response = json.loads(self.response.text)
        assert (len(server_status_response.get("errors")) > 0)
