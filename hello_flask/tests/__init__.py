import unittest

from hello_flask.tests.app import AppTestCase


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(AppTestCase))
    return suite
