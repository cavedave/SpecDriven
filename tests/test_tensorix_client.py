from unittest.mock import MagicMock, patch

import pytest
from openai import AuthenticationError

import tensorix_client
from tensorix_client import TensorixError, ask, get_api_key


def test_get_base_url_default(monkeypatch):
    monkeypatch.delenv("TENSORIX_BASE_URL", raising=False)
    with patch.object(tensorix_client, "load_dotenv"):
        assert tensorix_client.get_base_url() == "https://api.tensorx.ai/v1"


def test_get_base_url_from_env(monkeypatch):
    monkeypatch.setenv("TENSORIX_BASE_URL", "https://custom.example/v1")
    with patch.object(tensorix_client, "load_dotenv"):
        assert tensorix_client.get_base_url() == "https://custom.example/v1"


def test_get_api_key_missing(monkeypatch):
    monkeypatch.delenv("TENSORIX_API_KEY", raising=False)
    with patch.object(tensorix_client, "load_dotenv"):
        with pytest.raises(TensorixError, match="TENSORIX_API_KEY"):
            get_api_key()


def test_get_api_key_present(monkeypatch):
    monkeypatch.setenv("TENSORIX_API_KEY", "sk-test")
    with patch.object(tensorix_client, "load_dotenv"):
        assert get_api_key() == "sk-test"


def test_ask_returns_paris_from_mock():
    mock_client = MagicMock()
    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content="The capital of France is Paris."))]
    )

    with patch.object(tensorix_client, "get_model", return_value="test-model"):
        result = ask("What is the capital of France?", client=mock_client)

    assert "Paris" in result
    mock_client.chat.completions.create.assert_called_once()


def test_ask_authentication_error():
    mock_client = MagicMock()
    mock_client.chat.completions.create.side_effect = AuthenticationError(
        "Invalid API key", response=MagicMock(), body=None
    )

    with patch.object(tensorix_client, "get_model", return_value="test-model"):
        with pytest.raises(TensorixError, match="authentication failed"):
            ask("Hello?", client=mock_client)


def test_ask_empty_response():
    mock_client = MagicMock()
    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content=""))]
    )

    with patch.object(tensorix_client, "get_model", return_value="test-model"):
        with pytest.raises(TensorixError, match="empty response"):
            ask("Hello?", client=mock_client)


def test_ask_no_choices():
    mock_client = MagicMock()
    mock_client.chat.completions.create.return_value = MagicMock(choices=[])

    with patch.object(tensorix_client, "get_model", return_value="test-model"):
        with pytest.raises(TensorixError, match="no choices"):
            ask("Hello?", client=mock_client)
