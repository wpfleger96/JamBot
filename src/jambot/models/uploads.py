from pydantic import BaseModel
from typing import Optional

class Upload(BaseModel):
    """
    Model for an upload response. Uploads are an array of dictionaries, where each dictionary represents an external upload.

    Example response:
    [
        {
            "id": 236,
            "show_id": "1746724630",
            "showdate": "2025-05-17",
            "URL": "https://elgoose.net/i/featured-image-1746724630.jpg",
            "img_name": "Featured Image, 2025-05-17 - Burlington, VT",
            "upload_type": "featured-image",
            "attribution": None,
            "created_at": "2025-05-15 11:05:57"
        },
        ...
    ]
    """
    id: int
    show_id: str
    showdate: str
    URL: str
    img_name: str
    upload_type: str
    attribution: Optional[str]
    created_at: str
