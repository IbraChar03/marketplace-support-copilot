# Dealer Onboarding Policy

Document ID: KB-DEALER-001
Version: 1.0

## Purpose

This policy defines the requirements a dealer must satisfy to publish
listings on the marketplace and the meaning of each onboarding status.

## Required onboarding documents

Before a dealer can be activated, the following documents must be uploaded
and verified:

- business registration certificate (`visura_camerale`);
- legal representative identity document (`documento_identita`);
- VAT registration number;
- signed marketplace terms of service.

A dealer cannot publish any listing until all required documents are
verified.

## Onboarding status

A dealer can have one of these statuses:

- `pending`: onboarding is not complete; one or more required documents are
  missing or waiting for verification. The dealer cannot publish listings;
- `active`: all documents are verified and the dealer can create and publish
  listings;
- `suspended`: the dealer was active but has been blocked due to a policy
  violation or an expired document. Listings remain visible only if already
  published, but no new listing can be submitted.

## Missing business registration

If the `visura_camerale` is missing, the dealer stays in `pending` and cannot
be activated. The dealer must upload a valid, non-expired business
registration certificate.

## Missing identity document

If the legal representative `documento_identita` is missing or unreadable,
onboarding cannot be completed and the dealer remains in `pending`.

## Suspension

A dealer is moved to `suspended` when:

- a required document expires and is not renewed within 30 days;
- repeated listing rejections indicate fraudulent or misleading content.

To return to `active`, the dealer must resolve the cause of suspension and
request a manual review.

## Onboarding time

A complete document set is normally verified within 48 hours. Verification of
a renewed or corrected document can require up to 72 hours.
