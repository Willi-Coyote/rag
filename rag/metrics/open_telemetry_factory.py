from config import configuration
from config.configuration import Environment
from metrics.azure.azure_open_telemetry import AzureOpenTelemetry
from metrics.open_telemetry import OpenTelemetry


def get_open_telemetry() -> OpenTelemetry:
    environment = configuration.environment
    return {
        Environment.AZURE: AzureOpenTelemetry(configuration),
        Environment.AWS: None
    }.get(environment, None)
