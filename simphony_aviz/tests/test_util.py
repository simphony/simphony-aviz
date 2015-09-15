import unittest

from simphony_aviz.util import run_aviz


class TestUtil(unittest.TestCase):
    def test_run_aviz_fail(self):
        with self.assertRaises(RuntimeError):
            run_aviz(aviz="dummy_aviz")

if __name__ == '__main__':
    unittest.main()
