from pythonjsonlogger import jsonlogger

# From: https://github.com/jd/daiquiri/blob/master/daiquiri/formatter.py

DATADOG_UNIFIED_TAG_ATTRIBUTES = {"dd.env", "dd.service", "dd.version"}


class DatadogFormatter(jsonlogger.JsonFormatter):
    def __init__(self):
        super().__init__(timestamp=True)

    def add_fields(self, log_record, record, message_dict):
        super().add_fields(log_record, record, message_dict)
        log_record["status"] = record.levelname.lower()
        del log_record["level"]
        logger_dict = {
            "name": record.name,
            "method_name": f"{record.module}.{record.funcName}",
        }
        if record.threadName:
            logger_dict["thread_name"] = record.threadName
        log_record["logger"] = logger_dict
        if record.exc_info:
            log_record["error"] = {
                "kind": record.exc_info[0].__name__,
                "stack": message_dict.get("stack_info"),
                "message": message_dict.get("exc_info"),
            }
            del log_record["exc_info"]
            del log_record["stack_info"]
        for attr in DATADOG_UNIFIED_TAG_ATTRIBUTES:
            # If not set explicitly these will be blank, blocking them being set through other means
            # For example, determined based on the container producing the logs
            if attr in log_record and log_record[attr] == "":
                del log_record[attr]
