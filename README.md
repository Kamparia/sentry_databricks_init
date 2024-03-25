# sentry_databricks_init
This Python package provides an easy way to initialize [Sentry SDK with Databricks](https://docs.sentry.io/platforms/python/integrations/spark/) integration, making error tracking and monitoring in Databricks notebooks simpler.

## Features
- Easy initialization of Sentry SDK within Databricks notebooks
- Optional DSN configuration via environment variable

## Pre-requisites
Before you begin, ensure you have met the following requirements:

- Python 3.8+
- A Sentry account and a DSN for your project

## Installation
To install `sentry_databricks_init`, run the following command:

```bash
pip install sentry-databricks-init
```

## Usage
To use `sentry_databricks_init`, import the `init_sentry` function and call it in your Databricks notebook:

```python
from sentry_databricks_init import init_sentry

# Initialize with a DSN
init_sentry("your_sentry_dsn_here")

# Or, if you've set the SENTRY_DSN environment variable:
init_sentry()
```

Setting the `SENTRY_DSN` environment variable is recommended for security reasons. You can set it in your Databricks cluster's configuration.

## Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

To contribute to `sentry_databricks_init`, follow these steps:

1. Fork this repository.
2. Create a new branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`.
4. Push to the original branch: `git push origin <project_name>/<location>`.
5. Create a pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Running Tests
To run tests, run the following command:

```bash
python -m unittest discover tests
```

This command will discover and run all tests in the `tests` directory.

## Contact
If you want to contact me, you can reach me at [somideolaoye@gmail.com](mailto:somideolaoye@gmail.com).

## License
This project uses the following license: [MIT License](https://github.com/Kamparia/sentry_databricks_init/blob/main/README.md).
