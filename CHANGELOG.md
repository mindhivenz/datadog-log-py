# Change log history

## 1.4.0

- If Datadog unified tag attributes are set but blank then remove them so Datadog will fallback to trying to determine
  them from other sources (for example the container producing the logs)

## 1.3.0

- Add more standard attributes:
    - `logger.thread_name`
    - `logger.method_name`   
