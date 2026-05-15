"""Unit tests for the validation helpers."""

import pytest

from jambot import validation
from jambot.errors import JambotValidationError


@pytest.mark.unit
@pytest.mark.validation
def test_validate_band_accepts_supported():
    validation.validate_band("goose")
    validation.validate_band("um")


@pytest.mark.unit
@pytest.mark.validation
def test_validate_band_rejects_unknown():
    with pytest.raises(JambotValidationError):
        validation.validate_band("phish")


@pytest.mark.unit
@pytest.mark.validation
def test_validate_resource_type_rejects_unknown():
    with pytest.raises(JambotValidationError):
        validation.validate_resource_type("not-a-resource")


@pytest.mark.unit
@pytest.mark.validation
def test_validate_format_rejects_unknown():
    with pytest.raises(JambotValidationError):
        validation.validate_format("xml")


@pytest.mark.unit
@pytest.mark.validation
def test_validate_order_by_rejects_unknown_field():
    with pytest.raises(JambotValidationError):
        validation.validate_order_by("not-a-field", "setlists")


@pytest.mark.unit
@pytest.mark.validation
def test_validate_order_by_accepts_known_field():
    validation.validate_order_by("showdate", "setlists")


@pytest.mark.unit
@pytest.mark.validation
def test_validate_direction_rejects_unknown():
    with pytest.raises(JambotValidationError):
        validation.validate_direction("sideways")


@pytest.mark.unit
@pytest.mark.validation
def test_validate_direction_accepts_known():
    validation.validate_direction("asc")
    validation.validate_direction("desc")
