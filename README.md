Module 14: Finalizing BREAD, New Feature & Deployment
This repository contains the solution for Module 14, which is the culmination of our backend and CI/CD work. This module focuses on bringing the full BREAD (Browse, Read, Edit, Add, Delete) functionality for calculations to the frontend, integrating it seamlessly with our JWT-secured backend. Additionally, a new, custom project feature has been implemented, showcasing extended application capabilities.

Project Overview
In this module, the primary goal was to make the calculation management fully interactive on the frontend and to integrate a unique final project feature. This involved developing user interfaces for all calculation operations, ensuring client-side validation, and extending Playwright E2E tests to cover these new interactions. The existing Docker-based CI/CD pipeline was maintained to automate testing and deployment, ensuring a fully functional, secure, tested, and containerized Python web application as the final deliverable.

Key Features and Learning Outcomes
This project demonstrates:

Full Frontend BREAD for Calculations: Implemented web interfaces for adding, browsing, viewing, editing, and deleting calculation records.

Seamless Frontend-Backend Integration: Frontend functionality communicates securely with the JWT-authenticated FastAPI backend.

Custom Final Project Feature: A new, extended feature has been added to the application, showcasing additional development capabilities.

Client-Side Validation: Enhanced user experience with JavaScript validation for input fields on frontend forms.

Comprehensive Automated Testing: Extended unit, integration, and Playwright End-to-End (E2E) tests cover all new and existing functionalities, ensuring robustness.

Robust CI/CD Pipeline: The GitHub Actions workflow automates building, scanning (with Trivy), and deploying the Docker image to Docker Hub upon successful test completion.

Containerization & Deployment: Continued application of Docker for containerizing the entire application stack and deploying it.

Security Best Practices: Maintained secure authentication and authorization, including password hashing and JWT handling.

(Optional) Alembic Integration: (If applicable to your custom feature) Demonstrated professional database migration handling.

How to Run the Application and Tests Locally
To set up the project and run the application/tests on your local machine, follow these steps:

Clone the repository:

git clone https://github.com/camerunhannah/Assignment-14.git
cd Assignment-14/module14_is601

(Note: This project was re-initialized to create a clean Git history, so git clone will pull your unique project history.)

Create and activate a Python virtual environment:

python3.12 -m venv venv # Use your specific Python version if different
source venv/bin/activate

Install project dependencies:

pip install --upgrade pip
pip install -r requirements.txt

Install Playwright browser dependencies (for end-to-end tests):

sudo ../venv/bin/playwright install-deps

Start Docker Compose services (PostgreSQL, pgAdmin, and FastAPI app):
Ensure Docker Desktop is running. If you encounter any conflicts, run docker compose down -v first to clear all old containers and volumes.

docker compose up --build -d

Access the Front-End Application (Manual Checks):
Once Docker Compose is running, open your web browser and navigate to:

Login Page: http://localhost:8000/login

Register Page: http://localhost:8000/register

Dashboard (after login): http://localhost:8000/dashboard
Manually test user registration, login, and all calculation BREAD operations (Add, Browse, View, Edit, Delete) on these pages.

Run Automated Tests:
After your Docker Compose services are running, execute your test suite:

pytest

CI/CD Pipeline and Docker Hub Deployment
This project utilizes GitHub Actions for its robust CI/CD pipeline. Upon every push to the main branch, the workflow automatically:

Checks out the code.

Sets up Python and caches pip dependencies.

Installs project dependencies.

Runs all unit, integration, and end-to-end tests against a dedicated PostgreSQL container.

Builds the Docker image for the application.

Scans the Docker image for vulnerabilities using Trivy.

If all tests and security scans pass, the Docker image is pushed to Docker Hub.

Docker Hub Repository
The Docker image for this application is deployed to the following Docker Hub repository:

https://hub.docker.com/r/camhannah/module14_is601

Reflections and Insights
This Module 14 really connected the dots from earlier stuff, bringing my secure user and calculation models to life with FastAPI routes. Doing user login and registration, plus those BREAD operations for calculations, felt like building the actual frontend parts of the backend logic. My SQLAlchemy models were the solid backbone, and the Pydantic schemas just smoothly handled getting data in correctly and sending it back out right. Like, the UserCreate schema made sure registrations were clean, and UserResponse kept private user details safe.

Testing with Pytest and Docker was super important for making sure everything was reliable. Running tests against a real PostgreSQL database, not just fake stuff, proved that the whole flow, from hitting the API to what happened in the database, actually worked. This caught little issues that my unit tests alone couldn't. Thinking about security, these endpoints are locked down with a few layers. There is the password hashing when you log in, Pydantic's data checks, and importantly, making sure users can only mess with their own calculations. This really cemented how important solid security practices are. This whole integration thing just makes my understanding of building strong and safe web APIs even clearer.

#Docker #FastAPI #PostgreSQL #Testing #CI_CD #DevOps #SQLAlchemy #Pydantic #Security #SoftwareDevelopment #Learning #Database #WebDevelopment #Git #Automation #Containerization #DockerHub #Frontend #BREAD #E2ETesting #Playwright #FinalProject