import json
from pathlib import Path

from app.models import Dealer, Listing


def load_dealers(path: Path) -> list[Dealer]:
    testo = path.read_text(encoding="utf-8")
    dati = json.loads(testo)
    dealers: list[Dealer] = []

    for elemento in dati:
        dealer = Dealer.model_validate(elemento)
        dealers.append(dealer)

    return dealers


def load_listings(path: Path) -> list[Listing]:
    testo = path.read_text(encoding="utf-8")
    dati = json.loads(testo)
    listings: list[Listing] = []

    for elemento in dati:
        listing = Listing.model_validate(elemento)
        listings.append(listing)

    return listings
