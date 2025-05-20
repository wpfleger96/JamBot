from pydantic import BaseModel
from typing import Optional

class Venue(BaseModel):
    """
    Model for a venue response. Venues are an array of dictionaries, where each dictionary represents a venue.
    
    Example response:
    [
        {
            "venue_id": 1,
            "venuename": "Madison Theater",
            "city": "Covington",
            "state": "KY",
            "country": "USA",
            "zip": "41011",
            "capacity": 1200,
            "slug": "madison-theater-covington-ky-usa"
        },
        ...
    ]
    """
    venue_id: int
    venuename: str
    city: str
    state: str
    country: str
    zip: str
    capacity: int
    slug: str
