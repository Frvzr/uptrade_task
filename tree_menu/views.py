from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name ='tree_menu/base.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})



class TreeMenuView(TemplateView):
    template_name = 'tree_menu/base.html'
    
    def get(self, request, *args, **kwargs):
        context = {
            'selected_menu': kwargs['selected']
        }
        return render(request, self.template_name , context=context)