from jambot.constants import FORMATS, SUPPORTED_BANDS_MAP, RESOURCE_TYPES, RESOURCE_MODEL_MAP
from pydantic import BaseModel
from typing import Dict, Any, Type

def model_to_schema(model_class: Type[BaseModel]) -> Dict[str, Any]:
    """Convert a Pydantic model class to a schema dictionary.
    
    Args:
        model_class: The Pydantic model class to convert
        
    Returns:
        A dictionary containing the model's fields and their types
    """
    schema = model_class.model_json_schema()
    
    result = {}
    for field, info in schema.get("properties", {}).items():
        field_type = info.get("type", "any")
        if field_type == "array":
            items_type = info.get("items", {}).get("type", "any")
            field_type = f"array[{items_type}]"
        result[field] = field_type
        
    return result

def validate_format(format: str) -> bool:
    """Validate that the format is supported.
    """
    if format not in FORMATS:
        raise ValueError(f"Invalid format: {format}. Supported formats are: {','.join(FORMATS)}.")

def validate_band(band: str) -> bool:
    """Validate that the band is supported.
    """
    if band not in SUPPORTED_BANDS_MAP:
        raise ValueError(f"Invalid band: {band}. Supported bands are: {', '.join(SUPPORTED_BANDS_MAP.keys())}.")

def validate_resource_type(resource_type: str) -> bool:
    """Validate that the resource type is supported.
    """
    if resource_type not in RESOURCE_TYPES:
        raise ValueError(f"Invalid resource type: {resource_type}. Supported resource types are: {', '.join(RESOURCE_TYPES.keys())}.")

def validate_order_by(order_by: str, resource_type: str) -> bool:
    """Validate that the order_by parameter is valid.
    """        
    model_class = RESOURCE_MODEL_MAP[resource_type]
    valid_fields = set(model_class.model_fields.keys())
    if order_by not in valid_fields:
        raise ValueError(f"Invalid order_by parameter: {order_by}. Supported order_by parameters for {resource_type} are: {', '.join(valid_fields)}.")
    return True

def validate_direction(direction: str) -> bool:
    """Validate that the direction parameter is valid.
    """
    if direction is not None and direction not in ["asc", "desc"]:
        raise ValueError("Invalid direction parameter. Supported directions are: asc, desc.")
    return True
