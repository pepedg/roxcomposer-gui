# encoding: utf-8
#
# Define database models.
#
# devs@droxit.de
#
# Copyright (c) 2018 droxIT GmbH
#

import datetime

from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=200)
    service_json = models.TextField()

    def __str__(self):
        return self.name


class Logline(models.Model):
    service = models.CharField(max_length=200)
    msg = models.TextField()
    msg_id = models.CharField(max_length=200, default="")
    level = models.CharField(max_length=200, default="debug")
    time = models.DateTimeField()

    def __str__(self):
        logline = ""
        if self.time:
            logline += "{} ".format(str(self.time))
        if self.msg_id:
            logline += "Message ID: {}, ".format(self.msg_id)
        if self.service:
            logline += "Service: {}, ".format(self.service)
        if self.msg:
            logline += "Message: {}, ".format(self.msg)
        if self.level:
            logline += "Loglevel: {}, ".format(self.level)
        return logline

    def to_dict(self):
        return {"id":self.id, "service":self.service, "msg":self.msg, "level":self.level, "time":self.time.strftime("%B %d, %Y %H:%M"), "text": str(self)}


class Message(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    pipeline = models.CharField(max_length=200, default="")
    time = models.DateTimeField(default=datetime.datetime.now())
    message = models.TextField(default="")

    def __str__(self):
        return "Message ID: {} to pipeline: {}, created at {} \n {}".format(self.id, self.pipeline, self.time, self.message)

    def to_dict(self):
        return {"id":self.id, "pipeline":self.pipeline, "time":self.time.strftime("%B %d, %Y %H:%M"), "message":self.message}

class MessageStatus(models.Model):
    msg_id = models.CharField(max_length=200, default="")
    event = models.CharField(max_length=200, default="")
    status = models.CharField(max_length=200, default="")
    time = models.DateTimeField(default=None, null=True)
    service_name = models.CharField(max_length=200, default="")
    processing_time = models.TimeField(default=None, null=True)
    total_processing_time = models.TimeField(default=None, null=True)

    def __str__(self):
        return "Event: {}, Status: {}, Time: {}, Args: " \
               "Service_Name: {}, Message_ID: {}, Processing Time: {}, " \
               "Total Processing Time: {}".format(self.event, self.status, str(self.time),
                                                     self.service_name, self.msg_id,
                                                  str(self.processing_time), str(self.total_processing_time))

    def to_dict(self):
        return {"msg_id" : self.msg_id, "event": self.event, "status":self.status, "time":self.time.strftime("%B %d, %Y %H:%M"),
                "service_name":self.service_name, "processing_time":self.processing_time, "total_processing_time":self.total_processing_time}


class RoxSession(models.Model):
    """
    Table to store GUI sessions.

    A single session documents which services are currently being watched,
    together with corresponding ROXcomposer IDs and specified timeouts.
    """
    id = models.CharField(max_length=200, primary_key=True)
    services = models.TextField()
    timeout = models.IntegerField()

    def __str__(self):
        return "ID: {}, TIMEOUT: {}, SERVICES: {}.".format(str(self.id), str(self.timeout), str(self.services))