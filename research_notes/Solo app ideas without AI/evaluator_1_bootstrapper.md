# Evaluator 1 — "the Bootstrapper": independent full-business evaluation of 15 finalists and the BASELINE

Date: 2026-10-12. Evaluator background (hypothetical persona): has built, run and sold three profitable one-person software businesses. My verification focus was build feasibility and the operating load for one person: API and payment-rail access, realistic 12-week scope, and support burden. I scored every criterion for every idea myself, using the RULEBOOK exactly.

**How to read the evidence labels**
- **CONFIRMED / CONTRADICTED / UNVERIFIABLE** — the result of my own check. All my checks came from search-engine extracts of the cited pages. My one page fetch failed (DNS error) and was not retried. So "confirmed" means "confirmed by a search extract that attributes the fact to that URL".
- **per lens N** — a fact taken from that lens file. I did not re-check it. Many lens items were themselves verified only from search extracts.
- **JUDGEMENT (unverified)** — my own expertise or background knowledge. I found no source for it this session.
- **Search budget:** I used all 15 web searches (log in section 5). I did not open any evaluator_*.md file.

**Bottom line**
- **No idea reaches BUILD (75 or more).** Three reach TEST, and only just:
  - **L3-A** Biogas evidence log: **61.0**
  - **L1-A** Vet preventive plans: **60.5**
  - **L4-F1** Care-home financing case manager: **60.5**
- **All other ideas are in the KILL band (below 60) on score.** I found **no hard-rule violation that I could prove**. Six ideas carry an "at risk" flag.
- **I score BASE lower than any lens did: 42.5.** It is a low-ticket, safety-critical consumer subscription. Its LTV/CAC is below 2. In the US, even *free* versions struggle to keep people enrolled.
  - All 15 finalists score above BASE on my numbers.
  - Three of them lead by 5 points or less, which is within evaluator noise: L2-F2, L4-F3 and L5-F3.
  - Most lenses scored BASE at 51–57.5. At 57.5, only L3-A, L1-A, L4-F1 and L3-B would still beat it.
- **What my extra searches changed.** I looked for competitors in six places the lenses called gaps. In three of them the gap shrank:
  - **CRA tooling:** a $29/month tool with Article 14 deadline tracking already exists.
  - **German butcher pre-ordering:** at least nine branded pre-order apps already exist.
  - **Boarding-stable billing:** a free all-in-one app lists billing as a feature.
  - In the other three, the gap held: practice-run vet plans in Germany, care-home-side financing software, and Romanian tools that turn cash-on-delivery orders into prepaid ones.
- **Two facts the lenses missed:**
  - Romania's RoPay is not yet broadly available to merchants.
  - Romanian buyers are being warned against "pay via link" parcel messages, which are a common phishing pattern.

---

## (1) SUMMARY TABLE

Weights: C1 10 · C2 15 · C3 10 · C4 15 · C5 15 · C6 5 · C7 10 · C8 10 · C9 5 · C10 5. Weighted score = Σ(score × weight) / 10. Verdict: ≥75 BUILD; 60–74 TEST; <60 KILL; any hard-rule violation = KILL.

| ID | Idea (short) | Hard-rule flags | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | Score | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L1-A | Vet preventive-care plans (DE) | none | 5 | 6 | 7 | 5 | 7 | 8 | 6 | 6 | 5 | 6 | **60.5** | TEST |
| L1-B | Boarding-stable billing (DE) | none (H4 at risk: free Stabley) | 5 | 4 | 4 | 4 | 5 | 6 | 7 | 4 | 8 | 6 | **49.5** | KILL |
| L1-C | Music-teacher admin (DE) | none | 4 | 4 | 5 | 5 | 5 | 5 | 8 | 4 | 8 | 6 | **51.5** | KILL |
| L2-F1 | CRA Logbook (EU, launch DE) | none (H8 at risk) | 5 | 5 | 4 | 5 | 6 | 8 | 5 | 5 | 6 | 6 | **53.0** | KILL |
| L2-F2 | CRA vault for importers (EU, launch DE) | none (H4 at risk) | 4 | 4 | 4 | 4 | 5 | 6 | 7 | 3 | 6 | 5 | **46.0** | KILL |
| L2-F3 | Battery Passport Lite (EU) | none | 6 | 6 | 4 | 4 | 7 | 4 | 3 | 7 | 3 | 6 | **52.0** | KILL |
| L3-A | Biogas substrate & EEG evidence log (DE) | none | 7 | 7 | 5 | 6 | 7 | 7 | 5 | 5 | 5 | 6 | **61.0** | TEST |
| L3-B | Parent-duty rosters, parent-run daycares (DE) | none | 5 | 4 | 5 | 7 | 6 | 4 | 8 | 5 | 8 | 7 | **58.0** | KILL |
| L3-C | Swiss condominium (STWEG) self-admin (CH) | none | 6 | 6 | 4 | 4 | 5 | 8 | 5 | 6 | 6 | 5 | **53.0** | KILL |
| L4-F1 | Care-home financing case manager (NRW) | none | 8 | 7 | 6 | 5 | 7 | 8 | 4 | 5 | 4 | 6 | **60.5** | TEST |
| L4-F2 | SBV case tool (DE) | none | 5 | 4 | 5 | 6 | 6 | 7 | 7 | 5 | 5 | 5 | **54.5** | KILL |
| L4-F3 | Tenant benefit-deadline assistant (DE) | none (H4 at risk: housing ERPs) | 5 | 4 | 4 | 4 | 5 | 8 | 5 | 3 | 5 | 4 | **45.0** | KILL |
| L5-F1 | RambursFlip, COD→prepaid (RO) | none | 7 | 7 | 5 | 6 | 5 | 5 | 5 | 4 | 6 | 6 | **56.5** | KILL |
| L5-F2 | Vorbestell-Desk, butcher pre-orders (DE) | none (H8 at risk: branded pre-order apps) | 5 | 5 | 3 | 5 | 5 | 6 | 5 | 4 | 7 | 7 | **49.5** | KILL |
| L5-F3 | WP-Wächter, heat-pump check (DE) | none (H4 at risk: maker-controlled data) | 5 | 4 | 4 | 6 | 3 | 8 | 4 | 2 | 6 | 6 | **44.5** | KILL |
| BASE | Daily check-in call, 65+ (DE) | none | 5 | 4 | 5 | 3 | 3 | 9 | 5 | 3 | 3 | 7 | **42.5** | KILL |

"At risk" means evidence, or a clearly labelled judgement, points to a specific mechanism that could cause a violation, but not enough to prove one under the rule's exact wording. Section 2 explains each case. Where the only threat is generic copying or bundling, which every SaaS faces, section 2 says "watch" and the table shows nothing.

---

## (2) PER-IDEA NOTES

### 2.0 Cross-cutting findings and the four known issues

**Cross-cutting findings**
- **Lens CACs leave out the founder's time.** For a solo founder with no network, founder-led B2B selling costs 15–40 hours per closed account. Below I report two CACs:
  - **cash CAC**: what you actually spend;
  - **loaded CAC**: cash plus founder time at €50/h (my assumption).
  
  On loaded CAC, several "LTV/CAC 10–30" claims fall to 2–5.
- **I state LTV on a gross-margin basis**, capped at 60 months: LTV = (ARPU − variable cost) × expected lifetime in months.
- **"Customers needed"** = (€8,000 + fixed costs) ÷ (ARPU − variable cost). I recomputed it for every idea.
- **German VAT.** Consumer prices include 19% VAT: €9.90 is €8.32 net, and €4.99 is €4.19 net. Business-to-business prices are net.
- **Payment fees for the founder's own billing** are JUDGEMENT (unverified): about €0.35 per SEPA debit, or about 1.5% + €0.25 per European card payment.

