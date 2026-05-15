from typing import Any, Dict, Type

from pydantic import BaseModel


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
