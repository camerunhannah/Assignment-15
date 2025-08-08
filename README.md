Module 15: Final Project

Project Overview
In this module, the primary goal was to make the application fully functional and robust. This involved:

Finalizing BREAD Functionality: All core database operations for calculations (Create, Read, Edit, Add, Delete) are now fully integrated and accessible via the frontend.

Implementing a Custom Feature: The Modulo function was added as a new, more complex mathematical operation, demonstrating an ability to extend the project's scope.

Continuous Deployment: The entire application stack, from backend code to frontend UI and tests, is packaged into a Docker image and automatically deployed to Docker Hub upon passing all tests.

This project is a comprehensive demonstration of building a secure, tested, and containerized Python web application from start to finish.

Key Features and Learning Outcomes
This project demonstrates mastery of the following concepts:

Full Frontend BREAD for Calculations: Interactive web interfaces for all calculation operations (Add, Browse, View, Edit, Delete) are fully implemented and functional.

Custom Modulo Calculation: A new mathematical operation has been added, extending the core functionality.

Seamless Frontend-Backend Integration: The web-based forms and buttons communicate securely with the JWT-authenticated FastAPI backend.

Comprehensive Automated Testing: Unit, integration, and Playwright End-to-End (E2E) tests cover all new and existing functionalities, ensuring robustness.

Robust CI/CD Pipeline: The GitHub Actions workflow automates building, scanning (with Trivy), and deploying the Docker image to Docker Hub upon successful test completion.

Security Best Practices: Maintained secure authentication and authorization, including password hashing and JWT handling.

How to Run the Application and Tests Locally
To get the project running on your local machine, follow these steps:

Clone the repository:

Bash

git clone https://github.com/camerunhannah/Assignment-15.git
cd Assignment-15/module15_is601
Set up the environment:

Bash

python3.12 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
playwright install
Start Docker Compose services:
Ensure Docker Desktop is running.

Bash

docker compose down -v
docker compose up --build -d
Access the Front-End:
Once the containers are running, open your web browser and navigate to:

Dashboard (after login): http://localhost:8000/dashboard

API Docs: http://localhost:8000/docs

Run Automated Tests:
After your Docker Compose services are running, execute the test suite:

Bash

pytest
Deployment & Final Deliverables
The Docker image for this application is deployed to the following Docker Hub repository:

https://hub.docker.com/r/camhannah/module15_is601

