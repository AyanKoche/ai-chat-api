class OllamaConnectionError(Exception):
    """Raised when there is a connection error with the Ollama API."""
    pass


class OllamaResponseError(Exception):
    """Raised when the Ollama API returns an error response."""
    pass