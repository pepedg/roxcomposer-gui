# encoding: utf-8
#
# Define HTTP responses with JSON data.
#
# devs@droxit.de
#
# Copyright (c) 2019 droxIT GmbH
#

from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from web.local_request import file_request


@require_http_methods(["POST"])
def get_services(request):
    # Get JSON data of local services.
    file_result = file_request.get_local_services()
    local_services_json_dict = file_result.data
    # Prepare and return JSON response.
    context = {"local_services": local_services_json_dict}
    return JsonResponse(context)
