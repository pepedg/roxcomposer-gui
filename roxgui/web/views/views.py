import os

import requests
from django.http import JsonResponse
from web.local_request import rox_request
from web.local_request.rox_response import RoxResponse


def check_rox_composer_log_file_path(file_path: str) -> bool:
    """
    Check if ROXcomposer log file is
    available using specified path.
    :param file_path: str - Path to ROXcomposer log file.
    :return: True if ROXcomposer log file is available
        using specified path and False otherwise.
    """
    return os.path.isfile(file_path)


def check_rox_connector_url(url: str) -> bool:
    """
    Check if ROXconnector is
    available using specified URL.
    :param url: str - ROXconnector URL.
    :return: bool - True if ROXconnector is available
        using specified URL and False otherwise.
    """
    try:
        requests.get(url)
        return True
    except requests.exceptions.ConnectionError:
        return False


def check(request) -> RoxResponse:
    """
    Check if parameters specified
    in config.ini file are valid.
    :param request: HTTP request.
    :return: RoxResponse - Indicate if parameters
        in config.ini file are valid.
    """
    result = dict()
    success = False

    # Check ROXcomposer directory.
    log_file_path = rox_request.get_rox_composer_log_file_path()
    res = check_rox_composer_log_file_path(log_file_path)
    result["log_file_path"] = (res, log_file_path)
    if not res:
        success = False

    # Check ROXconnector URL.
    url = rox_request.get_rox_connector_url()
    res = check_rox_composer_log_file_path(url)
    result["url"] = (res, url)
    if not res:
        success = False

    response = RoxResponse(success)
    response.data = result
    return JsonResponse(response.convert_to_json())