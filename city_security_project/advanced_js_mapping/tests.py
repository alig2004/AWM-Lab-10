from django.test import TestCase
from django.contrib.auth import get_user_model

class MappingPagesTests:
    @classmethod
    def setUp(self):
        user = get_user_model().objects.create_user(username="searcher", password="test-password")
        self.client.force_login(user)