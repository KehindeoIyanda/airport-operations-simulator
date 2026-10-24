# Airport Operations Simulator — Troubleshooting Guide

## 1. Application Service Is Not Running

**Check the service status:**

```bash
sudo systemctl status airport-simulator.service --no-pager -l
```

**Restart the application:**

```bash
sudo systemctl restart airport-simulator.service
```

**Inspect recent service logs:**

```bash
sudo journalctl -u airport-simulator.service -n 30 --no-pager
```

Look for Python errors, incorrect paths, permission problems, or missing dependencies.

## 2. The API Does Not Respond

Test the local API:

```bash
curl --silent --show-error --fail --max-time 5 http://127.0.0.1:5000/
```

Test the flight endpoint:

```bash
curl --silent --show-error --fail --max-time 5 http://127.0.0.1:5000/flights
```

If the request fails, verify that the application is active and listening on the expected port.

```bash
sudo systemctl is-active airport-simulator.service
sudo ss -ltnp | grep ':5000'
```

## 3. Health Check Fails

Run the health-check service manually:

```bash
sudo systemctl start airport-health-check.service
```

Inspect its recent execution history:

```bash
sudo journalctl -u airport-health-check.service -n 30 --no-pager
```

Read the health-check log:

```bash
tail -n 30 /home/admin/airport-operations-simulator/logs/health_check.log
```

Look for messages beginning with `FAIL:`. Confirm that the application service is running and the local HTTP endpoint responds.

## 4. The Timer Is Not Scheduling Checks

Check whether the timer is enabled:

```bash
sudo systemctl is-enabled airport-health-check.timer
```

Check whether it is active:

```bash
sudo systemctl status airport-health-check.timer --no-pager -l
```

View scheduled timer events:

```bash
systemctl list-timers --all | grep airport
```

If you have changed a systemd unit file, reload systemd's configuration:

```bash
sudo systemctl daemon-reload
```

If the timer is disabled, enable and start it:

```bash
sudo systemctl enable --now airport-health-check.timer
```

## 5. Health-Check Log Is Missing or Cannot Be Written

Check whether the log directory exists:

```bash
ls -ld /home/admin/airport-operations-simulator/logs
```

Check the log file:

```bash
ls -l /home/admin/airport-operations-simulator/logs/health_check.log
```

Confirm that the account running the script has permission to write to the directory and file. Avoid changing permissions broadly with `chmod 777`.

## 6. systemd Unit Changes Do Not Take Effect

After modifying a unit file under `/etc/systemd/system/`, run:

```bash
sudo systemctl daemon-reload
```

Then restart the relevant service or timer if appropriate.

For a service that has failed repeatedly, inspect the journal before attempting further changes:

```bash
sudo journalctl -u airport-simulator.service -n 50 --no-pager
```

## 7. Useful Diagnostic Commands

| Command | Purpose |
|---|---|
| `systemctl is-active airport-simulator.service` | Checks application service state |
| `systemctl status airport-simulator.service` | Shows service details |
| `systemctl list-timers --all` | Lists systemd timers |
| `journalctl -u airport-simulator.service` | Reads application service logs |
| `journalctl -u airport-health-check.service` | Reads health-check execution history |
| `curl http://127.0.0.1:5000/flights` | Tests the flight API |

## Troubleshooting Approach

1. Identify the failing component.
2. Check its current status.
3. Read the relevant logs.
4. Test the API independently.
5. Make one change at a time.
6. Repeat the failed test to verify the fix.

## Safety Notice

This project uses fictional flight data for learning Linux administration and backend operations. It does not connect to real airport or air traffic control systems.
