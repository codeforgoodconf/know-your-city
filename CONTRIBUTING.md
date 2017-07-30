# Setting up your development environment

1. Install [docker](https://www.docker.com/).
2. Clone this repo.
3. Copy `example.env` to `.env` and modify as needed.
4. Build the docker images with `make dev-build`.
5. To start the app, spin up the docker containers with `make dev-up`.
6. See the app by visiting [http://localhost:8000](http://localhost:8000).
7. Shut down the app with `make dev-down`.
