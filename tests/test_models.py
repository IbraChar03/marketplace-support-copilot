from app.models import Listing
import pytest
from pydantic import ValidationError


def test_listing_valido():
    listing = Listing(
        id="CAR-1", dealer_id="D1", status="draft", missing_fields=["vin_photo"]
    )
    assert listing.status == "draft"
    assert listing.missing_fields == ["vin_photo"]


def test_listing_invalido():
    with pytest.raises(ValidationError):
        Listing(id="CAR-1", dealer_id="D1", status="BOH", missing_fields=["vin_photo"])


def test_missing_fields_default_vuoto():
    listing = Listing(
        id="CAR-1",
        dealer_id="D1",
        status="draft",
    )

    assert listing.missing_fields == []
