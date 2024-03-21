from abc import ABC
from enum import Enum


class Environment(Enum):
    AZURE = "azure"
    AWS = "aws"


class Configuration(ABC):
    azure_app_insights_connection_string: str
    environment: Environment
    token_validation: bool


class MissingConfigurationException(Exception):
    def __init__(self, key: str, additional_message: str = ""):
        self.message = (f"No value could be found for the configuration key '{key}'. "
                        f"{additional_message}")
        super().__init__(self.message)
