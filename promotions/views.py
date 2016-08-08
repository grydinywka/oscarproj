from django.core.urlresolvers import reverse
from django.views.generic import RedirectView, TemplateView
from oscar.apps.catalogue.models import Category, Product
from oscar.core.loading import get_class, get_model
from django.core.paginator import InvalidPage
from django.shortcuts import get_object_or_404, redirect


get_product_search_handler_class = get_class(
    'catalogue.search_handlers', 'get_product_search_handler_class')

class HomeView(TemplateView):
    """
    This is the home page and will typically live at /
    """
    context_object_name = "products"
    template_name = 'promotions/home.html'

    def dispatch(self, request, *args, **kwargs):

        return super(HomeView, self).dispatch(request,*args, **kwargs)

    def render_to_response(self, context, **response_kwargs):
        # import pdb;pdb.set_trace()
        return super(HomeView, self).render_to_response(context, **response_kwargs)
    #
    # def get_context_data(self, **kwargs):
    #     context =  super(HomeView, self).get_context_data(**kwargs)
    #     context['products'] = Product.objects.all()
    #     print context['products']
    #     return context
    #
    def get(self, request, *args, **kwargs):
        try:
            self.search_handler = self.get_search_handler(
                self.request.GET, request.get_full_path(), [])
        except InvalidPage:
            # Redirect to page one.
            return redirect('catalogue:index')
        return super(HomeView, self).get(request, *args, **kwargs)

    def get_search_handler(self, *args, **kwargs):
        return get_product_search_handler_class()(*args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(HomeView, self).get_context_data(**kwargs)
        ctx['summary'] = "All products"
        search_context = self.search_handler.get_search_context_data(
            self.context_object_name)
        ctx.update(search_context)
        return ctx

class RecordClickView(RedirectView):
    """
    Simple RedirectView that helps recording clicks made on promotions
    """
    permanent = False
    model = None

    def get_redirect_url(self, **kwargs):
        try:
            prom = self.model.objects.get(pk=kwargs['pk'])
        except self.model.DoesNotExist:
            return reverse('promotions:home')

        if prom.promotion.has_link:
            prom.record_click()
            return prom.link_url
        return reverse('promotions:home')
