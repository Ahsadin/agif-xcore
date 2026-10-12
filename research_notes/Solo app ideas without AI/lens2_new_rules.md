# Lens 2 — New legal obligations (in force or phasing in 2025–2028) as a source of non-AI "must-buy" solo apps

Research date: 2026-10-12. I applied the METHOD (Q1–Q10) and RULEBOOK (H1–H8, C1–C10) exactly as given. Every raw idea starts from Q1: a concrete person's pain caused by a new obligation.

## How I checked facts, and what I could not check

- **Primary sites were blocked.** The session's egress policy refused direct connections to EUR-Lex, GOV.UK, legislation.gov.uk, FDA, the Federal Register, BOE and ENISA (HTTP 403 on CONNECT). WebFetch failed on DNS. I therefore checked primary texts through search-engine extracts of those pages. I mark these **[P\*]**.
- **Search budget ran out.** The shared web-search budget was used up before I could check payment-processor fees, hosting prices, or several dates in the kill log. Those numbers are marked **ASSUMPTION** or **[U]**.
- **Labels used below:**
  - **[P\*]** = primary or official page, read through a search extract.
  - **[S]** = secondary source (law firm, trade press, government-adjacent).
  - **vendor claim** = a vendor's own marketing.
  - **[U]** = prior knowledge, not re-verified in this pass. Treat it as a pointer only. All [U] items are listed in the Gaps sections.

> **Bottom line**
> - I generated **32 raw candidates**: 28 killed, 1 merged into a finalist, 3 finalists.
> - The obligations the brief names first are already crowded or served for free by governments, platforms, banks or payroll and landlord incumbents. These are e-invoicing, MTD, Renters' Rights, short-term rentals, time recording, privacy and EPR. New niches fill quickly too: Awaab's Law and Digital Waste Tracking each drew 6+ vendors within months of the rule.
> - The gap that survives is **EU product-security and product-data rules that apply regardless of company size**. Here the tools are priced for large manufacturers, and micro firms have nothing that fits.
> - **F1 — CRA Logbook for micro hardware/IoT makers** (EU, launch Germany): **64.5 (TEST)**. This clearly beats the BASELINE, which I scored at **52.0**.
> - **F2 — Connected-product compliance vault for small importers/distributors** (EU, launch Germany): **55.0 (KILL band)**.
> - **F3 — Battery Passport Lite for small LMT/industrial battery assemblers** (EU): **56.0 (KILL band)**.
> - **Plainly: only F1 robustly beats the baseline.** F2 and F3 beat my baseline score by only 3–4 points, which is within evaluator noise, and both sit below 60.

---

## (1) KILL LOG

### Takeaway
New obligations create real pain, but most pain that is loud and broad has already attracted vendors, often within months of the rule. Many obligations are also served free by:
- governments (KSeF, Defra waste tracking, SIA/ProtectUK)
- banks and marketplaces
- payroll and landlord incumbents

Some obligations were removed or narrowed in 2025–2026: the NY LLC Transparency Act for domestic LLCs, and the EUDR for micro/small primary operators.

The surviving gap is size-agnostic EU product rules for micro firms: the Cyber Resilience Act and the Batteries Regulation passport.

### Kill log — one line per raw candidate (each starts from a Q1 pain)

