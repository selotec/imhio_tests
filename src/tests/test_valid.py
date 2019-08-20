from ..nps_requests import NpsRequsests


class TestValid(NpsRequsests):

    def setup(self):
        self.endpoint = "nps"

    def test_0_and_comment(self):
        """
        Case B-01
        """
        self.send_request(self.endpoint, "mobile", "0_and_comment")
        self.assert_response_code(200)
        self.assert_response_status()

    def test_1_no_comment(self):
        """
        Case B-02
        """
        self.send_request(self.endpoint, "desktop", "1_no_comment")
        self.assert_response_code(200)
        self.assert_response_status()

    def test_10_and_comment(self):
        """
        Case B-03
        """
        self.send_request(self.endpoint, "mobile", "10_and_comment")
        self.assert_response_code(200)
        self.assert_response_status()

    def test_10_no_comment(self):
        """
        Case B-04
        """
        self.send_request(self.endpoint, "desktop", "10_no_comment")
        self.assert_response_code(200)
        self.assert_response_status()

    def test_6_and_comment(self):
        """
        Case B-05
        """
        self.send_request(self.endpoint, "desktop", "6_and_comment")
        self.assert_response_code(200)
        self.assert_response_status()

    def test_6_no_comment(self):
        """
        Case B-06
        """
        self.send_request(self.endpoint, "desktop", "6_no_comment")
        self.assert_response_code(200)
        self.assert_response_status()

    def test_empty_comment(self):
        """
        Case B-010
        """
        self.send_request(self.endpoint, "desktop", "empty_comment")
        self.assert_response_code(200)
        self.assert_response_status()
