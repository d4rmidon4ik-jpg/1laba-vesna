import json
import subprocess
import unittest
from unittest.mock import patch, MagicMock

class TestPythonPart(unittest.TestCase):
    @patch('subprocess.Popen')
    def test_send_data_to_go(self, mock_popen):
        mock_process = MagicMock()
        mock_process.communicate.return_value = ('{"answer": "yeeees"}', '')
        mock_process.returncode = 0
        mock_popen.return_value = mock_process
        
        data = {"message": "1 laba?"}
        process = subprocess.Popen(
            ["go", "run", "main.go"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            text=True
        )
        stdout, _ = process.communicate(input=json.dumps(data))
        response = json.loads(stdout)
        
        self.assertEqual(response["answer"], "yeeees")
        mock_popen.assert_called_once()
