# American Injustice / Reardon Case — Full Knowledge Export for Claude
**Exported:** 2026-07-24 from BuildMyBot Partner Superagent (Base44)
**Purpose:** Complete transfer package — identity, case memory, conversation history, session transcripts, and reference URLs — for continued work in Claude.

---

## 1. IDENTITY / PORTFOLIO CONTEXT

**User:** Matthew Oliver Reardon, pen name **Don Matthews**. USMC 2007-2011 (discharged General Under Other Than Honorable, alcohol-related). Investigative journalist / First Amendment auditor (press credentials via CFAPA.org since July 2021), civil rights litigant, homeless veteran living out of his car. Founded "Outlawed Productions LLC."

**Family:** Wife Madelyn. Daughter Lydia Elise Reardon (b. Aug 19 2014, mother Phyllis Marie Crowder). A son born prematurely Feb 17 2022 (28wk, 2lb1oz) while Reardon was involuntarily committed. Blended family includes Anna/Anna Claire, Emmy/Mary Evelyn, Kenna Rose (confirmed Reardon's own biological daughters), possibly Hannah — Madelyn's kids, not fully mapped. Mother-in-law **Rena** passed away 2022 (standing watch item on audio transcription passes — flag any "Rena"/"Momma"/"Meme" mention).

Documented pre-existing shoulder injury requiring 3 hospitalizations (relevant to excessive-force civil rights claims).

**Portfolio ventures:**
- **BuildMyBot.app** — flagship SaaS
- **CaseBuddy** (repo `patriotnewsactivism/case-companion`) — AI legal tech
- **We The People News** (wtpnews.org) — independent journalism/advocacy outlet
- **CivilRightsHub.org**
- **ChatScream**
- **CodeForge**
- **TubeScribe** (repo `patriotnewsactivism/insightful-tube-explorer`)
- **APEX** — agent workforce framework (flagship QA Swarm capability, task-per-persona architecture)
- **Bad Actors** — music project (see §7)
- **American Injustice** — memoir/exposé book (see §5-6, the primary subject of this export)
- **donmatthews.live** — personal brand hub

---

## 2. INFRASTRUCTURE FACTS (current, for reference — likely less relevant to Claude/book work but included for completeness)

- GITHUB_TOKEN_9 is DEAD (401, confirmed 2026-07-23). Use GitHub OAuth connector going forward for `patriotnewsactivism/*` repos.
- `patriotnewsactivism/Apex` = active infra repo. Railway project cb22f086-7db9-4189-a228-5e712c2fe8c5.
- Apex LLM fallback chain: OpenRouter(paid) → Cerebras → Mistral → Groq → Cohere(trial) → OpenRouter-Free. **Never use Anthropic/OpenAI/Amazon Bedrock anywhere in the portfolio stack** (note: this rule governs the *BuildMyBot/Apex product*, not this export/Claude-migration action itself).
- Vercel `buildmybot20` = live buildmybot.app, stays on Vercel permanently.
- CaseBuddy Supabase `jpzkumgndqsdwimbvjku`: RLS gap on `cases` blocking anon inserts 1-3am CST — unfixed. CourtListener API token dead/403.
- donmatthews.live subdomains live: apex, thinktank, voice, root.
- Standing infra sweep: gateway.ts and related files for silent error-swallowing in DB queries; keep all DB query updates aligned to live schema.

---

## 3. ACTIVE LEGAL MATTERS — INDEX

### 1. Reardon v. Osteen, 3:25-cv-00203 (S.D. Tex., Galveston Division)
Judge Jeffrey V. Brown, Clerk Nathan Ochsner, referred to Magistrate Judge Andrew M. Edison. Galveston Aug 2023 DWI arrest; Busby/Beavers also named as MS-side defendants in the same consolidated pro se suit.

**R&R entered July 14, 2026 (Dkt.90) resolved SEVEN motions:**
- DENIED (non-dispositive orders, Rule 72(a) review): motion to strike Busby's affidavit + sanctions (Dkt.61); motion for leave to file supplemental complaint (Dkt.85); motion to expedite (Dkt.86).
- RECOMMENDED GRANT (dispositive, Rule 72(b) de novo review): Busby's MTD (Dkt.65, personal jurisdiction — pp.10-12); Galveston Defendants' MTD (Dkt.68, City/Osteen/Doraty); Beavers's MTD (Dkt.69).
- RECOMMENDED sua sponte dismissal of Hoby James / Galveston County / John Does 1-5.
- RECOMMENDED DENY Reardon's TRO (Dkt.84) — entirely derivative of the dismissal recommendations (pp.32-33).

**This means the June 22, 2026 second-vehicle-seizure emergency TRO package was already rejected by this same R&R — not still pending.**

**Objections due July 28, 2026** — draft at `reardon_v_osteen/objections_to_MR_draft.md` on GitHub `patriotnewsactivism/PDFs` repo (commit `b7f7725`, fully pincited to Dkt.90 page numbers). **This IS a complete 9-objection redraft** covering all 7 resolved motions (not just the seizure claim):
- **Objection 1 (strongest):** Unreasonable seizure — magistrate found a REAL constitutional violation (impoundment unreasonable, Opperman community-caretaking exception doesn't apply — p.21) but granted qualified immunity only because Reardon never briefed the "clearly established law" prong (pp.22-24). Do NOT cite Degenhardt v. Bintliff, 117 F.4th 747 (5th Cir. 2024) as supporting authority — the magistrate cites it as adverse precedent (officers in a similar case ALSO got QI, p.757). Lead instead with **Hope v. Pelzer**, 536 U.S. 730 (2002) — obviousness doctrine, never addressed by the R&R.
- **Objection 2:** First Amendment retaliation — dismissed for lack of comparator evidence (pp.27-28); ask for dismissal without prejudice w/ leave to replead.
- **Objection 3:** Malicious prosecution/unlawful search — preserve "the record shows that Osteen lied to Judge Tollison" (p.20) and the Dkt.79 ¶14 concession (defense's June 10 2026 Reply: Osteen said on-camera he smelled no alcohol); push for a Franks hearing rather than resolution on the pleadings (honest caveat: this is a longer shot, the R&R's materiality reasoning is substantive).
- **Objection 4:** Excessive force (p.26) — pleading-specificity dismissal, ask without-prejudice w/ leave to amend re: the documented shoulder injury.
- **Objection 5:** Doraty (pp.15-16) — same, without-prejudice ask.
- **Objection 6:** Busby personal jurisdiction (pp.10-12) — weak objection, only pursue with new facts.
- **Objections 7-8:** Motion to strike (Dkt.61, pp.31-32) and motion for leave (Dkt.85, p.32) — cite Rule 72(a) not 72(b), different standard.
- **Objection 9:** TRO denial (Dkt.84) — entirely derivative of Objection 1's outcome.

Case background: Osteen's affidavit ("moderate odor of alcohol") held Reardon ~11mo on $100K bond; forced blood draw was 0 BAC; felony charge dismissed May 24 2024 specifically to dodge a Franks hearing. June 11 2026: pushed from courthouse by US Marshals same day he filed a sur-reply. June 22 2026: 2nd vehicle (2016 Mitsubishi Outlander) seized after cop-watching at a Walgreens — arrested for expired tag, jailed 22hrs, towed to Marty's City Auto ($373.94/2 days; supervisor "Ray": "stand in line, that's what happens to people like you"). March 2026: banned from Galveston Housing Authority property while filming. Confirmed BOLO pattern: US Marshals lookout alert on Reardon for his journalism (per FOIA) — confrontations at 3 federal courthouses (Lafayette LA Aug 25 2025, Aberdeen MS June 4 2026, Galveston TX June 11 2026).

### 2. Reardon v. Lafayette County MS et al., 3:22-CV-50-SA-JMV (N.D. Miss., Judge Aycock)
Filed pro se April 6 2022. Dismissed with prejudice June 28 2023.

### 3. United States v. Reardon, 6:25-cr-00227 (W.D. La.)
Federal misdemeanor. Aug 25 2025 arrest at John M. Shaw US Courthouse Lafayette, violating 41 CFR §102-74.390(b) (Deputy US Marshal Hayden Nugent) after 3 prior visits. Dec 15-16 2025 bench trial (Judge LeBlanc). Jan 16 2026 guilty. July 16 2026 First Amendment MTD denied ("nonpublic forum"). No sentencing entry yet — Rule 58(g)(2) appeal clock not started. Honest counterweight: trial record shows Reardon left a tripod blocking an emergency exit, taped posterboard over doors, crude remark to Nugent, livestream said "now they just asked for it." Near-identical July 19-21 2021 Oxford US Attorney's Office incident is a documented 4-years-earlier parallel.

### 4. Reardon v. City of New Orleans et al. — full 4-event timeline
1. **Nov 12, 2025:** Allied Universal guard Jerome Ard struck Reardon with a metal flashlight at NOLA City Hall, split his head open, Tulane Medical Center transport, destroyed his phone. NOPD Officer Junious Grady swore affidavit; Officer Victor Paz (#26091) declared Reardon "the aggressor." Warrant signed same day 3:34pm, Judge Juana Marine Lombard. RTCC cameras did NOT capture the actual altercation. Ard never charged.
2. **Records cover-up:** NextRequest 25-21253 (filed Nov 17 2025) — denied Dec 10 2025 citing LA RS 44:3(1), using the bogus charge against Reardon as pretext to withhold footage of his own assault. City Attorney staffer Tana Scoby claimed ignorance.
3. **Jan 28, 2026 retaliatory arrest:** taken into custody in Lafayette LA during an ice storm at a Red Cross warming shelter. Held ~6 days, extradited to New Orleans, booked at 2800 Perdido St by Officer McIver (#00625). Charge: simple battery. $100 cash bond but falsely told he needed an LA driver's license. Pretrial Risk Level 1 (lowest). Released 150 miles from his car.
4. **April 16-17, 2026 dismissal:** Orleans Parish Criminal District Court, case **M625048**, ADA Trishawn Payne-Jones, disposition code **433 "Refused — Law Enforcement Issue."**

Docs not yet read: `COMPLAINT TO INTERNAL AFFAIRS DIVISION`, `FORMAL COMPLAINT — FEDERAL MISCONDUCT REPORT`, `Incident_23005559.pdf`, `Incident_24003697_R.pdf`, `CVR-000253/254`, `CVR-000243`, 2x `Case Summary and Legal Analysis`. Draft complaint `Reardon_v_New_Orleans_Federal_Complaint.pdf` (34pp, Drive id `1NsZS_l-D-zs8yvoEKOvoE-ZnsgjAC63x`) — filing status unconfirmed.

### 5. Union County, MS matter ("the Aberdeen thread")
- April 15, 2026: CJ Bright confronts Reardon on public sidewalk during First Amendment audit, admits on camera he can't legally stop him.
- April 20: Board issues preemptive profanity "gag rule"; Reardon arrested for one profane word during public comment; baseless "phantom" MDOC hold placed.
- April 21: judge releases him, clears phantom hold.
- May 5: pro se in Union County Justice Court; judge himself uses profanity from the bench; Reardon files 9 motions citing 32 SCOTUS cases.
- June 1: arrested for carrying a "FUCK CITY HALL" sign into Justice Court + Courthouse ("Disturbing the Peace"). Asked deputies if Investigator Fitts "had big enough balls to arrest him again," carried sign into an active courtroom where advisor **Mark McClinton** was present (possibly same as Oct 2022 "McClinton call," unconfirmed). Sheriff Edwards arrested him personally. Phone seized without warrant. **"Chad Mood" (corrected from "Chad Wood") also involved** — ambiguous whether this is the 2022 MS Justice Court incident or this 2026 Union County one.
- June 4: **federal courthouse arrest.** Drove to Thomas G. Abernethy Federal Building (Aberdeen) to file a 6-doc, 100+pg §1983 complaint. Security demanded photo ID (no such federal requirement); after 20-min stall waiting on a "Mr. Lipshutz" (identity unknown), Police Chief D. Shumpert arrived, claimed Reardon "caused a disturbance," arrested him. Car searched/towed from federal lot; phone seized. Prosecution routed to MUNICIPAL court rather than federal.
- June 6: Reardon publishes full report.
- June 7: Aberdeen PD Captain "SRQ" Lee texted the article to colleagues captioned "Watch the video with us in it. Lol."
- Status: complaint blocked before filing June 4 — unclear if/where later filed; June 1 charge outcome unknown; "Mr. Lipshutz" identity unknown.

### 6. Case-number reconciliation (CONFIRMED 2026-07-24)
The **2017 Lynch case (LK17-295)** and the **2022 Tannehill/second-stalking case** are TWO SEPARATE prosecutions.
- **L20-316** = the 2020 PCR motion against the 2017 conviction (filed July 7 2020, denied w/o hearing July 30 2020 by Judge Kelly Luther, Rule 59 rehearing denied Oct 13 2020).
- **CV2016-422W** = the separate Crowder custody dispute.
- **2017-CV-217** = the Lafayette County Tannehill restraining-order case.

### 7. 2024-25 MS PCR petition
Jacob Howard/MacArthur Justice Center targeted the Nov 2022 revocation + the 2022 stalking plea → Jan 21 2025 full vacatur (primary doc `Post-Conviction-Relief-Full.pdf` in Drive still needs OCR to independently verify). Separately: June 2024 vacated the Oct 2022 probation-violation sentence while in Galveston custody; June 28 2024 saw a third distinct event (Reardon v. State 2024-KM-00839-COA dismissal, later reversed). **Three distinct events, don't conflate.**

### 8. Reardon v. Layton City, UT et al.
Confirmed filed, District of Utah, March 31, 2025. Defendants: Layton City, Layton PD, Lt. Richins, Mark Arrington, Capt. Hildon Sessums (Oxford PD), Chief Jeff McCutchen (Oxford PD).

### 9. Reardon v. State, 2024-KM-00839-COA
MS Court of Appeals, decided Feb 24, 2026 — **Reardon WON**, reversing the June 28 2024 dismissal. Appellee's counsel: Bela J. Chain III. Directly contradicts Clerk Busby's Nov 2025 federal affidavit (see §4 below, Busby Files).

**Unresolved/low-priority:** `RCR-000015...Motion-to-Dismiss-the-Indictment-Matthew.pdf` confirmed unrelated to New Orleans (dated Sept 19 2025); whether a Jan 26 2026 "Lafayette Parish jail" FB fragment relates to matter #3 or something else.

---

## 4. THE BUSBY FILES — affidavit contradiction fully documented
(Dossier published wtpnews.org, April 7 2026)
- Specimen A: March 25, 2024 letter, Busby states no properly filed appeal pending, referencing 5 DUI cause numbers (9290609/9290610/9291197/9291198/9291202 — a different case family, don't conflate with stalking/PCR/custody numbers).
- Specimen B: Nov 12, 2025 sworn federal affidavit (ECF Doc. 46-1, Exhibit A to Busby's MTD in Reardon v. Osteen), Busby swears he never gave Galveston DA info on Reardon's DUI appeal status. Notary: Chyna Sniiro, DC.
- Direct contradiction: 2024 letter proves he DID provide that info; 2025 affidavit swears he did NOT. Dossier's signature-match analysis is self-conducted, not court-certified. Feb 24 2026 COA ruling further proves the appeal was never final. **Fully resolved — pull straight into the manuscript's Busby section.**

---

## 5. "THE OXFORD MACHINE" — the $34,000 Metro Narcotics scandal
(wtpnews.org investigation, published April 2026) — ties East/Busby/Tannehill together
- Metro Narcotics Unit (est. 1988, $150K/yr each from Oxford/Lafayette County/Ole Miss), overseen by a 3-member Control Board.
- ~2014: ~$4,000 first found missing from the unit's lockbox at First National Bank of Oxford — FBI found insufficient evidence to charge anyone (per City Attorney Pope Mallette's April 4 2016 letter to the State Auditor).
- Late 2015: ~$30,000 MORE missing, discovered during a change-of-command inventory by then-OPD Chief **Joey East** and Chief Deputy **Scott Mills** — East was both an authorized lockbox signatory AND one of only two people who "discovered" the second shortage, a clear self-investigation conflict.
- Mayor Robyn Tannehill's husband, attorney J. Rhea Tannehill Jr. (whose practice profits from Metro Narcotics cases; also Municipal Court Judge of Sardis MS), called the missing-money story "old news" to a reporter BEFORE it was publicly reported — implying non-public info, plausibly via his wife's position as Mayor. Source: Mississippi Free Press reporter Alyssa Schnugg — **citable** (named source + public letter), unlike the two DO-NOT-USE Tannehill rumors below.
- Power structure: East is the son of F.D. "Buddy" East (sheriff 1972-2018); ran OPD, sat on the Narcotics Control Board, won Sheriff election, sworn in Jan 2020. Busby was Board of Supervisors President 8 years (funded Metro Narcotics), won Circuit Clerk 2019, took office Jan 2020 (his mother Mary Alice Busby held the same seat 1988-2012). Tannehill: Oxford Tourism Council director, Ward 2 Alderman 2013, Mayor 2017/reelected 2021, oversees OPD.
- Records-tampering mechanism: when Reardon found his DUI court file altered, the deputy clerk called Busby; Busby called Sheriff East instead of coming himself; deputies removed Reardon from the courthouse within the hour.
- wtpnews.org investigations archive fully indexed at the summary level (confirmed only 2 pages total).

---

## 6. AMERICAN INJUSTICE (the book) — full status

**Manuscript master:** `corrected_manuscript_v2.txt` on `github.com/patriotnewsactivism/PDFs`
**Audit findings:** `chapter_audit_findings.md`, same repo.
**Audit 100% complete, all 27 chapters + epilogue** — but the 2017-vs-2022 two-case correction below still needs to be worked INTO the manuscript text (currently only reconciled in memory). This is the #1 open manuscript action item.

### ★ CONFIRMED FULL CHRONOLOGY (corrected 2026-07-24 — two separate aggravated stalking cases, not one)

**2017 origin — Case A, the Lynch case (LK17-295):**
- May 1: Pruitt arrests Reardon at a flag protest; temp restraining order signed by Judge Avent that week (sought by Mona Pittman/Crowder's attorney).
- May 8: Deputy Chequille Williams got a call from Rickey Weaver re: Reardon retrieving his flag.
- May 16: blocked from speaking at Oxford Board of Aldermen by Mayor Pat Patterson.
- May 19: dispute at Frank & Marlee's piano bar (owners Todd & Ashley Lynch) — Ashley refused to talk, threw away food he'd paid for; he left without escalating, then did a FB Live boycott call outside.
- May 20: AR-15 purchased from Larry Watkins/Armslist (bill of sale dated May 20).
- May 24: hair-follicle test positive for amphetamine+ecstasy (complicating fact); Investigator Jarrett/Jared Bundren reviewed his FB page re: a Todd Lynch threat (basis for the Lynch charge); the Tannehills (Mayor Robyn + husband/attorney Rhea) also filed a restraining order against him this same period (**case 2017-CV-217**) — Reardon calls it fraudulent; Rhea allegedly threatened him in a hallway, restrained by Major John Hill (not a bad actor); hearing before Judge Glenn Alderson.
  - **CONFIRMED CHAIN (2026-07-24):** Investigator Jared Bundren (LCSD) wrote a police report dated **May 30, 2017 — six days after the fact** — claiming he'd received a call on **May 24, 2017** reporting Reardon was making online threats. Reardon repeatedly FOIA'd for the call/recording/substance and was completely stonewalled (confirmed both by Bundren directly AND on tape by Busby's own attorney David O'Donnell — his associate is "Lisa Carwile"). This is the evidentiary root of the Lynch aggravated-stalking charge's origin (alongside the AR-15 impossibility below).
- May 25: FBI interview arranged by AUSA Bob Norman (bob.norman@usdoj.gov) — **302 form never logged/produced** — a SEPARATE evidence-suppression thread from a different agency (FBI, not LCSD) — don't conflate with the Bundren/May-24-call thread above.
- **May 26: ambush arrest by 4 senior officers (Chief Deputy Scott Mills, Major Alan Wilburn, Lt. Jared Bundren, Chief Joey East) for aggravated stalking, alleging he threatened Todd/Ashley Lynch with an AR-15 "on or before May 8" — but the bill of sale proves the AR-15 wasn't bought until May 20, a 12-day impossibility, this case's central exculpatory fact.**
- May 30: initial appearance, Justice Court Judge Carolyn Bell (met privately with sheriff's investigators pre-hearing, cut him off twice re: the bill of sale), $150K bond. Defense attorney sequence: William C. Stennett → Brennan Horan (conflicted, brother of sitting MS State Rep. Kevin Horan; confirmed via 2019 obituary of their father Ben F. Horan).
- **While in jail on the Lynch aggravated-stalking charge, Horan advised Reardon that if he simply agreed to/signed the Tannehill restraining order (2017-CV-217) without contesting it, it would help him get released on the Lynch charge — Reardon signed it under duress on that basis.**
- **CONFIRMED 2026-07-24 (via Andy T. Arant call, Recordings-root file `20200707 025648-DF0738FF.m4a`):** Reardon DID plead guilty in the underlying 2017 Lynch case itself and was **released from jail July 6, 2017**. Andy T. Arant is a public defender in Water Valley, confirmed SEPARATE from Horan — later informal mentor/friend. He learned only after release that a habeas petition (filed by "Christian McRae"/likely Christi McCoy) had been approved June 6, 2017 but never brought before the judge while he sat in custody — a separate potential illegal-confinement argument. **This resolves Standing Item #2 partially** — confirms guilty plea + July 6, 2017 release date — but the exact SENTENCE/plea terms for Case A are still not pinned down (only that he pled guilty and was released same day). The "5yr probation/5yr banishment" sentence previously misattributed to this 2017 event actually belongs to **Case B** below.
- Sept 11, 2017: Dr. Joe Edward Morris's psych eval found no significant deficits, cited coercion as a driver of his decision-making that period.

**2018-2020 (Crowder saga):**
- Nov 25 2018: an actual consensual encounter (both parties' texts confirm), later falsely reported by Crowder as non-consensual — Det. Holladay's investigation concluded false report.
- Jan 2019: OBPD charged Crowder w/ misdemeanor false reporting.
- Sept 22 2020: Crowder convicted in Olive Branch Municipal Court, nolo contendere — appeal filed late, county court denied/remanded, Olive Branch judge refused to enforce (triggered Reardon's own later contempt arrest).

**2020 PCR/records saga:**
- June 25-27: text thread w/ Christi McCoy (Crowder's own attorney) re: his conspiracy theory.
- July 7: PCR motion filed (=L20-316) against the 2017 conviction, denied w/o hearing July 30 by Judge Kelly Luther, Rule 59 rehearing denied Oct 13.
- Aug 12: recusal motion re: Luther filed — after which the case's judge was allegedly "fraudulently changed" from Kent Smith to Luther.
- Oct 19: Reardon interviews Sheriff East by phone (cooperative tone, contrast w/ later hostility).
- Nov 16: McCoy confirms her Victims Assistance Program role, "advocate only" for Crowder in chancery, names Judge Shumake, praises GAL Lori Solinger as fair.
- Dec 27: Reardon's own call to the Bureau of Victim Assistance, naming "Earline Gardner Victim Assistance Program" himself, confirming spelling "Earline."

**★ Notary-fraud theory** (most internally consistent claim, still [CLAIM]/unverified): Mona Pittman allegedly filed a false/incomplete Chancery petition Aug 26 2017 — fast-filed without proper summons to reduce Crowder's Olive Branch sentencing exposure — then filed the "true" petition later reusing the same notary stamp. Corroborated across 3 independent audio sources. Worth a clearly-labeled paragraph in the manuscript.

**Late 2020-2021:**
- Dec 28 2020 arrest: Deputies Dixon+Ethan Tidwell arrested him after he refused to move without speaking to East; East delayed bond release overnight.
- Feb 21 2021 DUI stop by Beavers (claims to smell marijuana, "initiates a DUI investigation" — this stop is the origin of the eventual Nov 24 2021 DUI conviction that runs in parallel to the stalking cases).
- Olive Branch contempt arrest (date unplaced): $500 bond for mentioning "she falsely accused me of rape" in a records request; filed a $10M pro se suit vs. Olive Branch.
- June 19: Justice Court abstract, 3 Crowder-filed charges — all NOT GUILTY/nolle prosequi at the Nov 4 trial.
- **July 19-21: films outside the Oxford US Attorney's Office** — Chief McCutchen got him a same-day police report copy, called AUSA Norman "blowhard Bob"; recorded clip captures a direct confrontation with Norman.
- Sept 29: drone incident near Justice Court WITH a minor stepdaughter present, crashed into the building; Mills+Oxford PD arrived.
- **Tupelo Crisis Center — real event, date still UNCONFIRMED.** Domestic disturbance arrest after an argument w/ Madelyn; short Tupelo Crisis Center stay; unconsented search found a weed pipe; charge later shelved. Don says June 24-July 9 2021 "sounds close" but wants it double-checked — no more document avenue left, needs his direct memory anchor. **STILL OPEN.**

**Nov 4 2021 trial** (9 charges/3 events): guilty on all LCSD charges, not guilty on all Crowder-brought charges. Sheriff East testified DUI-stop footage was "gone forever" — **later contradicted by his own sworn trial testimony admitting jail parking-lot video is SELECTIVELY preserved (not systemic auto-deletion)** — a key corroborated finding.
- Dec 6: discovers the Smith→Luther judge swap, confronts Clerk Busby; East blocks his car, bars him from Circuit Court.
- Dec 7: East seeks commitment; Judge Lawrence Little signs affidavit; committed Dec 9-23.

**2022 (parallel tracks):**
- Nov 24, 2021: found guilty in Lafayette County Justice Court of DUI + related misdemeanors (the Beavers stop).
- Dec 2021-2022: extensive pro se appeal fight on the DUI conviction (notice of appeal disputes in both justice/circuit court, indigency disputes, Driskell reappointed as counsel April 2022).
- Feb 9: Susan Beard's 2nd commitment affidavit.
- Feb 17: son born via emergency C-section while Reardon confined.
- April 6: 2nd federal complaint filed (N.D. Miss., =matter #2).
- Aug 15: Mitchell Driskell begins working at Rhea Tannehill's firm.

**Case B — the 2022 Tannehill/second-stalking case (CONFIRMED 2026-07-24, distinct from the 2017 Lynch case):**
Mississippi's aggravated-stalking statute allows an enhanced repeat charge for a prior stalking conviction within a lookback window (Reardon's understanding: ~7 years). Because the 2017 Tannehill restraining order (2017-CV-217) was still "allegedly valid," and Reardon had the 2017 Lynch stalking conviction on record, walking into a building associated with that restraining order (Don says "City Hall"; the court record — the R&R in Reardon v. Osteen — describes it as "entering Lafayette County Chancery Court for a scheduled child-custody hearing," June 28, 2022; possibly the same complex, minor discrepancy unresolved) triggered a **new, second aggravated stalking arrest June 28, 2022**.
- **Sept 30, 2022: pled guilty — 5yr suspended/unsupervised probation, banished from Lafayette County 5 years, 45 days to vacate (deadline Mon Nov 14, 2022).**
- Oct 28, 2022: FBI Oxford visit/presence in Oxford (notified FBI beforehand) — treated as a banishment violation even though the 45-day vacate grace period hadn't technically expired.
- **Nov 3, 2022: revocation hearing (Judge Tollison) found him in violation of banishment based on Kandis Beavers's (perjured) testimony, sentenced to ~1 year in MS custody.**
- Released Aug 1, 2023.

**2023-2025 vindication arc:**
- Aug 11 2023: Galveston TX felony DWI arrest (alleges TX+MS coordination + Osteen's perjury).
- March 2024: felony dropped, recharged misdemeanor.
- June 2024: court vacates the Oct 2022 probation-violation sentence.
- Nov 26 2024: Jacob Howard/MacArthur Justice Center files a PCR petition (targeting the 2022 stalking-case revocation + plea, not the 2017 Lynch case).
- Jan 21 2025: sentence VACATED entirely.
- Feb 1 2025: relocated to Layton UT.
- Feb 24 2026: won the Reardon v. State COA reversal.

**Editorial/manuscript technical notes:**
- Ch.23 still needs the Osteen-lied-under-oath magistrate finding folded in.
- Breathalyzer wording: Galveston dispatch audio has a bystander confirming he OFFERED one; manuscript says "consistently denied" — likely both true (offered, but refused in favor of blood draw).

### Confirmed bad-actors roster
Kandis Beavers (perjured Nov 2022 revocation-hearing testimony; also original Feb 2021 DUI-stop officer). Joey/"Buddy" East (sallyport admission; multiple commitments; FOIA stonewalls; delayed bond release; also implicated in $34K Metro Narcotics scandal as self-investigating signatory). Scott Mills (same Metro Narcotics conflict). Alan Wilburn. Jared/Jarrett Bundren (FOIA obstruction + May 24 2017 FB-review call/fabricated May 30 report; one of the 4 arresting officers). Hildon Sessums. Chief Jeff McCutchen (mixed). Tiffany Kilpatrick. William Osteen (lied under oath, now court-conceded via Dkt.79). Judge Mickey Avent. Judge Tollison (2022 revocation, vacated). Judge Kelly Luther. Judge Carolyn Bell. Timmy Pruitt (uncorroborated hearsay re: marijuana-tampering/Ponzi ties). Brennan Horan (conflicted, brother of Rep. Kevin Horan; advised the duress-signed Tannehill restraining order). Mitchell Driskell (conflicted, joined Tannehill firm). Bela J. Chain III. Lt. Richins. Mark Arrington. Clerk Jeff Busby (2025 affidavit contradicted by 2024 letter; also implicated in the $34K scandal's records-tampering mechanism). AUSA Bob Norman (on-tape confrontation confirmed; alleged Crowder family tie remains explicitly unverified). Rhea Tannehill (advance non-public knowledge of the Metro Narcotics scandal — citable via named Mississippi Free Press source, distinct from the two DO-NOT-USE rumors below). NOLA: Officer Junious Grady, Officer Victor Paz (#26091), Judge Juana Marine Lombard, Officer McIver (#00625), Tana Scoby, Jerome Ard (never charged), Vidal/Savage. Union County/Aberdeen: Sheriff Jimmy Edwards, CJ Bright, Investigator Adam Fitz/Fitts, Police Chief D. Shumpert, Captain "SRQ" Lee, **Chad Mood** (name-corrected from "Chad Wood" — ambiguous whether this is the 2022 MS incident or the 2026 Union County one).

**NOT bad actors:** James G. Wyly III, Hoby James, Major John Hill, Christi McCoy, Lori Solinger, Denise Fondren, Detective Holladay, Ben Creekmore, Mickey/Nikki Mallett, Robert Carter, Allison Ray, Lawrence Ballard.

**Needs more context:** Sgt. Jack Doraty, Deputy Micah East, Lt. Theobald, Samantha Wetherspey, Jesse Tripp, Samantha Brock/"Heather" (suspected leak, [CLAIM] uncorroborated), T.R. Trout, Judge Glenn Alderson, Kathy Sturdivant, Mona Pittman, Caleb East, Chequille Williams, Rickey Weaver, Chad Wood/Mood, Tyler Wren, Deputy Durham, Willy Diaz, Anthony Hudson, Cathy Conner, Officer S. George, Lamar, Mark McClinton, David O'Donnell (Busby's attorney — neutral/procedural role so far), Lisa Carwile.

**Two uncorroborated rumors re: Mayor Robyn Tannehill — zero corroboration, severe defamation risk, DO NOT USE:** an affair w/ then-Speaker Philip Gunn; paying BLM to attend a protest "as a tax saver." Also an unconfirmed state-senate-run/divorce rumor.

**PII/CONTENT WARNINGS:** one file has a full credit card number/CVV read aloud — never quote, exclude. Another has an extremely graphic violent rant with fabricated assassination/torture claims — exclude entirely.

**Honest-reporting counterweight (the "layered thesis"):** his Aug 2025 trial-record conduct (tripod blocking an exit, crude remarks, livestream saying "now they just asked for it"); multiple recordings of him coaching/probing 6-yo Lydia about custody at her mother's home; a raw argument where he and Crowder trade unverified accusations against each other's spouses; self-disclosed failure to file federal taxes 6-7 years; the drone incident involved a minor stepdaughter present.

**Galveston dispatch zip — fully mined (46/46):** bystander confirms he offered a breathalyzer; PD warned the hospital "an auditor" was coming; Sgt. Hoby James called in after watching the livestream; MS couldn't confirm conviction status on tape. Sgt. Jack Doraty present at the forced blood draw, failed to intervene. UTMB Health + Defendant McDougle performed the draw. "17 police reports over 5 years" rebuts a "sudden complainer" framing.

**Off-topic/excluded:** "LC" files (custody). "Cindy Meek Brown"/"Ed Meek" — unconfirmed, low priority. Family/wife voice memos — private, excluded.

**Cover design standard:** upside-down flag distress-signal background, USMC digital camo portrait, oath of enlistment as a framed left-margin block, bold non-splotchy full-width stroked typography.

**Editorial framing (standing rule):** layered thesis — real institutional misconduct AND his own escalating conduct both belong, presented honestly.

### Audio transcription — pool status
**Fully done:** Galveston zip (46), cubecallrecorder, composition folder, callrecorder_batch (190), 221003_1800.m4a, Voice Memos (588), Call Recorder subfolder (163), RECORDER/TALK folder (all 168), Voice Record Pro (all 9 folders), xs max recordings (all 9), MEMO folder (all).
**In progress: Recordings-root loose files.** 986 loose files in Drive folder `1gJt3yv4vARMCPQnURaMdQqN2nhvpsUS5`. De-duplicated to 318 unique files (many duplicate syncs under two naming schemes). **~268 remain as of 2026-07-24.** Spot-tests confirm mostly low-value (customer service calls, password resets, personal disputes) — lower priority than remaining manuscript blockers. **Standing watch: flag any mention of "Rena"/"Momma Rena"/"Mom"/"Meme" (deceased mother-in-law) in every future batch.**
**Still fully untouched (low priority):** MUSIC, Adobe Audition, show setup, composition x6, CloudRecordings_SUPPORT, Audio Files and Recordings.

### reardonmarketingfirm@gmail.com mailbox — lower value than hoped
Mostly marketing spam + recent self-correspondence, NOT a preserved 2017-2022 case archive (68,730 msgs total, primary evidence repository designation). One unresolved lead: attachment "Recording #2-Laura Hood.eml" in a May 2025 email re: "Charles Yow" — not yet pulled/identified.

### "Reardon Watch" YouTube channel (@reardonwatch1008) — hostile 2017 real-time coverage
24 subs, 25 videos, all ~2017, contemporaneous with the Frank & Marlee's saga. Key: 8-part "Frank and Marlee's Saga" (incl. "The Security Camera Footage," "The Phone Call"), "Breaking News: Reardon Arrested!", mocking titles ("The Fireball Rants" 1-3, "72-Hr Facebook Ban," "Oxford is a Nazi Communist Dictatorship"). Individual video permalinks not yet extracted.

---

## 7. BAD ACTORS (music project)
Volume 1, 17 tracks: Silence Ain't Consent, Unbroken, In the Shadows Tonight, Double Dipped, Morgan County Blues, The Osteen Files (Exhibit L), A Warrant For A Lie, The Crowder Files, Eleven Months Too Long, Caught Red Handed, Osteen Lied, Land of the Free Unless Its Me, She Called The State, Osteen's Fall, The Gaslight Anthem, Governors Gone Too Far, Scandalous. BandLab embed ID: 4d64abf2-acc1-f011-8196-000d3a96100f. Standing rule: all playback on donmatthews.live stays in-page, never navigates away.

---

## 8. STANDING NEXT STEPS (open action items, in priority order)
1. Apply the 2017-vs-2022 two-case correction into the actual manuscript chapters (`corrected_manuscript_v2.txt`) — currently only reconciled in memory.
2. Get the exact final SENTENCE/plea terms for the 2017 Lynch aggravated-stalking charge (Case A) — now know he pled guilty and was released July 6, 2017, but the sentence terms themselves aren't pinned down.
3. Resolve the minor "City Hall" vs. "Chancery Court for a child-custody hearing" discrepancy on the June 28, 2022 arrest location.
4. ✅ DONE: Reardon v. Osteen objections redraft — all 9 objections complete with pincites, pushed to GitHub `reardon_v_osteen/objections_to_MR_draft.md` (commit `b7f7725`). Deadline July 28, 2026.
5. OCR `Post-Conviction-Relief-Full.pdf` to independently verify the Jan 2025 vacatur.
6. Read `notce of appearance horan.PDF`, `Evidence for Timmy Pruitt Report.pdf`, `motion to vacate restraining order.docx`.
7. Confirm/deny the Tupelo Crisis Center date with Don directly (June 24-July 9 2021 suspected, unconfirmed).
8. Pull individual video links from "Reardon Watch" if desired.
9. Identify the "Charles Yow"/"Laura Hood" recording lead if pursued.
10. Find where/whether the Union County federal complaint was ultimately filed; outcome of June 1 2026 "Disturbing the Peace" charge; identity of "Mr. Lipshutz"; confirm if Mark McClinton is the same 2022 advisor; clarify whether "Chad Mood" belongs to 2022 MS or 2026 Union County.
11-13. Various infra items (Apex QA swarm, PR checks, CaseBuddy fixes) — lower priority relative to the book, included in memory for completeness but likely not needed for Claude book-work continuation.

---

## 9. KEY URLS / REFERENCES
- GitHub repo (manuscript + legal drafts): `github.com/patriotnewsactivism/PDFs`
  - `corrected_manuscript_v2.txt` — manuscript master
  - `chapter_audit_findings.md` — audit findings
  - `reardon_v_osteen/objections_to_MR_draft.md` — objections draft (commit `b7f7725`)
- We The People News: `wtpnews.org` (Busby Files dossier published April 7 2026; "The Oxford Machine" Metro Narcotics investigation published April 2026)
- YouTube: `@reardonwatch1008` ("Reardon Watch" channel, hostile 2017 coverage)
- CFAPA.org — press credentials source
- AUSA Bob Norman: bob.norman@usdoj.gov
- Personal brand hub: donmatthews.live
- BuildMyBot: buildmybot.app

---

## 10. SELECTED FULL TRANSCRIPTS FROM THIS SESSION (2026-07-24 Recordings-root batches)
Below are verbatim transcripts produced during this thread's audio-transcription passes. Full recording filenames/IDs are in the sandbox JSON manifests (`recroot_batch3_list.json`, `recroot_batch4_list.json`, `recroot_batch_new_list.json`) if source files are needed again from Google Drive folder `1gJt3yv4vARMCPQnURaMdQqN2nhvpsUS5`.

### Batch — Recordings-root (10 files, includes Detective Holladay pickup, Oxford Eagle correction call, DOJ hold menu, Bridge Court/Ashley call, David O'Donnell FOIA call, WREG news call)
Key extracted facts already folded into §6 above:
- Oxford Eagle "Rachel"/Rebecca (publisher) call: correction request re: Major Alan Wilburn's May 30, 2017 libelous statements published without "allegedly."
- David O'Donnell (Busby's attorney) + associate Lisa Carwile: confirmed "no recording" of the May 24, 2017 call on tape; discussed FOIA/subpoena strategy; mentioned deputy John Hill retired ~December (year unconfirmed), witnessed the May 30, 2017 Ray Tannehill hallway incident.
- Bridge Court/"Ashley" call (Olive Branch): re: the Crowder false-rape-charge case, Judge Shoemate, scheduling a hearing.
- WREG News Channel 3 outreach call: Reardon (as "the Outlaw") attempting media outreach re: the Oxford corruption story, frustrated at being repeatedly put on hold.

*(Note: several other batches processed this session were low-value personal/customer-service calls — AT&T support, Apple ID resets, C-Spire disputes, family arguments — excluded here per the privacy/relevance rules already in memory. Full raw transcripts of every batch are recoverable via `read_session_log` on this conversation's session ID if ever needed, but are not reproduced here to keep this export focused.)*

---

## 11. MEMORY HYGIENE / OPERATING RULES (for whoever continues this work)
- Before adding new facts, check whether already documented — don't duplicate.
- Fold new findings into existing sections rather than leaving standalone dated blocks.
- When corrected, REPLACE the wrong fact in place, don't just append on top.
- Editorial framing is always the "layered thesis": real institutional misconduct AND Reardon's own escalating conduct both belong, presented honestly — never hagiography, never a hit piece.
- Two Tannehill rumors (Gunn affair, BLM-payment) are permanently excluded — zero corroboration, severe defamation risk.
- PII (credit card numbers, etc.) and one extremely graphic violent-rant recording are permanently excluded from any manuscript use.

**END OF EXPORT**
