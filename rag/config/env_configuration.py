import os

from dotenv import load_dotenv

from config.configuration import Configuration


class EnvConfiguration(Configuration):
    def __init__(self):
        load_dotenv()
        try:
            self.azure_app_insights_connection_string = os.environ[
                'APPLICATIONINSIGHTS_CONNECTION_STRING']
            self.token_validation = os.environ['TOKEN_VALIDATION'] == 'True'
        except KeyError as e:
            raise Exception(f'Missing environment variable: {str(e)}')
