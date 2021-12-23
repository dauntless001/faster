from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import View

# Create your views here.

class IndexView(View):
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, self.template_name, context)
    


class ContactView(View):
    def get(self, request):
        return redirect('base:index')
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            data = {}
            return JsonResponse(data, safe=False)


class ApplyView(View):
    def get(self, request):
        return redirect('base:index')
    def post(self, request, *args, **kwargs):
        if request.is_ajax():
            data = {}
            data['message']= 'You will receive a mail shortly on how to Become a partner with Faster'
            return JsonResponse(data, safe=False)