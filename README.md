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
from datadoglog import init_logging

init_logging()
log = logging.getLogger("example")
log.info("This line")
log.debug("With extra info", extra={ "json": "data" })
```
