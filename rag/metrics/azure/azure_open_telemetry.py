from azure.monitor.opentelemetry import configure_azure_monitor

from config.configuration import Configuration
from metrics.open_telemetry import OpenTelemetry


class AzureOpenTelemetry(OpenTelemetry):

    def __init__(self, configuration: Configuration):
        self._connection_String = configuration.azure_app_insights_connection_string

    def configure_azure_monitor(self):
        configure_azure_monitor(connection_string=self._connection_String)
