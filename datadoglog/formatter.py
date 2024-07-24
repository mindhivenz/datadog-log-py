from pythonjsonlogger import jsonlogger

# Originally from: https://github.com/jd/daiquiri/blob/master/daiquiri/formatter.py

DATADOG_UNIFIED_TAG_ATTRIBUTES = {"dd.env", "dd.service", "dd.version"}


class DatadogFormatter(jsonlogger.JsonFormatter):
    def __init__(self):
        super().__init__(timestamp=True)
        try:
            import better_exceptions
        except ModuleNotFoundError:
            self._format_exception = lambda _: None
        else:
            self._format_exception = lambda ei: "".join(better_exceptions.format_exception(*ei))

    def add_fields(self, log_record, record, message_dict):
        super().add_fields(log_record, record, message_dict)
        log_record["status"] = record.levelname.lower()
        log_record.pop("level", None)
        logger_dict = {
            "name": record.name,
            "method_name": f"{record.module}.{record.funcName}",
        }
        if record.threadName:
            logger_dict["thread_name"] = record.threadName
        log_record["logger"] = logger_dict
        if record.exc_info:
            error_dict = {
                "stack": self._format_exception(record.exc_info) or message_dict.get("stack_info"),
                "message": message_dict.get("exc_info"),
            }
            if record.exc_info[0]:
                error_dict["kind"] = record.exc_info[0].__name__
            log_record["error"] = error_dict
            log_record.pop("exc_info", None)
            log_record.pop("stack_info", None)
        for attr in DATADOG_UNIFIED_TAG_ATTRIBUTES:
            # If not set explicitly these will be blank, blocking them being set through other means
            # For example, determined based on the container producing the logs
            if attr in log_record and log_record[attr] == "":
                del log_record[attr]
