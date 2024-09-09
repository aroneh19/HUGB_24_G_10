# Hugb2024Template

This is a template project that contains the structure for the project work in T-303-HUGB Software Engineering, Fall 2024.

Please make sure to read the [Code of Conduct](https://gitlab.com/grischal/hugb2024template/-/blob/main/code-of-conduct.md).

## Running instructions
All commands are run from the src/ folder. You have to adapt your commands if you want to run from the top-level folder.

To execute the Flask server, run ``flask --app app.server.server run``. Unit tests are executed using ``python3 -m unittest test.interface_test`` (to run all tests in the module ``interface_test``) or ``python3 -m unittest discover -s test -p '*_test.py'`` (to run all tests in all modules ending on ``_test.py`` in the test folder).

To additionally run coverage analysis, unittest can be executed as a part of the ``coverage`` tool: 

```
coverage erase #erases the coverage file
coverage run -m unittest test.interface_test #runs all tests in module "test/interface_test.py" and records coverage
coverage run --append -m unittest test.interface_test #same as above, but does not override previous coverage information
coverage run --source app -m unittest test.interface_test #Only collects coverage information about the code in app folder
coverage report #shows textual coverage summary
coverage html #generates an HTML coverage report
```