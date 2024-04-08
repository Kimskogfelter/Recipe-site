from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from .models import ProfileModel
from .forms import ProfileForm


class ProfilesView(TemplateView):
    """View for user profiles"""

    template_name = "profiles/profile.html"

    def get_context_data(self, **kwargs):
        profile = ProfileModel.objects.get(user=self.kwargs["pk"])
        context = {
            "profile": profile,
            'form': ProfileForm(instance=profile)
        }

        return context
