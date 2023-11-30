from django.apps import AppConfig


class MonAppConfig(AppConfig):
    
    name = 'monapp'
    
def ready(self):
    import monapp.signals
        
