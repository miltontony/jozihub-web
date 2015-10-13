'''
Created on 25 Nov 2013

@author: michael
'''
from django.views import generic as generic_views

from tunobase.core import utils as core_utils
from tunobase.corporate.media import models
from forms import VenueHireForm
from django.contrib import messages

class Events(generic_views.TemplateView):

    def get_context_data(self, *args, **kwargs):
        context = super(Events, self).get_context_data(**kwargs)

        events = models.Event.objects.permitted().for_current_site()

        context.update({
            'current_and_future_events': events.current_and_future_events()\
                   .order_by('start'),
            'past_events': events.past_events(),
            'object_list': events,
        })


        return context


class EventDetail(generic_views.DetailView):

    def get_object(self):
        return core_utils.get_permitted_object_or_404(
            models.Event,
            slug=self.kwargs['slug']
        )

class VenueHire(generic_views.edit.FormView):
    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, 'Venue request sent')
        return self.render_to_response(self.get_context_data(form=form))
