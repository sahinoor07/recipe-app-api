"""
Test for models
"""
from decimal import Decimal

from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

class ModelTest(TestCase):
    """Test Models"""

    def test_user_creation_with_email_successful(self):
        "Creating an user with email is successful"

        email = 'test@email.com'
        password = 'test@123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )
        self.assertEqual(user.email, email)
        user.check_password(password)
        self.assertTrue(user.check_password('test@123'))

    def test_new_user_email_normalized(self):
        """ Test for email normalization. """
        sample_emails = [
            ['test1@EXAMPLE.COM', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@example.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com']
        ]

        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test for new user without email will raise ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test@124')

    def test_create_superuser(self):
        user = get_user_model().objects.create_superuser(
            'test@email.com',
            'test@123',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe_successful(self):
        user = get_user_model().objects.create_user(
            'test@example.com',
            'test@123'
        )

        recipe = models.Recipe.objects.create(
            user=user,
            title='Sample recipe name',
            time_minutes=5,
            price=Decimal('5.50'),
            description='Sample recipe description.'
        )
        self.assertEqual(str(recipe), recipe.title)
