from django.shortcuts import render
from django.http import (HttpResponse, 
                         HttpRequest,
                         )
from django.views import View

class HomeView(View):
    def get(self, request):
        return render(request = request,
                      context = {},
                      template_name = 'test_app/index.html',
                      )