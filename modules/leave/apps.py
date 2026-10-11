# apps.py

from django.apps import AppConfig

class LeaveConfig(AppConfig):
    name = 'modules.leave'
    verbose_name = 'Leave Management'

    def ready(self):
        import modules.leave.signals  # Register signals

