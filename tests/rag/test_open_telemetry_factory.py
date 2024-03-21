import os

from metrics.azure.azure_open_telemetry import AzureOpenTelemetry
from rag.metrics.open_telemetry_factory import get_open_telemetry


def test_get_open_telemetry_azure():
    os.environ["ENVIRONMENT"] = "AZURE"
    result = get_open_telemetry()
    assert isinstance(result, AzureOpenTelemetry)


def test_get_open_telemetry_aws():
    os.environ["ENVIRONMENT"] = "AWS"
    result = get_open_telemetry()
    assert result is None


def test_get_open_telemetry_unknown():
    os.environ["ENVIRONMENT"] = "UNKNOWN"
    result = get_open_telemetry()
    assert result is None
