from pydantic import BaseModel
from typing import Optional

class Jamchart(BaseModel):
    """
    Model for a jamchart response. Jamcharts are an array of dictionaries, where each dictionary represents a jam in a song.

    Example response:
    [
        {
            "uniqueid": "5934",
            "setnumber": "2",
            "position": 14,
            "footnote": "With Magic School Bus Theme teases.",
            "tracktime": "14:40",
            "jamchartnote": "Breaks into an awesome funk jam that leads into "Magic School Bus" teasing. Eventually makes a major...",
            "song_id": 414,
            "isrecommended": 0,
            "showid": 1614319723,
            "songname": "All I Need",
            "song_slug": "all-i-need",
            "showdate": "2019-02-15",
            "artist_id": 1,
            "artist": "Goose",
            "artist_slug": "goose",
            "venuename": "Octave",
            "venue_slug": "octave-covington-ky-usa",
            "city": "Covington",
            "state": "KY"
        },
        ...
    ]
    """
    uniqueid: str
    setnumber: str
    position: int
    footnote: Optional[str]
    tracktime: str
    jamchartnote: str
    song_id: int
    isrecommended: Optional[int]
    showid: int
    songname: str
    song_slug: str
    showdate: str
    artist_id: int
    artist: str
    artist_slug: str
    venuename: str
    venue_slug: str
    city: str
    state: str
    country: str
    permalink: str