# Task Management Backend Assessment

A Django Rest backend for tasks mananagement by users. It supports basic CRUD (Create, Read, Update, Delete), search and filtering of all tasks created.

## Features

- Endpoints for managing users authentication and authorization
- Endpoints for tasks managememnt by users
- Basic error handling
- Solid Continuous Integration Pipeline suporting docker-compose workflows
- Tasks searching and Filtering APIs


### Note: Future enhancements would be to use:
** Redis for catching to reduce database workloads and realtime updates
** Kafka or Rabbitmq handling stream of tasks creation
** Introducing email engine for notifications

## Getting Started

### Prerequisites

- Python 3.8+ install
- Make install
- Docker Compose install

```bash
    curl -L "https://github.com/docker/compose/releases/download/$(curl -s https://api.github.com/repos/docker/compose/releases/latest | jq -r .tag_name)/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

    chmod +x /usr/local/bin/docker-compose
```

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Horlawhyumy-dev/backend_assessment.git
   cd backend_assessment
    ```

2. **Build Docker Image**
    ```bash
        make build
    ```

3. **Start Docker Containers**

    ```
        make up
    ```

4. **To Create SuperUser**

    ```bash
        make createsuperuser
    ```

## Internal API Endpoints Documentation

    ```
        ./api_doc.txt file
    ```

## Assessment Feedback 🙏
