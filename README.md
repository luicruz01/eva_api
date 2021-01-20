# eva_api

API for EVA

# Prerequisites
- Python 3.8
- Make (used as a task runner)

# Development setup
To init the development environment, you should just run

```shell
make init
```

This will:
- Initialize a git repository
- Create python virtual environment on `.venv` with default dev dependencies installed
- Install pre-commit hooks

## Running scripts inside virtual env
```shell
source .venv/bin/activate.fish
python eva_api/eva_api.py
```

# Running tests
`pytest` is used for running tests inside the project.

You can use the Makefile script to run all the test battery
```shell
make test
```

# Linting
To lint the code, you can use
```shell
make lint
```

# Running the development server
You can start a `flask` development server by running
```shell
make run
```

This will start a server on the default ports. If you need to change the port, just overwrite the command on the Makefile
