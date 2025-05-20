from pydantic import BaseModel
from typing import Optional

class Latest(BaseModel):
    """
    Model for a latest response. Latest consists of an array of dictionaries, each representing the most recent setlist entry.
    """
    uniqueid: str
    show_id: int
    showdate: str
    showtitle: str
    artist: str
    song_id: int
    songname: str
    artist_id: int
    permalink: str
    settype: str
    setnumber: str
    position: int
    transition_id: int
    transition: str
    footnote: str
    isjamchart: int
    jamchart_notes: Optional[str]
    venue_id: int
    shownotes: str
    showyear: int
    showorder: int
    opener: str
    tour_id: int
    tourname: str
    soundcheck: str
    isverified: int
    slug: str
    isoriginal: int
    original_artist: str
    venuename: str
    city: str
    state: str
    country: str
    isreprise: int
    isjam: int
