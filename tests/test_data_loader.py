from pathlib import Path

from app.data_loader import load_dealers, load_listings
from app.models import Dealer, Listing

DATA_DIR = Path(__file__).resolve().parents[1] / "data"


def test_load_dealers():
    dealers = load_dealers(DATA_DIR / "dealers.json")

    assert len(dealers) == 3
    assert isinstance(dealers[0], Dealer)
    assert dealers[1].id == "D2"
    assert dealers[1].missing_documents == ["visura_camerale"]


def test_load_listings():
    listings = load_listings(DATA_DIR / "listings.json")

    assert len(listings) == 3
    assert isinstance(listings[0], Listing)
    assert listings[1].id == "CAR-2"
    assert listings[1].status == "rejected"
    assert "vin_photo" in listings[1].missing_fields
