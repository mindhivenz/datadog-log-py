# Datadog-log

Write out JSON formatted logs in the format and with
the [attributes](https://docs.datadoghq.com/logs/log_configuration/attributes_naming_convention/#default-standard-attribute-list)
that Datadog expects

## Installation

`pip install datadog-log`

## Setup

The simplest way is to use `init_logging()` which will log to stdout.

If you want finner control then you can use `DatadogFormatter` directly. See `init_logging` for example usage.

## Logging

Use logging as normal:

```python
import logging
import datadoglog

datadoglog.init_logging()
log = logging.getLogger("example")
log.setLevel(logging.INFO)
log.info("Some info", extra={"extra": ["json"]})
```

The above would output json like below (but as a single line, shown 'pretty' here for readability):

```json
{
  "message": "Some info",
  "extra": ["json"],
  "timestamp": "2021-09-18T21:14:07.707371+00:00",
  "status": "info",
  "logger": {
    "name": "example",
    "method_name": "<stdin>.<module>",
    "thread_name": "MainThread"
  }
}
```