**(a) Boarding-stable billing: L1-B finalist (lens 1) vs killed (lens 3, "Stabley is free and includes billing"). Which is right?**
- **What I found.** I re-checked the same directory listing. It describes Stabley as:
  - a free all-in-one progressive web app for stables and riders;
  - covering boxes, scheduling, horse data, **billing** and communication;
  - with core features free for stables and riders.
  
  It says nothing about billing depth: SEPA mandates, VAT per line item, extras logging or tamper-proof invoice numbering ([AlternativeTo](https://alternativeto.net/software/stabley/about/)). My search for paid German boarding-billing software found only generic SEPA tools ([JAM SEPA-Transfer](https://www.jam-software.com/sepa-transfer/editions.shtml); [SoftGuide SEPA list](https://softguide.com/function/sepa)).
- **Verdict: both lenses are partly right; lens 3's conclusion stands, but for a different reason.**
  - Lens 1's claim "no German-language tool with boarder billing" is contradicted in its strong form.
  - Lens 3's kill is not a hard-rule kill:
    - H8 needs 3 or more funded or profitable competitors at a similar price. That is not shown.
    - H4 needs the niche's *dominant* incumbent to ship the feature free. Stabley's dominance is not shown.
  - Even so, a free app that claims billing caps willingness to pay and erodes the gap. On my scores L1-B falls to **49.5 (KILL band)**.
- **The cheapest resolver takes one hour:** sign up to Stabley and test SEPA, VAT and extras handling.

**(b) German self-managed condominium (WEG) software was killed as crowded in lenses 1, 3 and 5. Does the same logic apply to L3-C in Switzerland?**
- **Partly, and the Swiss market is heading the same way.** In Germany the kill rested on three things:
  1. A **funded** player (Dotega, €1.3m pre-seed) targets exactly small self-managed WEGs.
  2. That player holds the main consumer-association channel.
  3. Long-established tools are explicitly sold to self-managers (per lens 1 and lens 3).
- **In Switzerland I found:**
  - one direct self-admin competitor at the same price, EinfachSTWEG (CHF 30/month);
  - one tool with self-admin capability (LIMMOBI);
  - a CHF 195 Excel tool;
  - professional suites (ImmoTop2, distributed by the owners' association HEV; AbaImmo; Fairwalter; softimo). Per lens 3, plus my check: AbaImmo covers condominium communities with meetings, minutes, annual statements and renewal funds ([Abacus flyer](https://www.ABACUS.ch/fileadmin/ablage/02_dokumente/01_flyer/de/flyer_abacus_abaimmo-immobilienbewirtschaftung_de.pdf));
  - a Weka calculator for heating and ancillary-cost statements, up to 20 units ([Weka](https://www.weka.ch/bau-immobilien/immobilien/immobilienverwaltung/rechner-heiz-und-nebenkostenabrechnung-im-stockwerkeigentum.html));
  - general Swiss accounting tools with QR-bills, such as Banana and bexio (JUDGEMENT, unverified).
- **What I did not find:** a *funded* self-admin specialist, or one that holds a neutral channel. HEV's channel is held by ImmoTop2, a professional tool.
- **Conclusion:**
  - H8 is not triggered on evidence.
  - But the "absent software" premise is weak, so C3 = 4.
  - With no channel and a foreign founder, distribution is the binding constraint: C4 = 4, C10 = 5.
  - L3-C scores **53.0 (KILL band)**.

**(c) 12 of 15 finalists launch in Germany. Is each choice evidence-driven or anchored by the German baseline?**

| ID | Launch market | Evidence-driven or anchored? | Clearly better alternative? |
|---|---|---|---|
| L1-A | DE | **Evidence-driven.** Plans exist in the UK, US, NL, FR and ES but were not found in DE, and the GOT fee floor explains why (per lens 1). My search also found none in DE. | No. Keep DE; Austria and Switzerland later. |
| L1-B | DE | Mostly evidence-driven (horse population, boarding share), but the inputs date from 2001–2017. | No. |
| L1-C | DE | Evidence-driven: a localisation gap (contracts, VAT wording). | No. |
| L2-F1 | DE (EU product) | **Partly anchored.** The product is language-light and the duty is EU-wide; Germany adds only the largest C26 firm count and IHK/BSI events. | **Yes, as a go-to-market change:** launch EU-wide in English through online maker communities from day one, and use Germany only for in-person events. Scored as proposed. |
| L2-F2 | DE (EU product) | Weakly evidenced. | No. The Netherlands is equal: its government addresses importers explicitly (per lens 2). |
| L3-A | DE | **Evidence-driven:** the EEG diary is German law. | n/a |
| L3-B | DE (Berlin) | **Evidence-driven:** parent-run daycares (Elterninitiativen) are a German legal form, and DaKS gives Berlin density. | No. US co-op preschools are unresearched (JUDGEMENT). |
| L4-F1 | DE (NRW) | **Evidence-driven:** NRW pays Pflegewohngeld directly to homes and has the highest co-payments; PwC and ARD data; the US version of the problem is already served (per lens 4). | No. |
| L4-F2 | DE | **Evidence-driven:** the SBV is a German statutory institution. | n/a |
| L4-F3 | DE | **Evidence-driven:** the due-month rule is German. | n/a |
| L5-F2 | DE | **Partly anchored.** It was picked because Wero launched in Germany; market facts were not researched. Existing German butcher apps let customers pay at pickup. | Possibly the Netherlands, with its stronger habit of prepaying online (JUDGEMENT, unverified). Not clearly better on evidence. |
| L5-F3 | DE | Evidence-driven: the largest recent install base, and Daikin's API covers EMEA only (per lens 5). | UK unresearched. |
| (L2-F3) | EU (DE+NL) | An assumption about e-bike hubs. | Unknown. Polish, Portuguese and Hungarian assembly hubs are possible (JUDGEMENT). |

Net: 9 of the 12 German launches are evidence-driven and 3 are partly anchored (L2-F1, L2-F2, L5-F2). Only L2-F1 has a clearly better launch approach, and that is a go-to-market change, not a different country.

**(d) Lens 5 says L5-F2's competitor check is incomplete. What exists?**
- **At least nine German butchers already run branded pre-order apps with the same flow** (CONFIRMED via App Store listings in search results):
  - the customer picks a pickup time and branch;
  - the order prints automatically in the shop;
  - confirmation arrives in the app;
  - **payment happens at pickup.**
  
  Examples: [Metzgerei Lotter](https://apps.apple.com/app/id1508324294), [Schreder](https://apps.apple.com/app/id1482256245), [Ambros BestellApp](https://apps.apple.com/us/app/-/id1549844655), [Breidert](https://apps.apple.com/app/id1536133403), [Metzler](https://apps.apple.com/app/id1551760911), [Petermann](https://apps.apple.com/app/id1589241464), [Steinleitner](https://apps.apple.com/app/id1596895369), [Müller-Herkommer](https://apps.apple.com/de/app/app/id1538437237), [Geiger](https://apps.apple.com/de/app/metzgerei-geiger/id1532742300).
- **The identical pattern implies a white-label vendor.** I could not identify it, its price or its funding.
- **Consequence:**
  - H8 is not *proven* violated: there is no evidence of 3 or more funded or profitable vendors at a similar price.
  - But the claimed gap mostly disappears. What remains is the deposit and the WhatsApp channel: C3 = 3.
  - Point-of-sale and scale vendors with click-and-collect modules are likely too (JUDGEMENT).
- **Next cheap check:** read the "Seller" field on these App Store listings to identify the vendor and its pricing.

---

### 2.1 L1-A — Monthly preventive-care plans for independent vet practices (Germany): 60.5, TEST

**Hard-rule findings**
- **H1 pass.** A plan builder, SEPA mandates, an entitlement ledger and reminders are all deterministic.
- **H2 pass.** The 12-week MVP in lens 1 is credible. One catch: each practice needs its own payment account (GoCardless or Stripe Connect) with identity checks, so onboarding takes longer than "one afternoon" (JUDGEMENT).
- **H3 pass, conditional:**
  - Owners pay into the practice's own payment account, never the founder's.
  - A plan that prepays a fixed list of predictable services transfers no risk, so it is not insurance. Adding "x% off treatment" stays a discount (JUDGEMENT).
  - Lens 1's kill test 1 (a vet-law memo) is the right gate.
- **H4 pass.** No big-tech angle. IDEXX/Petly, Premier Vet Alliance (PVA) or practice-software vendors could enter, but they would charge for it.
- **H5 pass.** The practice pays for recurring revenue and retention.
- **H6 pass, with a design guard.** If vaccines are delivered in month 1 and paid over 12 months, the plan looks like deferred-payment credit. Entitlements must accrue as payments arrive; lens 1 already proposes this.
- **H7 pass.** Single-sided B2B.
- **H8 pass.** Lens 1's three German searches and my own search found no practice-run plan software in Germany. My search returned only pet insurers ([HUK-COBURG](https://www.huk.de/presse/nachrichten/aktuelles/huk-coburg-tierkrankenversicherung.html); [Allianz](https://www.allianz.de/angebot/kooperation/h8w65b/freizeit/tierkrankenversicherung)).

**Scores**

| C | Score | One-line justification |
|---|---|---|
| C1 | 5 | Owners face lumpy prevention bills 2–3 times a year after the ~22% fee rise (per lens 1); the practice's pain (no recurring revenue, client leakage) is chronic, not acute. |
| C2 | 6 | The practice has a direct money reason, and practices abroad pay USD 4.35–4.95 per plan (Petly, per lens 1). German owner uptake without UK-style discounts is untested, and adoption takes two steps. |
| C3 | 7 | Best proof abroad of any finalist (CVS 519k members; PVA 3,000+ practices, per lens 1). Still absent in Germany after my extra search; the GOT floor is a plausible reason. |
| C4 | 5 | ~5–6k practices can be listed and only ~52 are needed, but practices are short-staffed and every sale is founder-led, with demos and plan design. |
| C5 | 7 | ~95% gross margin; LTV ≈ €8.6k vs loaded CAC €1.5–2k (4–6×; 12–17× on cash CAC). The fee is ~10–13% of plan revenue, in line with Petly. |
| C6 | 8 | ~52 practices ≈ 1% of the pool. The independent pool is shrinking as chains consolidate (BTK trend, per lens 1). |
| C7 | 6 | The payment provider automates collection, but each practice needs plan design, payment-account onboarding and staff training. Owner questions escalate to the founder through the practice. |
| C8 | 6 | Active mandates, plan contracts and entitlement history make switching painful. IDEXX, PVA and practice-software vendors are credible entrants. |
| C9 | 5 | Exposure to the GOT, consumer-subscription law, competitors' warning letters (Abmahnungen) and the insurance boundary. Drug-pricing rules may hit bundled prescription antiparasitics (JUDGEMENT). |
| C10 | 6 | Signed LOIs from practices within 90 days are realistic; a paid deposit is harder. A legal check uses €300–1,500 of the €2k. |

**What the researcher missed**
- **Capacity.** German practices widely report a vet shortage ("Tierärztemangel"; JUDGEMENT, unverified). Many do not want more appointments, so sell predictability and retention, not "more visits".
- **Prescription-drug pricing.** Germany's drug-price rules for vet dispensing (Arzneimittelpreisverordnung) may block "member prices" on bundled prescription antiparasitics (JUDGEMENT, unverified). Lens 1 listed this as an open question but did not price it into C9. Excluding these drugs shrinks the value owners see.
- **Insurers are moving into prevention.**
  - HUK-COBURG launched dog and cat cover on 1 Oct 2026 ([HUK](https://www.huk.de/presse/nachrichten/aktuelles/huk-coburg-tierkrankenversicherung.html)).
  - Allianz says vaccinations, deworming and a one-time microchip can be insured under its surgery cover ([Allianz](https://www.allianz.de/angebot/kooperation/h8w65b/freizeit/tierkrankenversicherung)) (CONFIRMED via search extract).
  
  Prevention budgets inside insurance compete for the same owner wallet.
- **Front-desk friction.** Without integration into the practice-management system, reception staff must work in a second system. Lens 1 put integration out of scope; this is the main day-to-day adoption risk (JUDGEMENT).
- **Revenue lag.** Revenue per practice starts near zero and grows only as owners enrol. A setup fee and the €99 minimum matter for cash flow.

**Recomputed unit economics**

| Item | Value |
|---|---|
| Price | €2.50 per active plan per month, €99 minimum after ramp (lens 1). I would add a €490 one-off setup fee. |
| Realistic ARPU | €200/month at ~80 plans per practice (year-1 uptake 40–120 plans; JUDGEMENT) |
| Cost to serve | ~€10/month (reminder SMS and e-mail, hosting, PDFs, support tooling) |
| Gross margin | ~95% |
| Fixed costs | ~€1,800/month (accountant, liability and cyber insurance, legal template upkeep, travel, tools) |
| CAC by channel | Phone plus visit: cash €500–700, loaded €1,500–2,000. Vet-consultant referral (20% of first-year revenue): ≈ €480. Congress booth: €3–5k per event, yield unproven. |
| Monthly churn | ~1% (practice level) |
| LTV / LTV:CAC | ≈ €8.6k; 12–17 on cash CAC, 4–6 loaded |
| Customers for €8k profit | **≈ 52 practices** (≈ 4,100 active plans) |
| Time to get there | **~26–32 months.** Signing 2–3 practices a month from month 4 is realistic, but each practice needs 6–12 months to reach ~80 plans. Likely misses 24 months unless setup fees are charged or owner uptake is faster. |

**Top 3 risks**
1. Owners don't enrol without discounts, leaving fewer than 40 plans per practice.
2. A legal blocker (GOT, drug pricing, insurance boundary or competition law) appears after launch.
3. Slow sales into overstretched practices while IDEXX, PVA or a practice-software vendor enters.

**Cheapest 30-day money test (≤ €800)**
- Call or visit 60 independent small-animal practices in one NRW region.
- Sell a "founding practice" setup at €490, paid now and refunded if fewer than 30 owners enrol within 90 days of go-live.
- Book a one-hour paid consult with a vet-law attorney (≈ €300) on the GOT, drug pricing and the insurance boundary.
- **Pass:** at least 3 paid setups (or 5 signed LOIs with a price), and no legal blocker.

---

### 2.2 L1-B — Boarder billing, extras logging and arena booking for boarding stables (Germany): 49.5, KILL

**Hard-rule findings**
- **H1–H3 pass.** Invoices and SEPA run through the stable's own account or a pain.008 export.
- **H4 pass, at risk.** Stabley lists billing and is free ([AlternativeTo](https://alternativeto.net/software/stabley/about/)). Free organiser apps (Stall Manager, StallZeit, ReitZeit; per lens 1 and 3) could add billing. None is shown to be the *dominant* incumbent.
- **H5–H7 pass.**
- **H8 pass on evidence.** There is no evidence of 3 or more funded or profitable competitors at a similar price. See 2.0 (a).

**Scores**

| C | Score | One-line justification |
|---|---|---|
| C1 | 5 | Month-end invoicing for ~30–35 boarders plus extras is a real monthly chore; lost extras are unquantified. |
| C2 | 4 | Farm owners are price-sensitive. A free app claiming billing, generic invoicing tools and Excel cap willingness to pay. |
| C3 | 4 | "No German billing tool" is contradicted by the Stabley listing; how deep that billing goes is unknown. |
| C4 | 4 | No verified association or trade channel. Farm visits and Facebook groups; boarders spread the arena calendar but don't buy. |
| C5 | 5 | ~89% gross margin on €45 ARPU. LTV ≈ €1.3k vs loaded CAC €400–600 (2–3×; 5–9× on cash). |
| C6 | 6 | ~230 stables of ~16k operations (dated inputs). Stables with 15 or more boarders are a smaller pool, so ~3%. |
| C7 | 7 | Self-serve, with a month-end peak. VAT setup is the main support topic. |
| C8 | 4 | Free apps could add billing; invoice history gives only moderate lock-in. |
| C9 | 8 | Low liability; tax responsibility stays with the stable. |
| C10 | 6 | Prepaid founding deals with stables within 6 weeks are feasible. |

**What the researcher missed**
- **Lens 1 never checked Stabley.** Lens 3 relied on one directory line; see 2.0 (a).
- **VAT.** Horse boarding for hobby riders is generally standard-rated rather than agricultural flat-rate (JUDGEMENT; lens 1 cites a page on a related BFH ruling). That makes VAT setup support-heavy for farm stables.
- **A possible channel.** The German equestrian federation (FN) has a membership for horse businesses (JUDGEMENT, unverified).

**Recomputed unit economics**
- **Price and ARPU:** €39 or €59 per month; blended ARPU €45.
- **Cost to serve:** €5 including support time. Gross margin 89%.
- **Fixed costs:** €1,200/month.
- **CAC by channel:**
  - phone and visits: cash €150–250, loaded €400–600;
  - Facebook groups: €50–150 (unproven).
- **Churn:** 2.25%/month. LTV ≈ €1,320; LTV/CAC 5.3–8.8 on cash, 2.2–3.3 loaded.
- **Customers needed:** ≈ 230 stables.
- **Time:** ~24–30 months at 8–10 net additions a month, so borderline for the 24-month goal.

**Top 3 risks**
1. Stabley's free billing is good enough.
2. Farm owners don't value the time saved.
3. There is no scalable channel.

**Cheapest 30-day money test (≤ €300)**
1. First, spend an hour inside Stabley testing SEPA mandates, VAT per line, extras logging and invoice numbering. If it covers these, stop.
2. If not, call 100 stables with 20 or more boarders and sell a €390 annual prepay ("3 months free"). **Pass:** at least 5 prepaid.

---

### 2.3 L1-C — Lesson contracts, make-ups and SEPA billing for private music teachers (Germany): 51.5, KILL

**Hard-rule findings**
- **H1–H7 pass.**
- **H8 pass on evidence.** Lens 1 found no German-language tool for solo teachers. Whether My Music Staff or TutorBird offer German was not verified. Music-school administration tools exist (JUDGEMENT), but they serve schools rather than solo teachers.

**Scores**

| C | Score | One-line justification |
|---|---|---|
| C1 | 4 | Weekly but modest admin; standing orders already cover much of the payment side. |
| C2 | 4 | Cost-sensitive freelancers with a ~€12/month ceiling; German willingness to pay is unproven. |
| C3 | 5 | The localisation gap is plausible, but the North American leaders could add German quickly. |
| C4 | 5 | Teacher groups, SEO and the Deutscher Tonkünstlerverband (the freelance music-teacher association; JUDGEMENT) are named but unvalidated. |
| C5 | 5 | ~90% gross margin, but blended ARPU is only €15 and churn ~3.5%, so LTV ≈ €340 (4–9× on cash; 2–4× loaded). |
| C6 | 5 | ~670 customers ≈ 2.7% of a derived pool of ~25k. |
| C7 | 8 | Fully self-serve with light operations; September peak. |
| C8 | 4 | Low switching costs; incumbents can localise. |
| C9 | 8 | Low risk (GDPR for minors' data). |
| C10 | 6 | Founding-member annual pre-sales within 60 days are feasible. |

**What the researcher missed**
- **A named channel.** The Deutscher Tonkünstlerverband (JUDGEMENT).
- **A shrinking freelancer pool.** After the 2022 Federal Social Court "Herrenberg" ruling, many music schools moved freelance teachers into employment (JUDGEMENT, unverified).
- **The real hook is the make-up rules engine, not billing.** Most private teachers bill few families and are content with standing orders.

**Recomputed unit economics**
- **Price and ARPU:** €12 solo or €49 studio; blended ARPU €15.
- **Cost to serve:** €1.50 (each charge's payment fee ≈ €0.35–0.45, plus hosting). Gross margin 90%.
- **Fixed costs:** €1,000/month.
- **CAC by channel:**
  - SEO and content: €40–80;
  - teacher Facebook groups: €20–50;
  - paid social: €80–150.
- **Churn:** 3.5%/month. LTV ≈ €340; LTV/CAC 4.3–8.5 on cash.
- **Customers needed:** ≈ 670.
- **Time:** 30+ months, because SEO takes time to ramp and churn erodes the base. Misses the 24-month goal.

**Top 3 risks**
1. Low willingness to pay.
2. My Music Staff or TutorBird localise into German.
3. High churn among part-time teachers.

**Cheapest 30-day money test (≤ €400)**
- Put up a German landing page.
- Promote it with €300 of ads plus posts in teacher groups.
- Sell a €99/year founding plan.
- **Pass:** at least 30 pre-sales.

---

### 2.4 L2-F1 — CRA Logbook for micro hardware/IoT makers (EU, launch Germany): 53.0, KILL

**Hard-rule findings**
- **H1 pass.** Identifier matching, timers and templates.
- **H2 pass, with a caveat.** Many micro makers have no SBOM for their C/C++ firmware, and generating one needs binary-analysis tooling (JUDGEMENT). For those customers the MVP falls back to manual component entry.
- **H3 pass.** The tool keeps records, clocks and templates; it gives no legal advice.
- **H4 pass.** ENISA's reporting platform offers manufacturers **no API "at this stage"**: reports are typed into a web portal behind EU Login with MFA ([CSA research note](https://labs.cloudsecurityalliance.org/research/csa-research-note-enisa-cra-reporting-platform-20260918-csa/); [cyberresilienceact.eu guide](https://www.cyberresilienceact.eu/news/enisa-srp-step-by-step-instructions-31-july-2026.html)). So there is no gatekeeper integration to lose.
- **H5–H7 pass.**
- **H8 pass on evidence, but the market is filling fast:**
  - CRALedger Duty Records has a free tier and a **$29/month** Starter plan. It tracks product roles, checklists and **Article 14 reporting deadlines**, and gives no legal advice ([pickyourapp](https://pickyourapp.com/products/craledger-duty-records)).
  - CRA Evidence by Senda Tech ([GetApp AU](https://www.getapp.com.au/software/2141675/cra-evidence)).
  - CRA Gap Finder ([SoftwareAdvice UK](https://www.softwareadvice.co.uk/software/773157/Cyber-Resilience-Act-Gap-Finder)).
  - EU-funded tools for micro firms: ATHENA ([CORDIS](https://cordis.europa.eu/project/id/101225583)) and the CRACoWi assistant ([Hannover Messe](https://www.hannovermesse.de/product/eu-funded-cybersecurity-assistant/511395/N1483015)).
  - sbomify (per lens 2).
  
  None is shown to be funded or clearly profitable, so H8 is not triggered.

**Scores**

| C | Score | One-line justification |
|---|---|---|
| C1 | 5 | The 24 h/72 h reporting duty is live, but exploited-vulnerability events are rare and micro/small firms are not fined for missing the 24 h warning (per lens 2). The heavy part is a one-off push before Dec 2027. |
| C2 | 5 | The manufacturer pays to keep EU market access, but the low end is now anchored at $29/month and free public tools. |
| C3 | 4 | Lens 2's "only sbomify at a similar price" no longer holds: at least three micro-priced CRA tools plus EU-funded assistants exist. |
| C4 | 5 | Named channels (embedded communities, IHK/BSI events, CE consultants, trade-fair exhibitor lists), but every new CRA vendor works the same ones. |
| C5 | 6 | ~92% gross margin. Realistic ARPU ~€60 gives LTV ≈ €1.9k vs CAC €250–900 (2–8×). |
| C6 | 8 | ~180 customers ≈ 2% of Germany's 7,860 C26 firms (per lens 2); less of an EU pool. |
| C7 | 5 | Wrong matches (false positives and negatives) and "is my product Class I?" questions create support load; standards and implementing acts will change templates. |
| C8 | 5 | Ten-year records help retention; cheap rivals, free EU tools and platform alerts erode it. |
| C9 | 6 | A missed match could make a customer miss a deadline; disclaimers and the micro/small exemption soften this. |
| C10 | 6 | €490 founding pre-sales to makers preparing for Dec 2027 are plausible within 90 days. |

**What the researcher missed**
- **The competitor set above and the $29 price anchor.**
- **The planned reporting-platform API connects national CERTs, not manufacturers** (commentator quoted in search extracts). Automation stops where a person types into a browser.
- **Conflicting launch status.** The CSA note says the platform went live on 11 Sep 2026. An undated advisori.de page says it was not yet live, which is probably a pre-launch page ([advisori](https://www.advisori.de/blog/cra-single-reporting-platform-srp-registration)).
- **Firmware SBOMs are the hard part for hardware makers** (JUDGEMENT).

**Recomputed unit economics**
- **Price and ARPU:** list €49/€99/€199 (lens 2); realistic ARPU €60.
- **Cost to serve:** €5. Gross margin 92%.
- **Fixed costs:** €1,900/month.
- **CAC by channel:**
  - open-source lead magnet plus content: cash €100–250;
  - IHK or consultant webinars: €250–400;
  - trade fairs: €600–900 loaded.
- **Churn:** 2%/month. LTV ≈ €1.9k; LTV/CAC 4.8–7.7 on cash, 2.1–3.2 loaded.
- **Customers needed:** ≈ 180.
- **Time:** about 15–24 months, and only if the pre-December-2027 demand wave arrives and ARPU stays above €50. After Dec 2027, expect a plateau and churn.

**Top 3 risks**
1. A price war with micro tools and free EU-funded assistants.
2. Demand clustered before the Dec 2027 deadline, followed by churn.
3. The deadline slips or the rule is simplified (the EU has done this before, per lens 2).

**Cheapest 30-day money test (≤ €500)**
- Publish the free CLI.
- E-mail 200 makers, drawn from Tindie and Crowd Supply sellers and embedded-world exhibitors.
- Sell a €490/year founding plan that includes a two-hour readiness session.
- **Pass:** at least 5 prepaid.

**Launch market:** see 2.0 (c). Sell EU-wide in English from day one.

---

### 2.5 L2-F2 — CRA compliance vault for small importers/distributors (EU, launch Germany): 46.0, KILL

**Hard-rule findings**
- **H1–H3 pass.** Checks that documents are present, storage and reminders.
- **H4 pass, at risk.** Germany's dominant e-commerce legal-compliance providers already sell monthly compliance packages to shops (for example Händlerbund, IT-Recht Kanzlei and Trusted Shops; JUDGEMENT, unverified). They could add a CRA document checklist cheaply.
- **H5–H7 pass.**
- **H8 pass on evidence.** Lens 2 found no priced per-SKU CRA vault.

**Scores**

| C | Score | One-line justification |
|---|---|---|
| C1 | 4 | A real per-SKU chore, but binding only from 11 Dec 2027. |
| C2 | 4 | Shop owners pay, but awareness is low and the duty is 14 months away. |
| C3 | 4 | Thin evidence of a gap; GPSR and legal-text services sit next door. |
| C4 | 4 | Agencies, IHK webinars and shop communities: plausible but unvalidated. |
| C5 | 5 | ~91% gross margin. ARPU ~€45 gives LTV ≈ €1.3k vs CAC €150–600. |
| C6 | 6 | ~240 customers ≈ 2% of an unverified pool of 10k or more. |
| C7 | 7 | Simple records, reminders and exports. |
| C8 | 3 | An easy add-on for legal-text providers and GPSR services. |
| C9 | 6 | Risk of false comfort; needs a "checks presence, not authenticity" disclaimer. |
| C10 | 5 | LOIs are possible; real pre-sales this early are hard. |

**What the researcher missed**
- **The natural owners of this workflow** are the German legal-compliance services (JUDGEMENT).
- **All the value hangs on one date** that an EU simplification could move (per lens 2's precedents).
- **Overlap with L2-F1.** Importers that sell under their own brand become manufacturers (Art. 21; unverified in lens 2), so this should be combined with L2-F1 rather than run as a separate product.

**Recomputed unit economics**
- **ARPU:** €45. **Cost to serve:** €4. Gross margin 91%.
- **Fixed costs:** €1,900/month.
- **CAC by channel:**
  - agency revenue share: €150–300;
  - IHK webinars: €200–400.
- **Churn:** 2.5%/month. LTV ≈ €1.3k; LTV/CAC 4.3–8.5 on cash, 2.1–3.2 loaded.
- **Customers needed:** ≈ 240.
- **Time:** demand only appears in the second half of 2027, so €8k profit is unlikely before month 24–30.

**Top 3 risks**
1. Incumbents bundle the feature.
2. The deadline is postponed.
3. Awareness stays low.

**Cheapest 30-day money test (≤ €300)**
- Pitch 10 e-commerce agencies on a 20% revenue share.
- Offer €290/year founding seats to 200 shops.
- **Pass:** at least 5 prepaid. Expect this to fail, which lets you kill the idea fast.

---

### 2.6 L2-F3 — Battery Passport Lite for small LMT and industrial battery assemblers (EU): 52.0, KILL

**Hard-rule findings**
- **H1 pass.**
- **H2 pass, with risk.** A hosted ID + QR + record MVP is buildable. The data model must still track Annex XIII and standards that are still changing.
- **H3 pass.** No listed licence category applies.
- **H4 pass (watch).** Cell, pack or system suppliers could bundle passports (JUDGEMENT; no evidence either way).
- **H5–H7 pass.**
- **H8 pass on evidence only.** Passport vendors exist (Scantrust, Circuland, dpp-tool, Tracepas per lens 2). Funded enterprise players exist too (Circulor, Circularise, Minespider; JUDGEMENT). No SME pricing was found, so "a similar price" cannot be shown.

**Scores**

| C | Score | One-line justification |
|---|---|---|
| C1 | 6 | A hard market-access gate from 18 Feb 2027 for every battery (per lens 2). |
| C2 | 6 | The assembler pays, and a per-battery fee is tiny next to a pack's value. |
| C3 | 4 | Several vendors exist, and the big e-bike system suppliers will likely issue passports for their own packs (JUDGEMENT), so the "small finisher" gap is narrow. |
| C4 | 4 | Niche workshops and trade fairs; no verified cheap channel. |
| C5 | 7 | ~89% gross margin and low churn. LTV ≈ €7.6k vs CAC €600–2,500. |
| C6 | 4 | ~66 customers of an unverified pool of 1–3k (2–6%). |
| C7 | 3 | Changing standards plus a duty to keep passports available for years (JUDGEMENT: availability may have to outlast the operator) is the wrong shape for one person. |
| C8 | 7 | Once passports are issued, switching is painful. |
| C9 | 3 | Customers' market access depends on a solo founder's uptime and solvency. |
| C10 | 6 | The deadline 4 months away makes pre-sales possible, but buyers will hesitate to trust a one-person vendor. |

**What the researcher missed**
- **Who actually "finishes" e-bike batteries.** Most packs come from big system suppliers such as Bosch, Shimano, Yamaha and Bafang (JUDGEMENT), who will issue their own passports. Small DE/NL workshops are mostly re-cellers. Their remanufactured batteries need new passports linked to the original, which is a smaller and messier niche.
- **Continuity escrow is mandatory for a solo vendor, not optional** (JUDGEMENT).
- **An unsized segment.** Industrial batteries over 2 kWh include stationary storage (JUDGEMENT), so small storage integrators may be a larger pool.

**Recomputed unit economics**
- **Price and ARPU:** €99/month + €0.40 per passport; ARPU €180.
- **Cost to serve:** €20 (redundant hosting, escrow, share of insurance). Gross margin 89%.
- **Fixed costs:** €2,500/month.
- **CAC by channel:**
  - trade fairs: €1,500–2,500 loaded;
  - direct outreach: €600–1,000 cash.
- **Churn:** 0.8%/month. LTV ≈ €7.6k; LTV/CAC 7.6–12.7 on cash, 3.1–5.1 loaded.
- **Customers needed:** ≈ 66.
- **Time:** 18–30 months, and the pool is unverified.

**Top 3 risks**
1. Continuity and liability exposure.
2. Standards keep changing.
3. System suppliers or large vendors give passports away.

**Cheapest 30-day money test (≤ €800)**
- Run a "4 months to go" webinar.
- Reach out to 100 re-cellers, LMT brands and storage integrators.
- Sell a €990/year founding plan with an escrow clause.
- **Pass:** at least 3 prepaid.

---

### 2.7 L3-A — Audit-ready substrate and EEG-bonus evidence log for biogas plants (Germany): 61.0, TEST

**Hard-rule findings**
- **H1 pass.** No OCR, by design.
- **H2 pass.** Web app or PWA with CSV imports.
- **H3 pass.** The environmental verifier certifies; the app only keeps records.
- **H4 pass.** No single gatekeeper; feeding-controller vendors are fragmented.
- **H5–H7 pass.**
- **H8 pass on evidence.** Three young vendors exist (Nabisy Software, TerraVis, Biotaktix); their funding and profitability are unknown (per lens 3).

**Scores**

| C | Score | One-line justification |
|---|---|---|
| C1 | 7 | Daily logging plus a hard 28 Feb deadline; a lapsed bonus is lost for good (per lens 3). |
| C2 | 7 | The payer is the sufferer. An average plant makes ~3.1 GWh a year and already pays verifiers (one anecdote: €15k a year), so €790–1,190 a year is small. |
| C3 | 5 | Excel is still standard, but three vendors appeared in 2024–26; the window is closing. |
| C4 | 6 | Environmental verifiers are a small, listable group whose clients are exactly these plants. FvB regional groups and farm trade press are cheap and named. Being an outsider is the hurdle. |
| C5 | 7 | ~90% gross margin. At €99/month, LTV ≈ €3.9k vs loaded CAC €0.8–1.2k (3–5×; 8–13× on cash). At €66 the loaded ratio drops to 2–3×, so raise the price. |
| C6 | 7 | ~107–163 plants ≈ 1–2% of 9,605, but the bonus-relevant pool shrinks as older EEG plants reach the end of their terms. |
| C7 | 5 | Rule tables per EEG version, a CSV import per feeding-controller vendor, farmers who prefer the phone, and a January–February support spike. |
| C8 | 5 | One season of data creates switching cost, but "no OCR, no hardware" is easy to copy. |
| C9 | 5 | A wrong evidence pack could cost a bonus. This is insurable, and the verifier stays the certifier. |
| C10 | 6 | Prepaid founding plants through verifiers before the deadline season are plausible. |

**What the researcher missed**
- **The pool is shrinking and the rules are shifting.** Plants under the EEG 2004 and 2009 bonus rules are reaching the end of their 20-year terms from the mid-2020s (JUDGEMENT). Plants that move into tenders still keep a substrate diary to prove the maize cap (JUDGEMENT). So sell "the diary for tenders and flexibility rules", not only "EEG 2009 bonus proof".
- **Build and operating load.** Each feeding-controller vendor has its own CSV export, so imports need one mapping per vendor (JUDGEMENT).
- **Pricing.** Lens 3's €790 a year is too low for the stakes. At €1,190 a year, the customers needed fall to ~107.

**Recomputed unit economics**

| Item | Value |
|---|---|
| Price | €790/year (lens 3). I recommend €1,190/year (€99/month) with a founding discount. |
| Cost to serve | €6–7/month (hosting, backups, payment fees, support tooling) |
| Gross margin | 91–93% |
| Fixed costs | €1,800/month (incl. professional liability insurance) |
| CAC by channel | Verifier referral (20% of first-year revenue ≈ €160–240) plus travel: cash €300–500. FvB regional meetings and events: €400–800. Loaded: €800–1,200. |
| Monthly churn | 1–1.5% (incl. plants leaving the EEG) |
| LTV / LTV:CAC | ≈ €2.5k at €66, or ≈ €3.9k at €99. 5–13× on cash; 2–5× loaded. |
| Customers for €8k profit | **≈ 163 at €66, or ≈ 107 at €99** |
| Time to get there | Sales concentrate in October–February. At €99: ~18–22 months, after two selling seasons. At €66: ~28–30 months. |

**Top 3 risks**
1. One of the three existing vendors wins the verifier channel first.
2. Operators stay with Excel plus their verifier.
3. Rules across EEG versions become too complex for one person to maintain.

**Cheapest 30-day money test (≤ €600)**
1. Get the public list of environmental verifiers active in biogas and call 20 of them.
2. Offer each a free reviewer portal and an export format designed with them. Ask for 2–3 introductions to plants.
3. Sell a "Saison 2027" founding plan at €590 prepaid, including a free import of last year's Excel diary.
4. **Pass:** at least 2 verifier partners and at least 5 prepaid plants within 30 days.

---

### 2.8 L3-B — Parent-duty rosters, hours ledger and board handover for parent-run daycares (Germany, Berlin first): 58.0, KILL

**Hard-rule findings**
- **H1–H7 pass.** No child data is stored, parents consent, and the association pays.
- **H4 note.** Free generic tools (Doodle, Spond, WhatsApp) and daycare apps could add rosters. None is a dominant free incumbent for this specific workflow on the evidence.
- **H8 pass.** No product selling this workflow was found (per lens 3).

**Scores**

| C | Score | One-line justification |
|---|---|---|
| C1 | 5 | Weekly duty coordination plus board handovers; intensity is evidenced only indirectly. |
| C2 | 4 | Associations have small budgets and free tools anchor prices low. €49 a month is a stretch for initiatives with 15–25 children; €29–39 is realistic (JUDGEMENT). |
| C3 | 5 | No product for this workflow found. Daycare apps target staff-run centres; whether they include parent-duty rosters was not checked (JUDGEMENT). |
| C4 | 7 | DaKS (~800 Berlin initiatives) and the 29 member organisations of BAGE give a dense, cheap channel. |
| C5 | 6 | ~87% gross margin. LTV ≈ €1.2k vs CAC €100–400. |
| C6 | 4 | ~280 associations ≈ 4–6% of the 5–7.5k pool. |
| C7 | 8 | Simple domain, low data risk, light support. |
| C8 | 5 | Copyable; the handover vault adds some stickiness. |
| C9 | 8 | Low liability. |
| C10 | 7 | Berlin's density makes paid pilots within weeks plausible. |

**What the researcher missed**
- **Daycare apps may already have duty rosters** (JUDGEMENT).
- **Boards change every 1–2 years,** so each customer has to be re-sold to the next board.
- **Berlin alone is too small:** even 10% of DaKS's ~800 facilities is only ~80 customers. Several cities are needed.

**Recomputed unit economics**
- **Price and ARPU:** list €49; realistic €39.
- **Cost to serve:** €5. Gross margin 87%.
- **Fixed costs:** €1,500/month.
- **CAC by channel:** DaKS workshops and newsletters, €100–200 cash or €250–400 loaded.
- **Churn:** 2%/month. LTV ≈ €1.2k; LTV/CAC 6–12 on cash, 3–5 loaded.
- **Customers needed:** ≈ 280.
- **Time:** 30–36 months, because it needs several cities. Misses the 24-month goal.

**Top 3 risks**
1. Free tools are good enough.
2. The share of the pool needed is too high.
3. Daycare apps add rosters.

**Cheapest 30-day money test (≤ €200)**
- Offer DaKS a free board workshop, "Elterndienste ohne Chaos".
- Sell a €290/year founding plan.
- **Pass:** at least 5 boards prepay.

---

### 2.9 L3-C — Self-administration for small Swiss condominium communities: 53.0, KILL

**Hard-rule findings**
- **H1 pass.**
- **H2 pass.** The QR-bill is the Swiss standard, and banks offer QR-IBAN payment slips for condominium accounts. The ZKB account-opening form for these communities lists QR-IBAN payment slips as an option for the administration ([ZKB form](https://www.zkb.ch/media/zkb/dokumente/formulare/Formular_Er%C3%B6ffnungsantrag_20STWEG_11_23.pdf); CONFIRMED). Matching payments by QR reference from bank notification files (camt.054) is deterministic. Open-source QR-bill libraries exist, but bank file formats vary (JUDGEMENT).
- **H3 pass.** Software only, and owners pay into the community's account. No Swiss licence applies to software (JUDGEMENT).
- **H4 pass.** Banks' QR tools and general accounting tools overlap only partly.
- **H5–H7 pass.**
- **H8 pass on evidence.** See 2.0 (b).

**Scores**

| C | Score | One-line justification |
|---|---|---|
| C1 | 6 | Monthly billing, annual accounts and meetings; administrators turn down small mandates (NZZ, per lens 3). |
| C2 | 6 | Owners are both payers and sufferers, and a CHF 30/month price anchor exists. |
| C3 | 4 | Several young tools, professional suites and general accounting already cover it; the gap is being filled. |
| C4 | 4 | No neutral channel (HEV distributes ImmoTop2). SEO for "STWEG selbst verwalten" is slow but compounding; Swiss ads are expensive. |
| C5 | 5 | ~84% gross margin. LTV ≈ €1.4k vs CAC €250–900 (1.6–5.6×). |
| C6 | 8 | ~340 communities ≈ 0.35% of ~97k (derived), or ~1–2% of the self-administered share. |
| C7 | 5 | Bank-file variants, cost-key edge cases, three languages and a January–April peak. |
| C8 | 6 | Once adopted, multi-year ledgers make switching painful. |
| C9 | 6 | Bookkeeping errors turn into neighbour disputes; no licence needed. |
| C10 | 5 | An unknown foreign founder in a trust-sensitive market: LOIs are feasible, prepayment is slower. |

**What the researcher missed**
- **Substitutes.** Banana and bexio (JUDGEMENT), and AbaImmo (CONFIRMED) for professionally run communities.
- **Swiss VAT.** Foreign providers of electronic services must register for Swiss VAT once worldwide turnover passes CHF 100k (JUDGEMENT). Lens 3 also flagged this as unverified.
- **A possibly less contested segment.** The French-speaking market (PPE, Romandie) (JUDGEMENT).
- **Local expectations.** Users expect Swiss hosting and Swiss-German support (JUDGEMENT).

**Recomputed unit economics**
- **Price:** CHF 35/month (≈ €37).
- **Cost to serve:** €6. Gross margin 84%.
- **Fixed costs:** €2,500/month (native-speaker support freelancer, VAT, insurance, base ad budget).
- **CAC by channel:**
  - SEO and free templates: €150–250 after 9–12 months;
  - Google Ads in CH: €400–800;
  - insurer or notary content partnerships: unproven.
- **Churn:** 1%/month. LTV ≈ €1.4k; LTV/CAC 2.3–5.6 on cash, 1.6–2.8 loaded.
- **Customers needed:** ≈ 340.
- **Time:** 28–36 months, because SEO takes time to ramp. Misses the 24-month goal.

**Top 3 risks**
1. EinfachSTWEG and others win the SEO terms first.
2. CAC is too high without a channel.
3. Support in three languages.

**Cheapest 30-day money test (≈ €1,100)**
- Publish 5 free German templates.
- Spend CHF 800 on Google Ads for "STWEG selbst verwalten" and "Stockwerkeigentum Buchhaltung".
- Run discovery calls and sell a CHF 290 founding first year.
- **Pass:** at least 5 prepaid.

---

### 2.10 L4-F1 — Care-home financing case manager for Hilfe zur Pflege and Pflegewohngeld (NRW; the care home pays): 60.5, TEST

**Hard-rule findings**
- **H1 pass.**
- **H2 pass.** A case file, checklist rules, a family portal and the top NRW forms are credible in 12 weeks. Covering every local office's forms takes longer: NRW has 31 districts and 22 district-free cities, each with its own office (JUDGEMENT).
- **H3 pass, conditional:**
  - Preparing applications for third parties raises the Legal Services Act (RDG) question. In 2021 the Federal Court of Justice held that a rule-based contract-document generator is not a legal service (BGH "Smartlaw", I ZR 113/20; JUDGEMENT, background knowledge).
  - The founder must never submit documents or collect claims for homes, which would need a debt-collection licence.
  - Lens 4's counsel check (KT5) is mandatory.
- **H4 pass (watch).** Myosotis is funded and has 400+ care-home customers for its relatives app (per lens 4), so it could bundle this. Care-home ERPs could add the feature (unverified).
- **H5 pass.** The home has a quantified money reason (PwC 2026, per lens 4).
- **H6 pass.** No success fees, and the family portal is consent-based.
- **H7 pass.**
- **H8 pass.** No home-side tool was found by lens 4 or by my search, which returned only process guidance ([betanet](https://www.betanet.de/hilfe-zur-pflege.html); [RBK FAQ](https://www.rbk-direkt.de/download/429/hilfe-zur-pflege-in-einem-pflegeheim---fragen-und-antworten)).

**Scores**

| C | Score | One-line justification |
|---|---|---|
| C1 | 8 | €3.1–3.4k a month pre-financed per case, and 6–12+ month decisions (per lens 4). One guide advises planning about two months just to gather the documents (CONFIRMED via search extract). |
| C2 | 7 | A clear payer with quantified receivables pain, and homes already buy factoring and billing services. There is no proof yet that they will pay for this tool. |
| C3 | 6 | No home-side product found by two lenses or by me. ERP features are unchecked, and part of the delay is office capacity that software cannot fix. |
| C4 | 5 | Public home directories and associations exist, but selling is founder-led outbound, and non-profit and chain homes buy centrally. |
| C5 | 7 | ~90% gross margin. LTV ≈ €6.9k vs CAC €0.5–3k (2.3–3.5× loaded; 9–14× on cash). |
| C6 | 8 | ~63 homes ≈ 0.6% of 11,250 long-term-care homes, or ~3% if NRW only. |
| C7 | 4 | Stressed, non-technical relatives (2–4 tickets per home per month, per lens 4), continuous upkeep of a form library across dozens of offices, and the security work that health data under GDPR Art. 9 demands. |
| C8 | 5 | Case history creates switching costs, but Myosotis, ERPs and care-financing reforms threaten. |
| C9 | 4 | Special-category data about vulnerable people, the open RDG question, and liability for lost benefit months. |
| C10 | 6 | €99 paid pilots or priced LOIs within 90 days are plausible; data-protection reviews slow some homes. |

**What the researcher missed**
- **The strongest single feature is legally grounded.** A 2024 ruling of the Baden-Württemberg state social court (L 7 SO 2479/23) held that even an incomplete application establishes the date from which the office knows about the need (CONFIRMED via search extract; the source page is probably [gegen-hartz](https://www.gegen-hartz.de/urteile/sozialhilfe-formloser-antrag-sichert-anspruch-auf-hilfe-zur-pflege)). That makes "secure the date on day one" the product's strongest single value.
- **Online filing is limited:**
  - The Berlin service entry offers online filing only for home-care (ambulant) cases, with upload limits of 85 MB in total and 3 MB per file ([fimportal](https://fimportal.de/api/v0/xzufi-services/L100108/L100108_324474/de/pdf)).
  - Care-home cases still go on paper, so printed, signed forms remain the delivery format.
- **Processing times vary widely by district** ([Landtag BW 17/9244](https://www.landtag-bw.de/resource/blob/585070/cf26fb5af1795d9bc21e527dfa3bf5bd/17_9244_D.pdf)).
- **Relatives' support load is the real cost for a solo founder** (scaled up from lens 4's own ticket estimate).
- **A breach of residents' financial and care data would be existential** for a one-person company.

**Recomputed unit economics**

| Item | Value |
|---|---|
| Price | €179/month average (€129–249 by beds) |
| Cost to serve | €18/month |
| Gross margin | 90% |
| Fixed costs | €2,200/month (data-protection officer and legal, security, insurance, travel) |
| CAC by channel | Outbound plus two visits: cash €500–800, loaded €2,000–3,000 (25–40 hours incl. data-protection paperwork). Factoring or consultancy referral (20% of first-year revenue): ≈ €430. |
| Monthly churn | 1.2% |
| LTV / LTV:CAC | ≈ €6.9k; 8.6–13.8 on cash, 2.3–3.5 loaded |
| Customers for €8k profit | **≈ 63 homes** |
| Time to get there | ~20–28 months (2–4 homes a month after the pilots) |

**Top 3 risks**
1. Support and security load overwhelms one person.
2. Myosotis or an ERP vendor bundles a home-side workflow.
3. Homes won't pay because they blame the offices for delays, or a reform shrinks caseloads.

**Cheapest 30-day money test (≤ €1,000)**
- Build a list of 150 independent NRW homes, from operators with 1–3 homes.
- Run outreach with a self-check of open items with the Sozialamt, based on the PwC figures.
- Offer a 3-month paid pilot at €99/month, prepaid (€297).
- Pay counsel ~€500 for a one-hour read on the RDG and GDPR model.
- **Pass:** at least 3 paid pilots, or at least 5 LOIs with a price.

---

### 2.11 L4-F2 — Case tool for the workplace representative for disabled employees (SBV) (Germany; the employer pays): 54.5, KILL

**Hard-rule findings**
- **H1, H2 pass.**
- **H3 pass, conditional.** Objection-letter templates are document generation (JUDGEMENT, following the Smartlaw logic).
- **H4 pass on evidence.** Works-council software was not verified.
- **H5 pass, with a concern.**
  - The employer must bear the SBV's necessary costs (§179(8) SGB IX, per lens 4), and savings on the quota levy give it a money reason.
  - But "necessity" can be disputed, and confidentiality means the employer cannot see the value.
- **H6 pass.** The architecture gives the employer no access.
- **H7, H8 pass.**

**Scores**

| C | Score | One-line justification |
|---|---|---|
| C1 | 5 | Real but episodic for each employee; the SBV's own pain is moderate. |
| C2 | 4 | The decision-maker (the SBV) is not the payer, and every purchase needs employer approval. |
| C3 | 5 | No SBV-specific product found; works-council suites unchecked. Many SBVs handle few cases a year (JUDGEMENT). |
| C4 | 6 | The Oct–Nov 2026 election wave, seminar providers and public-sector SBV web pages. |
| C5 | 6 | ~90% gross margin, but €39 ARPU, plus invoicing friction with employers. Public employers require e-invoices (JUDGEMENT). |
| C6 | 7 | ~266 of an assumed 20–40k SBVs; the pool size is unverified. |
| C7 | 7 | Simple case management; the deadline engine needs legal review. |
| C8 | 5 | Works-council suites could add a module; 4-year terms help retention. |
| C9 | 5 | Health data and employer pressure, handled by the architecture; deadline-calculation errors remain a risk. |
| C10 | 5 | Employer approval slows real money signals. |

**What the researcher missed**
- **Seminar providers control access** to new SBVs and could become competitors.
- **Invoicing public-sector employers requires e-invoices** (JUDGEMENT).
- **Active cases per SBV may be few,** so the value per SBV could be thin.

**Recomputed unit economics**
- **Price:** €39/month (€468/year).
- **Cost to serve:** €4. Gross margin 90%.
- **Fixed costs:** €1,300/month.
- **CAC by channel:**
  - seminar affiliates at 20% (≈ €94) plus content: €80–200 cash;
  - loaded: €250–400.
- **Churn:** 1.2%/month. LTV ≈ €1.5k; LTV/CAC 7.5–19 on cash, 3.8–6 loaded.
- **Customers needed:** ≈ 266.
- **Time:** 20–30 months, slowed by purchase approvals.

**Top 3 risks**
1. Employers refuse to accept the tool as "necessary".
2. Low case volume per SBV.
3. Works-council suites bundle an SBV module.

**Cheapest 30-day money test (≤ €300)**
- Send a starter pack to 300 newly elected public-sector SBVs.
- Sell at €468/year, with a ready-made §179(8) cost-request letter to the employer.
- **Pass:** at least 3 employer-paid invoices or purchase orders. Allow 60–90 days rather than 30.

---

### 2.12 L4-F3 — Tenant benefit-deadline assistant (Germany; the landlord pays): 45.0, KILL

**Hard-rule findings**
- **H1, H2 pass.**
- **H3 pass, conditional.** General information plus a letter template; needs an RDG check.
- **H4 pass, at risk.** Housing ERP vendors, the niche's dominant incumbents (e.g., Aareon; unverified, per lens 4), can add a notice and QR code cheaply.
- **H5 pass,** but the landlord's money reason is unquantified.
- **H6 pass.** Tenants opt in; the landlord sees confirmations only.
- **H7, H8 pass.**

**Scores**

| C | Score | One-line justification |
|---|---|---|
| C1 | 5 | ~€900 a year at stake per affected tenant, but the miss rate is unknown. |
| C2 | 4 | The landlord's loss is unquantified, and social-management teams already exist. |
| C3 | 4 | Only one search was run, and a printed notice is a near-free substitute. |
| C4 | 4 | Slow, committee-driven B2B sales. |
| C5 | 5 | High gross margin, but €2.5–4k CAC and long cycles give 3–5× on cash. |
| C6 | 8 | ~35 companies needed. |
| C7 | 5 | Rule churn after the July 2026 reform, and hundreds of office addresses to maintain. |
| C8 | 3 | ERP vendors can copy it, and the rules are volatile. |
| C9 | 5 | RDG question and sensitive social data. |
| C10 | 4 | Utility statements are seasonal, so proof takes time. |

**What the researcher missed**
- **A paragraph on the utility statement is the near-free substitute** (JUDGEMENT).
- **Courts are already reinterpreting the reform** (per lens 4), so rule upkeep will be heavy.

**Recomputed unit economics**
- **Price and ARPU:** €0.08 per unit; ARPU ~€300.
- **Cost to serve:** €25. Gross margin 92%.
- **Fixed costs:** €1,500/month.
- **CAC:** €2,500–4,000 cash.
- **Churn:** 1%/month. LTV ≈ €12.5k; LTV/CAC 3–5 on cash, 2–3 loaded.
- **Customers needed:** ≈ 35.
- **Time:** 30–36 months, because sales cycles run 9–12 months. Misses the 24-month goal.

**Top 3 risks**
1. ERP vendors add the feature.
2. Landlords prefer their own dunning process.
3. Benefit rules keep changing.

**Cheapest 30-day money test (≤ €500)**
- Call the heads of social management at 50 housing cooperatives.
- Sell a €990 paid pilot on their next statement batch.
- **Pass:** at least 1 signed paid pilot.

---

### 2.13 L5-F1 — RambursFlip: converts cash-on-delivery orders to prepaid for Romanian web shops (RoPay + WhatsApp Business API): 56.5, KILL

**Hard-rule findings**
- **H1 pass.**
- **H2 pass, but RoPay must wait for a later phase:**
  - Netopia's RoPay payments are live, but only through an ING integration in which ING is the technical service provider. Netopia is still working toward the role that would open RoPay to its whole merchant portfolio ([wall-street.ro](https://www.wall-street.ro/articol/finante-banci/netopia-payments-aduce-platile-instant-a2a-prin-ropay-in-productie-cu-ing-bank.html)).
  - EuPlătesc is in the first stage of a direct connection. A payment-facilitator model is planned for autumn 2026 ([revistabiz](https://www.revistabiz.ro/euplatesc-se-conecteaza-direct-la-infrastructura-transfond-acces-la-ropay-simplificat-pentru-comercianti/)).
  - **No merchant fees are published.**
  - Card payment links (Stripe, Netopia, EuPlătesc) work today.
- **H3 pass.** Money flows from the buyer to the merchant's licensed processor.
- **H4 pass (watch):**
  - Each merchant's WhatsApp account is subject to Meta's enforcement. WhatsApp's commerce rules bar transacting in "unsafe ingestible supplements" (at WhatsApp's sole discretion) and in certain healthcare products, including medical devices ([Meta policy-enforcement page](https://developers.facebook.com/documentation/business-messaging/whatsapp/policy-enforcement-violations)).
  - A 2022 change may limit the Commerce Policy to catalogue and payment tools (secondary, unverified: [taqnyat](https://blog.taqnyat.sa/en/post/prohibited-cases-in-whatsapp/)).
  - An SMS fallback and several shop platforms mean there is no single gatekeeper.
- **H5–H7 pass.**
- **H8 pass on evidence:**
  - Caty and Zarina CRM confirm cash-on-delivery orders over WhatsApp; Zarina claims "recovery" of unpaid ones ([Zarina](https://www.zarinacrm.ro/automatizare-comenzi-online/); [Caty](https://aws.plainenglish.io/clientul-tău-a-comandat-cine-îi-spune-că-a-plecat-coletul-caty-ecf9f9f49316)).
  - No Romanian prepaid converter was found.
  - Couriers do not offer online payment before delivery (see below).

**Scores**

| C | Score | One-line justification |
|---|---|---|
| C1 | 7 | Daily, measurable losses: 5–15% of cash-on-delivery parcels come back (Packeta, per lens 5), plus a collection fee on every parcel. |
| C2 | 7 | The merchant pays out of savings; paid local tools (Caty from €10/month, per lens 5) show willingness to pay. |
| C3 | 5 | India proves the category. But card prepayment has been possible in Romania for years and RoPay is not yet broadly available to merchants, so "why now" is weaker than lens 5 says. |
| C4 | 6 | Shopify and WooCommerce listings, agencies and Romanian e-commerce events and communities (JUDGEMENT), worked through a Romanian freelancer. |
| C5 | 5 | ~86% gross margin. E-commerce app churn of ~5% a month gives LTV ≈ €1.1k vs CAC €250–700 (1.6–4.6×). |
| C6 | 5 | ~172 merchants is ~1–2% of all shops (assumed 10–20k), but a far larger share of shops with enough cash-on-delivery volume to pay €39 or more (JUDGEMENT). |
| C7 | 5 | Two shop platforms, Meta onboarding per merchant, payment webhooks, Romanian support through a freelancer, and Black Friday peaks. |
| C8 | 4 | Caty, Zarina or GoMag could add payment links; switching costs are low. |
| C9 | 6 | No funds are handled. The exposure is the phishing association and consent rules. |
| C10 | 6 | €99 refundable pilots within 60–90 days through a local freelancer. |

**What the researcher missed**
- **The phishing climate.**
  - FAN Courier warns customers about fraudulent SMS messages in its name that ask them to open a link.
  - It also says it has no system that lets buyers pay online; card payment is only by POS at its offices ([economica](https://www.economica.net/fan-courier-avertizeaza-clientii-asupra-unei-tentative-de-frauda-prin-intermediul-mesajelor-tip-sms_524562.html); [profit.ro](https://profit.ro/povesti-cu-profit/it-c/fan-courier-avertizeaza-clientii-asupra-unei-tentative-de-frauda-prin-intermediul-mesajelor-tip-sms-20324181); article date not visible).
  - The good news: couriers are not competing on pre-delivery payment.
  - The bad news: Romanian buyers are being taught to distrust "pay via link" parcel messages. That threatens conversion and can trigger WhatsApp spam reports, which lower the number's quality rating and messaging limits.
  - Mitigations: a verified business sender, a message sent seconds after checkout, and a payment page on the shop's own domain (JUDGEMENT).
- **Conflicting data on the cash-on-delivery share.**
  - A Cargus/Visa whitepaper says almost 7 in 10 Romanians report paying by card on the website, and cash-on-delivery is the main method for almost 1 in 5 online buyers ([Cargus/Visa](https://www.cargus.ro/wp-content/uploads/Cargus-whitepaper-Visa.pdf)).
  - Forbes Romania estimates "about two-thirds of orders" (per lens 5).
  - The first is a card-network-sponsored, self-reported survey; the second is an estimate. Unresolved, and material to C6.
- **A possible competitor I could not identify.** One Forbes Romania article describes a variant where the buyer gets a payment link by SMS or e-mail and the courier is told the parcel can be handed over. The provider was not identified, because the page fetch failed (UNVERIFIABLE).
- **Marketplace volume is out of reach.** Much cash-on-delivery volume runs through marketplaces such as eMAG, where a shop-side tool cannot act (JUDGEMENT).

**Recomputed unit economics**
- **Price and ARPU:** €39/€89/€179 per month; ARPU €70, excluding message fees passed through at cost.
- **Cost to serve:** €10. Gross margin 86%.
- **Fixed costs:** €2,300/month.
- **CAC by channel:**
  - demos booked by a freelancer, plus a pilot: €250–400 cash;
  - app-store organic installs: €50–150 for small shops;
  - agencies at a 20% revenue share: ≈ €170.
- **Churn:** 5%/month. LTV ≈ €1.1k; LTV/CAC 2.9–4.6 on cash, 1.6–2.9 loaded.
- **Customers needed:** ≈ 172 merchants.
- **Time:** 14–20 months if pilots show at least 10% conversion. Below 5% conversion, never.

**Top 3 risks**
1. Conversion stays below 5% because of trust and phishing fears.
2. RoPay delays leave a card-only product with a weak wedge.
3. Caty, Zarina or GoMag add payment links.

**Cheapest 30-day money test (≈ €1,500, incl. freelancer and translation)**
1. Run a concierge test in 3 shops for 2 weeks: send confirmation messages plus card-payment links by hand from each shop's own WhatsApp Business app.
2. Charge each shop €99, refundable.
3. Measure conversion on at least 300 cash-on-delivery orders.
4. **Pass:** at least 3 paid pilots and at least 8% conversion.

**Launch market:** Romania is evidence-driven, with Bulgaria second.

---

### 2.14 L5-F2 — Vorbestell-Desk: WhatsApp pre-orders, pickup slots and instant deposits for butchers, bakeries and farm shops (Germany): 49.5, KILL

**Hard-rule findings**
- **H1–H3 pass.** Deposits go to the shop's own payment account.
- **H4 pass (watch).** Meta's free WhatsApp Business app already has a catalogue and cart (per lens 5). POS and scale vendors could add pre-ordering (JUDGEMENT).
- **H5–H7 pass.**
- **H8 at risk, not proven.** At least nine branded butcher pre-order apps exist; see 2.0 (d).

**Scores**

| C | Score | One-line justification |
|---|---|---|
| C1 | 5 | Intense before Christmas and Easter, moderate the rest of the year (assumed in lens 5). |
| C2 | 5 | The shop pays to avoid no-shows; €35/month is untested, and butchers' margins are thin. |
| C3 | 3 | Branded pre-order apps already serve butchers; only the deposit is new. |
| C4 | 5 | Guild meetings and cold visits are cheap but slow. |
| C5 | 5 | ~80% gross margin. Seasonal churn of ~3% a month gives LTV ≈ €780 vs CAC €150–500. |
| C6 | 6 | ~350 shops of an assumed ~20k; the receptive share is smaller. |
| C7 | 5 | A simple product, but every customer peaks on 20–24 December, making a solo founder the single point of failure on the shop's busiest days. |
| C8 | 4 | White-label app vendors or POS vendors can add deposits, and payment links are a commodity. |
| C9 | 7 | Low liability, because deposits go to the shop's own account. |
| C10 | 7 | A €149 concierge Christmas 2026 pilot can be sold now. |

**What the researcher missed**
- **Existing branded apps,** listed in 2.0 (d).
- **German customers expect to pay at pickup.** All the listed apps let them pay at the counter, so requiring deposits may reduce orders (JUDGEMENT).
- **Reminder costs.** WhatsApp reminders sent outside the 24-hour window cost a utility-template fee; the German rate card was not verified by lens 5 or by me.

**Recomputed unit economics**
- **Price:** €35/month (€420/year).
- **Cost to serve:** €7. Gross margin 80%.
- **Fixed costs:** €1,800/month.
- **CAC by channel:** guild talks and cold visits, €150–300 cash or €300–500 loaded.
- **Churn:** 3%/month. LTV ≈ €780; LTV/CAC 2.6–5.2 on cash, 1.6–2.6 loaded.
- **Customers needed:** ≈ 350.
- **Time:** 30–36 months, because there is effectively one selling season a year. Misses the 24-month goal.

**Top 3 risks**
1. Customers refuse deposits.
2. White-label app or POS incumbents add the feature.
3. Seasonality.

**Cheapest 30-day money test (≤ €900)**
1. Identify the developer behind the branded butcher apps, so you can price against it.
2. Sell the €149 concierge Christmas 2026 pilot to shops within 50 km.
3. **Pass:** at least 10 paid pilots by mid-November.

---

### 2.15 L5-F3 — WP-Wächter: monthly efficiency check and fix list for heat-pump owners (Germany): 44.5, KILL

**Hard-rule findings**
- **H1, H2 pass.** Manual readings plus official APIs.
- **H3 pass.**
- **H4 pass narrowly — flagged.** The automated value depends on each maker's permission:
  - **Viessmann:**
    - every user must register their own personal API client (per [PyViCare docs](https://pypi.org/project/PyViCare/));
    - Viessmann caps requests per application;
    - its ViCare app terms say the app is aimed exclusively at consumers ([Viessmann legal document](https://api.viessmann-climatesolutions.com/legal/v3/documents/918cfb4f-8bda-41c2-9a9d-b603aa668b54/download?country=GB));
    - I found no commercial third-party terms.
  - **Vaillant:** no official API (per lens 5).
  
  Because there are several makers and a manual path, there is no *single* gatekeeper, so I do not count this as a violation. But the paid product's core value rests on permissions any maker can revoke.
- **H5–H7 pass.**
- **H8 pass on evidence.**
  - Efficiency monitoring exists in Switzerland: NeoVac's apps ([NeoVac](https://www.neovac.ch/pdf/energie-ueberwachen/161_waermepumpen_effizienzmessung_de.pdf)) and the non-profit WP-Cockpit platform ([WP-Cockpit](https://www.fws.ch/wp-content/uploads/2019/11/191105_WP-Cockpit_FWS-Tagung.pdf)).
  - NeoVac's approach relies on a dedicated heat-pump meter.
  - No German consumer service was found.

**Scores**

| C | Score | One-line justification |
|---|---|---|
| C1 | 5 | Real but invisible waste. In a WP-Cockpit example, efficiency of 3.5 vs 1.75 changes the bill by ~CHF 570 a year at 10,000 kWh heat demand; typical gaps are smaller (JUDGEMENT). |
| C2 | 4 | Homeowners' willingness to pay €4.99/month is uncertain, and the value comes up front. |
| C3 | 4 | Maker apps, DIY tools and installer services overlap; the German diagnosis gap is unverified. |
| C4 | 6 | Owner forums, Facebook groups and YouTube are cheap. |
| C5 | 3 | €4.19 net, ~79% gross margin and ~6% monthly churn give LTV ≈ €53 vs CAC €15–60. |
| C6 | 8 | ~3,000 subscribers ≈ 1% of recent installs from supported brands. |
| C7 | 4 | Rate limits, per-user API setup friction and technical support questions from owners. |
| C8 | 2 | Makers control the data and can ship the same diagnosis free. |
| C9 | 6 | Advice is routed through the installer. |
| C10 | 6 | Community pre-sales are feasible. |

**What the researcher missed**
- **Per-user API setup for Viessmann** adds onboarding friction and terms risk.
- **Other official APIs were not considered:** NIBE myUplink, Samsung SmartThings and LG ThinQ (JUDGEMENT).
- **Manual efficiency calculation needs meters.** Few homes have a separate heat meter (JUDGEMENT; NeoVac's approach relies on a dedicated meter).
- **A subsidised substitute.** Independent energy checks from consumer advice centres (JUDGEMENT).

**Recomputed unit economics**
- **Price:** €4.99 incl. VAT (€4.19 net).
- **Cost to serve:** €0.90. Gross margin 79%.
- **Fixed costs:** €1,800/month.
- **CAC by channel:**
  - forums and Facebook groups: €15–25;
  - YouTube sponsorships: €30–60.
- **Churn:** 6%/month. LTV ≈ €53; LTV/CAC 1.3–3.6 on cash.
- **Customers needed:** ≈ 2,980.
- **Time:** more than 36 months, or never. Holding 3,000 subscribers at 6% churn needs ~180 new sign-ups a month.

**Top 3 risks**
1. Makers ship the same diagnosis.
2. API access is revoked or limited.
3. Users cancel after the first fixes.

**Cheapest 30-day money test (≤ €500)**
- Pre-sell a €39 "founding season" in 3 owner forums and through one YouTuber (€300).
- **Pass:** at least 50 pre-sales.

---

### 2.16 BASE — Daily automated check-in call for people 65+ living alone (Germany): 42.5, KILL

**Hard-rule findings**
- **H1 pass.** The person presses 1 on the keypad; no speech recognition.
- **H2 pass.** A telephony API plus a scheduler: 4–6 weeks of work.
- **H3 pass.** No licence is needed. It must be marketed clearly as not an emergency service.
- **H4 pass.** Hausnotruf providers or telecoms could add a phone-only tier, but probably not free. Smartphone check-in features don't reach landline seniors (JUDGEMENT).
- **H5 pass.** The family pays.
- **H6 pass only with the senior's own consent.** If a family signed up a parent without consent, this would be surveillance.
- **H7 pass.**
- **H8 pass.** My search found no German phone-only provider.

**Scores**

| C | Score | One-line justification |
|---|---|---|
| C1 | 5 | A rare but catastrophic event for the senior, plus daily low-level worry for the family. |
| C2 | 4 | The family pays, but in the US even free sheriff and state programmes struggle to keep enrolment: participants move or die and too few new seniors sign up ([newsaegis](https://newsaegis.com/?p=48162); [pressreader](https://www.pressreader.com/canada/sherbrooke-record/20180117/281578061072379)). That is weak demand even at €0, and "I'll call Mum myself" is free. |
| C3 | 5 | No German phone-only service was found, but the reason may be weak demand as much as neglect. |
| C4 | 3 | Adult children are reached mainly through paid search and social ads, in competition with Hausnotruf advertisers. |
| C5 | 3 | €9.90 incl. VAT is €8.32 net; ~70% gross margin and ~5% churn give LTV ≈ €110 vs CAC €60–200 (0.6–1.9×). |
| C6 | 9 | ~1,550 families out of millions of people 65+ living alone (roughly 6 million; JUDGEMENT, unverified). |
| C7 | 5 | Simple telephony, but a safety-critical service 365 days a year. False alarms happen when people forget the scheduled call or don't hear the phone (CONFIRMED via search extract). |
| C8 | 3 | Trivial to copy; low switching costs. |
| C9 | 3 | A missed alert that coincides with a death is a reputational and legal disaster. |
| C10 | 7 | A landing page plus ads can bring paid sign-ups within weeks. |

**What the researcher missed**
- **The US analogues are mostly free and government-run:**
  - Maryland's Senior Call Check ([Maryland](https://aging.prod.maryland.gov/senior-call-check));
  - California's 65 Check;
  - Oklahoma's CONFIRM OK, run through the sheriff ([Baxter County Sheriff](https://www.baxtercountysheriff.com/press-releases/confirm-okautomated-wellness-systemseniorsdisabledlivingalone)).
- **The product path leads to a staffed alarm centre, which is expensive.** Doro alerts a loved one first, then its own alarm centre ([Doro](https://www.doro.com/en-ca/services/)).
- **Telephony cost is plausible.** Roughly €0.5–2.5 per customer per month, depending on landline vs mobile (JUDGEMENT), so the brief's ~€3 is fair.
- **VAT takes the net price down to €8.32.**

**Recomputed unit economics**
- **Price:** €9.90 incl. VAT (€8.32 net).
- **Cost to serve:** €2.50 (calls and retries, alert SMS, ~€0.35 payment fee, support). Gross margin 70%.
- **Fixed costs:** €1,000/month.
- **CAC by channel:**
  - Google Ads: €60–200;
  - Facebook: €80–150;
  - flyers in pharmacies and senior advice offices: unproven.
- **Churn:** 5%/month. LTV ≈ €111; LTV/CAC 0.7–1.9.
- **Customers needed:** ≈ 1,550.
- **Time:** not reachable at a sustainable CAC.

**Top 3 risks**
1. Liability for a missed alert.
2. Churn.
3. CAC.

**Cheapest 30-day money test (≤ €1,000)**
- Put up a German landing page.
- Spend €800 on Google Ads for "Hausnotruf ohne Pflegegrad" and "täglicher Anruf Eltern".
- Take €29.70 for 3 months prepaid, after a 14-day free trial.
- **Pass:** at least 30 paid sign-ups at a CAC of €40 or less.

---

## (3) RANKING OF ALL 16 IDs AND WHICH BEAT BASE

| Rank | ID | Score | Verdict | Margin vs BASE (42.5) | Beats BASE? |
|---|---|---|---|---|---|
| 1 | L3-A Biogas evidence log | 61.0 | TEST | +18.5 | Yes, clearly |
| 2= | L1-A Vet preventive plans | 60.5 | TEST | +18.0 | Yes, clearly |
| 2= | L4-F1 Care-home financing case manager | 60.5 | TEST | +18.0 | Yes, clearly |
| 4 | L3-B Parent-duty rosters | 58.0 | KILL | +15.5 | Yes, clearly |
| 5 | L5-F1 RambursFlip | 56.5 | KILL | +14.0 | Yes, clearly |
| 6 | L4-F2 SBV case tool | 54.5 | KILL | +12.0 | Yes, clearly |
| 7= | L2-F1 CRA Logbook | 53.0 | KILL | +10.5 | Yes, clearly |
| 7= | L3-C Swiss condominium self-admin | 53.0 | KILL | +10.5 | Yes, clearly |
| 9 | L2-F3 Battery Passport Lite | 52.0 | KILL | +9.5 | Yes, clearly |
| 10 | L1-C Music-teacher admin | 51.5 | KILL | +9.0 | Yes, clearly |
| 11= | L1-B Boarding-stable billing | 49.5 | KILL | +7.0 | Yes |
| 11= | L5-F2 Vorbestell-Desk | 49.5 | KILL | +7.0 | Yes |
| 13 | L2-F2 CRA vault for importers | 46.0 | KILL | +3.5 | Within noise |
| 14 | L4-F3 Tenant deadline assistant | 45.0 | KILL | +2.5 | Within noise |
| 15 | L5-F3 WP-Wächter | 44.5 | KILL | +2.0 | Within noise |
| 16 | BASE Daily check-in call | 42.5 | KILL | — | — |

**Which beat BASE?**
- All 15 finalists score above my BASE score.
- Twelve lead by more than 5 points.
- Three are within evaluator noise: L2-F2, L4-F3 and L5-F3.

**Sensitivity to how BASE is scored.** The lenses scored BASE at 51.0–57.5.
- At **57.5**, only L3-A, L1-A, L4-F1 and L3-B (58.0, by 0.5) beat it.
- At **51.0**, ten finalists beat it: everything down to L1-C.

**Why my BASE score is low.** On a bootstrapper's lens, BASE has the two traits I most avoid:
- a low-ticket consumer subscription with paid acquisition, where LTV/CAC is below 2;
- a safety-critical promise run by one person.

**No idea reaches BUILD.** Each of the three TEST ideas has one unproven point that a cheap 30–90-day test can settle:
- **L3-A:** will operators prepay instead of using Excel?
- **L1-A:** will owners enrol without discounts?
- **L4-F1:** will homes pay, and can one person carry the support and security load?

---

## (4) MY €10,000 BET AND MY NEVER-FUND PICK

**Bet: L3-A — the audit-ready substrate and EEG evidence log for German biogas plants.**

Why, in bootstrapper terms:
1. **The payer is the sufferer and has deep pockets.** An average plant produces ~3.1 GWh a year and already pays for verifier reports (per lens 3). A €1,190 annual fee is noise next to a lapsed bonus.
2. **Cash comes up front.** Annual prepayment, timed to a hard yearly deadline (28 February), finances growth with no investor.
3. **Few customers are needed.** ~107 plants at €99/month. They can be reached through a small, listable group of referrers, the environmental verifiers, who gain from cleaner input.
4. **It is a deterministic, low-churn system of record.** No client money, no health data and no 24/7 duty. The worst case is a liability claim over one plant's pack, which is insurable.
5. **Existing competitors prove demand without dominating.** Three young vendors exist, but most plants still use Excel (per lens 3).

**How I would stage the €10k**
- **€2,000 on the 90-day proof:**
  - travel to one FvB regional meeting and 5–8 verifier visits;
  - the founding-plan landing page;
  - a one-off review of the terms of use.
- **Kill if** by 31 Jan 2027 there are fewer than 2 verifier partners or fewer than 10 prepaid plants. That leaves €8k intact.
- **If it passes:**
  - €3,000 on professional liability insurance and legal terms;
  - €3,000 on events, travel and ag-press ads before the 2027/28 season;
  - €2,000 on a part-time farm-domain freelancer to build feeding-controller import mappings and cover the January–February support peak.

**Runner-up: L1-A (vet plans).** It has the strongest proof abroad. I rank it second because:
- it costs legal money before the first euro of revenue;
- adoption is two-sided (practice, then owners);
- revenue lags while plan numbers ramp up.

**Never fund: L5-F3 (WP-Wächter).** It fails the bootstrapper's first test: *who controls my inputs, and can they give my product away?*
- The heat-pump makers control the data.
  - Viessmann's access is per personal API client, with consumer-only app terms.
  - Vaillant has no official API.
  - Daikin caps calls.
- The same makers can ship the same diagnosis free in their apps.
- The economics are broken even if the inputs were free: €4.19 net per month, ~6% churn, LTV ≈ €53. That is roughly break-even against even cheap community CAC.
- A successful pre-sale test would not fix any of this.

**Also no, briefly:**
- **BASE:** safety-critical consumer service with LTV/CAC below 2.
- **L2-F3:** a one-person vendor cannot credibly promise multi-year availability of legally required battery passports on which customers' market access depends.

---

## (5) VERIFICATION LOG

All 15 web searches are listed. "CONFIRMED", "CONTRADICTED" and "UNVERIFIABLE" refer to what the search extracts showed. No full page could be opened: the one fetch attempt failed with a DNS error and was not retried.

| # | Claim checked (idea) | Result | URL(s) |
|---|---|---|---|
| 1 | RoPay merchant fees, and whether processors give merchants RoPay acceptance (L5-F1) | **Fees: UNVERIFIABLE** (none published; only a forum guess at "lower" fees). **Access: CONTRADICTS lens 5's implied readiness.** Netopia is live only through ING as technical service provider, and its provider role for all merchants is pending. EuPlătesc is in its first stage, with a payment-facilitator model planned for autumn 2026. | https://www.wall-street.ro/articol/finante-banci/netopia-payments-aduce-platile-instant-a2a-prin-ropay-in-productie-cu-ing-bank.html ; https://www.revistabiz.ro/euplatesc-se-conecteaza-direct-la-infrastructura-transfond-acces-la-ropay-simplificat-pentru-comercianti/ ; https://forum.softpedia.com/topic/1237616-ropay-o-noua-metoda-de-plata-instant-mai-sigura/ |
| 2 | Romanian tools that convert cash-on-delivery orders to prepaid (L5-F1, H8) | **CONFIRMED** that local tools only confirm orders (Zarina, Caty). **New conflicting data:** the Cargus/Visa whitepaper says ~7 in 10 report paying by card on the site and cash-on-delivery is the main method for ~1 in 5, vs Forbes Romania's "two-thirds" — **CONTRADICTED / conflicting.** A Forbes Romania article describes a pay-by-link-before-handover variant from an unidentified provider (**UNVERIFIABLE**). | https://www.zarinacrm.ro/automatizare-comenzi-online/ ; https://aws.plainenglish.io/clientul-tău-a-comandat-cine-îi-spune-că-a-plecat-coletul-caty-ecf9f9f49316 ; https://www.cargus.ro/wp-content/uploads/Cargus-whitepaper-Visa.pdf ; https://www.forbes.ro/?p=277382 |
| 3 | WhatsApp commerce rules on supplements and medical products (L5-F1, L5-F2) | **CONFIRMED:** businesses may not transact in "unsafe ingestible supplements" (at WhatsApp's discretion), certain healthcare products including medical devices, or prescription drugs. **UNVERIFIABLE:** whether a 2022 change limits the policy to catalogue and payment tools. | https://developers.facebook.com/documentation/business-messaging/whatsapp/policy-enforcement-violations ; https://developers.facebook.com/docs/whatsapp/overview/policy-enforcement/violations ; https://blog.taqnyat.sa/en/post/prohibited-cases-in-whatsapp/ |
| 4 | ENISA's single reporting platform has no API for manufacturers (L2-F1) | **CONFIRMED (secondary).** No manufacturer API "at this stage"; reports go through a web portal with EU Login and MFA; the planned API is for national CERTs. Launch status conflicts: CSA says live on 11 Sep 2026; an undated advisori page says not live. | https://labs.cloudsecurityalliance.org/research/csa-research-note-enisa-cra-reporting-platform-20260918-csa/ ; https://www.cyberresilienceact.eu/news/enisa-srp-step-by-step-instructions-31-july-2026.html ; https://www.advisori.de/blog/cra-single-reporting-platform-srp-registration |
| 5 | "Only sbomify sells a comparable CRA tool at a similar price" (L2-F1, H8/C3) | **CONTRADICTED.** CRALedger has a free tier and a $29/month plan that tracks Art. 14 deadlines. CRA Evidence, CRA Gap Finder and the EU-funded ATHENA and CRACoWi tools also exist. No funding or profitability evidence for any of them, so H8 is not triggered. | https://pickyourapp.com/products/craledger-duty-records ; https://www.getapp.com.au/software/2141675/cra-evidence ; https://www.softwareadvice.co.uk/software/773157/Cyber-Resilience-Act-Gap-Finder ; https://cordis.europa.eu/project/id/101225583 ; https://www.hannovermesse.de/product/eu-funded-cybersecurity-assistant/511395/N1483015 |
| 6 | Viessmann API terms for commercial third-party apps (L5-F3) | **Commercial terms: UNVERIFIABLE** (not found). **CONFIRMED in part:** each user registers a personal API client; requests are capped per application; ViCare app terms are "aimed exclusively at consumers" (the clause is cut off in the extract). | https://pypi.org/project/PyViCare/ ; https://api.viessmann-climatesolutions.com/legal/v3/documents/918cfb4f-8bda-41c2-9a9d-b603aa668b54/download?country=GB ; https://knx-user-forum.de/forum/supportforen/smartvisu/1517343-vissmann-heizungssteuerung-vicare-vitaconnect |
| 7 | German consumer heat-pump efficiency services (L5-F3, H8/C3) | **German services: UNVERIFIABLE** (none found). **CONFIRMED in Switzerland:** NeoVac apps (meter-based) and the non-profit WP-Cockpit; WP-Cockpit's CHF 570/year example. | https://www.neovac.ch/pdf/energie-ueberwachen/161_waermepumpen_effizienzmessung_de.pdf ; https://www.fws.ch/wp-content/uploads/2019/11/191105_WP-Cockpit_FWS-Tagung.pdf ; https://bau.de/text/240313-jaz-cop-waermepumpen-betrieb.php |
| 8 | Swiss condominium software, and QR-bill/QR-IBAN rails (L3-C, issue b) | **CONFIRMED:** AbaImmo covers condominium communities (meetings, annual statements, renewal fund); the ZKB opening form offers QR-IBAN payment slips; the Weka calculator covers up to 20 units. **No new self-admin competitor found.** | https://www.ABACUS.ch/fileadmin/ablage/02_dokumente/01_flyer/de/flyer_abacus_abaimmo-immobilienbewirtschaftung_de.pdf ; https://www.zkb.ch/media/zkb/dokumente/formulare/Formular_Er%C3%B6ffnungsantrag_20STWEG_11_23.pdf ; https://www.weka.ch/bau-immobilien/immobilien/immobilienverwaltung/rechner-heiz-und-nebenkostenabrechnung-im-stockwerkeigentum.html |
| 9 | Stabley is free and includes billing (L1-B, issue a) | **CONFIRMED** that the listing says free core features and billing for stable operators, as a PWA. **Billing depth: UNVERIFIABLE.** | https://alternativeto.net/software/stabley/about/ |
| 10 | Romanian couriers already offer online payment of cash-on-delivery before delivery (L5-F1, H4 incumbent risk) | **CONTRADICTED** (no courier offers it). FAN Courier says it has no system for buyers to pay online and warns about phishing SMS links in its name. Sameday's 2020 PIN delivery covers prepaid parcels only. | https://www.economica.net/fan-courier-avertizeaza-clientii-asupra-unei-tentative-de-frauda-prin-intermediul-mesajelor-tip-sms_524562.html ; https://profit.ro/povesti-cu-profit/it-c/fan-courier-avertizeaza-clientii-asupra-unei-tentative-de-frauda-prin-intermediul-mesajelor-tip-sms-20324181 ; https://www.wall-street.ro/articol/Auto/252272/sameday-serviciul-de-livrare-fara-interactiune-intre-curier-si-destinatar.html |
| 11 | German butcher/bakery pre-ordering competitors (L5-F2, issue d) | **CONTRADICTS the "gap".** At least 9 branded butcher pre-order apps share one flow (pickup slot, in-store auto-print, pay at pickup). Vendor **UNVERIFIABLE**. | https://apps.apple.com/app/id1508324294 ; https://apps.apple.com/app/id1482256245 ; https://apps.apple.com/us/app/-/id1549844655 ; https://apps.apple.com/app/id1536133403 ; https://apps.apple.com/app/id1551760911 ; https://apps.apple.com/app/id1589241464 ; https://apps.apple.com/app/id1596895369 ; https://apps.apple.com/de/app/app/id1538437237 ; https://apps.apple.com/de/app/metzgerei-geiger/id1532742300 |
| 12 | German phone-only daily check-in providers; US demand signals (BASE) | **German providers: none found** (consistent with the brief). **CONFIRMED:** US programmes are mostly free (Maryland, California, Oklahoma); police programmes struggle with enrolment and attrition; false alarms when people forget the call; Doro escalates to its alarm centre. | https://aging.prod.maryland.gov/senior-call-check ; https://www.baxtercountysheriff.com/press-releases/confirm-okautomated-wellness-systemseniorsdisabledlivingalone ; https://newsaegis.com/?p=48162 ; https://www.pressreader.com/canada/sherbrooke-record/20180117/281578061072379 ; https://whyy.org/articles/older-delaware-adults-automated-calls/ ; https://www.doro.com/en-ca/services/ |
| 13 | No practice-run vet plans in Germany (L1-A, H8/C3) | **CONFIRMS lens 1's absence** (only insurers returned). **CONFIRMED:** HUK-COBURG launched dog/cat cover on 1 Oct 2026; Allianz says vaccinations, deworming and a microchip can be insured under surgery cover. | https://www.huk.de/presse/nachrichten/aktuelles/huk-coburg-tierkrankenversicherung.html ; https://www.allianz.de/angebot/kooperation/h8w65b/freizeit/tierkrankenversicherung ; https://www.test.de/Haustiere-Was-Hund-und-Katze-wirklich-kosten-4469034-4469041/ |
| 14 | Care-home-side software for Hilfe zur Pflege files (L4-F1, H8/C3) | **CONFIRMS lens 4's absence** (no software found). **CONFIRMED process facts:** aid only from the application date or the date need became known; incomplete applications secure the date (LSG BW L 7 SO 2479/23); ~2 months to gather documents; online filing only for home-care (ambulant) cases, with upload limits; processing times vary in BW. | https://www.betanet.de/hilfe-zur-pflege.html ; https://www.gegen-hartz.de/urteile/sozialhilfe-formloser-antrag-sichert-anspruch-auf-hilfe-zur-pflege ; https://fimportal.de/api/v0/xzufi-services/L100108/L100108_324474/de/pdf ; https://www.landtag-bw.de/resource/blob/585070/cf26fb5af1795d9bc21e527dfa3bf5bd/17_9244_D.pdf ; https://www.rbk-direkt.de/download/429/hilfe-zur-pflege-in-einem-pflegeheim---fragen-und-antworten |
| 15 | Dedicated German boarding-stable billing software (L1-B, C3) | **None found**; only generic SEPA tools. Consistent with lens 1, though Stabley (check 9) partly contradicts it. | https://www.jam-software.com/sepa-transfer/editions.shtml ; https://softguide.com/function/sepa |
| F1 | Page fetch of the Forbes Romania article on the pay-by-link-before-handover variant (L5-F1) | **UNVERIFIABLE.** DNS failure (ENOTFOUND); not retried, as instructed. | https://www.forbes.ro/?p=277382 |

**Decisive lens claims I relied on without re-checking.** Treat these as search-extract-verified by the researchers, not by me:
- **L1-A:** CVS (519k members) and PVA (3,000+ practices) figures; Petly pricing; the GOT 1× floor.
- **L3-A:** biogas plant count (9,605) and output; the €15k verifier-cost anecdote.
- **L4-F1:** PwC care-home receivables data; vdek co-payments.
- **L2-F1:** C26 firm count (7,860); CRA dates and fine exemption.
- **L5-F1:** Packeta return rates; Romanian WhatsApp rates.
- **L3-C:** NZZ/Wüest Partner unit counts.

**Main items labelled JUDGEMENT (unverified).** These would move scores if they turn out wrong:
- the vet shortage and the drug-pricing constraint (L1-A);
- EEG term expiries and maize-cap diaries (L3-A);
- the RDG/Smartlaw reading (L4-F1, L4-F2, L4-F3);
- German legal-compliance incumbents (L2-F2);
- e-bike system suppliers "finishing" batteries, and passport continuity duties (L2-F3);
- Swiss VAT registration and Banana/bexio substitutes (L3-C);
- the size of the German pool of over-65s living alone and telephony costs (BASE).
