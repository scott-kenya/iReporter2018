
# iReporter Application

[![Coverage Status](https://coveralls.io/repos/github/scott-kenya/iReporter2018/badge.svg?branch=develop)](https://coveralls.io/github/scott-kenya/iReporter2018?branch=develop)
[![Build Status](https://travis-ci.com/scott-kenya/iReporter2018.svg?branch=develop)](https://travis-ci.com/scott-kenya/iReporter2018)

App Description
This is a Ireporter application that enables any/every citizen to bring any form of corruption to the notice of appropriate authorities and the general public. Users can also report on things that needs government intervention.

Sign up to the application
Login to the application
Post a redflag or intervention
Get all redflags or intervention
Get single redflags or intervention
Update a redflag or intervention
Delete a redflag or intervention

Installation
Take the following steps:

Create a virtual enviroment with the command $ virtualenv -p python3 venv
Activate the virtual enviroment with the command $ source venv/bin/activate
Ensure you have installed GIT
Clone the repository i.e $ git clone https://github.com/scott-kenya/iReporter2018.git
Install requirements $ pip install -r requirements.txt

Heroku Deploy
https://ireporter-scott.herokuapp.com/

Running Tests
After completing the following, it is time to run the app

To run the tests use $ pytest -v
To run the application use export SECRET_KEY="<your secret key>"
`export FLASK_APP=run.py'
flask run
The following endpoints should be working:

Endpoint	functionality	contraints(requirements)
get /api/v1/redflags	get all the redflags	
get /api/v1/redflags/id	return a single redflag by id
post /api/v1/redflags	create a new redflag

Technologies used include:
Python
Flask
Flask-Restplus
Heroku
Travis CI
Coveralls
