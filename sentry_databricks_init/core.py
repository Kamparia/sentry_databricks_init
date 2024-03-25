import os
import sentry_sdk
from sentry_sdk.integrations.spark import SparkIntegration


def init_sentry(dsn=None):
    """
    Initialize the Sentry SDK with Databricks integration.
    
    Args:
    - dsn: The DSN (Data Source Name) provided by Sentry for your project. Optional if SENTRY_DSN environment variable is set.
    """
    # If DSN is not provided, try to fetch it from the environment variable 'SENTRY_DSN'
    if dsn is None:
        dsn = os.environ.get('SENTRY_DSN', None)
    
    if dsn is None:
        raise ValueError("A Sentry DSN must be provided either as a function argument or as the SENTRY_DSN environment variable.")

    sentry_sdk.init(
        dsn=dsn,
        enable_tracing=True,
        integrations=[
            SparkIntegration(),
        ],
    )
