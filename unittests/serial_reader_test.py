import unittest
import mock
from serial import SerialException
from utils.serial_reader import SerialDataAdapter
class SerialDataAdapterTest(unittest.TestCase):

    def setUp(self):
        self.serial_adapter = SerialDataAdapter('/dev/tty/ACM0')
        self.serial_adapter.serial_connection = mock.MagicMock()
        self.serial_adapter.serial_connection.isOpen = mock.MagicMock()

    @mock.patch('utils.serial_reader.time')
    @mock.patch('utils.serial_reader.serial.Serial')
    def test_open_connection(self, mock_serial, mock_time):
        adapter = SerialDataAdapter('/dev/tty/USB0')
        adapter.check_connection_status = mock.MagicMock()
        adapter.check_connection_status.return_value = True
        try:
            value = adapter.open_connection()
        except:
            self.fail("Exception did rise")
        self.assertFalse(value)
        adapter.check_connection_status.return_value = False
        try:
            value = adapter.open_connection()
        except:
            self.fail("Exception did rise")
        self.assertTrue(value)
        mock_serial.side_effect = SerialException("")
        self.assertRaises(SerialException, adapter.open_connection)

    def test_check_connection_status(self):
        self.serial_adapter.serial_connection.isOpen.return_value = True
        self.assertTrue(self.serial_adapter.check_connection_status())
        self.serial_adapter.serial_connection.isOpen.side_effect = SerialException("")
        self.assertFalse(self.serial_adapter.check_connection_status())
        self.serial_adapter.serial_connection.isOpen.side_effect = AttributeError("")
        self.assertFalse(self.serial_adapter.check_connection_status())

    def test_read_int(self):
        self.serial_adapter.serial_connection.isOpen.return_value = True
        self.serial_adapter.disconnect()
        self.assertIsNone(self.serial_adapter.serial_connection)

    def test_read_int(self):
        self.serial_adapter.serial_connection.readline.return_value = 1
        value = self.serial_adapter.read_int()
        self.assertEqual(1, value)
        self.serial_adapter.serial_connection.readline.return_value = "a"
        self.assertRaises(ValueError, self.serial_adapter.read_int)
