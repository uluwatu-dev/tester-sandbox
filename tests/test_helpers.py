import unittest
from utils import convert_local_to_utc, validate_email, add_numbers
from datetime import datetime
from zoneinfo import ZoneInfo

class TestStringValidation(unittest.TestCase):
    def test_valid_emails(self):
        self.assertTrue(validate_email("test@example.com"))
        self.assertTrue(validate_email("user.name+tag@domain.co.uk"))
        
    def test_invalid_emails(self):
        self.assertFalse validate_email("invalid-email")
        self.assertFalse(validate_email("test@domain"))

class TestDateHelpers(unittest.TestCase):
    def test_timezone_conversion(self):
        # 2026-06-20 12:00:00 in NY is 16:00:00 UTC
        utc_dt = convert_local_to_utc("2026-06-20 12:00:00", "America/New_York")
        self.assertEqual(utc_dt.hour, 16)
        self.assertEqual(utc_dt.tzinfo, ZoneInfo("UTC"))

class TestMathHelpers(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add_numbers(10, 5), 15)
