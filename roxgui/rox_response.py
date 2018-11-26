# encoding: utf-8
#
# Class encapsulating ROXconnector response.
#
# devs@droxit.de
#
# Copyright (c) 2018 droxIT GmbH
#


class RoxResponse:
    """Class encapsulating ROXconnector response."""

    def __init__(self, success: bool, message: str = ""):
        self.success = success
        self.message = message
        # Provided data concerning successful request.
        self._data = []
        # Provided data concerning failed request.
        self._error_data = []

    # Getter and setter.
    # ==================

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, new_data):
        self._data = new_data

    @property
    def error_data(self):
        return self._error_data

    @error_data.setter
    def error_data(self, new_data):
        self._error_data = new_data