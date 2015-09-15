import unittest


class TestPluginIntegration(unittest.TestCase):

    def test_plugin_integration(self):
        try:
            from simphony.visualisation import aviz  # noqa
        except ImportError:
            self.fail('Could not import the aviz plugin')


if __name__ == '__main__':
    unittest.main()
