# !/uer/bin/env python3
# coding=utf-8

import unittest
from .element_finder import MobileDriver
from time import sleep
from .apper import Apper
from base.log import logged


class TestCase(unittest.TestCase, MobileDriver):
    @classmethod
    def setUpClass(cls):
        cls.driver = Apper()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    @logged
    def assertTitle(self, title, second=3):
        """
        Asserts whether the current title is in line with expectations.
        The default is 3 seconds.

        Usage:
        self.assertTitle("title")
        """
        if title is None:
            raise NameError("'title' can't be empty.")
        for s in range(second):
            try:
                self.assertIn(title, self.get_title())
                break
            except AssertionError:
                sleep(1)
        else:
            self.assertIn(title, self.get_title())

    @logged
    def assertText(self, actual_el, expect_result):
        """
        Asserts whether the text of the current page conforms to expectations.
        - actual_el: The actual element text.
        - expect_result :expected results.

        Usage:
        self.assertText("#el","text")
        """
        if actual_el is None or expect_result is None:
            raise NameError("'actual' or 'exect' can't be empty.")
        actual_result = self.get_text(actual_el)
        self.assertEqual(actual_result, expect_result)

    @logged
    def assertAlert(self, expect_text):
        """
        Asserts whether the text of the current page conforms to expectations.
        - actual_el: The actual element text.
        - expect_result :expected results.

        Usage:
        self.assertText("#el","text")
        """
        if expect_text is None:
            raise NameError("'expect_text' can't be empty.")
        alert_text = self.get_alert_text()
        self.assertEqual(alert_text, expect_text)
