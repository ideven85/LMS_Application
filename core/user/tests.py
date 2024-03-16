from django.test import TestCase

from core.user.models import User

data_user = {
"username": "test_user",
"email": "test@gmail.com",
"first_name": "Test",
"last_name": "User",
"password": "test_password"
}
# Create your tests here.
class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            email='deven@gmail.com',
            username='deven',
            is_active=True,
            is_staff=True,
            is_superuser=False,
            first_name='Deven',
            last_name='Kalra',



        )

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'deven@gmail.com')
        self.assertEqual(self.user.username, 'deven')
        self.assertEqual(self.user.is_superuser,False)
        self.assertEqual(self.user.is_staff,True)