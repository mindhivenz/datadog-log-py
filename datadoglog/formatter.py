from pythonjsonlogger import jsonlogger

# From: https://github.com/jd/daiquiri/blob/master/daiquiri/formatter.py


class DatadogFormatter(jsonlogger.JsonFormatter):
    def __init__(self):
        super().__init__(timestamp=True)

    def add_fields(self, log_record, record, message_dict):
        super(DatadogFormatter, self).add_fields(log_record, record, message_dict)
        log_record["status"] = record.levelname.lower()
        log_record.pop("level", None)
        log_record["logger"] = {"name": record.name}
        if record.exc_info:
            log_record["error"] = {
                "kind": record.exc_info[0].__name__,
                "stack": message_dict.get("stack_info"),
                "message": message_dict.get("exc_info"),
            }
            log_record.pop("exc_info", None)
            log_record.pop("stack_info", None)
