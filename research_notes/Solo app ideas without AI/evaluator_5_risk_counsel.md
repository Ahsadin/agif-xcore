# Evaluator 5 — "the Risk Counsel-Operator": independent full-business evaluation of the 15 finalists and the BASELINE

Prepared 2026-10-12. Evaluator background (hypothetical): former general counsel and compliance officer who has also run a company as CEO. I read all five lens files in full, verified the claims most likely to flip a verdict (mostly licensing, liability and platform terms), and scored all 16 IDs myself with the coordinator's RULEBOOK, unchanged.

**How to read the evidence labels**

| Label | Meaning |
|---|---|
| (extract) | Confirmed from a search-engine extract of the cited page this session. Page fetching failed (DNS), so the full page was not read. |
| (lens N) | Taken from a lens file and not re-checked by me. The URL is the lens's own source. |
| STATUTE (not fetched) | My reading of a statute. The official URL is given, but I did not open it this session. Counsel should confirm the wording. |
| JUDGEMENT (unverified) | My professional judgement, with no source checked this session. |
| ASSUMPTION | A planning number, not a fact. |

**Budget used:** 15 of 15 web searches and 1 page fetch, which failed (DNS). I did not retry it.

> **Takeaway**
> - **No idea reaches BUILD (75+). Two reach TEST:**
>   - **L4-F1, care-home financing case manager: 64.0.**
>   - **L2-F1, CRA Logbook: 61.5.**
> - **Three are just below the TEST line:** L3-A biogas (59.0), L1-A vet plans (57.5) and L5-F1 RambursFlip (57.0).
> - **I score the BASELINE at 49.0 (KILL).** Eleven ideas beat it, but only five do so by more than 5 points (evaluator noise).
> - **I found no outright hard-rule violation.** Seven ideas carry an "at risk" hard-rule flag (H4, H6 or H8). Three more pass H3 or H6 only if the product is designed a certain way (L1-A, L4-F1, BASE). L4-F2 is borderline on H5.
> - **Seven finalists plus the BASELINE need a qualified lawyer before launch:** L1-A, L2-F3, L4-F1, L4-F2, L4-F3, L5-F1, L5-F2 and BASE. L2-F1 and L2-F2 need only a light check.
> - **My €10,000 bet is L4-F1, released in stages behind a legal-opinion gate. My never-fund pick is the BASELINE.** Among the 15 finalists, the one I would never fund is L2-F3.

---

## (1) Summary table

Weights: C1 10 · C2 15 · C3 10 · C4 15 · C5 15 · C6 5 · C7 10 · C8 10 · C9 5 · C10 5. Weighted score = Σ(score × weight) / 10. I checked the arithmetic with a script.

