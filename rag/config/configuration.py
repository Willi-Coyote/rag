from abc import ABC
from dataclasses import dataclass


@dataclass
class Configuration(ABC):
    azure_app_insights_connection_string: str
    token_validation: bool


class MissingConfigurationException(Exception):
    def __init__(self, key: str, additional_message: str = ""):
        self.message = (f"No value could be found for the configuration key '{key}'. "
                        f"{additional_message}")
        super().__init__(self.message)
