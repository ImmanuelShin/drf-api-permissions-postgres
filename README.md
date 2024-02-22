# Lab - Class 32

## Project: Permissions & Postgresql

### Author: [Immanuel Shin](https://github.com/ImmanuelShin)

A small web application showcasing permissions & Postgresql alongside DRF and Docker.

### Setup

#### Requirements

- Docker: Ensure that you have Docker installed on your machine. You can download and install Docker from [here](https://docs.docker.com/get-docker/).

**How to initialize/run your application:**

  1. Clone the repository.
   ```bash
   git clone
   ```
  2. Navigate to the project directory.
   ```bash
   cd [name-of-directory]
   ```
  3. Build the docker container:
  ```bash
  docker build .
  ```
  4. Run database migrations:
  ```bash
  docker-compose run web python manage.py makemigrations
  docker-compose run web python manage.py migrate
  ``` 
  5. **Optional** Create a superuser (admin account) for Django admin access:
  ```bash
  docker-compose run web python manage.py createsuperuser
  ```
  Follow the prompts to set up your admin account.
  6. Run the Docker containers:
  ```bash
  docker-compose up
  ``` 
  7. The application will be accessible at http://localhost:8000/ or http://127.0.0.1:8000/.  
  - API access at /api/v1/integers endpoint (e.g http://127.0.0.1:8000/api/v1/integers/)
      - Individual details access at /[index] endpoint (e.g http://127.0.0.1:8000/api/v1/integers/1/)  
  - Due to a bug with DRF/Django, switching users will be done via the admin endpoint:
      -   http://127.0.0.1:8000/admin/
#### Cleanup (Optional)

If you want to stop and remove the Docker containers, run the following command:
```bash
docker-compose down
```

### Tests

To run tests, run ```docker-compose -f docker-compose.test.yml up --build```
