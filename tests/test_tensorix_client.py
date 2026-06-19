import base64
from unittest.mock import MagicMock, patch

import pytest
from openai import AuthenticationError

import tensorix_client
from tensorix_client import TensorixError, ask, extract_text_from_image, get_api_key


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


def test_extract_text_returns_tokyo_from_mock():
    mock_client = MagicMock()
    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[
            MagicMock(
                message=MagicMock(content="TOKYO HIROSHIMA OSAKA — B-29 incendiary attacks")
            )
        ]
    )

    with patch.object(tensorix_client, "get_model", return_value="test-model"):
        result = extract_text_from_image(b"fake", "image/jpeg", client=mock_client)

    assert "TOKYO" in result
    mock_client.chat.completions.create.assert_called_once()


def test_extract_text_sends_multimodal_message():
    mock_client = MagicMock()
    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content="some text"))]
    )
    image_bytes = b"fake-image-data"

    with patch.object(tensorix_client, "get_model", return_value="test-model"):
        extract_text_from_image(image_bytes, "image/jpeg", client=mock_client)

    content = mock_client.chat.completions.create.call_args.kwargs["messages"][0][
        "content"
    ]
    assert content[0]["type"] == "text"
    assert content[1]["type"] == "image_url"
    expected_b64 = base64.b64encode(image_bytes).decode("ascii")
    assert content[1]["image_url"]["url"] == f"data:image/jpeg;base64,{expected_b64}"


def test_extract_text_empty_bytes():
    with pytest.raises(TensorixError, match="must not be empty"):
        extract_text_from_image(b"", "image/jpeg", client=MagicMock())


def test_extract_text_empty_response():
    mock_client = MagicMock()
    mock_client.chat.completions.create.return_value = MagicMock(
        choices=[MagicMock(message=MagicMock(content=""))]
    )

    with patch.object(tensorix_client, "get_model", return_value="test-model"):
        with pytest.raises(TensorixError, match="empty response"):
            extract_text_from_image(b"fake", "image/jpeg", client=mock_client)


def test_extract_text_authentication_error():
    mock_client = MagicMock()
    mock_client.chat.completions.create.side_effect = AuthenticationError(
        "Invalid API key", response=MagicMock(), body=None
    )

    with patch.object(tensorix_client, "get_model", return_value="test-model"):
        with pytest.raises(TensorixError, match="authentication failed"):
            extract_text_from_image(b"fake", "image/jpeg", client=mock_client)
