import os
from typing import List

from django.http import HttpResponseNotAllowed
from django.shortcuts import render


class AllowedMethods:
    def __init__(self, allowed_methods: List[str]):
        self.allowed_methods = [m.upper() for m in allowed_methods]

    def __call__(self, view_func):
        def wrapped_view_func(request, *args, **kwargs):
            method = request.method.upper()

            if method not in self.allowed_methods:
                return HttpResponseNotAllowed(
                    self.allowed_methods,
                    content=render(
                        request,
                        'not_allowed_405.html',
                        context={'method': method, 'project_name': os.getenv('PROJECT_NAME')}
                    )
                )
            return view_func(request, *args, **kwargs)

        return wrapped_view_func
