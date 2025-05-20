from pydantic import BaseModel
from typing import Optional

class Appearance(BaseModel):
    """
    Model for an appearance response. Appearances are an array of dictionaries, where each dictionary represents an appearance in a show.

    Example response:
    [
        {
            "show_id": 1621475790,
            "showdate": "2012-01-12",
            "artist_id": 2,
            "artist_name": "Vasudo",
            "person_id": 31,
            "personname": "Matt Campbell",
            "slug": "matt-campbell",
            "appearance_type": "musician",
            "notes": ""
        },
        ...
    ]
    """
    show_id: int
    showdate: str
    artist_id: int
    artist_name: str
    person_id: int
    personname: str
    slug: str
    appearance_type: str
    notes: str
