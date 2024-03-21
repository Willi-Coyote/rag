from typing import Protocol


class OpenTelemetry(Protocol):
    def configure_azure_monitor(self, connection_string: str):
        ...
