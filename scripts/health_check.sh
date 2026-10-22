#!/bin/bash

 # Airport Operations Simulator - Health Check

SERVICE="airport-simulator"
URL="http://127.0.0.1:5000/"
LOG_DIR="/home/admin/airport-operations-simulator/logs"
LOG_FILE="$LOG_DIR/health_check.log"


# Create the log directory if it does not exist

mkdir -p "$LOG_DIR"


# Record a message on the screen and in the log file


log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log_message "Starting health check."



# Check whether the systemd service is running
if systemctl is-active --quiet "$SERVICE"; then
log_message "PASS: Airport simulator service is running."
else
log_message "FAIL: Airport simulator service is not running."
exit 1
fi


# Check whether the API responds successfully
if curl -silent --fail --max-time 5 "$URL" > /dev/null; then
log_message "PASS: Airport simulator API is responding."
else
log_message "FAIL: Airport simulator API is not responding."
exit 1
fi

log_message "SUCCESS: All health checks passed."




