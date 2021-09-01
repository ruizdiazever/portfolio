from django.views.generic import TemplateView

class SteamDeckView(TemplateView):
    template_name = "steamdeck/steamdeck.html"