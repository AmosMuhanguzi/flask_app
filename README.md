# Banking Flask App Containerised with Docker

This repo contains a simple banking flask application that has the python content directly inside the application.
it displays a user interface for withdraw, depositing and current balance with amount of money withdrawn if any

### app.py
This contains code for the main Flask application.

### Dockerfile
It contains docker configarations for the application.

### requirement.txt
This contains the python dependencies ie Flask==3.1.0

### README.md
This has all the description for the directory.

### How to acces the application
### 1. Clone the Repository 

``` bash
git clone https://github.com/AmosMuhanguzi/flask_app.git
cd flask_app
```

### 2. Build the Docker Image

```bash
docker build -t flask_one .
```
the `Dockerfile` will create a Docker image with the name `flask_app`.

### 3. Run the Docker Container

Once the image is built, run the Flask app container:

```bash
docker run -p 5000:5000 flask_app
```

### 4. Verify the Flask App

on your browser go to `http://localhost:5000`. to access the banking app
