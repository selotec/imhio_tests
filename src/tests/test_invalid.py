import pytest
from ..nps_requests import NpsRequsests


class TestValid(NpsRequsests):

    def setup(self):
        self.endpoint = "nps"

    def test_missing_bracket(self):
        """
        Case B-07
        """
        self.send_request(self.endpoint, "mobile", "missing_bracket", valid=False)
        self.assert_response_code(400)
        self.assert_has_error()
        self.assert_errors_not_empty()

    def test_missing_value(self):
        """
        Case B-08
        """
        self.send_request(self.endpoint, "mobile", "missing_value", valid=False)
        self.assert_response_code(400)
        self.assert_has_error()
        self.assert_errors_not_empty()

    @pytest.mark.skip(reason="currently broken, bug in cases B09, B-11")
    def test_empty(self):
        """
        Case B-09
        """
        self.send_request(self.endpoint, "mobile", "empty")
        self.assert_response_code(400)
        self.assert_has_error()
        self.assert_errors_not_empty()

    @pytest.mark.skip(reason="currently broken, bug in cases B09, B-11")
    def test_comment_only(self):
        """
        Case B-11
        """
        self.send_request(self.endpoint, "desktop", "comment_only")
        self.assert_response_code(400)
        self.assert_has_error()
        self.assert_errors_not_empty()

    def test_below_zero(self):
        """
        Case B-12
        """
        self.send_request(self.endpoint, "mobile", "below_zero")
        self.assert_response_code(400)
        self.assert_has_error()
        self.assert_errors_not_empty()

    def test_above_ten(self):
        """
        Case B-13
        """
        self.send_request(self.endpoint, "desktop", "above_ten")
        self.assert_response_code(400)
        self.assert_has_error()
        self.assert_errors_not_empty()

    def test_string_as_rating(self):
        """
        Case B-14
        """
        self.send_request(self.endpoint, "desktop", "string_as_rating")
        self.assert_response_code(400)
        self.assert_has_error()
        self.assert_errors_not_empty()

    def test_exceeding_comment(self):
        """
        Case B-15
        """
        self.send_request(self.endpoint, "desktop", "exceeding_comment")
        self.assert_response_code(400)
        self.assert_has_error()
        self.assert_errors_not_empty()
