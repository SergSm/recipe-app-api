from unittest.mock import patch


from django.core.management import call_command  # for calling django-admin...
# ...command. via manage.py

from django.db.utils import OperationalError  # raised when db isn't available
from django.test import TestCase


class CommandTest(TestCase):

    def test_wait_for_db_ready(self):
        """test new wait_for_db command if the database is ready"""

        # __getitem__ used to get the first database from connection
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.return_value = True
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=True)  # speeding test
    def test_wait_for_db(self, ts):
        """Test waiting for db. After 5 unsuccessfull tries the 6-th time
        must be successful"""

        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            # fist 5 calls of __getitem__ call will raise OperationError
            gi.side_effect = [OperationalError] * 5 + [True]

            call_command('wait_for_db')  # 6 times called
            self.assertEqual(gi.call_count, 6)
