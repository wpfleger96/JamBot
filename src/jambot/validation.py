"""Validation helpers for Jambot tool inputs."""

from jambot.constants import FORMATS, RESOURCE_MODEL_MAP, RESOURCE_TYPES, SUPPORTED_BANDS_MAP
from jambot.errors import JambotValidationError


def validate_format(format: str) -> None:
    if format not in FORMATS:
        raise JambotValidationError(
            f"Invalid format: {format}. Supported formats are: {','.join(FORMATS)}."
        )


def validate_band(band: str) -> None:
    if band not in SUPPORTED_BANDS_MAP:
        raise JambotValidationError(
            f"Invalid band: {band}. Supported bands are: {', '.join(SUPPORTED_BANDS_MAP.keys())}."
        )


def validate_resource_type(resource_type: str) -> None:
    if resource_type not in RESOURCE_TYPES:
        raise JambotValidationError(
            f"Invalid resource type: {resource_type}. Supported resource types are: {', '.join(RESOURCE_TYPES.keys())}."
        )


def validate_order_by(order_by: str, resource_type: str) -> None:
    model_class = RESOURCE_MODEL_MAP[resource_type]
    valid_fields = set(model_class.model_fields.keys())
    if order_by not in valid_fields:
        raise JambotValidationError(
            f"Invalid order_by parameter: {order_by}. Supported order_by parameters for {resource_type} are: {', '.join(valid_fields)}."
        )


def validate_direction(direction: str) -> None:
    if direction is not None and direction not in ["asc", "desc"]:
        raise JambotValidationError(
            "Invalid direction parameter. Supported directions are: asc, desc."
        )
