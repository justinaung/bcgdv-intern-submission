# BCGDV Internship Application Submission

## Requirements
- Python 3.7
- pipenv

## Installation
Type in the following command line in the root directory to install the requirements.
```
pipenv install --python=3.7
```

And, enter this command to load the python virtual environment.
```
pipenv shell
```

## Usage

Load the BCGDV interns base url as `BASE_URL` to the environment.

Use the follow command line to submit internship application to BCGDV. You will need to provide your name and email.
```
python submit_application.py -n <name> -e <email>
```
