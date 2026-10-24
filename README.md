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

Test the application locally:

```bash
curl http://127.0.0.1:5000/