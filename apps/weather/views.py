import os

from django.http import HttpRequest, HttpResponse
from django.template.response import TemplateResponse

from weathersite.utils import AllowedMethods


@AllowedMethods(['PUT'])
def homepage_view(request:HttpRequest) -> HttpResponse:
    return TemplateResponse(
        request=request,
        template='home_page.html',
        context={'project_name': os.getenv('PROJECT_NAME')}
    )
