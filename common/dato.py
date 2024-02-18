import unittest
from datetime import datetime, timedelta

class Dato:
    """
    A class to perform date operations.

    Attributes:
        current_date (datetime): The current date.
    """

    def __init__(self, current_date=None):
        """
        Initializes the Date object.

        Args:
            current_date (datetime, optional): The current date. Defaults to None.
        """
        if current_date is None:
            self.date = datetime.now()
        else:
            self.date = current_date

    def get_now_date(self):
        """
        Get the current date.

        Returns:
            datetime: The current date.
        """
        return self.date

    def get_date(self, date_format="%Y-%m-%d"):
        """
        Get the formatted date string.

        Args:
            date_format (str, optional): The format string. Defaults to "%Y-%m-%d".

        Returns:
            str: The formatted date string.
        """
        return self.date.strftime(date_format)

    def calculate_date(self, duration):
        """
        Calculate an older date based on the given duration.

        Args:
            duration (int): The duration in days.

        Returns:
            datetime or None: The older date, or None if duration is negative.
        """
        if duration < 0:
            print("Duration cannot be negative")
            return None
        old_date = self.date - timedelta(days=duration)
        return old_date

class TestDate(unittest.TestCase):
    def test_calculate_date_positive_duration(self):
        test_date = datetime(2024, 2, 18)
        myDate = Date(current_date=test_date)
        result = myDate.calculate_date(30)
        self.assertEqual(result, datetime(2024, 1, 19))

    def test_calculate_date_negative_duration(self):
        test_date = datetime(2024, 2, 18)
        myDate = Date(current_date=test_date)
        result = myDate.calculate_date(-30)
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()