| # | Raw candidate (Q1 pain → app idea) | Killed by | Why (evidence) |
|---|---|---|---|
| 1 | A Leipzig plasterer must issue structured e-invoices to business clients (reception has been mandatory since 2025; issuance is phased 2027–28) → XRechnung/ZUGFeRD invoicing app | H8 | One source cites an €800k turnover split for 2027 vs 2028; the dates come from vendor roundups ([Shared Services Link](https://sharedserviceslink.com/webinar/2027-eu-mandates-what-6-countries-require-and-when), [OriginStamp](https://originstamp.com/en/blog/reader/eu-e-invoicing-mandates-timeline-2026-2030)). The vendor field is crowded: Seeburger, Fonoa, Doxis, SPS Commerce, OriginStamp and e-invoice.app all sell e-invoicing compliance (vendor claims, e.g. [Fonoa](https://www.fonoa.com/blog/e-invoicing-and-digital-reporting-in-the-eu-upcoming-changes)). No uncopyable wedge. |
| 2 | A French micro-entrepreneur must receive e-invoices from Sept 2026 and issue/e-report from Sept 2027 via an approved platform → micro e-invoicing app | H8 (H3-adjacent: transmission runs through certified platforms) | Dates per [SPS Commerce](https://www.spscommerce.com/community/articles/e-invoicing-mandates-in-europe-the-2026-business-guide); sources conflict on details. Crowding by platforms and banks is [U]. |
| 3 | A Belgian sole trader must send Peppol e-invoices since 1 Jan 2026 → Peppol sender | H8 | In force since 1 Jan 2026 ([SPS Commerce](https://www.spscommerce.com/community/articles/e-invoicing-mandates-in-europe-the-2026-business-guide)). Many access points and accounting tools [U]. Penalties not verified. |
| 4 | A Polish micro firm must invoice through KSeF (large firms Feb 2026, most Apr 2026, last group Jan 2027) → KSeF front-end | H4/H8 | Phasing per [OriginStamp](https://originstamp.com/en/blog/reader/eu-e-invoicing-mandates-timeline-2026-2030). Free ministry tools and many Polish invoicing apps [U]. |
| 5 | A Spanish autónomo needs VeriFactu-compliant invoicing software (2027) → VeriFactu app | H8 + Q10 (dates moving) | Postponement details could not be confirmed (gap). One roundup lists a Spanish B2B e-invoicing date of Oct 2027 ([e-invoice.app](https://www.e-invoice.app/blog/global-einvoice-mandates-2026)). Crowded local vendors [U]. |
| 6 | A UK landlord or sole trader over the income threshold must file quarterly Making Tax Digital updates (2026–28) → MTD app | H8/H4 | [U] HMRC-recognised software includes free products, and banks bundle accounting software. Not re-verified. |
| 7 | A UK self-managing landlord must adapt to the Renters' Rights Act (rent-increase procedure, database, ombudsman) → RRA compliance app | H8/H4 | [U] Landlord platforms are adding these features, and the government database is free. |
| 8 | A housing officer at a social landlord with fewer than 1,000 homes must meet Awaab's Law clocks → hazard-clock app | H8 (C3 ≤ 3) | Clocks: 24 h for emergencies; 10 working days to investigate; safety work within 5 working days of the investigation ending; Phase 2 hazards from 30 Nov 2026 ([GOV.UK Phase 2 guidance](https://www.gov.uk/government/publications/awaabs-law-phase-2-guidance-for-social-housing-landlords/awaabs-law-phase-2-guidance-for-social-landlords) [P\*]). Dedicated tools for small and mid-size providers already exist: [AwaabSafe](https://www.awaabsafe.co.uk/), [HazardClock](https://hazardclock.co.uk/blog/awaabs-law-compliance-software-guide/), [CHICS](https://chics.co.uk/awaabs-law). Netcall, OneAdvanced, Weightmans, Neo, REBIM and HousingSurvey Pro also sell into this space (vendor claims). The pool is small: 1,624 registered providers in 2021, 1,411 of them private ([RSH briefing](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1027024/RP_statistic_2020-21_briefing_note_v1.0__FINAL_.pdf) [P\*]). |
| 9 | A village-hall committee or 300-capacity pub must notify the SIA and keep public-protection procedures under Martyn's Law → compliance kit | C1/C2 (+H8 risk) | The duty is mostly one-off and the standard-tier maximum fine is £10k ([Foot Anstey](https://www.footanstey.com/our-insights/articles-news/martyns-law-an-update-following-final-statutory-guidance/)). Enforcement is expected around spring/April 2027, and the SIA notification site is not live ([Burges Salmon](https://www.burges-salmon.com/articles/102mqoj/martyns-law-counting-down-to-live-implementation)). Halo offered its tool free to venues under 800 capacity in 2023 ([The Ticketing Business](https://www.theticketingbusiness.com/2023/06/12/halo-solutions-to-offer-safety-platform-for-free-to-support-martyns-law/)). SIM Martyn's Law Manager is listed at £50–£5,000 per licence per month ([G-Cloud](https://www.applytosupply.digitalmarketplace.service.gov.uk/g-cloud/services/342763487779972)). |
| 10 | A small waste transfer station must submit every load to Digital Waste Tracking within 2 working days from 1 Oct 2026 (carriers follow in 2027) → gate-entry app | H8 (H4-adjacent) | Start date per [gov.wales](https://www.gov.wales/mandatory-digital-waste-tracking-system) [P\*] and the 2-day rule per [Karmactive](https://www.karmactive.com/uk-digital-waste-tracking-rules-start-october-2026/). The official service offers a portal, CSV and API; one source cites about £26 per entity per year (unverified). At least 8 vendors already sell DWT modules: [FieldMotion](https://fieldmotion.com/blog/digital-waste-tracking-module/), [Avery Weigh-Tronix](https://www.averyweigh-tronix.com/en-gb/weighing_guide/digital-waste-tracking-2026-what-the-new-defra-legislation-means-for-waste-operators/), [Weightron](https://www.weightron.com/news/digital-waste-tracking-phase-1-october-26-phase-2-2027-update/), [Fissara](https://www.fissara.com/mandatory-digital-waste-tracking/), [Wastebolt](https://wastebolt.app/waste-blog/digital-waste-tracking-waste-receivers-2026), [Brik.ly](https://www.brik.ly/blog/digital-waste-tracking-october-2026-cafes/), Waste Logics and Access Group (vendor claims). |
| 11 | A US produce or seafood distributor must keep traceability records and give FDA a sortable spreadsheet within 24 h under FSMA 204 → traceability log | Q10 + H8 | Congress fixed enforcement to 20 July 2028 ([FDA](https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-requirements-additional-traceability-records-certain-foods) [P\*]). FDA is studying "additional flexibilities", with a public meeting on 15 June 2026 ([FDA](https://www.fda.gov/food/workshops-meetings-webinars-food-and-dietary-supplements/fda-public-meeting-challenges-and-solutions-lot-level-food-traceability-06152026) [P\*]). Retail food establishments and restaurants with ≤$250k annual food sales are exempt ([FDA Q&A](https://www.fda.gov/media/191182/download) [P\*]). Crowded: [FoodReady](https://foodready.ai/blog/fsma-204/), [Four Foxes](https://fourfoxes.io/blog/fsma-204-compliance-date-extension/), [Dill](https://mydill.com/compliance-hub/fsma-204-food-traceability-rule), [PolicyCanary](https://policycanary.io/regulations/fsma-204), [Xenia](https://www.xenia.team/food-safety-ops/fsma-204-food-traceability-rule), [TrueCommerce](https://www.truecommerce.com/blog/fsma-food-traceability-rule/) (vendor claims). |
| 12 | A NY LLC owner must file beneficial-ownership reports under the NY LLC Transparency Act → filing app | Q10 (obligation gone) | After the veto of S8432 on 19 Dec 2025, domestic LLCs file nothing; only foreign LLCs are covered ([Seward & Kissel](https://www.sewkis.com/publications/domestic-llcs-escape-new-yorks-transparency-act/), [Bonadio](https://www.bonadio.com/?p=5960)). |
| 13 | An Australian sole-practice accountant or estate agent became an AUSTRAC reporting entity on 1 Jul 2026 (CDD, AML/CTF programme) → AML records app | H8 (+H1: ID checks are normally OCR/biometric) | Scope, dates and the 29 Jul 2026 enrolment deadline per [AUSTRAC](https://austrac.gov.au/node/1158) [P\*]. About 80–90k new reporting entities ([Legl](https://legl.com/articles/austrac-opens-enrolment-for-tranche-2-professions-what-law-firms-need-to-know-before-1-july)). Many vendors already: Legl, [Persona](https://withpersona.com/blog/tranche-2-australia), [Zyphe](https://www.zyphe.com/resources/blog/austrac-tranche-2-enrolment-guide), [EasyAML](https://easyaml.com/wp-content/uploads/2025/11/AML-Obligations-Brochure-1.pdf), ShareRing (vendor claims). |
| 14 | A Mallorca scooter or campervan rental shop must send each contract to SES.HOSPEDAJES within 24 h and keep data 3 years → SES connector | H8 + C6 | Duties per [Partee](https://partee.es/seshospedajes/) and [Pulso](https://pulsorent.com/es/resources/ses-hospedajes-automatizar-el-registro-de-alquileres-de-coches-y-motos/); a vendor claims fines of €100–30,000. Tools already sold: Pulso, Partee, [seshospedajes.es](https://seshospedajes.es/), campervan-rental software. Small pool. |
| 15 | An EU micro/small operator placing in-scope commodities on the market faces the EUDR from 30 Jun 2027 → declaration tool | C1/Q10 + H8 | Micro/small primary operators now make one simplified declaration, which is effectively one-off. Dates are 30 Dec 2026 and 30 Jun 2027, and the Commission ruled out a further delay in May 2026 ([Bird & Bird](https://www.twobirds.com/en/insights/2025/out-of-the-woods-the-eudr-postponed-and-simplified), [myDPP](https://mydpp.app/en/knowledge/eudr-delay-current-status-and-deadlines)). Crowded: [Coolset](https://www.coolset.com/academy/eudr-delay-2025-explained), Trusty, myDPP (vendor claims). |
| 16 | A cross-border micro e-seller must register and report packaging, battery and WEEE producer responsibility (EPR) in each country → multi-country EPR hub | H8 (+H2/H3: authorised-representative roles need a legal presence) | [U] Crowded EPR service providers. |
| 17 | A small DE/EU e-shop (10+ staff) must meet the European Accessibility Act (from 28 Jun 2025) → accessibility monitor | H8 | [U] Crowded scanners and overlays; micro service providers are reportedly exempt (verify). |
| 18 | An EU employer with fewer than 100 staff must answer pay-information requests (Pay Transparency Directive) → pay-transparency responder | C1/H8 | [U] Reporting starts at 100+ staff; HR suites cover the rest. |
| 19 | An EU handmade seller must show product-safety (GPSR) data per listing → listing helper | H4/H8 | [U] Marketplaces collect the fields; responsible-person services are crowded. |
| 20 | A small connected-product maker must share device data under the EU Data Act → data-request portal | Q1 (no duty) | [U] Micro and small enterprises are reportedly exempt from the data-sharing chapter (verify). |
| 21 | An EU short-term-rental host must display a registration number (EU STR Regulation, 2026) → host compliance app | H8/H4 | [U] Duties fall mainly on platforms; host check-in tools are crowded (e.g. Partee, vendor claim). |
| 22 | An EU repair shop under the Right to Repair Directive → repair-form generator | Q1 (no recurring duty) | [U] The EU repair form is reportedly voluntary for repairers. |
| 23 | A US micro e-commerce firm and the state privacy laws → privacy request desk | Q1/H8 | [U] Thresholds exempt most micro firms; consent tools are crowded. |
| 24 | A DE/ES employer must record working time digitally → time-recording app | H8 + Q10 | [U] Dozens of apps; the German law is still pending. |
| 25 | A US independent pharmacy loses its small-dispenser DSCSA exemption (Nov 2026) → DSCSA desk | H4 | [U] Wholesaler portals and pharmacy-system vendors cover it. |
| 26 | A US machine shop subcontracting to the DoD needs CMMC Level 1/2 self-assessments → CMMC L1 kit | H8 | [U] Crowded compliance vendors. |
| 27 | A UK hobby-forum admin must keep Online Safety Act risk records → OSA records app | H5/C2 | [U] Payers are volunteers; the regulator offers a free toolkit. |
| 28 | A UK micro employer must keep holiday-pay records and make guaranteed-hours offers (Employment Rights Act 2025) → records app | H4/H8 | [U] Payroll and rota incumbents will add these features. |
| 29 | A micro hardware/IoT maker must report actively exploited vulnerabilities within 24 h (since 11 Sep 2026) and meet CRA product rules from 11 Dec 2027 → **FINALIST 1: CRA Logbook** | — | See card F1. |
| 30 | A small importer/distributor of connected products must verify CE marking, the declaration of conformity and technical documentation, and keep them for 10 years (CRA, 11 Dec 2027) → **FINALIST 2: compliance vault** | — | See card F2. |
| 31 | A small e-bike/LMT battery assembler must issue a battery passport for every battery from 18 Feb 2027 → **FINALIST 3: Battery Passport Lite** | — | See card F3. |
| 32 | An Australian/UK smart-device maker needs a statement of compliance and a published support period (AU since 4 Mar 2026; UK PSTI [U]) → SoC generator | Merged into F1 | It is a feature of F1, not a business on its own ([legislation.gov.au F2025L00276](https://legislation.gov.au/F2025L00276/asmade/2025-03-04/text/original/epub/OEBPS/document_1/document_1.html) [P\*]). |

### Obligation register (answers the key questions)

| Obligation | Who must comply | From | Penalty / consequence | Entities affected | Recurring? | Existing tool prices seen | Deterministic tool without advice (H3)? | Underserved for micro firms? | Check level |
|---|---|---|---|---|---|---|---|---|---|
| EU Cyber Resilience Act Art. 14 (reporting) + product rules | Manufacturers of products with digital elements on the EU market, incl. non-EU firms | Art. 14: 11 Sep 2026; rest: 11 Dec 2027 | Up to €15m or 2.5% of turnover; micro/small firms are not fined for missing the 24 h early warning; no CE marking means no EU sale | No count found; ENISA says SMEs are most of the manufacturers, importers and distributors | Yes: continuous monitoring, every release, 10-year records | Free OSS; €10/mo SBOM-only; $159–199/mo SBOM + CRA wizard; $18k/yr enterprise | Yes | **Yes** | [P\*]+[S] |
| CRA Art. 19/20 (importers/distributors) | Importers and distributors of those products | 11 Dec 2027 | Fines (figures conflict between sources); withdrawal | No count | Yes: per SKU, alerts, 10-year retention | No priced tool found | Yes | Probably (thin evidence) | [S] |
| Batteries Regulation Art. 77 (passport) | The operator that completes the battery: light-means-of-transport (LMT, e.g. e-bike), EV and industrial >2 kWh batteries | 18 Feb 2027 | Battery cannot be placed on the market; national penalties not verified | No count | Yes: per battery, data kept alive | Not found (enterprise digital-product-passport vendors) | Yes | Probably | [S] |
| AU smart-device security standards | Manufacturers/suppliers of consumer smart devices | 4 Mar 2026 | Not verified | — | Per product | Free gov template | Yes | Merged into F1 | [P\*] |
| UK Awaab's Law | Social landlords in England | 27 Oct 2025; Phase 2: 30 Nov 2026; Phase 3: 2027 | Implied tenancy term, Ombudsman, regulator | ~1,411 private providers (2021) | Yes | Several vendors (prices not public) | Yes | No (crowded) | [P\*] |
| UK Martyn's Law | Venues with 200+ capacity and qualifying events | ~Spring 2027 | £10k (standard tier); £18m or 5% (enhanced) | ~180k premises across both tiers (second-hand estimate, unverified) | Weakly | Free (Halo 2023), £50+/mo | Yes | No (low WTP) | [S] |
| UK Digital Waste Tracking | Permitted waste receivers (Phase 1); carriers, brokers and dealers (2027) | 1 Oct 2026 | Not verified | No count | Yes: every load | Gov service (~£26/yr per one source); 8+ vendors | Yes | No (crowded) | [P\*]+[S] |
| US FSMA 204 | Holders of foods on the traceability list (small retailers/restaurants exempt) | 20 Jul 2028 | FDA enforcement | No count | Yes | Many vendors | Yes | No (crowded, may be softened) | [P\*] |
| AU AML/CTF Tranche 2 | Lawyers, accountants, real-estate firms, trust/company service providers, dealers in precious metals/stones | 1 Jul 2026 | AUSTRAC enforcement | 80–90k entities | Yes | Many vendors | Partly (ID checks usually OCR/biometric) | No (crowded) | [P\*]+[S] |
| EUDR | Operators/traders | 30 Dec 2026 / 30 Jun 2027 | National | — | Micro/small primary operators: one simplified declaration | Many tools | Yes | No | [S] |
| E-invoicing DE/FR/BE/PL | All VAT businesses (phased) | 2025–2027 | National | Millions | Yes | Many tools, some free | Yes | No | [S] |
| ES SES.HOSPEDAJES (vehicle rental) | Car/moto/campervan renters without driver | In force | €100–30k (vendor claim) | Small pool | Yes: per contract | Several tools | Yes | No | [S] |
| NY LLC Transparency Act | Foreign LLCs only | 2026 | — | Domestic LLCs out | — | — | — | No duty | [S] |

### Inferences
- The fastest-filling niches had three things in common: a single country, a single payer type, and a loud deadline. Examples: Awaab's Law, DWT, Tranche 2 and FSMA 204. Vendors (including existing incumbents) added modules within months.
- **Size-agnostic EU product rules hit micro firms that have never bought compliance software.** The CRA and the Batteries Regulation passport are examples. Existing tools are priced per developer or per enterprise, for example Interlynk at $18k/yr for 10 developers ([AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-n6mc7symiq2rm)). This is the clearest root-cause class (a)+(d) gap I found.
- **"Free from the authority" is a real H4-style threat in this lens.** Examples include KSeF, the Defra DWT service and ProtectUK guidance, even though H4 lists only big tech, banks and incumbents.

### Gaps
- **[U] rows were not re-verified.** Rows 6, 7 and 16–28 rely on prior knowledge for dates and crowding claims; the web-search budget ran out. Missing items include:
  - MTD ITSA thresholds and dates
  - Renters' Rights Act commencement dates
  - the European Accessibility Act micro exemption
  - Pay Transparency transposition status
  - the GPSR date
  - the Data Act exemption
  - the STR Regulation date
  - Right to Repair transposition
  - the DSCSA exemption date
  - CMMC phases
  - UK PSTI dates
- **Penalty amounts not found** for Belgian Peppol, Digital Waste Tracking, the Battery passport (national rules under Art. 93) and the AU smart-device rules.
- **H8 tests are incomplete.** Funding or profitability of Awaab/DWT/FSMA vendors was not verified. H8 is "funded or clearly profitable" and those kills rest on vendor counts. They are at least C3 failures.
- **Two numbers could not be traced to a named source.** Both appeared only in search summaries that did not attribute them:
  - "~180,000 premises in scope of Martyn's Law (both tiers)", said to come from a Home Office impact assessment;
  - "~£26 per legal entity per year" for the Defra Digital Waste Tracking service.
- **Conflicting dates.** Sources disagree on whether Digital Waste Tracking Phase 2 starts in April or October 2027.
- **Martyn's Law fine figures.** The standard-tier maximum of £10k comes from one law-firm summary. Another source cites £50k per day; this is unreconciled.

---

## (2) FINALIST IDEA CARDS

### F1 — "CRA Logbook": a deterministic Cyber Resilience Act workbook for micro hardware/IoT makers (EU-wide; launch Germany)

**Takeaway:** This is the strongest idea from this lens. The duty has been live since 11 Sep 2026 and a larger cliff comes on 11 Dec 2027. Micro firms are within scope and the tools on offer are priced for enterprises or cover SBOMs only. The main uncertainties are whether micro makers will pay and how quickly they become aware of the duty.

**Hard-rule check:**
- **H1 pass:** core logic is SBOM parsing, string and identifier matching against public vulnerability feeds, timers and templates.
- **H2 pass:** see the 12-week plan in Q6.
- **H3 pass:** a records and clocks tool, not legal advice; it never decides whether a product is compliant.
- **H4 pass, with risk:** GitHub and OSS tools commoditise vulnerability matching, but not the CRA workflow, documents or multi-jurisdiction statements. There is no single gatekeeper; ENISA's platform has no API, so nothing to revoke.
- **H5 pass:** the manufacturer pays directly.
- **H6 pass.**
- **H7 pass.**
- **H8 pass:** only sbomify sells a comparable CRA wizard at a similar price; others are SBOM-only, free, waitlisted or enterprise-priced.

**Q1 — Who suffers, when, how often, what it costs.** The founders of a 3-person company selling its own smart-home sensor in the EU must notify the authorities within 24 hours whenever they learn a product has an actively exploited security hole. This has applied since 11 Sep 2026. From 11 Dec 2027 they must also keep, for every product:
- an SBOM (software parts list)
- a declared security-support period
- vulnerability records
- a CE technical file

They have no security team, no process, and no affordable tool.
- *Moment:* a security researcher's email, a dependency CVE, a new firmware release, or preparing CE paperwork.
- *Frequency:* continuous monitoring; every release (assumed monthly); exploited-vulnerability events are rare but carry a deadline.
- *Cost:* days of engineering time per product to build the documentation (ASSUMPTION: 5–10 person-days initially, 1–2 per month after), plus fine and market-withdrawal risk, plus 24-hour-clock stress.

**Exact obligation:**
- **Law:** Regulation (EU) 2024/2847 (Cyber Resilience Act).
- **Article 14 deadlines, actively exploited vulnerability:** early warning within **24 h** of becoming aware; vulnerability notification within **72 h**; final report no later than **14 days** after a corrective measure is available ([EUR-Lex consolidated text](https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20) [P\*]).
- **Article 14 deadlines, severe incidents:** 24 h, 72 h, and a final report within one month ([EUR-Lex HTML](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ%3AL_202402847) [P\*]).
- **Start dates:** Article 14 has applied since **11 Sep 2026**; the rest applies from **11 Dec 2027** ([EUR-Lex HTML](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ%3AL_202402847) [P\*]; [Commission CRA reporting page](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting) [P\*]). The Dec 2027 obligations include CE marking, technical documentation, SBOM and conformity assessment ([Themio](https://www.themio.ai/en/blog/cyber-resilience-act-software-sme-2026), vendor claim; [ING-ISM](https://www.ing-ism.de/magazin/sbom-cyber-resilience-act-compliance/) [S]).
- **Where reports go:** through ENISA's Single Reporting Platform (SRP) to the national CSIRT of the main establishment, with ENISA notified at the same time ([Commission](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting) [P\*]).
  - The SRP launched on 11 Sep 2026 ([ENISA](https://www.enisa.europa.eu/news/the-cra-single-reporting-platform-is-launched) [P\*]).
  - It is a web portal behind EU Login with multi-factor authentication: one primary representative and up to 20 secondary ones.
  - **There is no API yet; one is "planned"** ([CSA research note](https://labs.cloudsecurityalliance.org/research/csa-research-note-enisa-cra-reporting-platform-20260918-csa/); [cyberresilienceact.eu](https://www.cyberresilienceact.eu/es/news/enisa-srp-guidance-update-3-august-2026.html) [S]).
- **Who must comply:** manufacturers of hardware or software products with digital elements made available in the EU, including non-EU companies ([Baker McKenzie](https://connectontech.bakermckenzie.com/new-eu-regulation-requires-cybersecurity-for-software-and-smart-devices/) [S]). Reporting also covers products already on the market; there is no grandfathering ([The Lawyer](https://www.thelawyer.com/briefing/selling-products-with-digital-elements-in-the-eu/) [S]).
- **Penalty:**
  - Up to **€15m or 2.5%** of worldwide turnover ([Greenberg Traurig](https://www.gtlaw.com/en/insights/2026/9/eu-cyber-resilience-act-cra-and-software-new-cybersecurity-obligations-and-ce-marking); [shattered.io](https://shattered.io/at/cyber-resilience-act-2026/) [S]). One vendor cites €5m/1% for "other actors", so the sources conflict ([ecocomply](https://ecocomply.ai/blog/cyber-resilience-act-reporting-2026), vendor claim).
  - **Micro and small enterprises are not fined for missing the 24-hour early-warning deadline** (CRA recitals, [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ%3AL_202402847) [P\*]). The operative article number was not visible in the extract; my reading is Art. 64(10)(a), to be verified.
- **SBOM format:** CycloneDX and SPDX are both accepted under BSI TR-03183-2 ([sbom-management.de](https://sbom-management.de/checkliste) [S]).
- **Adjacent rules the same product serves:** Australia's smart-device standards have been in force since 4 Mar 2026. Each device needs a statement of compliance and a support-period declaration ([legislation.gov.au](https://legislation.gov.au/F2025L00276/asmade/2025-03-04/text/original/epub/OEBPS/document_1/document_1.html) [P\*]; [Home Affairs template](https://www.homeaffairs.gov.au/cyber-security-subsite/files/soc-template-security-standards-for-smart-devices.pdf) [P\*]). The UK PSTI regime is [U].

**Q2 — The one thing.** For each product, the app does four things:
- keeps the SBOM current from the maker's build files and checks it daily against public vulnerability feeds;
- runs the 24 h / 72 h / 14-day / 1-month clocks with copy-ready report drafts for ENISA's SRP;
- generates the CRA paperwork: support-period statement, user security information, vulnerability-disclosure policy and security.txt, technical-file index, and an EU declaration of conformity skeleton;
- produces the AU and UK statements of compliance.

**Q3 — Who already solves it** (searched in English and German)

| Name | Country | Price | What it does | Gap for micro hardware makers |
|---|---|---|---|---|
| [sbomify](https://sbomify.com/pricing/) | n/v | Community free. Business $159/mo billed annually; the [FAQ](https://sbomify.com/faq/) says $199; [SourceForge](https://sourceforge.net/software/product/sbomify/) says £49/mo. Vendor claims that conflict. | SBOM management, with a "CRA Compliance Wizard" in Business | SBOM-centric and aimed at "mid-size teams". Reporting clocks, hardware technical file and AU/UK statements not evident. **Closest competitor.** |
| Interlynk ([AWS listing](https://aws.amazon.com/marketplace/pp/prodview-n6mc7symiq2rm); [free tier](https://www.interlynk.io/resources/interlynk-launches-free-tier-of-sbom-automation-platform)) | n/v | Free tier; paid $18k/yr for 10 developers up to $100k/yr for 100 | SBOM automation for FDA and CRA | Enterprise pricing; developer-seat model doesn't fit hardware micro firms |
| [SBOM Central](https://sbomcentral.com/pricing/) | n/v | €10/mo (1 user, 1 product); listing ~623 days old | SBOM hosting | SBOM only; no CRA workflow evident |
| OCCTET open-source toolkit ([B2B Cyber Security](https://b2b-cyber-security.de/cyber-resilience-act-cra-open-source-toolkit-fuer-kmu-meldeplichten/)) | EU (n/v) | Free | Open-source help for SMEs to find components and vulnerabilities | Do-it-yourself, needs engineers; scope unclear. **Free substitute risk.** |
| [cyberresilienceact.eu analyser](https://www.cyberresilienceact.eu/analysis.html) | n/v | €0 | SBOM and vulnerability analysis for Art. 14 | Free point tool; no records or clocks evident |
| [Themio](https://www.themio.ai/en/blog/cyber-resilience-act-software-sme-2026) | n/v | Waitlist only | Vulnerability-reporting workflow for software SMEs | Not selling yet; software-focused |
| [Certivo](https://www.certivo.com/frameworks/eu-cyber-resilience-act) | n/v | n/v | Collects supplier SBOMs; validates against 21 essential requirements | Aimed at supply-chain teams in larger firms |
| [distr.sh](https://distr.sh/cyber-resilience-act/) | n/v | n/v | CRA for software vendors (distribution platform) | Software-only |
| Cycode / Mend / FOSSA / Cloudsmith ([Cycode](https://cycode.com/blog/cyber-resilience-act/), [Mend](https://www.mend.io/blog/eu-cyber-resilience-act-compliance-guide/)) | US/IL (n/v) | Quote-based | Application security and SBOM platforms | Priced for large B2B organisations |
| [ENISA SRP](https://www.enisa.europa.eu/news/the-cra-single-reporting-platform-is-launched) | EU | Free | Official reporting portal | No clocks across products, no drafts, no documents, no API |
| [BSI helpdesk / IHK guidance](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Cyber_Resilience_Act/cyber_resilience_act.html) | DE | Free | Advice and information for small firms | Advice, not tooling. **Referral channel, not a competitor.** |

German-language search turned up checklists, consultancies and the free toolkit, but **no priced CRA tool for small firms** ([sbom-management.de](https://sbom-management.de/checkliste), [ING-ISM](https://www.ing-ism.de/magazin/sbom-cyber-resilience-act-compliance/), [shattered.io](https://shattered.io/at/cyber-resilience-act-2026/)). No traction data was found for any vendor.

**Q4 — Root-cause class: (d) + (a)** (and partly (b)).
- **(d) A new rule made it necessary:** reporting went live on 11 Sep 2026.
- **(a) Too small for funded companies:** ENISA says SMEs make up most manufacturers, importers and distributors ([ENISA SME model, July 2026](https://www.enisa.europa.eu/sites/default/files/2026-07/SME%20maturity%20assessment%20model_final.pdf) [P\*]). Funded vendors sell per developer seat at enterprise prices (Interlynk).
- **(b) Partly fragmentation:** EU CRA plus the AU and UK regimes.

Not (f) or (g): the economics work and it is solo-buildable.

**Q5 — Is it profitable?**

| Item | Value | Status |
|---|---|---|
| Price | Starter €49 / Pro €99 / Team €199 per month | ASSUMPTION, anchored to sbomify Business $159/mo ([VERIFIED vendor claim](https://sbomify.com/pricing/)) and SBOM Central €10/mo ([VERIFIED vendor listing](https://sbomcentral.com/pricing/)) |
| Blended revenue per customer (ARPU) | €85/month | ASSUMPTION |
| Cost per customer | €5.50/month: compute and feed sync €3, email/SMS alerts €1, payment fees €1.50 | ASSUMPTION (payment-fee rate not re-verified) |
| Gross margin | ≈ 93.5% | Derived from assumptions |
| Fixed business costs | €1,900/month: tooling/hosting €150, accountant €250, professional-indemnity insurance €150, legal €100, marketing €800, translation €200, events €150, misc €100 | ASSUMPTION |
| Customers needed for €8k/month profit | (8,000 + 1,900) / (85 − 5.5) ≈ **125** | Derived |
| Reachable pool | Germany has **7,860** computer/electronics/optical manufacturers (NACE C26, 2024) | [VERIFIED (Statista/Eurostat)](https://statista.com/statistics/383747/enterprises-manufacturing-computer-electronic-optical-products-germany) |
| Wider pool | EU-wide connected-hardware makers plus own-brand importers ≥ 12,000 (assumes 40–60% of C26 firms make connected products, scaled to the EU) | ASSUMPTION |
| Share of pool needed | ≈ 1.6% of Germany's C26 firms alone; ≈ 1% of a conservative EU hardware pool | Derived |
| Customer acquisition cost (CAC) | €250 | ASSUMPTION |
| Lifetime value / LTV:CAC | 24-month life → ≈ €1,900 → LTV:CAC ≈ 7.6 | Derived from ASSUMPTIONS |

**Q6 — How to build it.**
- **MVP scope:** organisations, products, releases and components; SBOM import (CycloneDX/SPDX) plus manual entry for hardware parts; daily vulnerability matching; event clocks with escalating alerts; document generator; evidence export.
- **Stack:** Django or Next.js, Postgres, a job queue, object storage, Stripe Billing, an email API plus SMS for escalation.
- **Data rails:** public vulnerability databases such as OSV/NVD/EUVD and an "exploited" signal such as CISA's catalogue. These are ASSUMPTIONS: availability and licences not verified in this pass.
- **No ENISA integration is possible yet** because the SRP has no API, so the app produces copy-ready drafts.

| Weeks | Build |
|---|---|
| 1–2 | Data model, authentication, billing, SBOM import |
| 3–4 | Matching engine (identifier rules), per-product status (affected / not affected / fixed), daily sync, alerts |
| 5–6 | Report clocks (24 h / 72 h / 14 d / 1 month), timestamped audit log, SRP-field drafts |
| 7–8 | Document generator: support period, user security info, disclosure policy and security.txt, technical-file index, declaration of conformity skeleton, AU statement-of-compliance template |
| 9–10 | GitHub Action/CLI for SBOM upload from CI; multi-product dashboard; evidence pack (PDF/ZIP) |
| 11 | German localisation, onboarding wizard, disclaimers, data-processing agreement, security hardening |
| 12 | Beta with 5 design partners; launch |

**Q7 — Where to launch first: Germany, with an English UI from day one.** The evidence for the gap:
- Germany has the largest national pool among the C26 counts I found: 7,860 firms, against Greece's 421 ([Statista DE](https://statista.com/statistics/383747/enterprises-manufacturing-computer-electronic-optical-products-germany); [Statista GR](https://www.statista.com/statistics/383752/enterprises-manufacturing-computer-electronic-optical-products-greece)).
- Institutions are actively pushing awareness: BSI plans helpdesks for small firms and IHK publishes manufacturer duties ([BSI](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Cyber_Resilience_Act/cyber_resilience_act.html); [IHK Schwaben](https://www.ihk.de/schwaben/produktmarken/digitalisierung/it-sicherheit/cyber-resilience-act-pflichten-hersteller-6951410)).
- German search found no priced CRA tool for small firms (Q3).

Second markets: NL and the Nordics (English-friendly; the Dutch government publishes CRA guidance on [business.gov.nl](https://business.gov.nl/amendments/mandatory-cybersecurity-requirements-for-products-cra/)). Then non-EU makers who sell into the EU and AU.

**Q8 — How it makes money.**
- **Model:** subscription tiered by number of products; annual prepay with 2 months free.
- **Founding offer:** "CRA Readiness" at €490/yr for the first 20 customers, used as the pre-sale (ASSUMPTION).
- **Payer:** the manufacturer (managing director or CTO).
- **Payment:** card or SEPA direct debit via a payment processor (fees are an ASSUMPTION).

**Q9 — How one person runs it.**
- **Automation:** feed sync, matching, clocks and documents are fully automatic. Support is through documentation, templates and a monthly office hour. Legal questions are referred to the BSI helpdesk or lawyers (keeps it inside H3).
- **Failure modes and mitigations:**

| Failure mode | Mitigation |
|---|---|
| Feed outage | Secondary feed as fallback |
| False positives | Per-product "not affected" statuses |
| False negatives | Disclaimer plus manual entry |
| Alert not delivered | Email + SMS + acknowledgement required |
| Template drift after rule changes | Versioned templates |

- **Support load:** ASSUMPTION of < 5 tickets per week per 100 customers.

**Q10 — What did I miss? Kill tests.**
- **Deadline postponed or rule simplified:**
  - Reporting is already live, so it cannot be postponed backwards.
  - The EU has slipped other product rules: EUDR twice, and battery due diligence moved to Aug 2027 ([Bird & Bird](https://www.twobirds.com/en/insights/2025/out-of-the-woods-the-eudr-postponed-and-simplified); [Battery-Tech](https://battery-tech.net/the-eu-battery-passport-belongs-to-whoever-finishes-the-battery-four-months-before-it-becomes-mandatory/)). So a delay to Dec 2027 or an SME carve-out is plausible. That would stretch the sales cycle.
  - Mitigation: keep the core value in reporting clocks, support-period records and documents, which survive a simplification.
- **Platform kill:** GitHub/GitLab dependency alerts [U] commoditise matching. If they add CRA templates, hardware micro makers still need the technical file, AU/UK statements and 10-year records. **Risk: medium.**
- **Incumbent copy:** sbomify already has a CRA wizard (vendor claim), and the free OCCTET toolkit exists. **Risk: medium.** Compete on price and hardware fit.
- **Liability:** a missed match could lead a customer to miss a deadline. Mitigate with disclaimers and a "diligent process" log. Stakes are lower because micro/small firms are not fined for missing the 24-hour warning [P\*].
  - **That same exemption also lowers urgency. This is the weakest point of the pain story.**
- **False assumptions:**
  - Willingness to pay is untested.
  - Awareness may be low: the ENISA SME survey had only 194 respondents ([ENISA](https://www.enisa.europa.eu/news/where-do-smes-stand-in-preparing-for-the-cyber-resilience-act) [P\*]).
  - Own-brand importers being treated as manufacturers (Art. 21) is not verified.
- **Churn:** records must be kept 10 years (ASSUMPTION: low churn), but product exits create churn (ASSUMPTION ~2%/month).
- **Seasonality:** a spike before Dec 2027, then risk of a plateau.

**First 10 paying customers** (≤ €2,000, ≤ 90 days; all ASSUMPTIONS):
1. Open-source a free "cra-clock" CLI/GitHub Action that turns an SBOM into a readiness report and clock template, as a lead magnet (€0).
2. German/English landing page with the €490/yr founding plan (≤ €100).
3. Personal outreach to 300 German micro electronics makers (IHK directories, embedded-trade-fair exhibitor lists, Tindie/Crowd Supply seller pages), offering a 30-minute "CRA gap call" (≤ €300 for list cleaning).
4. Posts in Hackaday.io, r/embedded, Home Assistant/ESPHome and Zephyr communities (€0).
5. Two webinars co-hosted with an IHK or a CE consultancy (≤ €500).
6. Referral deals with 3 CE/RED test labs or consultants at a 20% revenue share.

Goal: 10 × €490 = **€4,900** pre-paid signal.

**Inferences:** F1's strengths:
- The obligation is already live and covers products already on sale.
- The pool is large (≤ 2% needed).
- Competitors are either free and do-it-yourself, or enterprise-priced.

F1's weaknesses:
- The micro/small fine exemption for the 24-hour warning dampens fear.
- Willingness to pay is unproven.

**Gaps:**
- No count of CRA-affected manufacturers; the Commission's impact assessment was not retrieved.
- Funding and traction of sbomify, Themio and Certivo unknown.
- Art. 64 numbering and the €5m vs €15m conflict unresolved.
- Art. 21 (own brand) not verified.
- Licences and availability of the vulnerability feeds not verified.
- UK PSTI dates not verified.

---

### F2 — "Connected-product compliance vault" for small importers and distributors (EU; launch Germany)

**Takeaway:** This is a real, recurring duty with a clear payer. But it binds only from 11 Dec 2027, evidence of the gap is thin, and marketplaces or legal-text providers can copy it. It scores in the KILL band and only marginally above my baseline score.

**Hard-rule check:**
- **H1 pass:** checklists, document storage, reminders.
- **H2 pass.**
- **H3 pass:** it verifies that documents are present, not that products comply.
- **H4 pass, with risk:** a marketplace such as Amazon could add document checks [U]. The launch targets own-shop and B2B distributors, not Amazon-only sellers, and does not depend on any one marketplace.
- **H5 pass:** the shop pays.
- **H6 pass.**
- **H7 pass:** suppliers upload for free and are not a second paying side.
- **H8 pass on available evidence:** no priced deterministic tool found.

**Q1.** The owner of a 6-person Cologne web shop importing smart cameras and plugs from three Shenzhen factories must, for every SKU:
- check the CE marking, EU declaration of conformity and technical documentation;
- show manufacturer and importer contact details;
- keep the papers for 10 years;
- pass on security problems.

This becomes legally binding under the CRA on 11 Dec 2027. Today the documents sit in email threads and supplier chats.
- *Frequency:* every new SKU, supplier change or advisory, assumed weekly.
- *Cost:* hours per SKU, plus withdrawal and fine risk.

**Exact obligation:**
- **Law:** Regulation (EU) 2024/2847.
- **Art. 19 (importers):** before placing a product on the market, verify the manufacturer's conformity assessment, CE marking, declaration of conformity and technical documentation; put contact details on the product or packaging; keep documentation available to authorities for **10 years** ([The Art of Service](https://compliance.theartofservice.com/controls/eu-cyber-resilience-act/cra-art-19-20); [Springlex Art. 19 text](https://www.springlex.eu/en/packages/cra/cra-regulation/article-19/) [S]).
- **Art. 20 (distributors):** verify the CE marking and that manufacturer and importer obligations were met and documents supplied ([Prighter Art. 20](https://prighter.com/resources/laws/cyber-resilience-act/articles/article-20) [S]).
- The Dutch government says importers and distributors must ensure products meet the requirements and **continue to** meet them, with documentation and reports ([business.gov.nl](https://business.gov.nl/amendments/mandatory-cybersecurity-requirements-for-products-cra/) [P\*]).
- **From:** 11 Dec 2027 ([EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ%3AL_202402847) [P\*]).
- **Penalty:** fine figures for non-manufacturer duties conflict (€5m/1% per [ecocomply](https://ecocomply.ai/blog/cyber-resilience-act-reporting-2026), vendor claim; my reading of Art. 64 is €10m/2%, unverified). Market-surveillance withdrawal is also possible.
- **Note:** importers selling under their own brand reportedly become manufacturers (Art. 21) [U]. That would make them F1 customers.

**Q2.** One vault per SKU that:
- collects supplier documents through a magic-link upload;
- runs a fixed checklist per SKU (CE, declaration fields, addresses, support period, user security info);
- tracks end-of-support dates and manufacturer advisories;
- exports an evidence pack in one click.

**Q3 — Competitors**

| Name | Country | Price | What it does | Gap |
|---|---|---|---|---|
| [xictron](https://www.xictron.com/de/blog/cyber-resilience-act-online-shops-pflichten-2026/) | DE | n/v (agency) | E-commerce agency publishing CRA duties for online shops | A service, not a self-serve tool. **Channel partner candidate.** |
| [ecocomply](https://ecocomply.ai/blog/cyber-resilience-act-reporting-2026) | n/v | n/v | Compliance for electronics sellers (AI-branded, vendor claim) | Not deterministic; price unknown |
| [Presencis](https://cdn.presencis.com/regulations/cra/article-20/) | n/v | n/v | CRA content and services | Unclear product |
| [The Art of Service](https://compliance.theartofservice.com/controls/eu-cyber-resilience-act/cra-art-19-20) | n/v | n/v | Control templates | Templates only, no workflow |
| [Prighter](https://prighter.com/resources/laws/cyber-resilience-act/quick-access) | n/v | n/v | Legal-text access and representation services | No per-SKU vault evident |
| GPSR document / responsible-person services; marketplace tools | various | [U] | Product-safety document storage | May extend to CRA. **Main copy risk.** |

**No priced, deterministic per-SKU CRA importer workflow was found.** That is absence of evidence, not evidence of absence.

**Q4 — Root cause: (d) + (b) + (a).**
- (d) A new rule.
- (b) Fragmentation across CRA, radio-equipment and product-safety rules plus national enforcement.
- (a) Shops are too small for enterprise product-compliance suites.

**Q5 — Is it profitable?**

| Item | Value | Status |
|---|---|---|
| Price | €29 (≤ 50 SKUs) / €69 (≤ 500) / €149 (unlimited, 5 users) per month | ASSUMPTION |
| ARPU | €55/month | ASSUMPTION |
| Cost per customer | €4/month (storage, email, payment fees) | ASSUMPTION |
| Gross margin | ≈ 93% | Derived |
| Fixed costs | €1,900/month | ASSUMPTION (as F1) |
| Customers needed for €8k profit | 9,900 / 51 ≈ **195** | Derived |
| Reachable pool | ≥ 10,000 EU e-shops and distributors selling connected products; DE first | ASSUMPTION (no verified count) |
| Share needed | ≈ 2% | Derived |
| CAC / LTV / LTV:CAC | €150 / ≈ €1,220 (24 months) / ≈ 8 | ASSUMPTION / derived |

**Q6 — Build: MVP in 12 weeks.**

| Weeks | Build |
|---|---|
| 1–2 | SKU/supplier data model; CSV import from shop systems |
| 3–4 | Supplier upload links and reminders; fixed Art. 19/20 checklists |
| 5–6 | Advisory watch (manufacturer RSS/CSAF feeds registered manually); end-of-support calendar |
| 7–8 | Evidence pack export; 10-year retention; audit trail |
| 9–10 | DE/EN UI; optional read-only shop integrations (CSV first, so no gatekeeper dependency) |
| 11–12 | Beta with 5 shops; launch |

**Q7 — Where to launch: Germany.** The evidence is weak:
- German-language content on CRA duties for online shops exists ([xictron DE](https://www.xictron.com/de/blog/cyber-resilience-act-online-shops-pflichten-2026/)).
- Germany has a large electronics base (7,860 C26 firms per [Statista](https://statista.com/statistics/383747/enterprises-manufacturing-computer-electronic-optical-products-germany)).
- NL is second because its government explicitly addresses importers and distributors ([business.gov.nl](https://business.gov.nl/amendments/mandatory-cybersecurity-requirements-for-products-cra/)).

**Q8.** Subscription by SKU band, annual prepay, founding price €290/yr. Payer: the shop or distributor owner. Paid by card or SEPA.

**Q9.**
- Supplier chasing is automated and checks are deterministic, so support is low (ASSUMPTION).
- **Failure modes:** forged supplier documents (the tool checks presence and format, not authenticity, so a disclaimer is needed); unresponsive suppliers (escalation templates).

**Q10 — Kill tests.**
- **Deadline postponed or simplified:** 100% of the value is tied to 11 Dec 2027, so this is **high risk.** Omnibus postponements have precedent (EUDR, battery due diligence). A simplification for distributors would gut the product.
- **Platform kill:** marketplaces adding free CRA document checks [U]. **Medium**, mitigated by targeting own-shop and B2B distributors.
- **Incumbent copy:** GPSR responsible-person services and legal-text providers are an easy extension for them. **High.**
- **Liability:** false comfort from "complete" checklists. **Medium.**
- **False assumptions:** pool size and awareness are both unverified.
- **Churn:** low switching cost early on.
- **Seasonality:** retail Q4 crunch delays onboarding.

**First 10 paying customers** (ASSUMPTIONS):
1. Revenue-share partnerships with 2 German e-commerce agencies (e.g. xictron-type agencies).
2. Shop-system community posts.
3. IHK retail webinars.
4. Personal outreach to 200 German shops selling smart-home gear (from public shopping listings).
5. €290/yr founding price.

Total ≤ €2,000.

**Inferences:** This is the same regulation as F1, so both share postponement risk. A combined F1+F2 offering could serve own-brand sellers.

**Gaps:** pool size; competitor prices; Art. 64 figures; Art. 21; whether marketplaces plan CRA document checks.

---

### F3 — "Battery Passport Lite" for small LMT and industrial battery assemblers (EU)

**Takeaway:** A hard legal gate in about 4 months, with per-battery recurring usage and high switching costs. But the pool is small and unverified, the standards are still moving, and long-term data-availability duties are a heavy liability for one founder. It scores in the KILL band and only marginally above my baseline score.

**Hard-rule check:**
- **H1 pass:** IDs, QR codes, record hosting and access control.
- **H2 pass:** see the 12-week plan.
- **H3 pass:** no licence needed.
- **H4 pass, with risk:** cell or pack suppliers, or enterprise passport vendors, could bundle free passports.
- **H5 pass:** the assembler pays.
- **H6 pass.**
- **H7 pass.**
- **H8 pass on available evidence:** passport vendors exist but no SME pricing was found.

**Q1.** A 4-person Utrecht workshop that assembles e-bike and cargo-bike battery packs fits the battery-management system (BMS), so it "finishes" the battery. From 18 Feb 2027 it must give every battery it places on the EU market a **battery passport**: a unique ID, a QR code and an online record kept available. Without one it may not sell the battery. Today it tracks cell batches in spreadsheets.
- *Frequency:* every battery shipped, assumed daily.
- *Cost:* market access, plus the time to build records.

**Exact obligation:**
- **Law:** Regulation (EU) 2023/1542 (Batteries Regulation), Art. 77.
- **Scope and date:** LMT batteries, industrial batteries > 2 kWh and EV batteries placed on the market or put into service from **18 Feb 2027** must have a battery passport ([Scantrust](https://www.scantrust.com/eu-battery-regulation-eu-battery-passport-requirements/); [dpp-tool](https://dpp-tool.com/en/guide/battery-passport/); [Circuland](https://circuland.co.uk/en/resources/battery-passport-timeline) [S]).
- **Who issues it:** the operator that completes the battery, usually where the BMS is fitted, per the Commission FAQ as reported by [Battery-Tech](https://battery-tech.net/the-eu-battery-passport-belongs-to-whoever-finishes-the-battery-four-months-before-it-becomes-mandatory/) [S].
- **Not yet required in Feb 2027:** carbon footprint, recycled content and due-diligence data. Due diligence was postponed to 18 Aug 2027 by Regulation (EU) 2025/1561 and does not apply below €40m turnover (Battery-Tech [S]).
- **Simplification packages:** none moves the 18 Feb 2027 date, but the "Omnibus VIII" package amends producer definitions and labelling (Battery-Tech [S]).
- **Penalty:** batteries without a passport cannot be placed on the market ([Scantrust](https://www.scantrust.com/eu-battery-regulation-eu-battery-passport-requirements/) [S]). National penalty amounts were not verified (gap).
- Primary text not retrieved because EUR-Lex was blocked.

**Q2.** Issue, host and keep alive a passport (ID + QR + public and restricted views) for every battery a small assembler ships, generated in bulk from its production spreadsheet and priced per battery.

**Q3 — Competitors**

| Name | Country | Price | What it does | Gap |
|---|---|---|---|---|
| [Scantrust](https://www.scantrust.com/eu-battery-regulation-eu-battery-passport-requirements/) | n/v | n/v | Battery passport / product identity | SME pricing unknown |
| [Circuland](https://circuland.co.uk/en/resources/battery-passport-timeline) | n/v | n/v | Battery passport resources and tool | Unknown |
| [dpp-tool.com](https://dpp-tool.com/en/guide/battery-passport/) | n/v | n/v | Digital-product-passport tool | Possibly SME-focused. **Closest risk.** |
| [Tracepas (ClouterX)](https://www.clouterx.com/en/regulations/battery-passport) | n/v | n/v | Battery passport | Unknown |
| Enterprise passport platforms (e.g. Circulor, Minespider) | various | [U] enterprise | Supply-chain battery passports | Priced for EV/OEM scale [U] |

No prices found. **H8 is passed only on absence of evidence.**

**Q4 — Root cause: (d) + (a).** (d) A new rule with a hard date; (a) enterprise passport vendors target EV and automotive OEMs ([Automotive IQ](https://www.automotive-iq.com/electrics-electronics/articles/eu-battery-passport-explained-requirements-timeline-and-compliance-steps-to-2027)).

**Q5 — Is it profitable?**

| Item | Value | Status |
|---|---|---|
| Price | €99/month base + €0.40 per passport | ASSUMPTION |
| ARPU | €180/month (≈ 200 passports/month) | ASSUMPTION |
| Cost per customer | €15/month (redundant storage, continuity escrow, payment fees) | ASSUMPTION |
| Gross margin | ≈ 92% | Derived |
| Fixed costs | €2,100/month (F1 costs + €200 for continuity/escrow and extra infrastructure) | ASSUMPTION |
| Customers needed for €8k profit | 10,100 / 165 ≈ **62** | Derived |
| Reachable pool | 1,000–3,000 EU finishers of LMT/industrial (> 2 kWh)/EV batteries | ASSUMPTION (no verified count) |
| Share needed | 2–6% | Derived |
| CAC / LTV / LTV:CAC | €400 / ≈ €7,900 (48 months; passports keep customers) / ≈ 20 | ASSUMPTION / derived |

**Q6 — Build: MVP in 12 weeks.**

| Weeks | Build |
|---|---|
| 1–2 | Data model following the Annex XIII categories as described in guides, with public / legitimate-interest / authority access tiers (ASSUMPTION: exact fields to be checked against the regulation); IDs; CSV bulk import |
| 3–4 | Fast public passport pages; restricted views with access requests and logs |
| 5–6 | Immutable version history; linking repurposed or remanufactured batteries to the original passport (ASSUMPTION) |
| 7–8 | Durability: multi-region backups, export, continuity escrow (whether this is legally required is unverified) |
| 9–10 | QR label PDFs; BMS-serial import; API for production lines |
| 11–12 | Pilot with 3 assemblers; launch |

**Q7 — Where to launch: Germany + Netherlands.** This is an ASSUMPTION based on e-bike assembly hubs; no country-level evidence was verified in this pass. The urgency evidence is EU-wide: the deadline is about 4 months away ([Battery-Tech](https://battery-tech.net/the-eu-battery-passport-belongs-to-whoever-finishes-the-battery-four-months-before-it-becomes-mandatory/)).

**Q8.** Base fee plus usage per passport, billed monthly or annually. The assembler or brand pays by card or SEPA. Founding plan: €990/yr including 2,000 passports (ASSUMPTION).

**Q9.**
- Mostly automated. Uptime matters because a passport outage reflects on the customer's market access.
- Standards and implementing acts will change and must be tracked.
- Support load is moderate: data mapping per customer at onboarding.

**Q10 — Kill tests.**
- **Deadline postponed or simplified:** Battery-Tech says no simplification moves Feb 2027 [S], but Omnibus VIII is reshaping definitions and labelling.
  - A postponement delays revenue.
  - A simplification (fewer fields) keeps the core value: ID, QR and hosting.
- **Platform kill:** Chinese cell or pack suppliers, or big passport platforms, offering passports free. **Medium-high.**
- **Incumbent copy:** passport vendors launching SME tiers. **Medium.**
- **Liability:** long data-availability expectations and the founder's insolvency risk. **High for a solo founder.**
- **False assumptions:** pool size; the issuer interpretation; whether the EU passport registry requires technical integration.
- **Churn:** low (records persist).
- **Seasonality:** e-bike production peaks in winter and spring.

**First 10 paying customers** (ASSUMPTIONS):
1. Personal outreach to battery-assembly and recell workshops and small LMT brands in DE/NL found through repair directories and trade-fair exhibitor lists.
2. A "4 months to go" webinar.
3. €990/yr founding plan with free migration from spreadsheets.

Total ≤ €2,000.

**Gaps:**
- Primary Art. 77/78 text not read.
- National penalties.
- Pool size.
- Competitor prices.
- Registry and standards status.
- Data-retention and insolvency duties.

---

## (3) PROVISIONAL SCORES

Weights: C1 10 · C2 15 · C3 10 · C4 15 · C5 15 · C6 5 · C7 10 · C8 10 · C9 5 · C10 5. Weighted score = Σ(score × weight) / 10.

### BASELINE: daily check-in call, Germany (for comparison)

| C | Score | One-line justification |
|---|---|---|
| C1 Pain | 6 | Daily worry about a parent lying undiscovered is real, but many families already run informal checks. |
| C2 WTP/payer | 5 | Families pay €27–40 for Hausnotruf, but the adult child pays while the senior uses it, and seniors may refuse. |
| C3 Gap | 5 | No device-free German service is named, but Hausnotruf providers could add a call service easily. |
| C4 Distribution | 4 | Consumer ads to adult children; no cheap named channel. |
| C5 Unit economics | 5 | ~70% margin at €9.90 vs €3 cost; consumer CAC and death/care-home churn give LTV:CAC ≈ 2. |
| C6 Market | 10 | 1,000 families out of millions of seniors living alone. |
| C7 Solo ops | 6 | Telephony plus 24/7 alerting, false alarms and family calls. |
| C8 Durability | 4 | Easy to copy; low switching costs. |
| C9 Risk | 4 | Liability if an alert fails and someone dies. |
| C10 Speed | 6 | A landing-page pre-sale is feasible. |
| **Total** | **52.0** | **KILL band** (sensitivity: plausible 50–58) |

### F1 — CRA Logbook

| C | Score | One-line justification |
|---|---|---|
| C1 Pain | 6 | Live 24 h/72 h duty, a Dec 2027 CE cliff and 10-year records; but exploited-vulnerability events are rare and micro/small firms are not fined for missing the 24 h warning. |
| C2 WTP/payer | 6 | The manufacturer pays directly to keep EU market access; an anchor price of $159–199/mo exists; micro willingness to pay is unproven. |
| C3 Gap | 7 | Tools found are free DIY, SBOM-only, waitlisted or enterprise-priced; German search found no priced tool for small firms. |
| C4 Distribution | 6 | Named cheap channels (OSS GitHub Action, maker communities, IHK/BSI events, trade-fair exhibitor lists), none validated yet. |
| C5 Unit economics | 7 | ~93% gross margin; LTV:CAC ≈ 7.6 on assumptions. |
| C6 Market | 9 | ~125 customers ≈ 1–1.6% of the pool. |
| C7 Solo ops | 6 | 12-week build is feasible; regulatory-interpretation questions and alert reliability add load. |
| C8 Durability | 6 | 10-year records and multi-jurisdiction templates help; GitHub, OSS toolkits and sbomify could encroach. |
| C9 Risk | 6 | Not advice; false-negative risk softened by disclaimers and the micro/small 24 h fine exemption. |
| C10 Speed | 7 | The duty is live now; a €490 founding pre-sale to makers preparing for Dec 2027 is feasible within 90 days. |
| **Total** | **64.5** | **TEST**: beats baseline by ~12 points |

### F2 — Connected-product compliance vault

| C | Score | One-line justification |
|---|---|---|
| C1 Pain | 5 | A real per-SKU chore, but legally binding only from Dec 2027. |
| C2 WTP/payer | 5 | Shop owner pays; budgets for compliance subscriptions exist but CRA awareness is low. |
| C3 Gap | 5 | No priced tool found, but evidence is thin and GPSR/legal-text providers sit next door. |
| C4 Distribution | 5 | Agencies, IHK and shop-system communities: plausible, unvalidated. |
| C5 Unit economics | 7 | ~93% margin; LTV:CAC ≈ 8 on assumptions. |
| C6 Market | 7 | ~195 customers ≈ 2% of an assumed pool. |
| C7 Solo ops | 7 | Simple CRUD, reminders and exports. |
| C8 Durability | 4 | Easy for marketplaces, GPSR vendors and legal-text providers to copy. |
| C9 Risk | 6 | Deterministic checks; risk of false comfort. |
| C10 Speed | 4 | The obligation is 14 months away; pre-sales are hard. |
| **Total** | **55.0** | **KILL band**: only +3 over baseline, within noise |

### F3 — Battery Passport Lite

| C | Score | One-line justification |
|---|---|---|
| C1 Pain | 6 | Hard market-access gate on 18 Feb 2027, needed for every battery. |
| C2 WTP/payer | 6 | The assembler pays directly; a per-battery fee is small next to the battery's value. |
| C3 Gap | 5 | Several passport vendors exist; their SME pricing is unknown. |
| C4 Distribution | 4 | Niche workshops and trade fairs; no verified cheap channel. |
| C5 Unit economics | 7 | ~92% margin; long lifetimes give LTV:CAC ≈ 20 on assumptions. |
| C6 Market | 4 | ~62 customers out of an assumed 1–3k pool (2–6%). |
| C7 Solo ops | 5 | Moving standards and long data-availability duties. |
| C8 Durability | 7 | High switching cost once passports are issued. |
| C9 Risk | 4 | Customers' market access depends on the founder's uptime and continuity. |
| C10 Speed | 7 | The deadline 4 months away makes pre-sales feasible. |
| **Total** | **56.0** | **KILL band**: only +4 over baseline, within noise |

**Verdict:** **Only F1 credibly beats the baseline.** F2 and F3 beat my baseline score by only 3–4 points, which is inside evaluator noise, and both are below the 60 TEST threshold. If evaluators score the baseline at 56 or higher, neither F2 nor F3 beats it.

---

## (4) SOURCES

### Cyber Resilience Act (primary or official, read via search extract)
- [EUR-Lex: Regulation (EU) 2024/2847, HTML](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ%3AL_202402847)
- [EUR-Lex: consolidated text](https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20)
- [EUR-Lex: PDF](https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX:32024R2847)
- [European Commission: CRA reporting obligations](https://digital-strategy.ec.europa.eu/en/policies/cra-reporting)
- [ENISA: Single Reporting Platform launched](https://www.enisa.europa.eu/news/the-cra-single-reporting-platform-is-launched)
- [ENISA: SME maturity assessment model (July 2026)](https://www.enisa.europa.eu/sites/default/files/2026-07/SME%20maturity%20assessment%20model_final.pdf)
- [ENISA: Where do SMEs stand](https://www.enisa.europa.eu/news/where-do-smes-stand-in-preparing-for-the-cyber-resilience-act)
- [Commission: CRA impact assessment](https://digital-strategy.ec.europa.eu/en/library/cyber-resilience-act-impact-assessment)
- [BSI: Cyber Resilience Act](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Cyber_Resilience_Act/cyber_resilience_act.html)
- [IHK Schwaben: CRA duties](https://www.ihk.de/schwaben/produktmarken/digitalisierung/it-sicherheit/cyber-resilience-act-pflichten-hersteller-6951410)
- [business.gov.nl: CRA](https://business.gov.nl/amendments/mandatory-cybersecurity-requirements-for-products-cra/)

### Cyber Resilience Act (secondary and vendor)
- Reporting and timing: [Crowell: reporting live](https://www.crowell.com/en/insights/client-alerts/its-live-the-cyber-resilience-act-reporting-is-mandatory-as-of-today-11-september-2026) · [Hogan Lovells](https://www.hlc.com/en/publications/eu-cyber-resilience-act-vulnerability-and-incident-reporting-obligations-now-apply) · [Brightdefense](https://www.brightdefense.com/news/eu-cyber-resilience-act-2026-reporting-deadline/) · [Global Law Experts](https://globallawexperts.com/cyber-resilience-act-reporting-obligations-from/)
- ENISA SRP: [CSA research note](https://labs.cloudsecurityalliance.org/research/csa-research-note-enisa-cra-reporting-platform-20260918-csa/) · [cyberresilienceact.eu SRP update](https://www.cyberresilienceact.eu/es/news/enisa-srp-guidance-update-3-august-2026.html) · [Help Net Security](https://helpnetsecurity.com/2026/09/14/enisa-cra-single-reporting-platform)
- Scope and penalties: [Greenberg Traurig](https://www.gtlaw.com/en/insights/2026/9/eu-cyber-resilience-act-cra-and-software-new-cybersecurity-obligations-and-ce-marking) · [Baker McKenzie](https://connectontech.bakermckenzie.com/new-eu-regulation-requires-cybersecurity-for-software-and-smart-devices/) · [The Lawyer](https://www.thelawyer.com/briefing/selling-products-with-digital-elements-in-the-eu/) · [shattered.io](https://shattered.io/at/cyber-resilience-act-2026/) · [William Fry](https://www.williamfry.com/knowledge/cyber-resilience-act-what-manufacturers-need-to-know/)
- SBOM guidance: [sbom-management.de](https://sbom-management.de/checkliste) · [ING-ISM](https://www.ing-ism.de/magazin/sbom-cyber-resilience-act-compliance/) · [B2B Cyber Security (OCCTET)](https://b2b-cyber-security.de/cyber-resilience-act-cra-open-source-toolkit-fuer-kmu-meldeplichten/) · [Sage DE](https://www.sage.com/de-de/blog/cyber-resilience-act-mittelstand/)
- Vendors: [sbomify pricing](https://sbomify.com/pricing/) · [sbomify FAQ](https://sbomify.com/faq/) · [sbomify on SourceForge](https://sourceforge.net/software/product/sbomify/) · [Interlynk on AWS](https://aws.amazon.com/marketplace/pp/prodview-n6mc7symiq2rm) · [Interlynk free tier](https://www.interlynk.io/resources/interlynk-launches-free-tier-of-sbom-automation-platform) · [SBOM Central](https://sbomcentral.com/pricing/) · [cyberresilienceact.eu analyser](https://www.cyberresilienceact.eu/analysis.html) · [Themio](https://www.themio.ai/en/blog/cyber-resilience-act-software-sme-2026) · [Certivo](https://www.certivo.com/frameworks/eu-cyber-resilience-act) · [distr.sh](https://distr.sh/cyber-resilience-act/) · [Cycode](https://cycode.com/blog/cyber-resilience-act/) · [Mend](https://www.mend.io/blog/eu-cyber-resilience-act-compliance-guide/) · [Cloudsmith](https://cloudsmith.com/blog/how-to-comply-with-eu-cyber-resilience) · [FOSSA](https://fossa.com/blog/sbom-requirements-cra-cyber-resilience-act/)
- Importers and distributors: [The Art of Service](https://compliance.theartofservice.com/controls/eu-cyber-resilience-act/cra-art-19-20) · [Prighter](https://prighter.com/resources/laws/cyber-resilience-act/quick-access) · [Prighter Art. 20](https://prighter.com/resources/laws/cyber-resilience-act/articles/article-20) · [AKD](https://www.akd.eu/insights/the-cyber-resilience-act-cybersecurity-obligations-for-importers-and-distributors) · [Springlex Art. 19](https://www.springlex.eu/en/packages/cra/cra-regulation/article-19/) · [Springlex Art. 20](https://www.springlex.eu/en/packages/cra/cra-regulation/article-20/) · [Presencis](https://cdn.presencis.com/regulations/cra/article-20/) · [xictron EN](https://www.xictron.com/en/blog/cyber-resilience-act-online-shops-obligations-2026/) · [xictron DE](https://www.xictron.com/de/blog/cyber-resilience-act-online-shops-pflichten-2026/) · [ecocomply](https://ecocomply.ai/blog/cyber-resilience-act-reporting-2026)
- Pool size: [Statista: DE C26 enterprises](https://statista.com/statistics/383747/enterprises-manufacturing-computer-electronic-optical-products-germany) · [Statista: GR C26 enterprises](https://www.statista.com/statistics/383752/enterprises-manufacturing-computer-electronic-optical-products-greece)

### Australian smart-device rules
- [legislation.gov.au F2025L00276](https://legislation.gov.au/F2025L00276/asmade/2025-03-04/text/original/epub/OEBPS/document_1/document_1.html)
- [Home Affairs statement-of-compliance template](https://www.homeaffairs.gov.au/cyber-security-subsite/files/soc-template-security-standards-for-smart-devices.pdf)
- [Teltonika wiki](https://wiki.teltonika-networks.com/view/AU_Cyber_Security_Rules_2025_Statement_of_Compliance)
- [Netgear statement-of-compliance example](https://www.downloads.netgear.com/files/AUS_DoC/212-10040-01_MR6110_DoC_AUS_202602251205.pdf)

### Batteries Regulation passport
- [Scantrust](https://www.scantrust.com/eu-battery-regulation-eu-battery-passport-requirements/)
- [Battery-Tech Network](https://battery-tech.net/the-eu-battery-passport-belongs-to-whoever-finishes-the-battery-four-months-before-it-becomes-mandatory/)
- [Circuland](https://circuland.co.uk/en/resources/battery-passport-timeline)
- [dpp-tool](https://dpp-tool.com/en/guide/battery-passport/)
- [Tracepas (ClouterX)](https://www.clouterx.com/en/regulations/battery-passport)
- [DPP Intel](https://dppintel.com/battery-passport/)
- [Automotive IQ](https://www.automotive-iq.com/electrics-electronics/articles/eu-battery-passport-explained-requirements-timeline-and-compliance-steps-to-2027)
- [AIAG blog](https://blog.aiag.org/battery-passport-updates-a-session-recap-from-aiags-responsible-materials-conference)

### Awaab's Law and social-housing sector size
- Official: [legislation.gov.uk SI](https://www.legislation.gov.uk/ukdsi/2025/9780348273083) · [GOV.UK Phase 2 guidance](https://www.gov.uk/government/publications/awaabs-law-phase-2-guidance-for-social-housing-landlords/awaabs-law-phase-2-guidance-for-social-landlords) · [GOV.UK collection](https://www.gov.uk/government/collections/awaabs-law-in-the-social-rented-sector) · [Regulations as they apply from 30 Nov 2026](https://assets.publishing.service.gov.uk/media/6a54d0862467584757371e07/Awaab_s_Law_Regulations_as_they_apply_from_30_November_2026.pdf) · [Somerset Council](https://www.somerset.gov.uk/housing-support/council-and-social-housing/awaabs-law-guidance/)
- Secondary: [Shelter](https://england.shelter.org.uk/professional_resources/news_and_updates/how_awaabs_law_changes_the_rules_on_hazards_in_social_housing) · [CIH](https://www.cih.org/news/second-phase-of-awaabs-law-laid-before-parliament/) · [Local Government Lawyer](https://www.localgovernmentlawyer.co.uk/housing-law/397-housing-news/101059-government-sets-date-for-rollout-of-second-phase-of-awaabs-law)
- Vendors: [AwaabSafe](https://www.awaabsafe.co.uk/) · [HazardClock](https://hazardclock.co.uk/blog/awaabs-law-compliance-software-guide/) · [CHICS](https://chics.co.uk/awaabs-law) · [HousingSurvey Pro](https://housingsurvey.pro/) · [Weightmans](https://www.weightmans.com/products/awaab-s-law-compliance-tool/) · [Netcall](https://www.netcall.com/complying-with-awaabs-law-what-good-looks-like/) · [Neo Technology](https://neotechnologysolutions.com/propsys360/case-management-dynamics-365/awaabs-law-practical-compliance-for-damp-mould/) · [REBIM](https://rebim.io/awaabs-law-social-housing-compliance/) · [OneAdvanced](https://www.oneadvanced.com/resources/housing-maintenance-and-repairs-management-software/) · [Rioo](https://riooapp.com/blog/awaabs-law-phase-2-what-changes-on-30-november-2026)
- Sector size: [RSH statistics briefing 2020-21](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1027024/RP_statistic_2020-21_briefing_note_v1.0__FINAL_.pdf) · [Cambridgeshire Insight](https://cambridgeshireinsight.org.uk/housing/local-housing-knowledge/housing-providers) · [Housing Today](https://housingtoday.co.uk/news/regulator-of-social-housing-publishes-guidance-on-tenant-satisfaction-measures/5126791.article)

### Martyn's Law
- Guidance and timing: [ProtectUK FAQ](https://www.protectuk.police.uk/martyns-law/martyns-law-frequently-asked-questions) · [Foot Anstey](https://www.footanstey.com/our-insights/articles-news/martyns-law-an-update-following-final-statutory-guidance/) · [Burges Salmon](https://www.burges-salmon.com/articles/102mqoj/martyns-law-counting-down-to-live-implementation) · [Restaurant Online](https://www.restaurantonline.co.uk/Article/2026/08/12/is-your-business-ready-for-martyns-law/)
- Vendors: [SIM on G-Cloud](https://www.applytosupply.digitalmarketplace.service.gov.uk/g-cloud/services/342763487779972) · [Halo free offer (2023)](https://www.theticketingbusiness.com/2023/06/12/halo-solutions-to-offer-safety-platform-for-free-to-support-martyns-law/) · [PolicyPros](https://www.policypros.co.uk/martyns-law-enhanced-tier-compliance-document/) · [PARiM](https://parim.co/blog/ready-for-martyns-law)

### Digital Waste Tracking
- Official and news: [gov.wales](https://www.gov.wales/mandatory-digital-waste-tracking-system) · [Circular Online](https://www.circularonline.co.uk/news/digital-waste-tracking-gets-official-start-date-as-uk-gears-up-for-sector-wide-rollout/) · [Karmactive](https://www.karmactive.com/uk-digital-waste-tracking-rules-start-october-2026/)
- Vendors: [Access Group](https://www.theaccessgroup.com/en-gb/waste-management/mandatory-digital-waste-tracking/) · [FieldMotion](https://fieldmotion.com/blog/digital-waste-tracking-module/) · [Avery Weigh-Tronix](https://www.averyweigh-tronix.com/en-gb/weighing_guide/digital-waste-tracking-2026-what-the-new-defra-legislation-means-for-waste-operators/) · [Weightron](https://www.weightron.com/news/digital-waste-tracking-phase-1-october-26-phase-2-2027-update/) · [Fissara](https://www.fissara.com/mandatory-digital-waste-tracking/) · [Wastebolt](https://wastebolt.app/waste-blog/digital-waste-tracking-waste-receivers-2026) · [Brik.ly](https://www.brik.ly/blog/digital-waste-tracking-october-2026-cafes/) · [Waste Logics](https://www.softwareadvice.co.uk/software/267658/waste-logics)

### FSMA 204
- Official: [FDA final rule page](https://www.fda.gov/food/food-safety-modernization-act-fsma/fsma-final-rule-requirements-additional-traceability-records-certain-foods) · [Federal Register: compliance date extension](https://www.federalregister.gov/documents/2025/08/07/2025-14967/requirements-for-additional-traceability-records-for-certain-foods-compliance-date-extension) · [FDA Q&A](https://www.fda.gov/media/191182/download) · [FDA public meeting, June 2026](https://www.fda.gov/food/workshops-meetings-webinars-food-and-dietary-supplements/fda-public-meeting-challenges-and-solutions-lot-level-food-traceability-06152026) · [FDA discussion paper](https://fda.gov/media/192696/download?attachment=)
- Vendors: [FoodReady](https://foodready.ai/blog/fsma-204/) · [Four Foxes](https://fourfoxes.io/blog/fsma-204-compliance-date-extension/) · [Dill](https://mydill.com/compliance-hub/fsma-204-food-traceability-rule) · [PolicyCanary](https://policycanary.io/regulations/fsma-204) · [Xenia](https://www.xenia.team/food-safety-ops/fsma-204-food-traceability-rule) · [TrueCommerce](https://www.truecommerce.com/blog/fsma-food-traceability-rule/) · [ifm](https://www.ifm.com/us/en/us/industries/food-and-beverage/food-safety-modernization-act/fsma-rule-204-food-traceability-rule)

### Other kill-log sources
- NY LLC Transparency Act: [Seward & Kissel](https://www.sewkis.com/publications/domestic-llcs-escape-new-yorks-transparency-act/) · [Bonadio](https://www.bonadio.com/?p=5960) · [Venable](https://www.venable.com/insights/publications/2026/01/new-for-2026-the-new-york-llc-transparency)
- AUSTRAC Tranche 2: [AUSTRAC](https://austrac.gov.au/node/1158) · [AUSTRAC factsheet](https://www.austrac.gov.au/sites/default/files/2025-07/AMLCTF_obligations_factsheet_for_tranche_2_REs.pdf) · [Legl](https://legl.com/articles/austrac-opens-enrolment-for-tranche-2-professions-what-law-firms-need-to-know-before-1-july) · [Zyphe](https://www.zyphe.com/resources/blog/austrac-tranche-2-enrolment-guide) · [Persona](https://withpersona.com/blog/tranche-2-australia) · [EasyAML](https://easyaml.com/wp-content/uploads/2025/11/AML-Obligations-Brochure-1.pdf) · [CCP](https://ccp.com.au/news/tranche-2-aml-ctf-obligations-accountants/)
- EUDR: [Bird & Bird](https://www.twobirds.com/en/insights/2025/out-of-the-woods-the-eudr-postponed-and-simplified) · [Coolset](https://www.coolset.com/academy/eudr-delay-2025-explained) · [Council press release](https://www.consilium.europa.eu/en/press/press-releases/2025/11/19/deforestation-council-ready-to-start-talks-with-parliament-on-a-targeted-revision-of-the-regulation/) · [myDPP](https://mydpp.app/en/knowledge/eudr-delay-current-status-and-deadlines) · [GlobalELR](https://www.globalelr.com/2026/05/european-commission-releases-new-eu-deforestation-regulation-measures/)
- E-invoicing roundups (vendor): [OriginStamp](https://originstamp.com/en/blog/reader/eu-e-invoicing-mandates-timeline-2026-2030) · [SPS Commerce](https://www.spscommerce.com/community/articles/e-invoicing-mandates-in-europe-the-2026-business-guide) · [Fonoa](https://www.fonoa.com/blog/e-invoicing-and-digital-reporting-in-the-eu-upcoming-changes) · [Shared Services Link](https://sharedserviceslink.com/webinar/2027-eu-mandates-what-6-countries-require-and-when) · [e-invoice.app](https://www.e-invoice.app/blog/global-einvoice-mandates-2026)
- SES.HOSPEDAJES: [Partee](https://partee.es/seshospedajes/) · [Pulso](https://pulsorent.com/es/resources/ses-hospedajes-automatizar-el-registro-de-alquileres-de-coches-y-motos/) · [seshospedajes.es](https://seshospedajes.es/) · [ASCAV](https://ascav.es/ses-hospedajes-todo-lo-que-necesitas-saber-acerca-de-la-nueva-plataforma/) · [Software Autocaravanas](https://softwareautocaravanas.com/requisitos-legales-alquiler-autocaravanas)
