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
  3. Activate your virtual environment (if applicable).
   ```bash
   `python3 -m venv .venv`

   `source .venv/bin/activate` (Linux/Mac)

   `source .venv/Scripts/activate` (Windows)
   ```
  4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
  5. Apply migrations:
  ```bash
  python manage.py migrate
  ```
  6. **Optional** Create a superuser (admin account) for Django admin access:
  ```bash
  python manage.py createsuperuser
  ```
  Follow the prompts to set up your admin account.
  7. Build and run the Docker containers:
  ```bash
  docker-compose up --build
  ```
  This command builds the Docker images and starts the application. The --build flag is used to ensure that the images are rebuilt if there are changes to the Dockerfile.  
  8. The application will be accessible at http://localhost:8000/ or http://127.0.0.1:8000/.  
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
