# Python scraper with a rest api 
This repo contains an example of scraper of Amazon page using BS4. 

You can get all products params and send it to be visible in the REST API endpoint.

It's possible to add or not some tags to get a  specific information, like best seller, rating ...etc

## Setting up your development environment

### Installing the libraries
At the same directory as this file, run:
  - `pip install pipenv`
  - `pipenv install`

### Running the API for development
Initialize your app using `pipenv`:

- `pipenv shell`

Then run the following commands:

- `uvicorn app.main:app --reload`

And your app will be running on http://localhost:8000/

Tip:

Access http://localhost:8000/docs to use the built-in interface.

### Running with debug on
If you want to run debbuging the aplication, you need to create a configuration (launch.json) like this:
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: Uvicorn",
            "type": "debugpy",
            "request": "launch",
            "module": "uvicorn",
            "args": ["app.main:app", "--reload"],
            "console": "integratedTerminal",
            "justMyCode": true,
            "env": {
                "PYTHONPATH":"${workspaceFolder}"
            }
        }
    ]
} 
