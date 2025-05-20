from pydantic import BaseModel
from typing import Optional

class Song(BaseModel):
    """
    Model for a song response. Songs are an array of dictionaries, where each dictionary represents a song.

    Example response:
    [
        {
            "id": 400,
            "name": "Turned Clouds",
            "slug": "turned-clouds",
            "isoriginal": 1,
            "original_artist": "Goose",
            "created_at": "1000-01-01 00:00:00",
            "updated_at": "2024-03-11 16:20:28"
        },
        ...
    ]
    """
    id: int
    name: str
    slug: str
    isoriginal: int
    original_artist: str
    created_at: str
    updated_at: str