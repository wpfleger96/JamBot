from pydantic import BaseModel
from typing import Optional

class Album(BaseModel):
    """
    Model for an album response. Albums are an array of dictionaries, where each dictionary represents a song in the album.

    Example response:
    [
        {
            "album_title": "Moon Cabin",
            "album_displayname": "",
            "artist": "Goose",
            "artist_id": 1,
            "album_url": "/albums/moon-cabin",
            "releasedate": "2016-02-17",
            "album_notes": None,
            "song_name": "Turned Clouds",
            "song_url": "/song/turned-clouds",
            "original_artist": "",
            "position": 1,
            "islive": 0,
            "tracktime": "06:31",
            "disc_number": 1,
            "track_updated_at": "2021-03-15 22:03:46",
            "album_updated_at": "2021-09-06 01:39:47"
        },
        ...
    ]
    """
    album_title: str
    album_displayname: str
    artist: str
    artist_id: int
    album_url: str
    releasedate: str
    album_notes: Optional[str]
    song_name: Optional[str]
    song_url: Optional[str]
    original_artist: Optional[str]
    position: int
    islive: int
    tracktime: str
    disc_number: int
    track_updated_at: str
    album_updated_at: str