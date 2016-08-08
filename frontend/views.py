from django.shortcuts import render
from django.views.generic import RedirectView, TemplateView

class FrontendView(TemplateView):
    template_name = "front_end/template1.html"
    def get_template_names(self):
        pk = self.kwargs['pk']
        if pk:
            name = ( 'front_end/template%s.html' % self.kwargs['pk'] )
        else:
            name = 'front_end/template.html'
        return [name]