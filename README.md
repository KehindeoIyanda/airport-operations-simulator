# Airport Operations Backend Simulator

## Project Overview

The Airport Operations Backend Simulator is a Linux home-lab project designed to practice backend application hosting, Linux system administration, service monitoring, and automation.

The application uses Python and Flask to serve fictional airport flight information. It runs as a background service on Rocky Linux and includes automated health checks, timestamped logging, and scheduled monitoring through systemd timers.

## Project Objectives

- Host a Python Flask API on Rocky Linux.
- Manage application services using systemd.
- Automate service and HTTP availability checks with Bash.
- Record health-check results in timestamped log files.
- Schedule recurring monitoring tasks using systemd timers.
- Practice Git version control and prepare the project for future CI/CD automation.

## Additional Documentation

- [Architecture Diagram](docs/architecture.md) — application components and health-check workflow.
- [Troubleshooting Guide](docs/troubleshooting.md) — commands for diagnosing service, API, timer, and logging issues.


## Technology Stack

| Technology | Purpose |
|---|---|
| Rocky Linux 9.8 | Linux server operating system |
| Python | Application programming language |
| Flask | Backend API framework |
| Bash | Health-check automation |
| systemd | Application service management |
| systemd timers | Scheduled health checks |
| curl | HTTP availability testing |
| Git | Source control and version management |

## Architecture

1. The Flask application serves fictional flight information.
2. `airport-simulator.service` runs the application in the background.
3. `health_check.sh` checks whether the service is active and the API responds.
4. The script records timestamped results in a log file.
5. `airport-health-check.service` executes the health-check script.
6. `airport-health-check.timer` schedules recurring health checks approximately every five minutes.

## Current Features

- Fictional flight information endpoint.
- Background application service.
- Automated service availability checks.
- HTTP endpoint validation using curl.
- Timestamped health-check logs.
- Scheduled monitoring with systemd timers.
- Git repository with generated logs excluded.

## API Endpoints

The application listens locally on port 5000.

| Endpoint | Purpose |
|---|---|
| `/` | Application health/landing response |
| `/flights` | Returns fictional flight information |

## Automated API Testing

The project includes automated API tests using `pytest` to validate the core Flask endpoints.

Run the test suite from the project root:

```bash
source .venv/bin/activate
python -m pytest -v
```

### Current Test Coverage

| Test | Result |
|---|---|
| `test_home_endpoint` | Passed |
| `test_flights_endpoint` | Passed |

**Latest local test run:** 2 tests passed.

Automated tests help verify API behavior and catch regressions when application code changes. Rerun the tests after relevant code updates.

## Continuous Integration with GitHub Actions

The project uses GitHub Actions to automatically run API tests when code is pushed to the `master` branch or when a pull request targets `master`.

### CI Workflow

The workflow is defined in `.github/workflows/ci.yml` and performs the following steps:

1. Checks out the repository.
2. Sets up Python 3.9.
3. Installs project dependencies from `requirements.txt`.
4. Runs the automated API test suite with `pytest`.

### Workflow Environment

- **CI platform:** GitHub Actions
- **Runner:** Ubuntu 24.04
- **Python:** 3.9
- **Test framework:** pytest
- **Workflow file:** `.github/workflows/ci.yml`

### Validation

The initial GitHub Actions workflow run failed during Python setup because of a runner/version configuration issue. The configuration was corrected, and workflow run #2 completed successfully.

The CI pipeline provides automated feedback on API test results after code changes are pushed to GitHub.

Test the application locally:

```bash
curl http://127.0.0.1:5000/