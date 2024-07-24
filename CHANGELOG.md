# Change log history

## 1.5.0

- If `better_exceptions` is installed then use it to format the stacktrace
- Minimum Python version 3.8 now that 3.7 is EOL
- Switch to Poetry

## 1.4.0

- If Datadog unified tag attributes are set but blank then remove them so Datadog will fall back to trying to determine
  them from other sources (for example the container producing the logs)

## 1.3.0

- Add more standard attributes:
    - `logger.thread_name`
    - `logger.method_name`   
