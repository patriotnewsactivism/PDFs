# VERIFIED — Court-signed and file-stamped documents

Official copies that bear a court file stamp and/or a judge or clerk signature, collected from:

- `patriotnewsactivism/PDFs`
- `patriotnewsactivism/American-Injustice` (`source-docs/reardon-v-osteen`)
- `patriotnewsactivism/americaninjustice` (same underlying court PDFs as `PDFs`)

## What counted as verified

A document was placed here only if it is an official court record, typically showing one or more of:

- Lafayette County Chancery/Circuit clerk file stamp (`FILED`, date/time, clerk initials or seal)
- Mississippi Supreme Court / Court of Appeals electronic filing header and digital judicial signature
- Federal CM/ECF “Filed … in TXSD” / “ENTERED” stamp (Southern District of Texas)
- A signed order, judgment, summons, or denial issued by the court

Drafts, news clippings, Facebook exports, police reports, tax/business filings (for example the Utah LLC certificate named “Stamped File Copy”), call transcripts, and unstamped compilations were **not** copied.

## Method

Filenames were screened for court-issued document types (orders, judgments, summonses, writs, denials, filed cover sheets). First pages of representative documents were visually inspected for clerk file stamps and judicial signatures. OCR was used as a secondary check on scanned Mississippi filings, which often have faint date/time stamps in the caption.

Party briefs whose filenames state they are the filed court copy (`Filed COA Brief`, `Appellant Brief Filed`, `Reardon V Osteen Filed Complaint`) are included as official filed records.

Most files already in this repository are linked from `VERIFIED/` to the same blob at the repo root (same official copy, no duplicate binary). Three federal orders that lived only in `American-Injustice` are listed below; download them from that repo until they can be added as binaries:

- `source-docs/reardon-v-osteen/90-Edison-RandR.pdf` — Memorandum Opinion, Order, and Recommendation (S.D. Tex., ENTERED July 14, 2026)
- `source-docs/reardon-v-osteen/93-Order-Adopting-MR.pdf` — Order Adopting Magistrate Judge’s M&R (ENTERED August 10, 2026)
- `source-docs/reardon-v-osteen/94-Final-Judgment.pdf` — Final Judgment signed August 10, 2026

`americaninjustice` stores the same court PDFs under `00_source_materials/legal_documents/by_date/` (matching blob SHAs). No additional unique court-stamped PDFs from that tree were needed beyond what is already in `PDFs`.
