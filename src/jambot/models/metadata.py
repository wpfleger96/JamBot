from pydantic import BaseModel

class Metadata(BaseModel):
    """
    Model for a metadata response. Metadata is a an array of dictionaries, where each dictionary represents a metadata entry.
    
    Example response:
    [
        {
            "show_id": 1613103303,
            "showdate": "2020-02-07",
            "artist": "Goose",
            "artist_id": 1,
            "song_id": 404,
            "song_slug": "time-to-flee",
            "meta_name": "Peter Yeah",
            "songname": "Time to Flee",
            "metadata_slug": "peter-yeah",
            "value": "1",
            "permalink": "/setlists/goose-february-7-2020-the-troubadour-west-hollywood-ca-usa.html",
            "venuename": "The Troubadour",
            "city": "West Hollywood",
            "state": "CA",
            "country": "USA"
        },
        ...
    ]
    """
    show_id: int
    showdate: str
    artist: str
    artist_id: int
    song_id: int
    song_slug: str
    meta_name: str
    songname: str
    metadata_slug: str
    value: str
    permalink: str
    venuename: str
    city: str
    state: str
    country: str
