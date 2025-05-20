from pydantic import BaseModel
from typing import Optional

class Setlist(BaseModel):
    """
    Model for a setlist response. Setslists are an array of dictionaries, each representing a song in the setlist.

    Example response:
    [
        {
            'artist': 'Goose',
            'artist_id': 1,
            'city': 'Pelham',
            'country': 'USA',
            'css_class': None,
            'footnote': 'The Wood Brothers.',
            'isjam': 0,
            'isjamchart': 0,
            'isoriginal': 0,
            'isrecommended': None,
            'isreprise': 0,
            'isverified': 1,
            'jamchart_notes': None,
            'opener': '',
            'original_artist': 'The Wood Brothers',
            'permalink': 'goose-may-9-2021-the-caverns-above-ground-amphitheater-pelham-tn-usa.html',
            'position': 1,
            'setnumber': '1',
            'settype': 'Set',
            'show_id': 1621488243,
            'showdate': '2021-05-09',
            'shownotes': '',
            'showorder': 1,
            'showtitle': '',
            'showyear': 2021,
            'slug': 'atlas',
            'song_id': 439,
            'songname': 'Atlas',
            'soundcheck': '',
            'state': 'TN',
            'tour_id': 1,
            'tourname': 'Not Part of a Tour',
            'tracktime': '14:32',
            'transition': ', ',
            'transition_id': 1,
            'uniqueid': '8427',
            'venue_id': 238,
            'venuename': 'The Caverns Above Ground Amphitheater'
        },
        ...
    ]
    """
    artist: Optional[str]
    artist_id: Optional[int]
    city: Optional[str]
    country: Optional[str]
    css_class: Optional[str]
    footnote: str
    isjam: int
    isjamchart: int
    isoriginal: int
    isrecommended: Optional[int]
    isreprise: int
    isverified: Optional[int]
    jamchart_notes: Optional[str]
    opener: Optional[str]
    original_artist: str
    permalink: Optional[str]
    position: int
    setnumber: str
    settype: Optional[str]
    show_id: int
    showdate: Optional[str]
    shownotes: Optional[str]
    showorder: Optional[int]
    showtitle: Optional[str]
    showyear: Optional[int]
    slug: str
    song_id: int
    songname: str
    soundcheck: Optional[str]
    state: Optional[str]
    tour_id: Optional[int]
    tourname: Optional[str]
    tracktime: Optional[str]
    transition: str
    transition_id: int
    uniqueid: str
    venue_id: Optional[int]
    venuename: Optional[str]