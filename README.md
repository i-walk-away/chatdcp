# ChatDCP

Simple messenger powered by FastAPI & SQLAlchemy.

## About this project

This is a backend for a messenger application. It features authorization, group chats
for any amounts of people and simple message exchange. **Three-tier-architecture** is established
in the source code, simplifying the process of adding new features.

## Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [MySQL](https://www.mysql.com/)
- [Docker](https://www.docker.com/)

## Setup & Installation

- Make `.env` file using [.env.example](.env.example) as a template

- Clone the repository and run the following command to build the project:  
  `docker-compose up --build`

- Apply database migrations:  
  `alembic upgrade head`

> make sure you check an important note about migrations in [.env.example](.env.example)
