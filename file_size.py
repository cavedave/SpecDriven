"""Helpers for displaying uploaded file sizes."""


def format_file_size(size_bytes: int) -> str:
    """Format byte count as human-readable B, KB, or MB (1024-based)."""
    if size_bytes < 0:
        raise ValueError("size_bytes must be non-negative")
    if size_bytes == 0:
        return "0 B"
    if size_bytes < 1024:
        return f"{size_bytes} B"
    if size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    return f"{size_bytes / (1024 * 1024):.1f} MB"
