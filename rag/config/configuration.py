from abc import ABC
from dataclasses import dataclass


@dataclass
class Configuration(ABC):

    azure_app_insights_connection_string: str
    token_validation: bool



