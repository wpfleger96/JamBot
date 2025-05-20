from jambot.models.setlists import Setlist
from jambot.models.latest import Latest
from jambot.models.shows import Show
from jambot.models.songs import Song
from jambot.models.venues import Venue
from jambot.models.jamcharts import Jamchart
from jambot.models.albums import Album
from jambot.models.metadata import Metadata
from jambot.models.links import Links
from jambot.models.uploads import Upload
from jambot.models.appearances import Appearance

UM_BASE_URL = "https://allthings.umphreys.com/api/v2"
GOOSE_BASE_URL = "https://elgoose.net/api/v2"

SUPPORTED_BANDS_MAP = {
    "um": {
        "name": "Umphrey's McGee",
        "url": UM_BASE_URL
    },
    "goose": {
        "name": "Goose",
        "url": GOOSE_BASE_URL
    }
}

RESOURCE_TYPES = {
    "setlists": "Setlist data for a given band",
    "latest": "Most recent show setlist for a given band",
    "shows": "Show data for a given band",
    "songs": "Song data for a given band",
    "venues": "Venue data for a given band",
    "jamcharts": "Jamchart data for a given band",
    "albums": "Album data for a given band",
    "metadata": "Setlist metadata for a given band",
    "links": "Links attached to shows for a given band",
    "uploads": "Show metadata including poster art and featured images",
    "appearances": "Musician appearances",
}

RESOURCE_MODEL_MAP = {
    "setlists": Setlist,
    "latest": Latest,
    "shows": Show,
    "songs": Song,
    "venues": Venue,
    "jamcharts": Jamchart,
    "albums": Album,
    "metadata": Metadata,
    "links": Links,
    "uploads": Upload,
    "appearances": Appearance
}

FORMATS = ["json", "html"]
