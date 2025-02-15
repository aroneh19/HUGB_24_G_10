# Meet4Real - Social Networking App for Making Friends

Social networking app that connects users based on shared interests, fostering meaningful frienships and communities.
Users can create profiles, highlight their hobbies and match with others who have similar passions, from spors and outdoor activities to book clubs and gaming
Our goal is to enable natural, interest-based connections and encourage real-world meetups.

Overview Report on Google Docs [here](https://docs.google.com/document/d/152uOSO3HXaR_VH70s5MGvPoHjmaE9rNMEzw18Dn9ckw/edit?usp=sharing).

## Table of Contents
- [Installation](#installation)
- [Running Instructions](#running-instructions)
- [Features](#features)
- [License](#license)

## Installation
1. Clone the repository:
```bash
git clone https://gitlab.com/aroneh19/hugb-24-g-10.git
```

## Running instructions
All commands are run from the src/ folder. You have to adapt your commands if you want to run from the top-level folder.

To execute the Flask server, run:
```bash
flask --app app.server.server run
```
Unit tests are executed using: 
```bash
python -m unittest test.base_test
```
(to run all tests in the module ``base_test``) or :
```bash
python -m unittest discover -s test -p '*_test.py'
```
(to run all tests in all modules ending on ``_test.py`` in the test folder).

To additionally run coverage analysis, unittest can be executed as a part of the ``coverage`` tool: 

Erases the coverage file:
```bash
coverage erase
```
Runs all tests in module "test/base_test.py" and records coverage:
```bash
coverage run --omit="test/*" -m unittest test.base_test
```
Same as above, but does not override previous coverage information:
```bash
coverage run --append --omit="test/*" -m unittest test.base_test
```
Only collects coverage information about the code in app folder:
```bash
coverage run --source app -m unittest test.base_test
```
Shows textual coverage summary:
```bash
coverage report
```
Generates an HTML coverage report:
```bash
coverage html
```

## Features

- Create a Profile and log in
- Swiping to match with others
- Messages for matches
- Filtering by: Interests, Location, Age and Gender
- Edit Profile
- Unmatch option
- See friendship status of matches

## License
This project is licensed under the [MIT License] (LICENSE).


