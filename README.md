# Dj-Online-Courses

Dj-Online-Courses is a web application built with Django and Vue.js that provides online courses functionality. It utilizes REST API architecture and is containerized using Docker. The project also integrates Redis for caching, PostgreSQL as the database, Celery for handling asynchronous tasks, and caching mechanisms for improved performance.

## Getting Started

### Prerequisites

Make sure you have the following installed on your machine:

- Docker
- Docker Compose

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Mohamed00Abdelmonem/Dj-Online-Courses.git
cd Dj-Online-Courses
```

2. Build and run the Docker containers:

```bash
docker-compose up --build
```

3. Access the application:

Open your browser and go to [http://localhost:8000](http://localhost:8000)

## Project Structure

The project structure is organized as follows:

- **backend**: Django application code.
- **frontend**: Vue.js application code.
- **docker**: Docker configuration files.
- **config**: Configuration files for various services.
- **requirements.txt**: Python dependencies.

## Technologies Used

- **Django**: Backend framework.
- **Vue.js**: Frontend framework.
- **Docker**: Containerization.
- **Redis**: Caching.
- **PostgreSQL**: Database.
- **Celery**: Asynchronous task processing.

Make sure to replace the placeholders like `[http://localhost:8000](http://localhost:8000)` with the actual URLs and add any additional information or sections specific to your project. Additionally, consider adding a `CONTRIBUTING.md` file if you want to provide guidelines for contributors.
