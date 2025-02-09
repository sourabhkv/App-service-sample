# Flask App Service Sample

This repository contains a sample Flask application that can be deployed as a web service.

## Requirements

To install the required dependencies, run:

```sh
pip install -r requirements.txt
```

### Running the Application
To run the application locally, use the following command:
```sh
python app.py
```

The application will be accessible at http://0.0.0.0:8000

### Endpoints
/: Returns a "Hello, World from flask app!" message.
/time: Returns the current date and time.

### Deployment
To deploy the application using Gunicorn, use the command specified in startup.txt
```sh
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```
