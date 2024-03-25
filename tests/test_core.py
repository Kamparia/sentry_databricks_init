import unittest
from unittest.mock import patch, MagicMock
from sentry_databricks_init.core import init_sentry


class TestInitSentry(unittest.TestCase):

    @patch('sentry_databricks_init.core.sentry_sdk.init')
    def test_init_sentry_with_dsn_argument(self, mock_init):
        """
        Test that Sentry is initialized with the DSN provided as an argument.
        """
        test_dsn = 'your_dsn_here'
        init_sentry(dsn=test_dsn)
        mock_init.assert_called_once_with(
            dsn=test_dsn,
            enable_tracing=True,
            integrations=[MagicMock()],
        )

    @patch('sentry_databricks_init.core.os.environ.get', return_value='env_dsn_here')
    @patch('sentry_databricks_init.core.sentry_sdk.init')
    def test_init_sentry_with_dsn_env_variable(self, mock_init, mock_env_get):
        """
        Test that Sentry is initialized with the DSN provided as an environment variable.
        """
        init_sentry()
        mock_init.assert_called_once_with(
            dsn='env_dsn_here',
            enable_tracing=True,
            integrations=[MagicMock()],
        )

    @patch('sentry_databricks_init.core.os.environ.get', return_value=None)
    def test_init_sentry_without_dsn(self, mock_env_get):
        """
        Test that an exception is raised when no DSN is provided either as an argument or an environment variable.
        """
        with self.assertRaises(ValueError) as context:
            init_sentry()
            
        self.assertTrue("A Sentry DSN must be provided either as a function argument or as the SENTRY_DSN environment variable." in str(context.exception))


if __name__ == '__main__':
    unittest.main()
