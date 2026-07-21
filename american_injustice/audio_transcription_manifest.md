# Audio Transcription Manifest — American Injustice
Last updated: 2026-07-21. Purpose: track exactly what's been transcribed across every audio source so we never re-download or re-transcribe the same files. Sandbox /tmp/ can be wiped on reset — this file is the durable source of truth (also push to GitHub PDFs repo).

## Source 1: Galveston PD Dispatch Zip — ✅ FULLY COMPLETE (46/46 files)
File: `/app/incoming_files/6a559ae34e50db4741d9e242/f4347fa4f_Audiofilesfrominvestigation.zip`
All 46 WAV files (08-11-2023, timestamps 1:47 AM–4:55 AM) transcribed. Do not reprocess. Full reconstructed timeline saved in memory.md entry on this topic + GitHub `american_injustice/cross_document_synthesis.md`. Key verdict: "final DUI conviction, no pending appeal" language never found verbatim — Galveston constructed that conclusion from an ambiguous MS record, not something MS affirmatively transmitted.

## Source 2: Google Drive "Recordings and Calls" root — trial testimony files (root-level, ~15 files)
Folder ID: `1HjfI5ie9srF9noPbYOMLUgvKgiJxlm1w`
**Transcribed (5):** joey_east_takes_stand.mp3 ✅ (sallyport video admission), candice_beavers_pt2.mp3 ✅ (citation drafting error), courtney_dixon_pt2.mp3 ✅ (parking-dispute arrest account — CONFLICTS with "rehearsed ambush" framing elsewhere, needs reconciliation), Liz Crowder confession.mp3 ✅ (NOT a real confession — religious/emotional, blames "Dustin"), LC_4th_20190713.mp3 ✅ (Dustin conflict).
**Downloaded, not yet transcribed:** ethan_tidwell_takes_stand.mp3, jacob_wiliford_takes_stand.mp3 (in /app/incoming_files/drive_testimony/), LC_1st/2nd/3rd_20190713.mp3, LC_20190720_incoming.mp3, Oxford Eagle Publisher.mp3, Officer Herrod recording, 2021 Wells Fargo fraud dispute (already transcribed actually — confirm).
**Too big, need ffmpeg chunking (untranscribed):** trial_mixdown.mp3 (79MB), Candice Beavers pt1.mp3 (47MB), Courtney Dixon pt1.mp3 (54MB), Hard Talk.mp3, 21-02-21 DUI Stop.mp3 (81MB).
**Untranscribed, ~1000 other root files:** timestamped filenames (YYYYMMDD HHMMSS.m4a) — recordings_root_batch sub-agent task prioritized 2021-2022/2019-2020/Aug 2023 dates, partial progress only, catalog at /tmp/recordings_root_batch/all_root_files.json if it survives.

## Source 3: Google Drive "Voice Memos" folder (588 files total)
Folder ID: `1M0fptu-SL2i1goMIsz29j2HnAG7dxHWY`
**Batch 1 (first chronological/alpha half, ~294 files):** 30 downloaded to /tmp/voice_memos_batch1/, 17 transcribed (Judge Whitwell clerk "corruption ring" calls, Cindy Meek Brown/Ed Meek threats, pauper's oath, 2017 false-report inquiry, Manic Mobile pitch, domestic dispute). 13 remain untranscribed in that batch of 30; ~264 more never downloaded.
**Batch 2 (second half, indices 294-587, ~46 priority files identified):** 2 test files transcribed. 44 remain, including high-value unprocessed leads: "Mickey Mallette Voicemail.m4a", "Senator McDaniels Office.m4a", "Oxford Eagle Publisher.m4a" (political/media contacts — HIGH PRIORITY, not yet done).

## Source 4: Google Drive "callrecorder" folder (255 files, subfolders 11-2021/12-2021/01-2022)
All 255 downloaded to /tmp/callrecorder_batch/. Partial transcription: several 11-2021 calls done (Crowder false-report complaint, counsel withdrawal). 12-2021 (180 files) and 01-2022 (64 files) mostly untranscribed — last continuation task was still running as of 2026-07-21 evening, status unconfirmed.

## Source 5: Google Drive "cubecallrecorder" folder — ✅ FULLY COMPLETE (287/287 unique files)
All 287 unique .amr files transcribed. Full log: /tmp/cubecallrecorder_batch/transcript_log.md (1372 lines, 89 files flagged for case keywords). Executive summary was being compiled by a sub-agent (task 00bc1d28) as of last save — check if /tmp/cubecallrecorder_batch/executive_summary.md exists. Key spot-checked finds: Justice Court tripod test (retaliation test), lobby-recording First Amendment dispute with judge's staff, garbled "Chad"/"Scott" Justice Court confrontation.

## Source 6: Google Drive "Recordings" subfolders — Call Recorder / Voice Record Pro / RECORDER (534 files, 296 priority 2021-2022)
Only ~11 of 296 priority files transcribed so far (progress slow — some .wma files are 28+ hrs long, need chunking, deprioritize). Continuation was running as of last save.

## Source 7: Google Drive "Recordings" subfolders — xs max recordings / Adobe Audition / show setup / Audio Files and Recordings / .CloudRecordings_SUPPORT
Cataloged, found Aug 11 2023 dated files that may DUPLICATE the already-fully-transcribed Galveston zip (Source 1) — dedup check was in progress, not confirmed either way as of last save. Adobe Audition/show setup likely music-production (Bad Actors project), not evidence — skip unless spoken word confirmed.

## Source 8: Google Drive "Recordings" — "composition" folders — ✅ FULLY COMPLETE (6/6 files)
All 6 2020-dated composition-folder recordings transcribed. Key finds: "17 police reports" pattern (Pleasant Ridge Rd recording), DOB confirmation + July 2020 court date, Section 1983 planning call w/ Jesse McBride & Ray Garrett ("the outlaw"), high-conflict domestic argument recording.

## Priority order for next session
1. Voice Memos batch2: Mickey Mallette / Senator McDaniels / Oxford Eagle Publisher (political/media leads, untranscribed, high value)
2. Recordings root: finish LC_1st/2nd/3rd/20190720_incoming to complete the Crowder/Dustin narrative arc
3. Confirm dedup status of Source 7 vs Source 1 (don't waste effort re-transcribing if duplicate)
4. callrecorder 12-2021/01-2022 (244 files) — biggest remaining unprocessed chunk
5. Voice Memos batch1: finish remaining 13 of the 30 already downloaded
6. Chunk and transcribe the 4 large trial-testimony files (Source 2)
7. The 6-page "2022-04-01 Certificate Of Service Backdated" document itself — STILL never actually OCR'd/read despite being flagged repeatedly as the top open item. Do this before anything else audio-related if credits allow — it's a document read, not a transcription swarm task, and should be cheap/fast.
