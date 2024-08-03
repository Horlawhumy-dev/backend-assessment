# Task Management Backend Assessment

A simple Django Rest backend for a tasks mananagement for users to manage all tasks. It supports basic CRUD (Create, Read, Update, Delete), search and filtering of all tasks .

### Note: Future enhancements would be to use:
** Redis for catche and realtime updates
** Kafka or Rabbitmq handling stream of tasks creation
** Introduce email engine for notifications

## Getting Started

### Prerequisites

- Python 3.8+ install
- Make install

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Horlawhyumy-dev/backend_assessment.git
   cd backend_assessment
    ```


2.  **Create Virtual Environment and Install Requirements**
    ```bash
        python3 -m venv env
        source env/bin/activate  # On Windows use `env\Scripts\activate`
        make install
    ```

3. **Build Docker Image**
    ```bash
        make build
    ```

4. **Start Docker Containers**

    ```
        make up
    ```

5. **Run Migrations**

    ```bash
        make migrate
    ```
6. **Create Super User**

    ```bash
        make createsuperuser
    ```

## Internal API Endpoints Documentation

    ```
        ./api_doc.txt file
    ```

## Assessment Feedback 🙏
