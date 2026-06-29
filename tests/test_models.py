from app.models import Listing, Dealer
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


def test_listing_missing_fields_default_vuoto():
    listing = Listing(
        id="CAR-1",
        dealer_id="D1",
        status="draft",
    )

    assert listing.missing_fields == []


def test_dealer_valido():
    dealer = Dealer(
        id="DEALER-1",
        name="autocar",
        onboarding_status="pending",
        missing_documents=["pdf"],
    )
    assert dealer.onboarding_status == "pending"
    assert dealer.missing_documents == ["pdf"]


def test_dealer_invalido():
    with pytest.raises(ValidationError):
        Dealer(
            id="DEALER-1",
            name="autocar",
            onboarding_status="bho",
            missing_documents=["pdf"],
        )


def test_dealer_missing_documents_default_vuoto():
    dealer = Dealer(
        id="DEALER-1",
        name="autocar",
        onboarding_status="pending",
    )

    assert dealer.missing_documents == []
