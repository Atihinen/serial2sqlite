import unittest
import mock
from utils.dummy_adapter import DummyAdapter
class DummyAdapterTest(unittest.TestCase):

    def setUp(self):
        self.dummy = DummyAdapter()

    @mock.patch('utils.dummy_adapter.randint')
    def test_get_randint(self, mock_randint):
        mock_randint.return_value = 3
        self.assertEqual(self.dummy.read_int(), 3)