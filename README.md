# Datadog-log

Write out JSON formatted logs in the format that Datadog expects

## Installation

`pip install datadog-log`

## Setup

The simplest way is to use `init_logging()` which will log to stdout.

If you want finner control then you can use `DatadogFormatter` directly. 
See `init_logging` for example usage. 

## Logging

Use logging as normal:

```python
import logging
import datadoglog

datadoglog.init_logging()
log = logging.getLogger("example")
log.setLevel(logging.INFO)
log.info("Some info", extra={"extra": "json"})
# Outputs {"message": "Some info", "extra": "json", "timestamp": "2021-02-02T19:11:12.716126+00:00", "status": "info", "logger": {"name": "example"}}
```
