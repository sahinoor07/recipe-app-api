"""
Test for models
"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    """Test Models"""

    def test_user_creation_with_email_successful(self):
        "Creating an user with email is successful"

        email = 'test@email.com'
        password = 'test@123'
        user = get_user_model().objects.create(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """ Test for email normalization. """
        sample_emails = [
            ['test1@EXAMPLE.COM', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@example.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.COM']
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)
