import json_log_formatter
import datetime


class JSONFormatter(json_log_formatter.JSONFormatter):
    def format(self, record, datefmt=None):
        date_format = datetime.datetime.fromtimestamp(record.created)
        if datefmt:
            seconds = date_format.strftime(datefmt)
        else:
            time_render = date_format.strftime("%Y-%m-%dT%H:%M")
            seconds = "%sZ" % time_render
        return seconds

    def json_(self, message, data, record):
        data['severity'] = record.levelname
        data['time'] = self.format(record)
        data['message'] = message
        return super(JSONFormatter, self).json_(message, data, record)
