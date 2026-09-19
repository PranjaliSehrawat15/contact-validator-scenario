import pytest
from src.contact_validator import is_valid_email, is_valid_phone, mask_email, normalize_phone

def test_is_valid_email_true():
    assert is_valid_email("student@lpu.in") is True

def test_is_valid_email_type_error():
    """Test that a non-string input raises TypeError."""
    with pytest.raises(TypeError):
        is_valid_email(12345)

def test_is_valid_phone_true():
    assert is_valid_phone("555-123-4567") is True

def test_normalize_phone():
    assert normalize_phone("555-123-4567") == "5551234567"

def test_normalize_phone_invalid():
    with pytest.raises(ValueError):
        normalize_phone("123")

def test_mask_email_basic():
    assert mask_email("priya@example.com") == "pr***@example.com"