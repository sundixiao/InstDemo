from django.views.generic import TemplateView

class HelloWord(TemplateView):
    template_name = 'test.html'