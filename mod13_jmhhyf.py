import unittest
from datetime import datetime

symbol = "GOOG"
chart_type = "1"
time_series = "3"
date_format = "%Y-%m-%d"
start_date = "2021-09-23"
end_date = "2021-10-23"

class symbol_Test(unittest.TestCase):
    def test_capitalized(self):
        self.assertTrue(symbol.isupper())

    def test_length(self):
        self.assertTrue(len(symbol) >= 1 and len(symbol) <= 7)

    def test_isAlpha(self):
        self.assertTrue(symbol.isalpha())

class chart_type_Test(unittest.TestCase):
    def test_isNumber(self):
        self.assertTrue(chart_type.isnumeric())

    def test_is1or2(self):
        self.assertTrue(chart_type == "1" or chart_type == "2")

class time_series_Test(unittest.TestCase):
    def test_isNumber(self):
        self.assertTrue(time_series.isnumeric() and len(time_series) == 1)

    def test_is1through4(self):
        self.assertTrue(time_series == "1" or time_series == "2" or time_series == "3" or time_series == "4")

class start_date_Test(unittest.TestCase):
    def test_dateType(self):
        self.assertTrue(datetime.strptime(start_date, date_format))

class end_date_Test(unittest.TestCase):
    def test_dateType(self):
        self.assertTrue(datetime.strptime(end_date, date_format))


if __name__ == '__main__':
    unittest.main()