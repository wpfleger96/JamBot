from pydantic import BaseModel


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

    artist: str | None
    artist_id: int | None
    city: str | None
    country: str | None
    css_class: str | None
    footnote: str
    isjam: int
    isjamchart: int
    isoriginal: int
    isrecommended: int | None
    isreprise: int
    isverified: int | None
    jamchart_notes: str | None
    opener: str | None
    original_artist: str
    permalink: str | None
    position: int
    setnumber: str
    settype: str | None
    show_id: int
    showdate: str | None
    shownotes: str | None
    showorder: int | None
    showtitle: str | None
    showyear: int | None
    slug: str
    song_id: int
    songname: str
    soundcheck: str | None
    state: str | None
    tour_id: int | None
    tourname: str | None
    tracktime: str | None
    transition: str
    transition_id: int
    uniqueid: str
    venue_id: int | None
    venuename: str | None
