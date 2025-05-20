from pydantic import BaseModel
from typing import Optional

class Links(BaseModel):
    """
    Model for a links response. Links are an array of dictionaries, where each dictionary represents an external link.

    Example response:
    [
        {
            "link_id": 647,
            "show_id": 1594067578,
            "description": "Bandcamp",
            "url": "https://goosetheband.bandcamp.com/album/2020-03-11-madison-theater-covington-ky",
            "updated_at": "2023-10-25 04:14:31"
        },
        ...
    ]
    """
    link_id: int
    show_id: int
    description: str
    url: str
    updated_at: str
