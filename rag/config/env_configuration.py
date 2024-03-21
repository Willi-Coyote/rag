import os

from dotenv import load_dotenv

from rag.config.configuration import Configuration, MissingConfigurationException, Environment


class EnvConfiguration(Configuration):
    def __init__(self):
        load_dotenv()
        self.azure_app_insights_connection_string = self._get_value(
            "APPLICATIONINSIGHTS_CONNECTION_STRING")
        self.token_validation = self._get_value("TOKEN_VALIDATION").lower() == "true"
        self.environment = Environment(self._get_value("ENVIRONMENT").lower())

    def _get_value(self, key: str) -> str:
        try:
            return os.environ[key]
        except KeyError:
            additional_message = "Please check your .env file and ensure that the key is set"
            raise MissingConfigurationException(key, additional_message)


configuration = EnvConfiguration()