| ID | Hard-rule flags (violated H-rules or "none") | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | Weighted | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L1-A Vet preventive-care plans (DE) | none (H3 passes only with prevention-only design and no instalment premium) | 5 | 6 | 6 | 5 | 6 | 8 | 6 | 6 | 5 | 5 | **57.5** | KILL |
| L1-B Boarding-stable billing (DE) | none (H4 at risk: Stabley is listed as free with billing) | 5 | 4 | 3 | 4 | 6 | 7 | 7 | 3 | 8 | 5 | **49.0** | KILL |
| L1-C Music-teacher admin (DE) | none | 4 | 4 | 5 | 5 | 6 | 6 | 8 | 4 | 8 | 6 | **53.5** | KILL |
| L2-F1 CRA Logbook (EU, DE first) | none | 6 | 6 | 6 | 6 | 7 | 8 | 6 | 5 | 6 | 6 | **61.5** | TEST |
| L2-F2 CRA vault for importers/distributors (EU) | none | 4 | 4 | 4 | 5 | 6 | 6 | 7 | 3 | 6 | 4 | **48.5** | KILL |
| L2-F3 Battery Passport Lite (EU) | none (H8 at risk: digital-product-passport vendors) | 6 | 6 | 4 | 4 | 6 | 4 | 4 | 6 | 3 | 7 | **51.0** | KILL |
| L3-A Biogas evidence log (DE) | none (H8 at risk: 3 vendors, funding unknown) | 7 | 7 | 4 | 5 | 7 | 8 | 6 | 4 | 5 | 6 | **59.0** | KILL |
| L3-B Parent-run daycare rosters (DE) | none | 5 | 4 | 5 | 6 | 6 | 5 | 8 | 4 | 8 | 6 | **55.5** | KILL |
| L3-C Swiss condominium self-admin (CH) | none (H8 at risk) | 6 | 6 | 4 | 3 | 6 | 8 | 6 | 5 | 6 | 4 | **52.5** | KILL |
| L4-F1 Care-home financing case manager (NRW) | none (H3 passes only with RDG/§13 SGB X design; H6 needs a conflict-of-interest guard) | 8 | 7 | 7 | 5 | 7 | 9 | 5 | 6 | 4 | 6 | **64.0** | TEST |
| L4-F2 SBV case tool (DE) | none (H5 borderline: employer pays by statutory duty) | 6 | 4 | 5 | 5 | 6 | 7 | 6 | 5 | 4 | 4 | **52.0** | KILL |
| L4-F3 Tenant benefit-deadline assistant (DE) | none (H4 at risk; H6 at risk unless the landlord sees aggregates only) | 6 | 4 | 4 | 4 | 6 | 8 | 6 | 3 | 4 | 3 | **47.5** | KILL |
| L5-F1 RambursFlip (RO) | none (H4 narrow pass; H6 needs a design guard for irrevocable prepayment) | 7 | 7 | 5 | 5 | 5 | 7 | 5 | 4 | 7 | 7 | **57.0** | KILL |
| L5-F2 Vorbestell-Desk (DE) | none (H8 at risk: white-label pre-order apps exist) | 6 | 5 | 3 | 5 | 5 | 7 | 6 | 4 | 7 | 7 | **52.0** | KILL |
| L5-F3 WP-Wächter (DE) | none (H4 at risk: maker APIs and maker apps) | 5 | 3 | 4 | 6 | 3 | 8 | 5 | 2 | 6 | 6 | **44.0** | KILL |
| BASE Daily check-in call (DE) | none (H6 needs the senior's own consent) | 6 | 5 | 5 | 4 | 4 | 9 | 5 | 4 | 3 | 7 | **49.0** | KILL |

---

## (2) Per-idea notes

Each note has the same parts:
- hard-rule findings with evidence
- one-line justification for each of C1–C10
- what the researcher missed
- recomputed unit economics
- top 3 risks
- cheapest 30-day money test
- lawyer gate and the questions counsel must answer

All CAC figures are loaded, meaning cash plus founder time at €40/h (ASSUMPTION), unless marked "cash". All prices are net of VAT.

---

### L1-A — Monthly preventive-care plans for independent vet practices (Germany): **57.5, KILL** (closest "TEST-if-proven" case)

**Hard rules**
- **H1, H2, H4, H5, H7 pass.** The product is deterministic plan rules, SEPA mandates and an entitlement ledger. Money flows through the practice's own GoCardless or Stripe account ([lens 1](https://idexx-prod-base.django-aws.idexx.com/en/veterinary/software-services/petly-plans/getting-started/pricing)).
- **H3 passes, but only with the right plan design.**
  - **Insurance:** a fixed list of scheduled preventive services for a fixed fee transfers no risk, so it is not insurance business. Cover for unforeseeable illness, such as "unlimited sick consultations", would add risk transfer and could make the *practice's* plan unlicensed insurance (JUDGEMENT; [§1 VAG](https://www.gesetze-im-internet.de/vag_2016/__1.html), STATUTE not fetched).
  - **Consumer credit:** consumer-credit rules reach deferred payment only when it is *paid for* ("entgeltlich") ([§506 BGB](https://www.gesetze-im-internet.de/bgb/__506.html), STATUTE not fetched). So instalments must never add up to more than the cash price.
- **The GOT fee floor is a fee rule, not a licence, but it is binding.**
  - Fees may not fall below the 1× rate except in a justified individual case agreed in writing before treatment ([BTK](https://www.bundestieraerztekammer.de/d.php?id=285), extract).
  - The only general exception is neutering feral cats ([Berliner Sparkasse](https://www.berliner-sparkasse.de/fi/home/ratgeber/ratgeber-heilberufe/finanzen/abrechnung-tierarztpraxis.html), extract).
  - A practice cannot be financed below 1× ([topagrar](https://www.topagrar.com/betriebsleitung/news/die-finanzierung-einer-tierarztpraxis-ist-bei-abrechnung-unterhalb-des-einfachen-gebuehrensatzes-nicht-moeglich-13496964.html), extract).
- **H6 passes with a design guard.** No interest or instalment premium, easy cancellation, and plan templates that do not bundle more vaccinations than veterinary vaccination guidance recommends. That last point is an over-servicing incentive the lens did not consider (JUDGEMENT).
- **H8 passes.** My two German searches found no practice-run plan. They returned only fee-schedule and insurance pages, e.g. [Allianz](https://www.allianz.de/gesundheit/hundekrankenversicherung/tierarztkosten-hund/) (extract). This agrees with lens 1's three searches.

**C1–C10**

| C | Score | Justification |
|---|---|---|
| C1 | 5 | Owners face 2–3 lumpy prevention bills a year, but plans smooth the *predictable* costs, not the unexpected bills that burden two-thirds of owners ([leinetal24, lens 1](https://www.leinetal24.de/verbraucher/umfrage-mehr-katzen-als-hunde-tierarzt-kosten-steigen-zr-94433587.html)). |
| C2 | 6 | The payer (the practice) is clear, and US practices pay USD 4.35–4.95 per plan ([IDEXX, lens 1](https://idexx-prod-base.django-aws.idexx.com/en/veterinary/software-services/petly-plans/getting-started/pricing)). German revenue depends on owner uptake that the 1× floor makes harder. |
| C3 | 6 | The gap is real: CVS alone has 519k UK members ([CVS RNS, lens 1](https://data.fca.org.uk/artefacts/NSM/RNS/5850272.html)) and no German plans were found. But the rule that explains the gap also removes the demand lever. |
| C4 | 5 | About 5–6k practices can be listed, but vets are hard to reach ([VetStage, lens 1](https://www.vetstage.de/pdf/vetstage-agenturvorstellung.pdf)). Sales are founder-led, in German, with no network. |
| C5 | 6 | About 94% gross margin and LTV/CAC ≈ 8, but practice revenue rests on 30–60 plans per practice, which is unproven. |
| C6 | 8 | About 85 practices, or 1.4–1.7% of the pool. |
| C7 | 6 | The payment partner automates collections. Each practice still needs plan design, staff training and GOT/consumer-law template upkeep. |
| C8 | 6 | Enrolled owners and mandates make it sticky. But IDEXX, Premier Vet Alliance or chains could enter, and a GOT evaluation is under discussion ([Lobbyregister RV0025695](https://www.lobbyregister.bundestag.de/inhalte-der-interessenvertretung/regelungsvorhabensuche/RV0025695), extract, entry dated 25 Jun 2026). |
| C9 | 5 | Four overlapping regimes (GOT, insurance boundary, consumer credit, consumer-contract terms) plus chamber codes and competitor cease-and-desist suits under unfair-competition law (UWG). One specialist opinion answers all of them. |
| C10 | 5 | Letters of intent (LOIs) are quick, but no responsible paid pilot should start before a vet-law opinion (≈€1,000–1,500). |

**What the researcher missed**
- **The GOT floor cuts both ways.** It blocks foreign copies, but it also removes the UK plans' main consumer lever: 10–15% off treatment, as in [Medivet](https://www.medivetgroup.com/medivet-healthcare-plan/) (lens 1). If a practice already bills routine prevention at 1×, a plan offers owners no price advantage, only budgeting and reminders (JUDGEMENT).
- **Rules may change.** A GOT evaluation is under discussion ([Lobbyregister](https://www.lobbyregister.bundestag.de/inhalte-der-interessenvertretung/regelungsvorhabensuche/RV0025695), extract).
- **Member-only pricing has an open legal question.** §2 GOT requires fees within the 1–3× range to reflect the circumstances of the case, and membership is not one of the listed criteria ([GOT](https://www.gesetze-im-internet.de/got_2022/BJNR140100022.html), JUDGEMENT).
- **Practice capacity.** German vets are trending towards employment ([BTK, lens 1](https://www.bundestieraerztekammer.de/presse/2024/08/PM-BTK_Tieraerztestatistik_Deutlicher-Trend-zum-Angestelltenverhaeltnis.pdf)). Practices that are already at capacity value client retention less (JUDGEMENT).
- **Chains still unchecked.** In-house plans at German chains (AniCura, Evidensia/IVC, Fressnapf vets) are still not checked (open gap from lens 1).

**Unit economics (recomputed)**

| Item | Value |
|---|---|
| Price | €2.50 per active plan per month, €99 minimum (lens 1) |
| Realistic uptake | 30–60 plans per practice in years 1–2, so ARPU ≈ €125 (JUDGEMENT: no discount lever) |
| Cost to serve | ≈ €8 per practice per month (hosting, reminder SMS/e-mail, PDFs) (ASSUMPTION) |
| Gross margin | ≈ 94% |
| Fixed costs | ≈ €1,900/month: lens 1's €1,500 plus €150 professional-liability insurance and €250 legal reserve (ASSUMPTION) |
| Customers needed for €8k profit | (8,000 + 1,900) ÷ (125 − 8) ≈ **85 practices** (≈ 4,250 plans) |
| CAC by channel | Field visit and demo ≈ €300 cash + 15 h ≈ €900. Practice-consultant referral (20% of first-year revenue) ≈ €300 + time. Regional CPD evening ≈ €500 per closed practice. |
| Churn | Practice 1%/month. Owner churn after the 12-month term is unknown. |
| LTV (capped at 60 months) / LTV:CAC | ≈ €7,000 / ≈ 7.8 |
| Time to €8k/month | ≈ 28–36 months: legal memo and build take 3–4 months, then 3–4 practices a month, and plans ramp up slowly inside each practice. **Probably misses the 24-month goal.** |

**Top 3 risks**
1. Owners do not join plans that offer no discount.
2. Legal design: GOT, insurance boundary, credit boundary, consumer terms, chamber codes and competitor suits.
3. An incumbent (IDEXX, Premier Vet Alliance, a chain or a practice-software vendor) enters, or the GOT is amended.

**Cheapest 30-day money test.** Buy a €500–800 quick check from a vet-law specialist. Then get 2 practices to offer a paper "Vorsorgeplan", collected through the practice's own payment link at a price that is safe at 1× GOT. **Pass:** ≥20 owners per practice pay month 1 within 30 days, and each practice signs a €99/month LOI.

**Lawyer before launch: YES (vet-law plus consumer-law specialist).** Questions:
1. Is a member rate that is ≥1× but below the practice's usual factor lawful under §§2 and 5 GOT? How must invoices itemise GOT positions for prepaid services?
2. Which plan features would turn it into insurance business under the VAG?
3. Could any instalment or year-end settlement design create a paid financing arrangement under §506 BGB?
4. Do the state vet chambers' professional codes restrict advertising plans or discounts, and what is the exposure to competitor suits under UWG §3a?
5. Can prescription antiparasitics be bundled into a flat fee under the veterinary-medicines pricing and dispensing rules?
6. Consumer terms: minimum term, renewal, the online cancellation button (§312k BGB) and pro-rata settlement. Does the practice or the founder carry liability for the standard-terms templates?

---

### L1-B — Boarder billing, extras logging and arena booking for boarding stables (Germany): **49.0, KILL** (ties BASE)

**Hard rules**
- **H1–H3, H5–H7 pass.** Boarders use the app free, and it is single-sided.
- **H4 is at risk.** Stabley is listed as a free all-in-one stable platform. Its listed features include occupancy, boarder communication *and billing*, and its core functions stay free for stables and riders ([AlternativeTo](https://alternativeto.net/software/stabley/about/), extract). Whether Stabley is the niche's *dominant* incumbent is unknown.
- **H8 passes.** A free tool is not a competitor "at a similar price", and no three funded paid rivals were shown. Horsebook is a further freemium alternative ([AlternativeTo](https://alternativeto.net/software/stabley/), extract).

**C1–C10**

| C | Score | Justification |
|---|---|---|
| C1 | 5 | A monthly invoicing grind for about 35 boarders plus extras; real but not acute, and lost extras are unquantified (lens 1). |
| C2 | 4 | Farm owners are price-sensitive, and free Stabley plus freemium Horsebook anchor willingness to pay near zero. |
| C3 | 3 | Lens 1's "no German billing tool found" is contradicted at listing level. How deep Stabley's billing goes is unverified. |
| C4 | 4 | No association, newsletter or event channel was verified; only farm visits and social groups. |
| C5 | 6 | About 93% gross margin, ARPU ≈ €45, LTV/CAC ≈ 8 on assumptions, but conversion against a free tool is unproven. |
| C6 | 7 | About 220 of roughly 16k operations; the inputs date from 2001–2017 and many stables are tiny. |
| C7 | 7 | Self-serve with month-end peaks. |
| C8 | 3 | A free incumbent can deepen its billing at no cost; invoice history gives only moderate lock-in. |
| C9 | 8 | Low liability; tax responsibility stays with the stable. |
| C10 | 5 | Pre-sales are feasible, but buyers are price-sensitive. |

**What the researcher missed**
- Lens 1 missed Stabley and Horsebook.
- The founder works in English and has no rural network, which is a trust barrier in a farm market (JUDGEMENT).
- Business boarders will fall under the German B2B e-invoicing phase-in (receiving since 2025, issuing from 2027–28 per [lens 2 sources](https://originstamp.com/en/blog/reader/eu-e-invoicing-mandates-timeline-2026-2030)).

**Known issue (a), resolved.** Lens 3 is closer to right on substance: a directory listing says Stabley is free for stables and includes boarder billing. But lens 3's "kill" was a judgement call (Q3/Q5), not a RULEBOOK hard-rule kill. H8 needs three or more *funded or profitable* competitors *at a similar price*, and one free tool does not meet that. Lens 1's gap claim is contradicted. **Net:** L1-B survives the hard rules but drops to 49.0 because C2, C3 and C8 collapse. One hour spent testing Stabley's billing would settle it. If Stabley lacks SEPA files, GoBD-proof numbering or extras logging, L1-B goes back to roughly the low-to-mid 50s, still KILL.

**Unit economics (recomputed)**

| Item | Value |
|---|---|
| Price | €39/€59 → ARPU ≈ €45 (lens 1) |
| Cost to serve | €3 |
| Gross margin | 93% |
| Fixed costs | €1,300 (ASSUMPTION) |
| Customers needed | (8,000 + 1,300) ÷ 42 ≈ **221 stables** |
| CAC by channel | Farm visit ≈ €390. Social ads ≈ €150–250. Boarder referral credit ≈ €45. Blended ≈ €250. |
| Churn | 2%/month |
| LTV / LTV:CAC | ≈ €2,100 / ≈ 8 |
| Time to €8k/month | ≈ 24–30 months |

**Top 3 risks**
1. Free Stabley billing.
2. Low willingness to pay and low digital readiness.
3. No channel to stables.

**Cheapest 30-day money test.** Spend one hour testing Stabley's billing first. Then offer 40 stables in one region a €49 one-off concierge service: "we prepare next month's invoices and your SEPA file". **Pass:** 5 paid.

**Lawyer before launch: NO; a tax adviser is enough (≈€300).** Questions:
- GoBD-compliant invoice numbering and archiving.
- VAT on boarding versus extras.
- SEPA creditor templates.
- E-invoicing for business boarders.

---

### L1-C — Lesson contracts, make-ups and SEPA billing for private music teachers (Germany): **53.5, KILL**

**Hard rules: all pass.**
- H3: no licence is involved.
- H8: the North American leaders (My Music Staff, TutorBird) were not shown to sell in German (lens 1).

**C1–C10**

| C | Score | Justification |
|---|---|---|
| C1 | 4 | Weekly but modest admin pain; standing orders already handle most payments. |
| C2 | 4 | Self-employed teachers are cost-sensitive; €12/month is untested in Germany. |
| C3 | 5 | No German product was found, but the reason may simply be low demand, and the leaders could localise. |
| C4 | 5 | Teacher groups and SEO, plus association channels the lens missed: the German music-teachers' association (Deutscher Tonkünstlerverband) and the private music-schools association (JUDGEMENT, unverified). |
| C5 | 6 | About 93% gross margin and LTV/CAC ≈ 5–11, but a low price ceiling. |
| C6 | 6 | About 550 customers, or roughly 2.2% of a derived pool of about 25k ([MIZ, lens 1](https://miz.org/de/media/666215/download?attachment)). |
| C7 | 8 | Fully self-serve. |
| C8 | 4 | Low switching costs; My Music Staff already has a French site ([lens 1](https://www.mymusicstaff.com/fr/wp-json/wp/v2/posts/31729)). |
| C9 | 8 | Only minors' data and VAT wording. |
| C10 | 6 | Annual founding-member pre-sales are feasible. |

**What the researcher missed**
- The association channels named in C4.
- VAT changes: the teaching exemption was reformed and the small-business threshold changed for 2025. Both affect invoice wording, so a tax adviser must confirm (JUDGEMENT).
- Substitute stack: a generic invoicing tool plus a calendar.

**Unit economics (recomputed)**

| Item | Value |
|---|---|
| Blended ARPU | ≈ €17.5 (85% solo at €12; 15% studio at €49) |
| Cost to serve | ≈ €1.2 |
| Gross margin | 93% |
| Fixed costs | €1,000 |
| Customers needed | (8,000 + 1,000) ÷ 16.35 ≈ **550 customers** |
| CAC by channel | SEO/content €20–40. Groups ≈ €30. Association partnership ≈ €50. Blended €50–100. |
| Churn | 3%/month |
| LTV / LTV:CAC | ≈ €545 / ≈ 5–11 |
| Time to €8k/month | ≈ 20–26 months; sign-ups cluster in September |

**Top 3 risks**
1. Low willingness to pay.
2. My Music Staff or TutorBird localises into German.
3. Seasonal churn.

**Cheapest 30-day money test.** A German landing page with a €99/year founding offer, posted in 5 teacher groups. **Pass:** 30 pre-sales.

**Lawyer before launch: NO; a tax adviser is enough.** Questions:
- VAT-exemption and small-business invoice wording.
- Make-up and notice clauses under German standard-terms law (parents are consumers).
- GDPR for minors' data.

---

### L2-F1 — CRA Logbook: vulnerability-reporting and compliance log for micro hardware/IoT makers (EU, launch Germany): **61.5, TEST**

**Hard rules**
- **H1, H2, H4–H7 pass.** Feeds are public and there is no single gatekeeper. ENISA's Single Reporting Platform has no API, so there is no permission to revoke ([ENISA, lens 2](https://www.enisa.europa.eu/news/the-cra-single-reporting-platform-is-launched)).
- **H3 passes.** The product is records, clocks and templates. Germany's top civil court (BGH) held that a question-driven generator of standard documents is not a legal service under §2(1) of the Legal Services Act (RDG) (BGH I ZR 113/20, 9 Sep 2021; [LTO](https://www.lto.de/recht/juristen/b/bgh-urteil-izr11320-vertragsgenerator-smartlaw-keine-unzulaessige-rechtsdienstleistung-rak-hamburg-rdg-legal-tech), [beck-aktuell](https://www.beck-aktuell.de/heute-im-recht/rechtsprechung/bgh-keine-konkrete-taetigkeit-smartlaw-ist-zulaessig-2021-10-01), extract). The planned "CRA gap call" should stay technical, not a legal review of the customer's case.
- **H8 passes.** Only sbomify sells a comparable CRA wizard at a similar price ([sbomify, lens 2](https://sbomify.com/pricing/)).

**C1–C10**

| C | Score | Justification |
|---|---|---|
| C1 | 6 | 24-hour, 72-hour and 14-day reporting duties have applied since 11 Sep 2026 ([Freshfields](https://www.freshfields.com/en/our-thinking/blogs/technology-quotient/cyber-resilience-act-reporting-obligations-take-effect-on-11-september-2026-102nzmk), extract), and the CE cliff follows on 11 Dec 2027. Actively exploited vulnerabilities are rare events. |
| C2 | 6 | The manufacturer pays to keep EU market access, and a $159–199/month anchor exists. Micro firms' willingness to pay is untested. |
| C3 | 6 | SME-priced CRA workflow tooling is thin today, but the gap will close in 2027. |
| C4 | 6 | Cheap named channels exist, and they work in English, which suits this founder: an open-source GitHub Action, maker communities, chamber of commerce (IHK) and federal IT-security office (BSI) events, and test labs. |
| C5 | 7 | About 93% gross margin, ARPU €85, LTV/CAC ≈ 5–13. |
| C6 | 8 | About 127 customers, or 1.6% of Germany's computer/electronics/optical manufacturers alone ([Statista, lens 2](https://statista.com/statistics/383747/enterprises-manufacturing-computer-electronic-optical-products-germany)); far less EU-wide. |
| C7 | 6 | Feeds and clocks are automated; alert reliability and regulatory-interpretation questions add load. |
| C8 | 5 | Every SBOM vendor will add CRA features in 2027; 10-year records give some lock-in. |
| C9 | 6 | The Art. 14 clock runs from the manufacturer's *awareness*, so a missed match does not itself breach a deadline (JUDGEMENT). B2B liability caps are workable. |
| C10 | 6 | €490 founding pre-sales to makers preparing for Dec 2027 are plausible within 90 days. |

**What the researcher missed**
- **No postponement.** I found no evidence that the Digital Omnibus postponed the Dec 2027 date. The omnibus material is about a single entry point for incident reporting ([Osborne Clarke](https://www.osborneclarke.com/insights/regulatory-outlook-november-2025-cyber-security); [Freshfields](https://www.freshfields.com/en/our-thinking/blogs/technology-quotient/cyber-resilience-act-reporting-obligations-take-effect-on-11-september-2026-102nzmk); [Steptoe](https://www.steptoe.com/en/news-publications/steptechtoe-blog/cra-countdown-european-commission-publishes-draft-guidance-highlighting-fast-approaching-deadlines.html), extract). Slip risk is lower than lens 2 feared.
- **The micro/small fine relief is narrow.** On my reading of Art. 64(10)(a), only a missed **24-hour early warning** is exempt from fines. The 72-hour notification and the final report are not ([CRA](https://eur-lex.europa.eu/eli/reg/2024/2847/oj), STATUTE not fetched, JUDGEMENT). Lens 2 treated the exemption as dampening urgency more than it does.
- **Penalty tiers, which resolve lens 2's conflict** (same source, JUDGEMENT):
  - €15m or 2.5% of turnover for the Annex I essential requirements and Arts 13–14;
  - €10m or 2% for other obligations, including importers and distributors;
  - €5m or 1% for misleading information.
- **The founder's own CRA exposure.** If the CLI or GitHub Action is *monetised*, it is itself a product with digital elements, and the founder becomes a manufacturer with reporting duties (JUDGEMENT). Keep it free open-source, or keep the product SaaS-only.
- **Legacy products.** Products already on the market are in scope for reporting ([cyberresilienceact.eu](https://www.cyberresilienceact.eu/es/news/legacy-products-in-scope-cra-reporting-11-september-2026.html), extract). This supports pain today.

**Unit economics (recomputed)**

| Item | Value |
|---|---|
| ARPU | €85 |
| Cost to serve | €6 (feeds/compute €3, alerts €1.50, payment fees €1.50) |
| Gross margin | 93% |
| Fixed costs | €2,000 (adds €200 professional-indemnity insurance and €300 events) |
| Customers needed | (8,000 + 2,000) ÷ 79 ≈ **127** |
| CAC by channel | Open-source-driven inbound ≈ €50–100 (time). Webinars with an IHK ≈ €150. Outbound to makers ≈ €400. Test-lab referral ≈ €200. Blended ≈ €300. |
| Churn | 2%/month |
| LTV / LTV:CAC | ≈ €3,950 / ≈ 13 (stress case: €500 CAC and 3% churn → ≈ 5.3) |
| Time to €8k/month | ≈ 15–20 months; demand rises through 2027 |

**Top 3 risks**
1. Micro makers lack willingness to pay or awareness.
2. Crowding and free tools during 2027 (open-source toolkits, GitHub, BSI guidance).
3. False-comfort claims, plus the founder's own CRA scope.

**Cheapest 30-day money test.** Release a free open-source "cra-clock" plus a €490/year founding plan, and e-mail 150 makers found on Tindie, Crowd Supply and IHK lists. **Pass:** 5 prepaid.

**Lawyer before launch: YES, a light check (≈€500–1,000).** Questions:
1. Do the declaration-of-conformity, vulnerability-disclosure-policy and support-period templates stay inside the BGH Smartlaw line?
2. Does the CRA apply to the founder's own CLI?
3. B2B liability caps: gross negligence cannot be excluded.
4. Do the vulnerability feeds (NVD, OSV, EUVD, CISA catalogue) allow commercial use?
5. Exposure under the new EU Product Liability Directive for B2B SaaS.

---

### L2-F2 — CRA compliance vault for small importers/distributors of connected products (EU): **48.5, KILL**

**Hard rules: all pass.** H8 passes only on thin evidence ([lens 2](https://www.springlex.eu/en/packages/cra/cra-regulation/article-19/)).

**C1–C10**

| C | Score | Justification |
|---|---|---|
| C1 | 4 | Binding only for products placed on the market from 11 Dec 2027. The EU General Product Safety Regulation (GPSR) already requires similar document checks (JUDGEMENT). |
| C2 | 4 | Shop owners would pay, but awareness and urgency are low 14 months out. |
| C3 | 4 | The gap rests on absence of evidence; GPSR responsible-person services sit next door. |
| C4 | 5 | Agencies, IHK events and shop-system communities; all unvalidated. |
| C5 | 6 | About 93% gross margin, ARPU €55, LTV/CAC ≈ 8 on assumptions. |
| C6 | 6 | About 194 of an unverified pool of at least 10k. |
| C7 | 7 | Simple records, reminders and exports. |
| C8 | 3 | Easy for GPSR, legal-text and marketplace players to copy. |
| C9 | 6 | Deterministic checks, but they can give false comfort. The fines for importers (€10m or 2%, JUDGEMENT) fall on the customer, not the founder. |
| C10 | 4 | Pre-sales are hard this far from the deadline. |

**What the researcher missed**
- The GPSR overlap.
- Stock placed on the market before Dec 2027 is out of scope.
- The penalty tier above.
- Own-brand importers become manufacturers and are L2-F1 customers instead (JUDGEMENT).

**Unit economics (recomputed)**

| Item | Value |
|---|---|
| ARPU | €55 |
| Cost to serve | €4 |
| Gross margin | 93% |
| Fixed costs | €1,900 |
| Customers needed | **≈ 194** |
| CAC | ≈ €250 |
| Churn | 2.5%/month |
| LTV / LTV:CAC | ≈ €2,040 / ≈ 8 |
| Time to €8k/month | 24+ months; demand only from mid-2027 |

**Top 3 risks**
1. All value is tied to the Dec 2027 deadline.
2. Copycats.
3. False comfort: supplier documents can be forged.

**Cheapest 30-day money test.** A €290/year founding offer to 100 smart-home shops through 2 agencies. **Pass:** 3 prepaid.

**Lawyer before launch: YES, a light check.** Questions:
- Scope of CRA Arts 19–21 versus the GPSR.
- Liability for checklists marked "complete".
- Offering 10-year retention as a service.

---

### L2-F3 — Battery Passport Lite for small LMT (e-bike) and industrial battery assemblers (EU): **51.0, KILL**

**Hard rules**
- **H1–H7 pass.**
- **H8 is at risk.** Several digital-product-passport vendors already exist; their SME pricing is unknown (lens 2).

**Verified status**
- The 18 Feb 2027 passport date is unchanged.
- The Council's environmental omnibus touches battery removability, not the passport ([projetcelsius FAQ](https://projetcelsius.com/en/faq/dpp-espr-affichage-env/l-echeance-du-18-fevrier-2027-peut-elle-etre-reportee/), extract).
- The Commission missed its 18 Aug 2026 deadline for the implementing act that defines who has a legitimate interest in restricted passport data ([battery-tech.net](https://battery-tech.net/why-the-eu-is-about-to-miss-its-own-battery-passport-deadline-while-industrys-stays-fixed/), extract).
- Due diligence moved to 18 Aug 2027 ([Arianee](https://www.arianee.com/en/blog/battery-due-diligence-august-2027), extract).

**C1–C10**

| C | Score | Justification |
|---|---|---|
| C1 | 6 | A hard market-access gate on 18 Feb 2027 for every LMT battery, every industrial battery over 2 kWh and every EV battery. |
| C2 | 6 | The assembler pays, and a per-battery fee is small next to the battery's value. |
| C3 | 4 | Several passport vendors exist; their SME pricing is unknown and crowding is likely. |
| C4 | 4 | Niche workshops and trade fairs; no verified cheap channel. |
| C5 | 6 | About 90% gross margin and ARPU €180, but heavy onboarding and a small pool. |
| C6 | 4 | About 64 of an unverified 1–3k pool, i.e. 2–6%. |
| C7 | 4 | Uptime and continuity duties, a specification that is still moving (the implementing act is late), and data mapping per customer. |
| C8 | 6 | Switching costs are high once passports are issued. |
| C9 | 3 | A one-person company becomes the single point of failure for other firms' legal market access, for years. |
| C10 | 7 | The deadline 4 months away makes pre-sales feasible. |

**What the researcher missed**
- The late implementing act.
- The omnibus scope.
- How a continuity or escrow duty would interact with a one-person company's insolvency (JUDGEMENT).
- German penalty amounts under the national implementing law are still unverified.

**Unit economics (recomputed)**

| Item | Value |
|---|---|
| ARPU | €180 |
| Cost to serve | €18 |
| Gross margin | 90% |
| Fixed costs | €2,400 (adds escrow and higher insurance) |
| Customers needed | **≈ 64** |
| CAC | ≈ €750 |
| Churn | 1%/month |
| LTV (capped at 60 months) / LTV:CAC | ≈ €9,700 / ≈ 13 |
| Time to €8k/month | ≈ 18–24 months, *if* the pool exists |

**Top 3 risks**
1. Continuity liability.
2. Specification churn.
3. A small pool plus crowding.

**Cheapest 30-day money test.** A €990/year founding plan to 50 LMT assemblers. **Pass:** 3 prepaid, plus 1 paid €300 data-mapping pilot.

**Lawyer before launch: YES, before signing any customer.** Questions:
1. Do Arts 77–78 require passports to stay available after the responsible operator ceases to exist, and who must fund that (escrow)?
2. Can the founder act as the operator's mandated service provider?
3. Liability caps for lost market access.
4. National penalties.
5. Access tiers while the implementing act is pending.

---

### L3-A — Audit-ready substrate and EEG-bonus evidence log for biogas plants (Germany): **59.0, KILL** (borderline)

**Hard rules**
- **All pass.**
- **H8 is at risk.** Three specialised vendors already exist: [Nabisy Software](https://nabisy-software.de/biogasanlagen-betreiber), [TerraVis](https://www.terravis-biogas.de/dienstleistungen/gocero2/digitale-massenbilanzierung) and [Biotaktix](https://www.biotaktix.de/en/) (lens 3). Their funding, profitability and prices are unknown.

**C1–C10**

| C | Score | Justification |
|---|---|---|
| C1 | 7 | Daily logging, a 28 February deadline and permanent loss of the bonus once conditions are not met ([WEMAG/Kremp, lens 3, 2019](https://www.wemag.com/sites/default/files/4_kremp_ug_im_eeg_2017_wemag_2019.pdf)). |
| C2 | 7 | The operator pays, and €790/year is small next to a reported ≈€15k verifier bill ([topagrar, lens 3, one-plant anecdote](https://www.topagrar.com/betriebsleitung/news/biogas-im-wuergegriff-der-buerokratie-b-20001963.html)). |
| C3 | 4 | Three vendors already digitise the diary, and free Excel templates persist. |
| C4 | 5 | Named channels exist (verifiers, the biogas association's regional groups, topagrar), but competitors use them too and the founder is an English-speaking outsider. |
| C5 | 7 | About 85% gross margin and LTV/CAC ≈ 6–9; price is small next to value. |
| C6 | 8 | About 183 of 9,605 plants, i.e. 1.9% ([topagrar census, lens 3](https://www.topagrar.com/energie/news/biogasbranche-2025-neue-zahlen-zeigen-grosses-potenzial-politik-bremst-ausbau-a-20023918.html)). |
| C7 | 6 | Several EEG versions and a deadline-season support peak. |
| C8 | 4 | Easy to copy, and the pool shrinks as 20-year EEG terms end. |
| C9 | 5 | A wrong evidence pack can cost a bonus worth more than years of fees. Cap liability and insure. |
| C10 | 6 | Prepaid founding plants before 28 Feb are feasible through verifiers. |

**What the researcher missed**
- Professional-liability insurance and a B2B liability cap are needed. Gross negligence cannot be excluded even between businesses (JUDGEMENT).
- The language and trust barrier with farm operators.
- Trade-fair costs.
- Post-EEG tender paths may keep the diary relevant (JUDGEMENT, unverified).

**Unit economics (recomputed)**

| Item | Value |
|---|---|
| ARPU | €65.8 (€790/year) |
| Cost to serve | €10 |
| Gross margin | 85% |
| Fixed costs | €2,200 |
| Customers needed | **≈ 183** |
| CAC by channel | Verifier referral ≈ €150 + time. Regional association meeting ≈ €300–500. Trade fair ≈ €800. Blended ≈ €600. |
| Churn | 1%/month |
| LTV (capped at 60 months) / LTV:CAC | ≈ €3,350 / ≈ 5.6 (≈ 9 uncapped) |
| Time to €8k/month | ≈ 24–30 months; sales cluster in October–February |

**Top 3 risks**
1. Competitors plus Excel.
2. Liability for a lost bonus.
3. A shrinking pool plus the trust barrier.

**Cheapest 30-day money test.** Contact 10 environmental verifiers and ask each for 2 introductions. **Pass:** 5 plants prepay a €390 founding year.

**Lawyer before launch: NO, but needs a terms review plus insurance (≈€500).** Questions:
- Which EEG versions' diary formats do grid operators accept?
- Liability cap clause.
- Retention of entries.

---

### L3-B — Parent-duty rosters, hours ledger and board handover for parent-run daycares (Germany, Berlin first): **55.5, KILL**

**Hard rules: all pass.** No child data is stored (lens 3).

**C1–C10**

| C | Score | Justification |
|---|---|---|
| C1 | 5 | Weekly coordination and board handover; the intensity is assumed, not evidenced. |
| C2 | 4 | The association has a budget, but volunteer boards and free tools (Doodle, Spond, WhatsApp) anchor willingness to pay low. |
| C3 | 5 | No product for this workflow was found, but "good enough" free tools may be the reason. |
| C4 | 6 | Dense, cheap channels — if they cooperate: the Berlin umbrella body DaKS (≈800 small self-managed facilities in an older figure, [DaKS](https://www.daks-berlin.de/system/files/media/files/PM_Warnstreik_final.pdf)) and the national umbrella body BAGE ([BAGE](https://www.lobbyregister.bundestag.de/suche/R003613)) (lens 3). |
| C5 | 6 | About 86% gross margin and LTV/CAC ≈ 7–10, but board turnover drives churn. |
| C6 | 5 | About 226 of 5,000–7,500, i.e. 3–4.5%. |
| C7 | 8 | Simple domain, minimal data. |
| C8 | 4 | Daycare apps could add a roster. |
| C9 | 8 | Low liability. |
| C10 | 6 | Berlin density allows paid pilots, but the daycare year starts in August. |

**What the researcher missed**
- Whether charges per missed duty hour are enforceable depends on the association's statutes versus the care contract, and on German standard-terms law (JUDGEMENT).
- Umbrella bodies may not endorse any vendor.

**Unit economics (recomputed)**

| Item | Value |
|---|---|
| ARPU | €49 |
| Cost to serve | €7 |
| Gross margin | 86% |
| Fixed costs | €1,500 |
| Customers needed | **≈ 226** |
| CAC | ≈ €200 |
| Churn | 2%/month |
| LTV / LTV:CAC | ≈ €2,100 / ≈ 10 |
| Time to €8k/month | ≈ 24–30 months; onboarding is seasonal |

**Top 3 risks**
1. Free tools are good enough.
2. A small pool plus board churn.
3. Umbrella bodies do not cooperate.

**Cheapest 30-day money test.** Offer DaKS a free workshop. **Pass:** 5 boards buy a €490/year founding plan.

**Lawyer before launch: NO.** A light check of charges for missed duty hours is enough.

---

### L3-C — Self-administration for small Swiss condominium communities (STWEG): **52.5, KILL**

**Hard rules**
- **H1–H7 pass.** Software alone needs no fiduciary licence (JUDGEMENT).
- **H8 is at risk.** Direct or adjacent players found:
  - EinfachSTWEG, from CHF 30/month ([site](https://einfachstweg.ch/), vendor claim, lens 3);
  - [LIMMOBI](https://limmobi.ch/de/stockwerkeigentum/);
  - a CHF 195 one-off Excel tool (lens 3);
  - Woonig's STWE module with owner e-voting ([App Store](https://apps.apple.com/app/id1476238924), extract);
  - [ImmoApp](https://apps.apple.com/ee/app/immoapp/id1493436309);
  - professional suites: [Abacus AbaImmo](https://www.ABACUS.ch/fileadmin/ablage/02_dokumente/01_flyer/de/flyer_abacus_abaimmo-immobilienbewirtschaftung_de.pdf) (extract) and ImmoTop2, distributed by the owners' association HEV ([HEV](https://www.hev-schweiz.ch/vermieten/verwalten/immobilien-software/software-immotop2/)).

  Funding and profitability are unknown, so "≥3 funded or profitable" is not proven.

**C1–C10**

| C | Score | Justification |
|---|---|---|
| C1 | 6 | Monthly billing, annual accounts and meetings, while administrators turn down small mandates ([NZZ, lens 3](https://www.nzz.ch/wirtschaft/hoher-aufwand-wenig-ertrag-viel-streit-warum-kleine-eigentuemergemeinschaften-kaum-noch-verwalter-finden-ld.1892411)). |
| C2 | 6 | The owners pay, and a CHF 30/month anchor exists. |
| C3 | 4 | Several Swiss tools already serve self-administrators. It is the German WEG pattern at an earlier stage. |
| C4 | 3 | No neutral channel (HEV pushes ImmoTop2), expensive Swiss paid search, a foreign founder and three languages. |
| C5 | 6 | About 78% gross margin and LTV/CAC ≈ 8. |
| C6 | 8 | About 366 of roughly 97k communities; the self-administered share is unknown. |
| C7 | 6 | Swiss accounting nuances and a January–April peak. |
| C8 | 5 | The ledger creates lock-in, but competitors offer much the same. |
| C9 | 6 | Bookkeeping errors turn into owner disputes; Swiss VAT registration is needed (JUDGEMENT). |
| C10 | 4 | A trust-sensitive market, so pre-sales will be slow. |

**Known issue (b), resolved: yes, the same logic applies, partly.**
- **Germany.** The WEG kill rested on two things. First, a funded player (Dotega, €1.3m pre-seed) holds the main owners'-association channel ([HTGF](https://www.htgf.de/dotega-pre-seed-finanzierung/); [it-boltwise](https://www.it-boltwise.de/?p=1548390), lens 1). Second, long-established profitable tools serve self-managers.
- **Switzerland shows the same structure at an earlier stage.** The main owners' association channel is again taken: HEV distributes ImmoTop2. At least two direct self-administration tools exist, plus e-voting and professional suites.
- **Rulebook result.** H8 is not triggered, because ≥3 *funded or profitable* direct rivals are not shown. But C3, C4 and C8 are low, so the idea lands in KILL on score, not on a hard rule.

**What the researcher missed**
- Woonig, ImmoApp and Abacus.
- Swiss VAT: a foreign supplier must register once worldwide turnover passes CHF 100k (JUDGEMENT).

**Unit economics (recomputed)**

| Item | Value |
|---|---|
| ARPU | ≈ €37 (CHF 35; exchange rate is an ASSUMPTION) |
| Cost to serve | €8 |
| Gross margin | 78% |
| Fixed costs | €2,600 (adds Swiss VAT administration and native-speaker support) |
| Customers needed | **≈ 366** |
| CAC by channel | Swiss paid search ≈ €400–600. SEO templates ≈ €100–150. Blended ≈ €350. |
| Churn | 1%/month |
| LTV / LTV:CAC | ≈ €2,900 / ≈ 8 |
| Time to €8k/month | ≈ 24–30 months |

**Top 3 risks**
1. Incumbents and the HEV channel.
2. High CAC for a foreign founder.
3. Bookkeeping disputes.

**Cheapest 30-day money test.** A German landing page with 5 templates and CHF 500 of ads, offering a CHF 290 founding year. **Pass:** 3 prepaid.

**Lawyer before launch: NO; a Swiss tax adviser YES.** Questions:
- VAT registration and a tax representative.
- Liability limits under the Swiss Code of Obligations: gross negligence cannot be excluded (Art. 100 OR, JUDGEMENT).
- Governing law.

---

### L4-F1 — Care-home financing case manager for social-assistance and Pflegewohngeld applications (NRW; the care home pays): **64.0, TEST** (my €10,000 bet)

**Hard rules**
- **H1, H2, H5, H7 pass.** The home has a direct, quantified money reason ([PwC 2026, lens 4](https://www.pwc.de/de/pressemitteilungen/2026/fehlende-liquiditaet-in-pflegeheimen-gefaehrdet-die-versorgung.html)).
- **H3 passes, but only with the right design.** Three layers:
  1. **The founder.** The founder sells software. Under BGH Smartlaw (I ZR 113/20), a question-driven generator of standard documents is not a legal service under §2(1) RDG ([LTO](https://www.lto.de/recht/juristen/b/bgh-urteil-izr11320-vertragsgenerator-smartlaw-keine-unzulaessige-rechtsdienstleistung-rak-hamburg-rdg-legal-tech); [RAK Hamburg press release](https://www.rak-hamburg.de/uploads/file/282565_Presseerkl%C3%A4rung%20vom%2009.09.2021.pdf), extract).
  2. **The home's staff.** When staff use the tool, they act in residents' own legal matters. Form-filling and document-chasing need little legal examination, and §5 RDG permits legal services that are ancillary to a main activity ([§5 RDG](https://www.gesetze-im-internet.de/rdg/__5.html), STATUTE not fetched). Counsel must confirm.
  3. **Representation.** Under §13 of Social Code Book X (SGB X), authorities may demand written proof of authority. They must reject representatives who provide legal services the RDG does not allow ([§13 SGB X](https://www.gesetze-im-internet.de/sgb_10/__13.html), STATUTE not fetched). A Bavarian decision on a social-assistance care case held an objection inadmissible because written authority was missing. The defect could not be cured afterwards ([gesetze-bayern.de](https://www.gesetze-bayern.de/Content/Pdf/Y-300-Z-BECKRS-B-2024-N-28787?all=False), extract only; fetch failed).

  → So the product must keep the family or legal guardian as the applicant. It must capture valid written authority (a power of attorney or the guardian's court appointment) before the home submits anything.
- **H4 passes.** Government online forms (OZG) could commoditise the forms, but not document-chasing, renewals or the receivables view.
- **H6 passes, with conditions.** The home wants to be paid fast. Families may want to protect gifts and assets, or fear having to pay towards a parent's care. So: no success fees (lens 4's design), no advice on assets, and the family controls what is shared.
- **H8 passes.**
  - My search found no software for the home's side ([betanet](https://www.betanet.de/hilfe-zur-pflege.html), extract).
  - Large operators publish paper checklists and model letters instead ([Agaplesion checklist](https://www.hdv.agaplesion.de/fileadmin/Agaplesion_hdv-darmstadt/Infomaterial/Checkliste_Sozialhilfetraeger_AGA_WuP_web.pdf), extract).
  - The only funded player (Myosotis) sells to public offices ([startbase, lens 4](https://www.startbase.de/news/105-millionen-euro-fuer-myosotis/)).

**C1–C10**

| C | Score | Justification |
|---|---|---|
| C1 | 8 | €3,108–3,427 a month accrues ([vdek, lens 4](https://www.vdek.com/presse/pressemitteilungen/2025/pflegeheim-monatliche-eigenbeteiligung-steigt-stationaere-pflege.html)) while ≈27% of social-welfare offices that answered a 2025 broadcaster survey (ARD) take 6–12 months to decide ([Ärzteblatt, lens 4](https://www.aerzteblatt.de/news/antragsstau-zur-pflege-in-sozialamtern-affb0712-f301-4506-b133-ea19da7c2365)). |
| C2 | 7 | The homes' money reason is quantified: 55% name the social-welfare office as their largest debtor, 1 in 5 has ≥€100k outstanding, and staff spend 8.3 hours a week on open items ([PwC](https://www.pwc.de/de/pressemitteilungen/2026/fehlende-liquiditaet-in-pflegeheimen-gefaehrdet-die-versorgung.html)). There is no direct proof yet that homes buy software for this. |
| C3 | 7 | 60% of those homes blame missing documents ([Apotheken Umschau, lens 4](https://www.apotheken-umschau.de/gesundheitspolitik/pflegeheime-warten-monatelang-auf-hilfe-zur-pflege-von-sozialaemtern-1539809.html)); no home-side tool surfaced, and homes use paper checklists. |
| C4 | 5 | Homes can be listed, but the founder must cold-call busy administrators in German, and chains buy centrally. |
| C5 | 7 | About 89% gross margin, ARPU €179, LTV/CAC ≈ 10. |
| C6 | 9 | About 65 homes, or 0.6% of about 11,250 long-term-care homes ([Curacon/Destatis, lens 4](https://www.curacon.de/fileadmin/user_upload/Curacon/Downloads/Produktbeispiel_sAHBenchmark_Max.pdf)). |
| C7 | 5 | A form library spanning many offices, support calls from relatives, and duties for special-category data (GDPR Art. 9) and impact assessments (DPIA). |
| C8 | 6 | Case history creates lock-in, and the draft reform adds a tailwind. Myosotis or the homes' ERP vendors could copy. |
| C9 | 4 | Special-category data of vulnerable people, the RDG boundary, and reputational exposure from conflicts of interest. |
| C10 | 6 | €99 paid pilots within 90 days are plausible after a quick legal check. |

**What the researcher missed**
- **Two aid types, two start rules** (JUDGEMENT; statutes not fetched):
  - Care assistance under chapter 7 of Social Code Book XII (Hilfe zur Pflege) starts once the social-welfare office *knows* of the need ([§18 SGB XII](https://www.gesetze-im-internet.de/sgb_12/__18.html)).
  - Old-age basic income (chapter 4) needs an *application*, which reaches back to the first of that month ([§44 SGB XII](https://www.gesetze-im-internet.de/sgb_12/__44.html)).
  - So the "date-securing" letter matters most for basic income and for NRW Pflegewohngeld. Lens 4's line that aid "generally" starts at the application date oversimplifies.
- **Which office is responsible.** It is usually the office for the resident's last home address *before* admission ([Schwalm-Eder-Kreis](https://schwalm-eder-kreis.de/Home/Barrierefreiheit.htm/Aemter/50-4-SGB-XII-Hilfe-zur-Pflege.html), extract). The form library must follow residents' previous addresses, not the home's location, so it will spill beyond NRW.
- **Reform direction is a tailwind.**
  - A draft care-reform law was presented on 3 Jun 2026, planned for 1 Jan 2027. It would start the full 75% co-payment subsidy after 54 instead of 36 months ([check24](https://www.check24.de/pflegeversicherung/pflegereform/); [gegen-hartz](https://www.gegen-hartz.de/news/3-245-euro-fuers-pflegeheim-ab-2027-zahlen-rentner-laenger-selbst), extract; not enacted).
  - That means more residents would need care assistance.
  - The long-term threat is a cap on co-payments. The Saarland premier is demanding a cap at €1,500 ([AOK](https://www.aok.de/pp/gg/update/pflegereform-und-eigenanteile/), extract).
- **Substitutes.** Paper checklists and model letters ([Agaplesion](https://www.hdv.agaplesion.de/fileadmin/Agaplesion_hdv-darmstadt/Infomaterial/Checkliste_Sozialhilfetraeger_AGA_WuP_web.pdf)), plus the social-welfare office's own statutory duty to advise.
- **Data protection.** A data-protection impact assessment (GDPR Art. 35) is almost certainly mandatory. The founder is a processor (Art. 28) and can be fined directly (JUDGEMENT; [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj)).

**Unit economics (recomputed)**

| Item | Value |
|---|---|
| Price | €129 / €179 / €249 by bed band → ARPU €179 (lens 4) |
| Cost to serve | ≈ €20/month: encrypted storage, SMS/e-mail to families, support tooling |
| Gross margin | ≈ 89% |
| Fixed costs | ≈ €2,300/month: adds €400 freelance German social-law specialist, €250 cyber and professional-liability insurance, €300 legal/data-protection officer (ASSUMPTION) |
| Customers needed | (8,000 + 2,300) ÷ (179 − 20) ≈ **65 homes** |
| CAC by channel | Outbound calls/e-mail plus demo ≈ €600. On-site visit ≈ €1,000. Factoring firm or care-home consultancy referral (20% of first-year revenue) ≈ €430. Blended ≈ €900. |
| Churn | 1.25%/month (closures, takeovers by chains) |
| LTV (capped at 60 months) / LTV:CAC | ≈ €9,500 / ≈ 10 |
| Time to €8k/month | ≈ 18–22 months: pilots by month 4, then about 4 homes a month. **Inside the 24-month goal, but tight.** |

**Top 3 risks**
1. Legal design and ethics: RDG, rules on who may represent residents, special-category data, and the home-versus-family conflict.
2. Distribution in German to busy administrators, with no network.
3. Myosotis or an ERP vendor copies it, or the reform changes direction.

**Cheapest 30-day money test.** Run a concierge "complete file" service for 3 NRW homes at €99/month, with a native-speaking freelancer: checklists, family document requests and status letters, run from a spreadsheet. **Pass:** 3 paying homes, or 5 LOIs that state a price.

**Lawyer before launch: YES (social-law plus data-protection specialist, ≈€1,500–2,500).** Questions:
1. Is home staff's preparation and submission of residents' applications an allowed ancillary service under §5 RDG, or must the family or guardian always be the applicant? Does the checklist and letter generator stay inside the Smartlaw line?
2. What written authority does §13 SGB X require for the home to submit, follow up or object? Can e-signatures or a guardian's appointment order be relied on? (See the Bavarian decision.)
3. Can the home's notice establish "knowledge" under §18 SGB XII, and can the home file the NRW Pflegewohngeld application on the resident's behalf?
4. GDPR: what is the legal basis for families' financial data and care-grade health data (explicit consent under Art. 9(2)(a) versus 9(2)(h))? Is a DPIA mandatory? What are the processor terms, retention rules and deletion rules?
5. Ethics and conflicts of interest: what product rules stop the home pressuring families over gifts and parents' maintenance?
6. Dunning templates sent to residents: compatibility with the residential care-contract law (WBVG).
7. The founder's liability if a wrong checklist delays aid.

---

### L4-F2 — Case tool for the workplace representative for disabled employees (SBV) (Germany; the employer pays): **52.0, KILL**

**Hard rules**
- **H1, H2, H4, H7 pass.**
- **H3 passes.** Three supports (JUDGEMENT; statutes not fetched):
  - The RDG says that discussing legal questions with employees' elected representatives is not a legal service ([§2(3) Nr. 3 RDG](https://www.gesetze-im-internet.de/rdg/__2.html)).
  - Helping employees apply for disability recognition and equal status is a statutory SBV task ([§178(1) SGB IX](https://www.gesetze-im-internet.de/sgb_9_2018/__178.html)).
  - Self-service letters fall under the Smartlaw logic ([LTO](https://www.lto.de/recht/juristen/b/bgh-urteil-izr11320-vertragsgenerator-smartlaw-keine-unzulaessige-rechtsdienstleistung-rak-hamburg-rdg-legal-tech)).
- **H5 is borderline.** The employer pays because §179(8) of Social Code Book IX obliges it to bear the SBV's costs ([§179 SGB IX](https://www.gesetze-im-internet.de/sgb_9_2018/__179.html); [betriebsrat.de, lens 4](https://www.betriebsrat.de/betriebsratslexikon/sbv/kosten-der-amtsfuehrung)), not because it feels the pain.
- **H6 passes, with conditions.** No marketing on levy savings, which would pressure employees to disclose a disability, and no employer access to the data.
- **H8 passes.** Works-council software suites are still unchecked.

**C1–C10**

| C | Score | Justification |
|---|---|---|
| C1 | 6 | Disability-degree procedures take 3–9 months and protections can be lost, but each employee's case is episodic. |
| C2 | 4 | The employer pays only if persuaded the tool is "necessary", and it can offer its own tools instead. There is no spending evidence. |
| C3 | 5 | No SBV-specific product was found; works-council suites are unchecked. |
| C4 | 5 | Public-sector SBV web pages, seminar providers and the 2026 election wave ([DGB, lens 4](https://www.dgb.de/fileadmin/download_center/Aufrufe/Aufruf_SBV-Wahl_2026.pdf)). |
| C5 | 6 | About 91% gross margin and LTV/CAC well above 3 on paper, but ARPU is only €39–45 and employer approval inflates CAC. |
| C6 | 7 | About 227 of an assumed 20–40k SBVs. |
| C7 | 6 | Simple workflows, but health-data security and deadline rules. |
| C8 | 5 | Works-council suites could add a module; 4-year terms help retention. |
| C9 | 4 | Special-category health data, an unclear data controller (employer or SBV), pressure from employers for access, and liability for deadline errors. |
| C10 | 4 | Employer purchase orders slow pre-sales. |

**What the researcher missed**
- The §2(3) Nr. 3 RDG carve-out, which helps legality.
- **Who is the data controller is unsettled.** For works councils, the employer has been the controller since 2021 ([§79a BetrVG](https://www.gesetze-im-internet.de/betrvg/__79a.html), STATUTE not fetched). If the same applies to the SBV, it collides with the "no employer access" design (JUDGEMENT).
- The employer usually chooses *which* tools it provides (JUDGEMENT).
- Public procurement rules apply in the public sector.
- The presumed-receipt rule for official letters may now be 4 days (lens 4 flagged it; JUDGEMENT).

**Unit economics (recomputed)**

| Item | Value |
|---|---|
| ARPU | ≈ €45 (blended tiers) |
| Cost to serve | €4 |
| Gross margin | 91% |
| Fixed costs | €1,300 |
| Customers needed | **≈ 227** |
| CAC by channel | Seminar affiliate ≈ €95. Outbound ≈ €150 plus approval friction. Blended ≈ €200 (stress case €400). |
| Churn | 1%/month |
| LTV / LTV:CAC | ≈ €4,100 / ≈ 10–20 |
| Time to €8k/month | ≈ 24–30+ months |

**Top 3 risks**
1. The employer refuses to pay.
2. GDPR: the controller question and health data.
3. A small, uncounted pool.

**Cheapest 30-day money test.** Contact 100 public-sector SBVs with a €468/year plan and a ready-made cost request. **Pass:** 3 employer purchase orders.

**Lawyer before launch: YES (labour plus data-protection law).** Questions:
1. Who is the controller for SBV data?
2. What is the legal basis for health data (Art. 9(2)(b) GDPR, and §26(3) BDSG after the EU court's ruling in C-34/21)?
3. Is a third-party SaaS "necessary" under §179(8) SGB IX?
4. Is there a co-determination right if the employer procures it?
5. Deadline rules for objections and presumed receipt.

---

### L4-F3 — Tenant benefit-deadline assistant (Germany; the landlord pays): **47.5, KILL**

**Hard rules**
- **H1, H2, H5, H7, H8 pass.**
- **H3 passes, subject to counsel.** It gives general information plus a generic letter, which fits the Smartlaw logic.
- **H4 is at risk.**
  - The dominant housing ERP vendor could add a notice and QR code cheaply; lens 4 rated this the highest exposure.
  - Jobcenters' own digital channels are a free substitute (JUDGEMENT).
- **H6 is at risk.** A landlord learning which tenants receive benefits is close to surveillance. Consent given to one's own landlord is unlikely to be "freely given" because of the power imbalance (JUDGEMENT; [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj)). It passes only if the landlord sees aggregates and never individual benefit status.

**C1–C10**

| C | Score | Justification |
|---|---|---|
| C1 | 6 | An average €907 back-payment ([inFranken, lens 4](https://www.infranken.de/ratgeber/karriere-geld/3000-euro-nebenkosten-warum-wohnen-in-deutschland-immer-teurer-wird-art-6350661)) can become arrears if the due-month rule is missed ([gegen-hartz, an advocacy source, lens 4](https://www.gegen-hartz.de/buergergeld-nachzahlung-fuer-nebenkosten-und-heizung-was-zahlt-das-jobcenter)). |
| C2 | 4 | The landlord's loss is unquantified, and social-management budgets are small. |
| C3 | 4 | Only one search was run; ERP and tenant portals are unchecked. |
| C4 | 4 | Slow B2B sales to housing companies. |
| C5 | 6 | High margin, but a loaded CAC of €3–4k. |
| C6 | 8 | About 36 companies needed. |
| C7 | 6 | The rules keep changing after the July 2026 benefit reform; content is needed in 7 languages. |
| C8 | 3 | Easy for an ERP vendor to copy, and the rules are volatile. |
| C9 | 4 | The RDG grey zone, consent under a power imbalance, and harm to tenants if a deadline is wrong. |
| C10 | 3 | Utility statements are seasonal and housing companies decide by committee. |

**What the researcher missed**
- The power-imbalance consent problem and the aggregate-only design it forces.
- Jobcenters' own digital channels.
- Reputational risk for the landlord.

**Unit economics (recomputed)**

| Item | Value |
|---|---|
| ARPU | ≈ €300 |
| Cost to serve | €25 |
| Gross margin | 92% |
| Fixed costs | €1,800 |
| Customers needed | **≈ 36** |
| CAC | ≈ €3,500 |
| Churn | 1%/month |
| LTV / LTV:CAC | ≈ €27,500 / ≈ 8 |
| Time to €8k/month | 30+ months; pilots must wait for statement batches |

**Top 3 risks**
1. The landlord's return is unproven, and the ERP vendor can copy it.
2. GDPR and ethics.
3. Benefit rules keep changing.

**Cheapest 30-day money test.** Interview 10 social managers at housing cooperatives. **Pass:** 2 sign a €500 pilot LOI tied to their next statement batch.

**Lawyer before launch: YES.** Questions:
1. Where is the RDG line between general information and an individual case?
2. Is GDPR consent valid under a power imbalance, and may the landlord see confirmations at all?
3. Liability if a deadline is wrong.
4. The benefit rules after the reform.

---

### L5-F1 — RambursFlip: converts cash-on-delivery orders to prepaid for Romanian web shops (RoPay + WhatsApp Business API): **57.0, KILL** (borderline)

**Hard rules**
- **H1, H2, H5, H7 pass.**
- **H3 passes.** The founder never holds funds. PSD2 excludes technical service providers that never come into possession of the funds (Art. 3(j); Romania transposed PSD2 through Law 209/2019). That covers creating payment links when the money flows from buyer to the merchant's licensed processor (JUDGEMENT; [PSD2](https://eur-lex.europa.eu/eli/dir/2015/2366/oj), STATUTE not fetched).
- **H4 passes, narrowly.** The WhatsApp Cloud API and the Shopify App Store can both be revoked, but SMS/e-mail and WooCommerce keep the core alive.
- **H6 passes, with a design guard.** Steering buyers from cash-on-delivery to irrevocable instant transfers removes their "pay on receipt" leverage. Instant account-to-account payments have no card-style chargeback (JUDGEMENT). So: processor-vetted merchants only, a card link offered next to RoPay, and no false urgency.
- **H8 passes on available evidence, but is flagged.**
  - Zarina CRM claims WhatsApp recovery of unpaid cash-on-delivery orders ([Zarina](https://www.zarinacrm.ro/automatizare-comenzi-online/), extract).
  - Forbes Romania describes sending a secure payment link by e-mail or SMS on delivery day, so buyers can pay before the courier arrives ([Forbes RO](https://www.forbes.ro/?p=277382), extract; provider not identified).

**C1–C10**

| C | Score | Justification |
|---|---|---|
| C1 | 7 | Daily refusals (5–15% of cash-on-delivery orders) plus collection fees ([Packeta via economica, lens 5](https://www.economica.net/alexandr-jeleascov-packeta-romania-rata-de-retur-la-magazinele-online-din-romania-este-in-crestere_625270.html/amp)). |
| C2 | 7 | The merchant pays out of its savings, and paid local tools exist (Caty from €10/month, vendor claim, lens 5). |
| C3 | 5 | The Indian playbook is proven, but Romania's cash-on-delivery share is contested and pay-before-delivery links already exist (see below). |
| C4 | 5 | App directories, agencies and communities, reached through a Romanian freelancer. |
| C5 | 5 | Merchant ROI is thin, because a perk forces marketing-category messages: €0.0712 vs €0.0239 for utility in Romania ([Profit.ro, lens 5](https://profit.ro/romania-conectata/schimbare-la-whatsapp-apare-plata-pentru-mesajele-de-asistenta-pe-whatsapp-business-api-22793043)). At 1,000 orders and 10% conversion, ≈€250 of value goes against the €89 price plus ≈€70–140 in messages. |
| C6 | 7 | About 163 of 10–20k shops (unverified); fewer if the cash-on-delivery share is low. |
| C7 | 5 | Many integrations (Shopify, WooCommerce, GoMag, MerchantPro, 2–3 processors, Meta) and Black Friday peaks. |
| C8 | 4 | Easy for Caty, Zarina, GoMag or processors to copy, and the decline of cash-on-delivery shrinks the market by design. |
| C9 | 7 | No funds handled; mostly consent and Meta-policy risk. |
| C10 | 7 | €99 refundable pilots are possible within 60–90 days. |

**What the researcher missed**
- **Meta forces the marketing category.** Meta classifies a template that mixes an order update with a promotion as **marketing** ([Meta developer docs](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-categorization), extract). A "pay now and get a perk" message cannot be sent at the cheaper utility rate.
- **The cash-on-delivery share is contested.**
  - A Cargus/Visa whitepaper says ~7 in 10 Romanians most often pay by card on the shop's site, and cash-on-delivery is the main method for only ~1 in 5 online buyers ([Cargus whitepaper](https://www.cargus.ro/wp-content/uploads/Cargus-whitepaper-Visa.pdf), extract).
  - Lens 5 cited about two-thirds of *orders* ([Forbes RO, lens 5](https://www.forbes.ro/?p=518750); an estimate).
  - Both sources have interests: Visa sells card payments, and couriers earn collection fees. Unresolved.
- **Pay-before-delivery links already exist** (Forbes RO, above).
- **Consumer protection.** Instant transfers cannot be charged back.
- **Meta's commerce policy** may restrict some product categories common in cash-on-delivery shops (alcohol; possibly supplements). Unverified this session.

**Unit economics (recomputed)**

| Item | Value |
|---|---|
| ARPU | €75, excluding pass-through message fees (lens 5) |
| Cost to serve | ≈ €11 (adds €1 of variable Romanian-freelancer support) |
| Gross margin | ≈ 85% |
| Fixed costs | €2,400 |
| Customers needed | (8,000 + 2,400) ÷ 64 ≈ **163 merchants** |
| CAC by channel | Freelancer-booked demos ≈ €250 cash + time ≈ €400. App-store organic ≈ €100. Agency referral (20% of first-year revenue) ≈ €180. Blended ≈ €300. |
| Churn | 4%/month |
| LTV / LTV:CAC | ≈ €1,600 / ≈ 5 (stress case: 6% churn and €400 CAC → ≈ 2.7) |
| Time to €8k/month | ≈ 16–22 months, *only* if conversion is ≥10% |

**Top 3 risks**
1. The cash-on-delivery share and conversion rate, and thin merchant ROI after Meta fees.
2. Copycats, plus a structurally shrinking cash-on-delivery market.
3. Meta recategorises templates or bans the account.

**Cheapest 30-day money test.** A concierge pilot with 3 shops: send "pay now" links by WhatsApp or SMS by hand on 300 cash-on-delivery orders each, for a €99 refundable fee. **Pass:** ≥5% convert and refusals fall.

**Lawyer before launch: YES (Romanian counsel, ≈€500–1,000).** Questions:
1. Does the technical-service-provider exclusion cover the exact link flow?
2. Consumer law on prepayment perks and on charging different prices for cash-on-delivery versus prepaid.
3. E-privacy consent for WhatsApp messages.
4. Restricted categories under Meta's commerce policy.
5. Unfair-practice rules for the perk wording.

---

### L5-F2 — Vorbestell-Desk: WhatsApp pre-orders, pickup slots and instant deposits for butchers, bakeries and farm shops (Germany): **52.0, KILL**

**Hard rules**
- **H1, H5, H7 pass.**
- **H2 and H3 pass.** Deposits go to the shop's own payment-provider account. The German Payment Services Supervision Act (ZAG) exempts technical service providers that never hold the funds (§2(1) Nr. 9 ZAG; JUDGEMENT; [ZAG](https://www.gesetze-im-internet.de/zag_2018/__2.html)). Use direct charges so the shop is the merchant of record.
- **H4 passes, narrowly.** A web-form fallback exists.
- **H6 passes.** Keep alcohol out of farm-shop WhatsApp catalogues; Meta's commerce policy was not verified.
- **H8 is at risk.**
  - At least five butcher-branded iOS apps offer pre-ordering with a chosen pickup time. The order prints in the shop and the customer pays at pickup: Metzgerei [Lotter](https://apps.apple.com/app/id1508324294), [Schreder](https://apps.apple.com/app/id1482256245), [Breidert](https://apps.apple.com/app/id1536133403), [Metzler](https://apps.apple.com/app/id1551760911) and [Ambros](https://apps.apple.com/us/app/-/id1549844655) (extract).
  - Their near-identical descriptions point to one white-label vendor.
  - A "MeatApp" organisation is also listed ([startbase](https://www.startbase.de/organization/meatapp/), extract).

**C1–C10**

| C | Score | Justification |
|---|---|---|
| C1 | 6 | A Christmas and Easter crunch with no-shows and queues; moderate the rest of the year. |
| C2 | 5 | The shop pays, but existing pre-order apps and the "pay at pickup" norm cap willingness to pay. |
| C3 | 3 | Pre-order apps with pickup slots already exist; only deposits, slot capacity and WhatsApp remain as a wedge. |
| C4 | 5 | Butcher-guild meetings and cold visits are cheap but slow and seasonal. |
| C5 | 5 | About 82% gross margin, churn after Christmas, LTV/CAC ≈ 4. |
| C6 | 7 | About 297 of roughly 20k shops (unverified). |
| C7 | 6 | Peaks in November–December and on-site onboarding. |
| C8 | 4 | Point-of-sale, scale and white-label app vendors can add deposits. |
| C9 | 7 | Low liability, but consumer-law template pitfalls. |
| C10 | 7 | A concierge Christmas 2026 pilot can be sold now. |

**Known issue (d), resolved.** I ran the missing competitor check (one search). The gap is narrower than lens 5 assumed. Pre-ordering with pickup-time selection is already sold to German butchers as white-label apps. I found no deposit feature in the extracts. Vendor identity, prices and funding are unknown, so H8 is not triggered, but C3 falls to 3.

**What the researcher missed**
- **German consumer law on deposits and no-shows** (JUDGEMENT; [§309 BGB](https://www.gesetze-im-internet.de/bgb/__309.html), [§312j BGB](https://www.gesetze-im-internet.de/bgb/__312j.html), statutes not fetched):
  - A contractual *penalty* for not collecting goods is void in consumer standard terms (§309 Nr. 6 BGB), so no-show rules must be built as part-payment of the price or as lump-sum damages that let the customer prove a lower loss (§309 Nr. 5).
  - Online orders need a "zahlungspflichtig bestellen" (order with obligation to pay) button (§312j(3)).
  - There is no withdrawal right for perishable goods (§312g(2) Nr. 2).
- Allergen information is required for loose food sold at a distance (JUDGEMENT).
- A better launch market may exist (see the anchoring table).

**Unit economics (recomputed)**

| Item | Value |
|---|---|
| ARPU | ≈ €40 (annual and monthly billing blended) |
| Cost to serve | €7 |
| Gross margin | 82% |
| Fixed costs | €1,800 |
| Customers needed | **≈ 297** |
| CAC by channel | Visit ≈ €310. Guild meeting ≈ €150. Blended ≈ €250. |
| Churn | 3%/month |
| LTV / LTV:CAC | ≈ €1,100 / ≈ 4.4 |
| Time to €8k/month | 30+ months; sales are seasonal |

**Top 3 risks**
1. Existing pre-order apps.
2. Older German customers may refuse deposits.
3. Seasonality and churn.

**Cheapest 30-day money test.** A €149 concierge Christmas pilot for 5 butchers within 50 km.

**Lawyer before launch: YES (consumer-law check, ≈€500).** Questions:
- Deposit and no-show clauses.
- The order button.
- Distance-selling information and withdrawal exclusions.
- Allergen information.
- The payment-flow structure.

---

### L5-F3 — WP-Wächter: monthly efficiency check and fix list for heat-pump owners (Germany): **44.0, KILL** (lowest)

**Hard rules**
- **H1–H3, H5, H7 pass.**
- **H4 is at risk.**
  - Viessmann's API terms for commercial use are unknown ([Home Assistant docs, lens 5](https://www.home-assistant.io/integrations/vicare)).
  - Daikin's API allows 200 calls a day ([Homey forum, lens 5](https://community.homey.app/t/app-pro-and-cloud-daikin-onecta/54088/338)).
  - Vaillant offers no official third-party API ([Vaillant, lens 5](https://vaillant.com/eu-data-act/)).
  - Makers' own apps could add diagnosis. Manual meter entry keeps the core alive.
- **H6 passes, but needs safety guardrails** (see below).
- **H8 is unverified.** Funded installers bundle their own monitoring (JUDGEMENT).

**C1–C10**

| C | Score | Justification |
|---|---|---|
| C1 | 5 | Invisible waste; monthly but low-intensity. |
| C2 | 3 | Consumer willingness to pay €4.99 is doubtful, and the value is front-loaded. |
| C3 | 4 | Maker apps and DIY dashboards already exist. |
| C4 | 6 | Owner forums and YouTube are cheap channels. |
| C5 | 3 | ARPU €4.19 net and ≈5% monthly churn give LTV ≈ €66 against a CAC of €20–40, so LTV/CAC ≈ 1.6–3.3. |
| C6 | 8 | About 3,000 users of roughly 850k units sold in 2023–25 ([solarserver, lens 5](https://www.solarserver.de/2026/01/27/bwp-waermepumpen-absatz-um-55-prozent-in-2025-gestiegen/)). |
| C7 | 5 | Fragile API limits and consumer support for about 3,000 users. |
| C8 | 2 | Makers control the data and can ship the same feature. |
| C9 | 6 | Recommendations go through the installer, but safety guardrails are needed. |
| C10 | 6 | Community pre-sales are feasible. |

**What the researcher missed**
- **A safety guardrail.** The fix list must never suggest hot-water temperatures below hygiene limits (Legionella risk), and it should warn that changing settings may affect the warranty (JUDGEMENT).
- **Data Act economics.** Data holders may ask third parties for compensation (JUDGEMENT).
- **Free bundled competitors.** Large funded installers include monitoring free for their own customers (JUDGEMENT).

**Unit economics (recomputed)**

| Item | Value |
|---|---|
| ARPU | €4.19 net |
| Cost to serve | €0.90 |
| Gross margin | 79% |
| Fixed costs | €1,800 |
| Customers needed | **≈ 2,980** |
| CAC | €20–40 |
| Churn | 5%/month |
| LTV / LTV:CAC | ≈ €66 / ≈ 2.2 |
| Time to €8k/month | Beyond 24 months; at target size, churn alone needs ≈150 new users a month |

**Top 3 risks**
1. Low willingness to pay and high churn.
2. Makers control the data.
3. Safety liability.

**Cheapest 30-day money test.** A €39 founding season promoted in 2 forums and by 1 YouTuber. **Pass:** 100 pre-sales.

**Lawyer before launch: NO; a light check is enough.**
- Maker API terms.
- Disclaimers.
- The online cancellation button and contract-term rules.

---

### BASE — Daily automated check-in call for people 65+ living alone (Germany): **49.0, KILL** (my never-fund pick)

**Hard rules**
- **H1 passes.** A "press 1" keypress is a deterministic signal, not speech recognition.
- **H2 passes.**
- **H3 passes.** It is not a medical device or a care-insurance-funded home-alarm aid, and it uses an off-the-shelf telephony API.
- **H4, H5, H7 pass.**
- **H6 passes, with a condition.** The senior must personally consent (or their legal representative, if they lack capacity). Otherwise it is surveillance without the person's own consent.
- **H8 passes in Germany.** My search found no device-free daily-call service ([web.de](https://web.de/magazine/ratgeber/kind-familie/notrufsysteme-senioren-moeglichkeiten-34479312), extract). The crowding is abroad, for example US volunteer and police "daily dial" programmes ([GovTech](https://www.govtech.com/health/with-a-daily-dial-police-reach-out-to-seniors.html)).

**C1–C10**

| C | Score | Justification |
|---|---|---|
| C1 | 6 | A rare catastrophic event plus daily family worry. |
| C2 | 5 | The family pays, but "I'll call Mum myself" is free. Consumer advice centres put basic device-alarm (Hausnotruf) tariffs at about €20/month ([web.de](https://web.de/magazine/ratgeber/kind-familie/notrufsysteme-senioren-moeglichkeiten-34479312), extract), below the brief's €27–40. |
| C3 | 5 | The gap is plausible (none found), but the reason may simply be low demand. |
| C4 | 4 | Paid ads to adult children; no cheap channel. |
| C5 | 4 | €8.32 net against €3 cost gives 64% gross margin (below 70%), and LTV/CAC ≈ 2. |
| C6 | 9 | About 1,800 families out of millions. |
| C7 | 5 | Reliable 24/7 alerting is very hard for one person. |
| C8 | 4 | Easy to copy; home-alarm providers can add a phone-only tier. |
| C9 | 3 | Consumer terms cannot exclude or cap liability for death or injury caused by negligence (§309 Nr. 7 BGB), and one press story could end the business. |
| C10 | 7 | Landing-page pre-sales are fast. |

**What the lenses missed**
- **§309 Nr. 7 BGB** ([BGB §309](https://www.gesetze-im-internet.de/bgb/__309.html), STATUTE not fetched). Standard consumer terms cannot exclude or limit liability for:
  - death or injury caused by negligent breach;
  - any damage caused by gross negligence.
- **The senior can sue too.** The senior, or their heirs, may claim as third parties protected by the family's contract (JUDGEMENT).
- **Margin after VAT.** Lens 5 alone used the net price; the margin is 64%.
- **Consent and capacity.** For a parent with dementia, a guardian or holder of a lasting power of attorney must consent.
- **Marketing.** Advertising must not suggest an emergency service, under unfair-competition law (JUDGEMENT).
- **Price conflict.** Basic home-alarm tariffs (≈€20) are lower than the brief states.

**Unit economics (recomputed)**

| Item | Value |
|---|---|
| ARPU | €8.32 net |
| Cost to serve | €3 |
| Gross margin | 64% |
| Fixed costs | €1,500 (includes liability insurance) |
| Customers needed | (8,000 + 1,500) ÷ 5.32 ≈ **1,786 families** (the brief's "≈1,000" ignores VAT and fixed costs) |
| CAC | €60–100 via paid channels; slow free referrals through local care-advice centres |
| Churn | 4%/month |
| LTV / LTV:CAC | ≈ €133 / ≈ 1.3–2.2 |
| Time to €8k/month | 30+ months |

**Top 3 risks**
1. A life-safety failure, uncapped negligence liability and reputational ruin.
2. The unit economics.
3. Consent, capacity and false alarms.

**Cheapest 30-day money test.** A landing page plus €500 of search ads aimed at adult children, with the €9.90 first month prepaid. **Pass:** 30 paid sign-ups.

**Lawyer before launch: YES.** Questions:
1. What do §309 Nr. 7 BGB limits mean for the contract design?
2. Third-party (protective-effect) claims by the senior.
3. Would liability insurance cover personal injury caused by an IT failure?
4. Marketing claims.
5. Consent and capacity.
6. Rules for automated calls.

---

### Cross-cutting (c): is each German launch evidence-driven or anchored by the German BASELINE?

| ID | Launch market | Evidence-driven or anchored? | Clearly better market? |
|---|---|---|---|
| L1-A | DE | **Evidence-driven:** lens 1 compared FR, ES and NL (all served) and found no German plans. But the GOT is both the wedge and the main legal and demand risk. | None evidenced. Austrian and Swiss fee rules were not checked; they might mean less legal friction. |
| L1-B | DE | **Partly anchored:** no cross-country comparison, and the SEPA/GoBD gap may already be covered by Stabley. | None evidenced. |
| L1-C | DE → DACH | **Partly anchored:** a language-gap argument only. | None evidenced. |
| L2-F1 | EU, DE first | **Evidence-driven:** the largest national pool of computer/electronics/optical makers, plus active BSI and IHK awareness campaigns. | Not a country switch, but sell EU-wide in English from day one. |
| L2-F2 | EU, DE first | **Weak evidence.** | NL is equally plausible: its government addresses importers directly. |
| L2-F3 | DE + NL | Assumption (e-bike assembly hubs). | None evidenced. |
| L3-A | DE | Forced by German EEG law. | n/a |
| L3-B | DE (Berlin) | Forced by a German institution; Berlin's density is evidenced. | n/a |
| L3-C | CH | **Evidence-driven:** deliberately chosen to avoid the crowded German WEG market. | n/a |
| L4-F1 | DE (NRW) | **Evidence-driven:** PwC and ARD data, NRW Pflegewohngeld. | n/a (but the form library must follow residents' previous addresses) |
| L4-F2 | DE | Forced by a German institution. | n/a |
| L4-F3 | DE | Forced by a German benefit rule. | n/a |
| L5-F1 | RO | **Evidence-driven,** but the cash-on-delivery share is contested. | Bulgaria and Greece report higher cash-on-delivery use, but Bulgaria's instant-payment duties start only in 2027 ([BTA, lens 5](https://www.bta.bg/en/news/1072635-bulgarian-banks-99-ready-for-instant-payments-rollout-in-2027)). No clearly better market today. |
| L5-F2 | DE | **Anchored:** no market or competitor research, only facts about the payment rails. | Possibly the Netherlands (instant-payment habits) or the UK (a culture of Christmas deposits): JUDGEMENT, unverified. Scored as proposed. |
| L5-F3 | DE | Evidence-driven on install base; the UK was not researched. | None evidenced. |
| BASE | DE | Set by the brief. | — |

**Count.** Of the 12 German launches:
- **5 are forced by German law or institutions:** L3-A, L3-B, L4-F1, L4-F2, L4-F3.
- **2 are evidence-based choices:** L1-A, L2-F1.
- **5 are partly or clearly anchored:** L1-B, L1-C, L2-F2, L5-F2, L5-F3.

Only L5-F2 has a plausibly better alternative market, and that is unverified.

### Cross-cutting: legal gates (which ideas need a qualified lawyer before launch)

| ID | Lawyer before launch? | Specialist | Est. cost (JUDGEMENT) |
|---|---|---|---|
| L4-F1 | **YES** | Social law (RDG, §13 SGB X, SGB XII) plus data protection (GDPR Art. 9, DPIA) | €1,500–2,500 |
| L1-A | **YES** | Vet law (GOT, chamber codes), insurance boundary, consumer credit and terms | €1,000–1,500 |
| L2-F3 | **YES** | Product regulation (Batteries Reg. Arts 77–78), continuity and escrow, liability | ≈ €1,500 |
| L4-F2 | **YES** | Labour and data-protection law (controller, §179(8) SGB IX) | €800–1,200 |
| L4-F3 | **YES** | RDG plus GDPR (consent under a power imbalance) | ≈ €1,000 |
| BASE | **YES** | Consumer liability (§309 Nr. 7 BGB), insurance, marketing claims, consent and capacity | €800–1,200 |
| L5-F1 | **YES** | Romanian counsel: PSD2 exclusion, consumer and e-privacy law, Meta policy | €500–1,000 |
| L5-F2 | **YES** | Consumer standard terms (§309 Nr. 5/6), order button, distance selling, allergen information | ≈ €500 |
| L2-F1, L2-F2 | YES (light) | IT and product compliance: template-generator boundary, CRA self-scope, liability caps | €500–1,000 |
| L1-B, L1-C, L3-A, L3-B, L3-C, L5-F3 | NO (tax adviser or a light terms review) | Tax adviser; Swiss tax adviser for L3-C | €300–800 |

**No idea needs a banking, payment-institution, e-money, credit, insurance, legal-advice, tax-advice, medical-device or debt-collection licence**, as long as the design conditions above are kept. L4-F1, L1-A, L4-F3 and BASE are the ones where a careless design could slip into a regulated activity or uncapped liability.

---

## (3) Ranking of all 16 IDs, and which beat BASE

| Rank | ID | Weighted | Verdict | vs BASE (49.0) | One-line reason |
|---|---|---|---|---|---|
| 1 | L4-F1 Care-home financing case manager | **64.0** | TEST | **+15.0** | The biggest quantified payer pain, no home-side tool, and only ≈65 customers needed. Legal design is the gate. |
| 2 | L2-F1 CRA Logbook | **61.5** | TEST | **+12.5** | A live EU duty with an unmoved Dec 2027 cliff; English, developer-friendly channels; low liability. |
| 3 | L3-A Biogas evidence log | 59.0 | KILL | +10.0 | Strong payer and pain, but three vendors already exist and the pool shrinks. |
| 4 | L1-A Vet preventive-care plans | 57.5 | KILL | +8.5 | Proven abroad, but the GOT floor removes the discount lever, and the legal design is unproven. |
| 5 | L5-F1 RambursFlip | 57.0 | KILL | +8.0 | Real daily losses, but the cash-on-delivery share is contested, Meta's marketing fees squeeze merchant ROI, and the market shrinks by design. |
| 6 | L3-B Parent-run daycare rosters | 55.5 | KILL | +6.5 | Dense umbrella channel, but weak willingness to pay and a 3–4.5% pool share needed. |
| 7 | L1-C Music-teacher admin | 53.5 | KILL | +4.5 | Easy to run, but a low price ceiling and easy to copy. |
| 8 | L3-C Swiss condominium self-admin | 52.5 | KILL | +3.5 | The German WEG pattern at an earlier stage; no neutral channel. |
| 9= | L4-F2 SBV case tool | 52.0 | KILL | +3.0 | The payer pays only by statutory duty; health-data controller question unresolved. |
| 9= | L5-F2 Vorbestell-Desk | 52.0 | KILL | +3.0 | White-label butcher pre-order apps already exist. |
| 11 | L2-F3 Battery Passport Lite | 51.0 | KILL | +2.0 | A hard deadline, but a solo-continuity liability and a moving specification. |
| 12= | L1-B Boarding-stable billing | 49.0 | KILL | 0.0 | A free tool (Stabley) lists billing. |
| 12= | **BASE** Daily check-in call | 49.0 | KILL | — | 64% gross margin, LTV/CAC ≈ 2, uncapped life-safety liability. |
| 14 | L2-F2 CRA vault for importers/distributors | 48.5 | KILL | −0.5 | Value tied to Dec 2027; GPSR tools sit next door. |
| 15 | L4-F3 Tenant benefit-deadline assistant | 47.5 | KILL | −1.5 | Weak payer evidence, ERP copy risk, and an ethics/GDPR design problem. |
| 16 | L5-F3 WP-Wächter | 44.0 | KILL | −5.0 | Consumers' willingness to pay plus makers' control of the data. |

**Which beat BASE?**
- **11 ideas score above my BASE of 49.0.**
- **Only 5 lead by more than 5 points:**
  - **L4-F1 (+15.0)**
  - **L2-F1 (+12.5)**
  - L3-A (+10.0)
  - L1-A (+8.5)
  - L5-F1 (+8.0)
- **Only two of those reach the TEST band:** L4-F1 and L2-F1.
- **Within ±5 points (evaluator noise):** L3-B, L1-C, L3-C, L4-F2, L5-F2 and L2-F3 are effectively ties with BASE.
- **At or below BASE:** L1-B ties it; L2-F2, L4-F3 and L5-F3 fall below.
- **Context.** My BASE score is lower than any lens gave (51.0–57.5) because I score its liability (C9 = 3) and its after-VAT economics (C5 = 4) harder. If other evaluators score BASE around 55, only the top five ideas beat it.

---

## (4) My €10,000 bet and my never-fund pick

### The bet: L4-F1, care-home financing case manager (NRW), funded in stages

**Why this one**
- **It has the clearest money reason of any idea.** The paying home pre-finances €3,100–3,400 per resident per month while files sit incomplete:
  - 1 in 5 homes has ≥€100k outstanding;
  - 60% of homes whose largest debtor is the social-welfare office blame missing documents;
  - staff spend 8.3 hours a week on open items ([PwC](https://www.pwc.de/de/pressemitteilungen/2026/fehlende-liquiditaet-in-pflegeheimen-gefaehrdet-die-versorgung.html); [Apotheken Umschau](https://www.apotheken-umschau.de/gesundheitspolitik/pflegeheime-warten-monatelang-auf-hilfe-zur-pflege-von-sozialaemtern-1539809.html)).
- **It needs few customers.** The goal needs only ≈65 homes at about €2,100 a year each.
- **The reform tailwind is real.** The draft care reform would delay the full co-payment subsidy from 36 to 54 months, so more residents would need social assistance.
- **The legal risks are known and answerable.** None needs a licence:
  - Smartlaw covers the generator;
  - §5 RDG and keeping the family as applicant cover the home's staff;
  - §13 SGB X sets out what written authority is needed;
  - GDPR Art. 9 is handled with a DPIA, encryption and processor terms.

  A ≈€2,000 specialist opinion either clears the design or tells me to narrow it to a tool for home staff only.
- **The product's purpose serves the residents.** It gets families the aid they are entitled to, faster. That matters for the reputational risk.

**How the €10,000 is spent, with kill gates**
1. **Weeks 1–4 (≈€3,000).**
   - Legal opinion (≈€2,000).
   - A freelance German social-law specialist, such as a former social-welfare caseworker (≈€600).
   - 20 interviews with NRW homes (≈€400 travel).
   - **Gate:** the opinion confirms the design, and ≥3 homes pay €99 for the concierge service.
2. **Months 2–4 (≈€4,000).**
   - MVP, DPIA template, security hardening, insurance.
   - **Gate:** ≥5 paying homes, with measurably fewer follow-up requests or faster complete files (lens 4's kill tests KT2–KT3).
3. **Months 5–9 (≈€3,000).**
   - Referral deals with factoring firms and consultancies, and a published case study.
   - **Gate:** 20 homes. If any gate fails, stop.

**Runner-up: L2-F1.** It has lower legal risk and better founder fit. I would not bet on it first because micro makers' willingness to pay is untested and the gap will crowd quickly during 2027.

### Never fund: the BASELINE (daily check-in call)

**Why, from a counsel-operator's chair**
- **The implicit promise is life-safety.** The product promises: "we will notice if your mother has fallen". One person cannot keep that promise 365 days a year without a 24/7 on-call operation.
- **The liability cannot be capped.** German consumer terms cannot exclude or limit liability for death or injury caused by negligence (§309 Nr. 7 BGB).
- **The economics leave nothing for safety.** 64% gross margin and LTV/CAC ≈ 2 leave no budget for the redundancy, monitoring and insurance the promise demands.
- **The downside is uninsurable in practice.** One press story about an undiscovered death would end the company, whatever the court outcome.
- It is not a bad cause. It is a mismatch between the risk the product carries and the structure of a one-person company.

**Among the 15 finalists, the one I would never fund is L2-F3, Battery Passport Lite**, for the same structural reason in a B2B form:
- A one-person company would become the single point of failure for other firms' legal right to sell batteries, for years.
- Its specification is still incomplete: the Commission missed its own August 2026 implementing-act deadline ([battery-tech.net](https://battery-tech.net/why-the-eu-is-about-to-miss-its-own-battery-passport-deadline-while-industrys-stays-fixed/)).
- The pool is small and unverified.

---

## (5) Verification log

### Claims checked by search this session (15 searches; 1 fetch failed)

| # | Claim checked | Result | URL(s) |
|---|---|---|---|
| 1 | A question-driven document generator is not a legal service under §2(1) RDG (BGH I ZR 113/20, 9 Sep 2021). Matters for L4-F1/F2/F3, L2-F1. | **Confirmed** (extract) | [LTO](https://www.lto.de/recht/juristen/b/bgh-urteil-izr11320-vertragsgenerator-smartlaw-keine-unzulaessige-rechtsdienstleistung-rak-hamburg-rdg-legal-tech); [beck-aktuell](https://www.beck-aktuell.de/heute-im-recht/rechtsprechung/bgh-keine-konkrete-taetigkeit-smartlaw-ist-zulaessig-2021-10-01); [RAK Hamburg](https://www.rak-hamburg.de/uploads/file/282565_Presseerkl%C3%A4rung%20vom%2009.09.2021.pdf); [anwalt24](https://www.anwalt24.de/urteile/bgh/2021-09-09/i-zr-113_20) |
| 2 | Commercial providers of social-law objection help (care grade) have been held to breach the RDG | **Unverifiable:** no decision found | Search set incl. [Verbraucherzentrale](https://www.verbraucherzentrale.de/node/11547), [Ärzteblatt](https://www.aerzteblatt.de/nachrichten/148119/Widerspruch-gegen-die-Pflegegradeinstufung-oft-erfolgreich) |
| 3 | An objection in a social-assistance care case filed without written power of attorney was inadmissible and could not be cured later | **Confirmed by extract only.** The fetch failed (DNS), so who filed it (home, relative) is unknown. | [gesetze-bayern.de](https://www.gesetze-bayern.de/Content/Pdf/Y-300-Z-BECKRS-B-2024-N-28787?all=False) |
| 4 | No German practice-run monthly vet plans exist (lens 1) | **Confirmed absence:** 2 more German searches found none; results were fee-schedule and insurance pages | [Allianz](https://www.allianz.de/gesundheit/hundekrankenversicherung/tierarztkosten-hund/); [Landtag Niedersachsen](https://www.landtag-niedersachsen.de/drucksachen/drucksachen_19_02500/01501-02000/19-01522.pdf) |
| 5 | Vet fees below 1× GOT only in justified individual cases with prior written agreement; the general exception is neutering feral cats | **Confirmed** (extract) | [BTK](https://www.bundestieraerztekammer.de/d.php?id=285); [Berliner Sparkasse](https://www.berliner-sparkasse.de/fi/home/ratgeber/ratgeber-heilberufe/finanzen/abrechnung-tierarztpraxis.html); [topagrar](https://www.topagrar.com/betriebsleitung/news/die-finanzierung-einer-tierarztpraxis-ist-bei-abrechnung-unterhalb-des-einfachen-gebuehrensatzes-nicht-moeglich-13496964.html) |
| 6 | A GOT evaluation is under discussion | **Confirmed** (extract; lobby-register entry dated 25 Jun 2026) | [Lobbyregister RV0025695](https://www.lobbyregister.bundestag.de/inhalte-der-interessenvertretung/regelungsvorhabensuche/RV0025695) |
| 7 | CRA reporting obligations apply from 11 Sep 2026 | **Confirmed** (extract) | [Freshfields](https://www.freshfields.com/en/our-thinking/blogs/technology-quotient/cyber-resilience-act-reporting-obligations-take-effect-on-11-september-2026-102nzmk) |
| 8 | The CRA's Dec 2027 date may be postponed (lens 2 risk) | **Contradicted:** no evidence of postponement; the Digital Omnibus consolidates reporting channels | [Osborne Clarke](https://www.osborneclarke.com/insights/regulatory-outlook-november-2025-cyber-security); [Steptoe](https://www.steptoe.com/en/news-publications/steptechtoe-blog/cra-countdown-european-commission-publishes-draft-guidance-highlighting-fast-approaching-deadlines.html); [Freshfields](https://www.freshfields.com/en/our-thinking/blogs/technology-quotient/cyber-resilience-act-reporting-obligations-take-effect-on-11-september-2026-102nzmk) |
| 9 | The battery passport date (18 Feb 2027) is unchanged; the Council's omnibus touches removability, not the passport | **Confirmed** (secondary, extract) | [projetcelsius](https://projetcelsius.com/en/faq/dpp-espr-affichage-env/l-echeance-du-18-fevrier-2027-peut-elle-etre-reportee/); [battery-tech.net](https://battery-tech.net/why-the-eu-is-about-to-miss-its-own-battery-passport-deadline-while-industrys-stays-fixed/); [S-GE](https://www.s-ge.com/export/en/articles/spotlight/introduction-eu-battery-passport-february-2027) |
| 10 | The Commission missed its 18 Aug 2026 implementing-act deadline on legitimate-interest access to restricted passport data | **Confirmed** (secondary) | [battery-tech.net](https://battery-tech.net/why-the-eu-is-about-to-miss-its-own-battery-passport-deadline-while-industrys-stays-fixed/) |
| 11 | Battery due diligence moved to 18 Aug 2027 (Reg. 2025/1561) | **Confirmed** (secondary) | [Arianee](https://www.arianee.com/en/blog/battery-due-diligence-august-2027); [Arianee timeline](https://www.arianee.com/en/blog/battery-passport-timeline-2027-2036) |
| 12 | A WhatsApp template that mixes an order update with a promotion is categorised as marketing | **Confirmed** (Meta documentation via extract) | [Meta developer docs](https://developers.facebook.com/documentation/business-messaging/whatsapp/templates/template-categorization); [LINK Mobility](https://www.linkmobility.com/blog/the-whatsapp-business-template-categories) |
| 13 | WhatsApp's Commerce Policy prohibits alcohol and some supplements | **Unverifiable** this session; a source only confirms marketing templates must follow the Commerce Policy | [Sinch community](https://community.sinch.com:443/t5/WhatsApp/What-category-of-template-should-I-use-to-send-promotional/ta-p/9319) |
| 14 | Stabley is free for stables and includes boarder billing (lens 3's kill) | **Confirmed as a directory-listing claim;** how deep the billing goes is **unverifiable** | [AlternativeTo](https://alternativeto.net/software/stabley/about/) |
| 15 | Freemium Horsebook is another stable-app alternative | **Confirmed** (directory) | [AlternativeTo alternatives](https://alternativeto.net/software/stabley/) |
| 16 | Swiss STWEG market has more players than lens 3 listed | **Confirmed:** Woonig STWE module with e-voting, ImmoApp, Abacus AbaImmo | [Woonig](https://apps.apple.com/app/id1476238924); [ImmoApp](https://apps.apple.com/ee/app/immoapp/id1493436309); [Abacus](https://www.ABACUS.ch/fileadmin/ablage/02_dokumente/01_flyer/de/flyer_abacus_abaimmo-immobilienbewirtschaftung_de.pdf) |
| 17 | No competitor exists for butcher/bakery pre-ordering in Germany (lens 5 assumption) | **Contradicted:** ≥5 butcher-branded pre-order apps (pickup time, in-store printing, pay at pickup), likely one white-label vendor; a MeatApp organisation listing | [Lotter](https://apps.apple.com/app/id1508324294); [Schreder](https://apps.apple.com/app/id1482256245); [Breidert](https://apps.apple.com/app/id1536133403); [Metzler](https://apps.apple.com/app/id1551760911); [Ambros](https://apps.apple.com/us/app/-/id1549844655); [infranken](https://www.infranken.de/lk/wuerzburg/grillabend-ohne-stress-mit-dieser-app-kannst-du-beim-metzger-grillgut-bestellen-art-2802701); [startbase MeatApp](https://www.startbase.de/organization/meatapp/) |
| 18 | No device-free daily check-in call service exists in Germany (BASE gap) | **Not contradicted:** none found in one search | [web.de](https://web.de/magazine/ratgeber/kind-familie/notrufsysteme-senioren-moeglichkeiten-34479312) |
| 19 | Home-alarm (Hausnotruf) costs €27–40/month (brief) | **Partly contradicted:** consumer advice centres cite basic tariffs around €20/month (secondary) | [web.de](https://web.de/magazine/ratgeber/kind-familie/notrufsysteme-senioren-moeglichkeiten-34479312) |
| 20 | BaFin's guidance notes on the Payment Services Supervision Act (ZAG) were updated on 14 Feb 2023 | **Confirmed** | [Bird & Bird](https://www.twobirds.com/en/insights/2023/germany/amendment-to-bafins-zag-guidance-notes); [YPOG](https://www.ypog.law/hubfs/YPOG%20Briefing_Aktualisierung%20ZAG%20Merkblatt_L%C3%B6sing.pdf) |
| 21 | BaFin's exact wording on technical service providers and commercial agents | **Unverifiable** this session; I relied on the statute (JUDGEMENT) | [ZAG §2](https://www.gesetze-im-internet.de/zag_2018/__2.html) (not fetched) |
| 22 | A care reform could cap co-payments and shrink social-assistance caseloads (lens 4 risk) | **Partly contradicted for the near term.** The draft reform law (3 Jun 2026, planned 1 Jan 2027) reportedly delays the full 75% subsidy to 54 months, meaning *more* cases. A cap is only a political demand (€1,500, Saarland premier). | [check24](https://www.check24.de/pflegeversicherung/pflegereform/); [gegen-hartz](https://www.gegen-hartz.de/news/3-245-euro-fuers-pflegeheim-ab-2027-zahlen-rentner-laenger-selbst); [AOK](https://www.aok.de/pp/gg/update/pflegereform-und-eigenanteile/); [Nordkurier](https://www.nordkurier.de/politik/pflege-im-heim-noch-teurer-was-bringt-die-reform-4716889) |
| 23 | About two-thirds of Romanian online orders are cash-on-delivery (lens 5) | **Contradicted / unresolved:** a Cargus/Visa whitepaper says cash-on-delivery is the main method for ~1 in 5 buyers and ~7 in 10 pay mostly by card. Both sources have interests. | [Cargus whitepaper](https://www.cargus.ro/wp-content/uploads/Cargus-whitepaper-Visa.pdf); vs [Forbes RO, lens 5](https://www.forbes.ro/?p=518750) |
| 24 | Local Romanian tools only confirm orders; nobody converts to prepaid before delivery (lens 5) | **Partly contradicted:** Forbes RO describes payment links on delivery day; Zarina claims WhatsApp recovery of unpaid cash-on-delivery orders | [Forbes RO](https://www.forbes.ro/?p=277382); [Zarina](https://www.zarinacrm.ro/automatizare-comenzi-online/) |
| 25 | No German software helps care homes manage social-assistance applications (L4-F1 gap) | **Not contradicted:** none found; homes use paper checklists and model letters | [Agaplesion](https://www.hdv.agaplesion.de/fileadmin/Agaplesion_hdv-darmstadt/Infomaterial/Checkliste_Sozialhilfetraeger_AGA_WuP_web.pdf); [betanet](https://www.betanet.de/hilfe-zur-pflege.html) |
| 26 | An informal letter or e-mail secures the application date | **Confirmed** (secondary) | [betanet](https://www.betanet.de/hilfe-zur-pflege.html) |
| 27 | The responsible social-welfare office is the one for the resident's address before admission | **Confirmed** (one district's service page) | [Schwalm-Eder-Kreis](https://schwalm-eder-kreis.de/Home/Barrierefreiheit.htm/Aemter/50-4-SGB-XII-Hilfe-zur-Pflege.html) |

### Statute-based judgements used in scoring (not fetched; counsel to confirm wording)

| # | Point | Source (not fetched) | Used for |
|---|---|---|---|
| J1 | Consumer standard terms cannot exclude or limit liability for death or injury caused by negligence, or for gross negligence (§309 Nr. 7 BGB) | [BGB §309](https://www.gesetze-im-internet.de/bgb/__309.html) | BASE C9 |
| J2 | Penalties for not collecting goods are void in consumer terms; lump-sum damages must allow proof of a lower loss (§309 Nr. 6 and Nr. 5) | [BGB §309](https://www.gesetze-im-internet.de/bgb/__309.html) | L5-F2 |
| J3 | Online orders need an "order with obligation to pay" button (§312j(3)) | [BGB §312j](https://www.gesetze-im-internet.de/bgb/__312j.html) | L5-F2 |
| J4 | Consumer-credit rules reach only *paid* deferred-payment arrangements (§506) | [BGB §506](https://www.gesetze-im-internet.de/bgb/__506.html) | L1-A H3/H6 |
| J5 | Not a legal service: discussing legal questions with elected employee representatives (§2(3) Nr. 3 RDG). Ancillary legal services allowed (§5 RDG) | [RDG §2](https://www.gesetze-im-internet.de/rdg/__2.html); [RDG §5](https://www.gesetze-im-internet.de/rdg/__5.html) | L4-F1, L4-F2 |
| J6 | Written proof of authority on request; rejection of representatives who provide legal services the RDG does not allow (§13 SGB X) | [SGB X §13](https://www.gesetze-im-internet.de/sgb_10/__13.html) | L4-F1 |
| J7 | Care assistance starts when the office knows of the need (§18 SGB XII); old-age basic income needs an application that reaches back to the start of the month (§44 SGB XII) | [SGB XII §18](https://www.gesetze-im-internet.de/sgb_12/__18.html); [SGB XII §44](https://www.gesetze-im-internet.de/sgb_12/__44.html) | L4-F1 |
| J8 | The SBV supports disability-recognition and equal-status applications (§178(1) SGB IX); the employer bears SBV costs (§179(8)) | [SGB IX §178](https://www.gesetze-im-internet.de/sgb_9_2018/__178.html); [SGB IX §179](https://www.gesetze-im-internet.de/sgb_9_2018/__179.html) | L4-F2 |
| J9 | The employer is the data controller for works-council processing (§79a BetrVG, 2021) | [BetrVG §79a](https://www.gesetze-im-internet.de/betrvg/__79a.html) | L4-F2 |
| J10 | Exemptions for commercial agents and for technical service providers that never hold funds (§2(1) Nr. 2 and Nr. 9 ZAG; PSD2 Art. 3(b), (j)) | [ZAG §2](https://www.gesetze-im-internet.de/zag_2018/__2.html); [PSD2](https://eur-lex.europa.eu/eli/dir/2015/2366/oj) | L5-F1, L5-F2, L1-A |
| J11 | CRA Art. 64 penalty tiers (€15m/2.5%; €10m/2%; €5m/1%). Art. 64(10)(a): micro and small firms are not fined only for a missed 24-hour early warning | [CRA](https://eur-lex.europa.eu/eli/reg/2024/2847/oj) | L2-F1, L2-F2 |
| J12 | GDPR Art. 9 (special-category data), Art. 28 (processors), Art. 35 (DPIA), Art. 7 (freely given consent) | [GDPR](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | L4-F1, L4-F2, L4-F3 |
| J13 | Batteries Regulation Arts 77–78: passport content, availability and continuity expectations | [Batteries Regulation](https://eur-lex.europa.eu/eli/reg/2023/1542/oj) | L2-F3 |
| J14 | Insurance business requires risk transfer for a premium (scope of the Insurance Supervision Act, VAG) | [VAG §1](https://www.gesetze-im-internet.de/vag_2016/__1.html) | L1-A |

### Gaps (not resolved; could move scores)

**Competitor facts still open**
- Funding and profitability of niche competitors (Stabley, EinfachSTWEG, LIMMOBI, Nabisy Software, TerraVis, Biotaktix, Caty, Zarina, sbomify). Every H8 "pass" rests on absence of evidence.
- How deep Stabley's billing goes (SEPA files, GoBD-proof numbering, extras logging). This decides whether L1-B's C3 and C8 recover.
- Identity, prices and deposit features of the white-label butcher pre-order vendor (L5-F2).
- In-house plans at German vet chains, and plan modules from German practice-software vendors (L1-A).
- Care-home ERP features for social-assistance application packets (L4-F1 C3/C8). My one search found none, but vendors were not checked one by one.

**Legal and policy facts still open**
- Which product categories WhatsApp's Commerce Policy restricts (L5-F1, L5-F2).
- Who is the data controller for SBV processing (L4-F2).
- The text of Romania's Law 209/2019, read directly (L5-F1).
- The Swiss VAT registration rule for foreign e-service providers (L3-C).
- National battery-passport penalties in Germany (L2-F3).

**Market numbers still open**
- How to reconcile Romania's cash-on-delivery share: the Visa survey, the Forbes estimate, and lens 5's tax-authority figure of 31bn lei (secondary). This decides L5-F1's C3 and C6.

**Method limit.** Every "(extract)" item is based on search-engine extracts, not full pages. In particular, the Bavarian power-of-attorney decision (log #3) should be read in full before relying on it.
