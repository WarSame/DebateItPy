from app.models import *
from app.db import initialize_db
import unittest


class testUser(unittest.TestCase):
    def setUp(self):
        initialize_db()

    def test(self):
        print("hello")

