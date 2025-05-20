from pydantic import BaseModel
from typing import Optional

class Show(BaseModel):
    """
    Model for a show response. Shows are an array of dictionaries, where each dictionary represents a show.
    
    Example response:
    [
        {
            "show_id": 1743796338,
            "showdate": "2012-01-14",
            "permalink": "vasudo-january-14-2012-viva-zapata-westport-ct-usa.html",
            "artist_id": 2,
            "artist": "Vasudo",
            "showtitle": "",
            "venue_id": 9,
            "venuename": "Viva Zapata",
            "location": "Westport, CT, USA",
            "city": "Westport",
            "state": "CT",
            "country": "USA",
            "tour_id": 1,
            "tourname": "Not Part of a Tour",
            "showorder": 1,
            "show_year": 2012,
            "show_day": 14,
            "show_dayname": "Saturday",
            "show_month": 1,
            "show_monthname": "January",
            "updated_at": "2025-04-04 19:52:18"
        },
        ...
    ]
    
    """
    show_id: int
    showdate: str
    permalink: str
    artist_id: int
    artist: str
    showtitle: Optional[str]
    venue_id: int
    venuename: str
    location: str
    city: str
    state: str
    country: str
    tour_id: int
    tourname: str
    showorder: int
    show_year: int
    show_day: int
    show_dayname: str
    show_month: int
    show_monthname: str
    updated_at: str
    created_at: Optional[str]
