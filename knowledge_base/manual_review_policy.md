# Manual Review Policy

Document ID: KB-REVIEW-001
Version: 1.0

## Purpose

This policy defines when a manual review can be requested, how it is handled,
and the expected resolution time. A manual review is a human re-evaluation of
a listing or a dealer account.

## When a manual review applies

A manual review can be requested in these cases:

- a listing is in `rejected` status and the dealer believes the rejection was
  incorrect;
- a listing has been in `pending_review` for more than 48 hours;
- a `suspended` dealer wants to be reactivated after resolving the cause of
  suspension.

A manual review cannot be used to skip required documents. If a listing was
rejected because of a missing VIN photo, the dealer must first upload the
photo, then request the review.

## How a manual review is requested

The support operator submits the manual review request on behalf of the
dealer. The request is recorded as a pending action and is not executed
automatically.

Each manual review request must include:

- the listing or dealer identifier;
- the reason for the review;
- confirmation that the original blocking issue has been resolved.

## Approval

A manual review that changes the status of a listing or a dealer is a
write action with a side effect. It stays pending until a human operator
approves it. Duplicate requests for the same listing are ignored using an
idempotency key, so approving twice does not trigger two reviews.

## Resolution time

A manual review is normally completed within 48 hours. During the review the
listing keeps its current status and is not published until the review ends
with an approval.

## Outcome

A manual review can end with one of these outcomes:

- approved: the listing is moved back to `pending_review` or `published`, or
  the dealer is reactivated to `active`;
- rejected: the original status is kept and the reason is recorded.

Every outcome, including who approved it and when, is logged for audit.
