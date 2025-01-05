import os

from django.template.response import TemplateResponse


def home(request):
    return TemplateResponse(request, 'home_page.html', {'project_name': os.getenv('PROJECT_NAME')})
