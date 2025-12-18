# Oilfield Project

A Python-based management system for oilfield operations. This project uses Django and Docker to provide a scalable environment for tracking resources and operational data.

## 🚀 Features

- **Oilfield Operations Management:** Core logic for tracking field activities.
- **Resource Tracking:** Manage equipment and site resources.
- **Dockerized Environment:** Easy setup using Docker and Docker Compose.
- **Environment Configuration:** Support for `.env` variables.

## 🛠️ Tech Stack

- **Language:** Python 3.12+
- **Framework:** Django
- **Containerization:** Docker & Docker Compose
- **Environment Management:** Python-dotenv

## 📦 Project Structure

```text
.
├── oilfield_operations/    # Core Django application/settings
├── resources/              # Resource management module
├── manage.py               # Django management script
├── Dockerfile              # Docker build instructions
├── docker-compose.yaml     # Service orchestration
└── requirements.txt        # Python dependencies

```

## ⚙️ Getting Started

### Prerequisites

- Docker and Docker Compose installed.
- Python installed (if running locally without Docker).

### Running with Docker

1. Clone the repository:

```bash
git clone [https://github.com/emilx01/oilfield_project.git](https://github.com/emilx01/oilfield_project.git)
cd oilfield_project

```

2. Build and start the containers:

```bash
docker-compose up --build

```

### Running Locally

1. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # or venv/bin/activate.fish

```

2. Install dependencies:

```bash
pip install -r requirements.txt

```

3. Run migrations and start the server:

```bash
python manage.py migrate
python manage.py runserver

```
