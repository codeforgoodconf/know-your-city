# Setting up your development environment

1. Install [docker](https://www.docker.com/).
1. Clone this repo.
1. Copy `example.env` to `.env` and modify as needed.
1. Build the docker images with `make dev-build`.
1. To start the app, spin up the docker containers with `make dev-up`.
1. Perform an initial database migration with `make dev-migrate`.
1. See the app by visiting [https://localhost:8000](https://localhost:8000).
1. Shut down the app with `make dev-down`.
