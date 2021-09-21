from django.apps import AppConfig


class CtacConfig(AppConfig):
    name = 'ctac'


    def ready(self):
        import ctac.signals
