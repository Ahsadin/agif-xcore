# Lens 4: household pains with a third-party payer (B2B2C) as a source of non-AI solo apps

Research date: 2026-10-12. Scope: everyday household, family and individual pains that stay unsolved because the person who suffers can't or won't pay, paired with a third party that has a direct financial reason to pay. The RULEBOOK and METHOD (Q1–Q10, H1–H8, C1–C10, BASELINE) were applied as given.

**How numbers were verified.** In this session the fetch tool could not resolve most German and some other domains (DNS errors), and the sandbox proxy blocked direct HTTP. A number marked **VERIFIED** was confirmed from a search-engine extract that attributes it to the cited URL. The page itself was usually not opened, so treat these as "verified by extract". Evidence older than 2024 is flagged **[OLD]**. Vendor statements are labelled **(vendor claim)**.

**Bottom line (provisional).**
- 20 raw candidates were narrowed to 3 finalists. All three pass H1–H8.
- Only **F1** clearly beats my provisional BASELINE score: **69.0 vs 57.5**. F1 is a case manager for care-home financing paperwork, launched in NRW, Germany, and paid for by the care home.
- **F2** (an SBV case tool paid for by the employer) scores 58.0, which is a statistical tie with the baseline.
- **F3** (a tenant benefit-deadline assistant paid for by the landlord) scores 56.5, below the baseline.
- Said plainly: **two of the three finalists would not beat the baseline.** They are listed because they were the next-best candidates that survived the hard rules.

---

## (1) KILL LOG

One line per raw candidate. Each starts from a person's pain (Q1), then the app, then the payer.

| # | Raw candidate (pain → app → payer) | Killed by | Why (evidence) |
|---|---|---|---|
| 1 | Family of a care-home resident whose savings ran out must file Hilfe zur Pflege, Pflegewohngeld and Wohngeld while the home pre-finances the costs → case manager plus family document portal → care home pays | **FINALIST F1** | Passes H1–H8. See card F1. |
| 2 | Employee with a disability or chronic illness is stuck in 3–9-month disability-degree (GdB) or equal-status procedures, while the volunteer SBV juggles cases → SBV case tool plus employee self-service → employer pays (it legally bears the SBV's costs) | **FINALIST F2** | Passes H1–H8. See card F2. |
| 3 | Low-income tenant loses Jobcenter coverage of a ~€900 utility back-payment by missing the month it falls due → QR-linked deadline assistant → landlord pays | **FINALIST F3** | Passes H1–H8, but has the highest H4 exposure. See card F3. |
| 4 | Same disabled-employee pain, but the employer buys a "disclose your disability, cut our levy" navigator paid by success fee | Q10 (+ H6 risk) | The employer's return comes only if employees disclose a health status. That return is the Ausgleichsabgabe, the levy on unfilled disability-quota places, at €155–815 per place per month ([IHK Chemnitz](https://www.ihk.de/chemnitz/standortpolitik/fachkraefte/beratungsangebote/ausgleichsabgabe-2024-6024450)). Paying a vendor on that outcome pressures a vulnerable group. A search for employer programmes that encourage disclosure found none ([search result set](https://www.forum-verlag.com/fachwissen/personalmanagement/schwerbehinderung-arbeitsplatz)). The idea was salvaged as F2 (controlled by the SBV, flat price). |
| 5 | Foreign nurse stuck in recognition or visa limbo. Up to four authorities are involved ([der-betrieb](https://der-betrieb.de/meldungen/fachkraeftemangel-stolperfallen-mit-medizinischen-fachkraeften-aus-dem-ausland/)), and the 24-month §16d window is hard to meet ([KDA position paper](https://kda.de/wp-content/uploads/2023/01/Positionen-zur-erleichterten-Fachkraefte-Einwanderung.pdf) [OLD 2023]) → case tracker → recruitment agency or employer pays | H8 | [Ankaadia](https://www.ankaadia.com/en/functions/international-recruitment) covers recognition and visa and claims 800+ organisations (vendor claim). WorkAbroad and [Recruitroo](https://www.recruitroo.com/how-it-works) sell the same thing ([OMR list](https://omr.com/de/reviews/product/ankaadia/alternatives)). The certified-agency pool is small: 50 holders of the Gütesiegel (fair-recruitment seal) in Sept 2022 [OLD] ([Bundestag hib](https://www.bundestag.de/presse/hib/kurzmeldungen-916382)). |
| 6 | Migrant employee's residence permit expires while the Ausländerbehörde (immigration office) has no appointments → expiry and renewal tracker → employer pays | Q4 (root cause beyond software) / H4 | The binding constraint is the authority's appointment capacity, which an app can't fix. Grabbing appointments would need scraping (H4). That expiry reminders are a commodity HR-suite feature is **not verified** this session. |
| 7 | Sponsored worker's family faces visa curtailment if the UK employer loses its sponsor licence → compliance tracker → sponsor pays | H8 | Cheap tools already exist: [SMS System](https://www.capterra.com/p/10048254/SMS-SYSTEM/) lists £39.99 (billing period unclear) and [CloudNet UKVI](https://www.capterra.co.uk/software/1108137/UKVI-Sponsor-Licence-Compliance-Software) costs £998 one-off. A [law-firm managed service](https://www.ukimmigration.law/sponsor-compliance-service/) starts at £275/month. UK immigration-advice regulation adds an H3 grey zone (not verified). |
| 8 | UK parent forgets the 3-monthly reconfirmation of the 30-hours childcare code and loses the funded hours → reminder service → nursery pays | Q4 / C3 (largely solved) | HMRC already sends two reminders, 4 and 2 weeks before the deadline, and a grace period protects the place ([Bolton](https://www.bolton.gov.uk/downloads/file/3309/30-hours-funding-things-to-remember-parents-), [Coventry](https://www.coventry.gov.uk/downloads/file/31305/2-reconfirmation-of-funding-codes)) [OLD 2017–2023]. |
| 9 | Eligible English family never registers for free school meals, so the school loses Pupil Premium funding → registration tool → school pays | H4 | Councils run opt-out auto-award using DWP data ([Gloucestershire, June 2026](https://www.gloucestershire.gov.uk/media/y25fdrvs/schoolsnet-free-school-meals-and-pupil-premium-opt-out-auto-award-june-2026.docx)). A Devon case added 1,064 pupils and £1.4m of Pupil Premium ([APSE](https://www.apse.org.uk/sites/apse/assets/File/Ashlee%20and%20Cressida.pdf)). Auto-enrolment is council-led ([Wokingham FOI](https://www.wokingham.gov.uk/foi/auto-enrolment-free-school-meals)), and a private vendor can't get that data. |
| 10 | Bereaved German family must cancel dozens of contracts → notification service → funeral home pays | H8 | Columba already works with more than 1,500 funeral homes at flat fees ([t-online](https://www.t-online.de/digital/aktuelles/id_84818402/neue-helfer-regeln-den-digitalen-nachlass.html), [WinFuture](https://winfuture.de/news,76351.html)) [OLD 2013–2019]. |
| 11 | US adult loses Medicaid at the new 6-monthly renewals and work requirements → keep-coverage navigator → health system or MCO pays | H8 + C4 | Fortuna Health raised an $18m Series A in July 2025, led by a16z, to do this with health systems and MCOs ([HC Innovation Group](https://www.hcinnovationgroup.com/policy-value-based-care/medicare-medicaid/news/55304442/fortuna-gets-funding-to-expand-medicaid-enrollment-solution)). HIPAA rules and enterprise sales don't suit a solo founder with no network. |
| 12 | US nursing-home family stuck in "Medicaid pending" → document portal → nursing home pays | H8 | [SNF Metrics AR Tracker](https://snfmetrics.com/ar-tracker-dashboard/), [Aidace](https://www.capterra.co.uk/software/1238013/Aidace), [AR Proactive](https://www.arproactive.com/nursing-homes) and [ExaCare](https://www.exacare.com/article/medicaid-pending-nursing-homes) already target this (vendor pages). This is why F1 launches in Germany. |
| 13 | Family caregiver leaves the €131/month Entlastungsbetrag (relief allowance) unused; unused amounts expire on 30 June of the next year ([AOK](https://www.aok.de/pk/pflegeleistungen/entlastungsbetrag/)) → budget ledger and billing kit → small household-help provider or neighbour-helper pays | Q4 / Q5 | The binding constraint is provider supply, not paperwork. Neighbour-helpers can be paid only in some states, and sources conflict ([test.de](https://www.test.de/Entlastungsbetrag-pflege-6242425-0/) vs a [Niedersachsen form](https://soziales.niedersachsen.de/download/184112)). Micro-helpers can pay very little. Billing centres already exist ([DMRZ care tariffs from €49.99/month](https://www.dmrz.de/fileadmin/Presse/DMRZ_PM_Individuelle-Service-und-Tarifwahl-2019.pdf) [OLD 2019]). The "~4 in 10 use it" figure comes from an unnamed survey ([gegen-hartz](https://www.gegen-hartz.de/news/pflegegeld-rentnerin-mit-pflegegrad-3-verliert-1572-euro-obwohl-das-pflegegeld-weiterluft)). |
| 14 | Household must stay home for chimney-sweep or maintenance visits announced by notes in the stairwell → self-scheduling → sweep pays | Q1 | Pain is low in intensity and frequency: the Feuerstättenschau (fireplace inspection) happens twice in 7 years ([haustechnikdialog](https://www.haustechnikdialog.de/SHKwissen/1492/Feuerstaettenschau)). The cost of failed visits is not quantified. Trades already bolt on generic booking tools such as Terminland ([Handwerksblatt](https://www.handwerksblatt.de/betriebsfuehrung/bei-schoellgen-haustechnik-koennen-kunden-ihre-wartungstermine-entspannt-online-buchen)). |
| 15 | Eligible tenants don't claim or renew Wohngeld (housing benefit) → take-up service → housing company pays | Q5 / C2 | No reliable non-take-up rate exists: the [Bremen Senate](https://www.bremische-buergerschaft.de/dokumente/wp21/land/drucksache/D21L1816.pdf) says no concrete data basis exists, and estimating it needs microsimulation ([IWU](https://www.iwu.de/fileadmin/publikationen/vortrag/2021-06-14_Wohngeld-Fachgespr%C3%A4ch_Cischinsky_Slides_Zur-Inanspruchnahme-des-Wohngelds.pdf) [OLD 2021]). So the ROI can't be shown. The hard-deadline element was folded into F3. |
| 16 | Child with a disability starts the school year without an approved school aide → approval tracker → aide provider pays | Q3 / Q5 | Late approvals ([SH ombudsman](https://eno.ombudsman.europa.eu/home/news/archives-2016/maincontent/schulbegleitung-auch-das-sozialg.html) [OLD 2016]) and annual re-applications ([Langerwehe concept](https://www.ge-langerwehe.de/wp-content/uploads/2021/12/Konzept-zur-Schulbegleitung-an-der-ES-Langerwehe.pdf)) are documented. Provider pre-financing and budgets are not. Evidence is too thin. |
| 17 | People moving house forget address changes and utility set-up → concierge → utilities or telcos pay commissions | H5 | Revenue would come from selling the household's switching intent. That is lead-gen, close to data-selling (structural reason, no source needed). |
| 18 | Shift-working nurse can't cover childcare for night shifts → carer matching → hospital pays | H7 | Needs liquidity on both sides (carers and parents) before it delivers any value (structural). |
| 19 | UK self-funder's savings fall below the council threshold and the care home faces a funding gap → depletion forecaster → care home pays | Q10 / H3 risk | Same mechanism as F1 in a market where I gathered no evidence. Care-fee planning sits next to regulated financial advice (not verified). |
| 20 | Low-income German family misses renewals of child supplement, Wohngeld or education-and-participation benefits → renewal calendar → family pays | H5 / C2 | The sufferer can't or won't pay, and no third party loses money directly. Renewal-period details were not verified this session. |

### 1.1 Key-question answers

#### Which household pains cost the most, recur, and are still handled by paper, phone or memory?

**Takeaway.** The biggest are moments where a public office decides slowly while the household holds the documents. Care-home financing has the most money at stake; disability-status procedures and benefit deadlines tied to utility statements follow. All of them still run on paper, post and phone.

**Cited findings**
- The average resident co-payment (Eigenanteil) in a care home's first year was **€3,108/month** on 1 July 2025, up 8.3% ([vdek](https://www.vdek.com/presse/pressemitteilungen/2025/pflegeheim-monatliche-eigenbeteiligung-steigt-stationaere-pflege.html)). It was €3,245 on 1 January 2026 ([cash-online](https://www.cash-online.de/a/pflegeheimkosten-steigen-weiter-eigenanteil-erreicht-3-245-euro-im-ersten-jahr-710392/)) and €3,427 in NRW ([vdek NRW](https://www.vdek.com/LVen/NRW/Presse/Pressemitteilungen/2025/stationaere-pflege-nrw.html)).
- In May 2025 ARD's Report Mainz wrote to 478 social-welfare offices (Sozialämter); 113 answered on processing times. About **27% need 6–12 months** for Hilfe zur Pflege (care assistance) and about **5% need more than 12 months**. Homes are paid only after approval, so residents risk losing their place ([Ärzteblatt](https://www.aerzteblatt.de/news/antragsstau-zur-pflege-in-sozialamtern-affb0712-f301-4506-b133-ea19da7c2365); [bpa newsletter](https://www.bpa.de/fileadmin/News___Fachinformationen/bpa.newsletter/mailing_13-05-2025.pdf)).
- In Berlin, Hilfe zur Pflege for people living in a care home can't be applied for online. It must go on paper by post ([service.berlin.de](https://service.berlin.de/dienstleistung/324474/pdf/)).
- Net spending on Hilfe zur Pflege was **€5.3bn in 2024 (+17.7%)** ([Destatis via presseportal](https://www.presseportal.de/pm/32102/6098431); [Ärzteblatt](https://www.aerzteblatt.de/news/sozialhilfetrager-geben-mehr-geld-aus-85df9e1c-bc46-4920-82d3-20b4222c0f99)).
- Decisions on a disability degree (GdB) take 5–6 months on average in Berlin ([service.berlin.de](https://service.berlin.de/dienstleistung/326173/pdf/)). They took more than 9 months on average in Sachsen-Anhalt over 2020–2025 (MDR via [gegen-hartz](https://www.gegen-hartz.de/news/schwerbehinderung-der-gang-bis-zum-bescheid-ist-wahnsinn)) and up to 9 months in Landkreis Ludwigsburg ([Landtag BW, 2025](https://www.landtag-bw.de/resource/blob/583480/33e870282b2ece8283f9bb7144051c59/17_9140_D.pdf)).
- The average utility back-payment is **€907** (WiWo via [inFranken](https://www.infranken.de/ratgeber/karriere-geld/3000-euro-nebenkosten-warum-wohnen-in-deutschland-immer-teurer-wird-art-6350661)). For a tenant on Grundsicherung (basic income support), the back-payment must reach the Jobcenter in the month it falls due, or the claim is lost ([gegen-hartz](https://www.gegen-hartz.de/buergergeld-nachzahlung-fuer-nebenkosten-und-heizung-was-zahlt-das-jobcenter)). This is an advocacy source.

**Inferences**
- The pains with the most money per episode cluster where household paperwork gates a third party's revenue: care-home fees, quota levies and rent.
- Households don't pay to fix them because each episode is rare for them and money is already short at that moment.

**Gaps**
- I did not retrieve the national count of Hilfe zur Pflege recipients from Destatis. The only figure is a secondary one of ~354,000 people in facilities in 2024, with unclear provenance ([medi-karriere](https://www.medi-karriere.de/magazin/pflegeheime-bewohner-auf-sozialhilfe-angewiesen/)).
- I found no time-use data on the hours families spend on these applications.

#### Who else loses money when the household suffers, and how much?

**Takeaway.** Care homes are the clearest losers: one in five carries six-figure receivables. Employers pay a quota levy, English schools lose Pupil Premium, and landlords absorb uncovered back-payments, though that last loss is not quantified.

**Cited findings**
- A PwC/Strategy& survey of more than 100 care homes, published 12 June 2026, found:
  - **55%** name the Sozialamt as the payer with the largest outstanding amounts, 25% name residents or relatives, and 20% name the care insurers.
  - **One in five** homes has **≥€100,000** outstanding.
  - Homes spend **8.3 staff hours a week** on open items.
  - **46%** have no standardised claims and reminder process.
  - Source: [PwC press release](https://www.pwc.de/de/pressemitteilungen/2026/fehlende-liquiditaet-in-pflegeheimen-gefaehrdet-die-versorgung.html); [PwC topic page](https://www.pwc.de/de/gesundheitswesen-und-pharma/liquiditaet-in-pflegeeinrichtungen.html).
- **60%** of the homes that name the Sozialamt as their largest debtor blame **missing documents and evidence** ([Apotheken Umschau](https://www.apotheken-umschau.de/gesundheitspolitik/pflegeheime-warten-monatelang-auf-hilfe-zur-pflege-von-sozialaemtern-1539809.html)).
- The quota levy (Ausgleichsabgabe) since 2025 is **€155 / €275 / €405 / €815** per unfilled place per month. It was first due under these tiers on 31 March 2026 ([IHK Chemnitz](https://www.ihk.de/chemnitz/standortpolitik/fachkraefte/beratungsangebote/ausgleichsabgabe-2024-6024450); [LAGeSo Berlin](https://www.berlin.de/lageso/behinderung/inklusionsamt-arbeit-und-behinderung/ausgleichsabgabe/); [IHK Ostwestfalen](https://www.ihk.de/ostwestfalen/newsportal/ausgleichsabgabe-2026-6964718)).
- In 2021, 39% of obligated employers met the quota and **25.9% employed no severely disabled person** [OLD] ([Ärzteblatt](https://www.aerzteblatt.de/news/arbeitsmarkt-quote-fuer-menschen-mit-schwerbehinderung-unzureichend-erfuellt-e7959c48-814b-4bf8-a368-b3471d5064ba)).
- NRW's Pflegewohngeld (a state subsidy for a care home's investment costs) is **paid directly to the home** and approved for 12 months at a time ([Kreis Euskirchen](https://kreis-euskirchen.de/fileadmin/user_upload/1946-Z.I.P._-_Merkblatt_Heimplatzfinanzierung_neu.pdf); [Verbraucherzentrale NRW](https://www.verbraucherzentrale.nrw/wissen/gesundheit-pflege/pflege-im-heim/pflegewohngeld-in-nrw-finanzielle-hilfe-in-stationaeren-einrichtungen-86793); [recht.nrw.de](https://recht.nrw.de/system/files/BH/5196-21888.htm)).
- A Devon case added 1,064 pupils to free school meals and brought £1.4m of Pupil Premium ([APSE](https://www.apse.org.uk/sites/apse/assets/File/Ashlee%20and%20Cressida.pdf)).
- The Triple Win programme's placement fee was about €8,500 per nurse in 2023 [OLD] ([Arbeitsagentur slides](https://www.staedteregion-aachen.de/fileadmin/user_upload/A_53/Pflegeoffensive/Workshop4_Praesentation_Arbeitsagentur.pdf)).

**Inferences**
- A care home's loss per delayed case is roughly one month's co-payment (€3,100–3,400) for each month the decision is late, plus staff time.
- That is the most direct and measurable third-party money reason found in this lens.

**Gaps**
- How much landlords lose on back-payments that the Jobcenter doesn't cover.
- How many Hilfe zur Pflege cases a typical home has open.

#### Has anyone built the B2B2C version, with what traction and pricing? Is there evidence of direct consumer willingness to pay?

**Takeaway.** In most of the obvious spots, yes:
- German care-home financing: Myosotis "formfix", sold to Sozialämter and described as using AI.
- US Medicaid: Fortuna Health.
- Foreign-nurse recruitment: Ankaadia.
- German bereavement: Columba.
- English free school meals: councils themselves.
- UK sponsor compliance: several cheap tools.

Three openings remain. None is verified as a full gap:
- the care-home-side workflow for receivables and documents in Germany (F1);
- tools for SBVs (F2);
- deadline help triggered by the landlord (F3).

**Cited findings**
- Myosotis raised a Series A in February 2024. TVM led with €8m. The total was €10.5m per [startbase](https://www.startbase.de/news/105-millionen-euro-fuer-myosotis/), or about €12m per the [investor](https://tvm-capital.com/?p=6430).
- Myosotis says it has 400+ customers in DACH and England (vendor claim). It describes formfix as an aid that guides applicants for Hilfe zur Pflege and saves Sozialämter time ([job posting](https://join.com/companies/myo/16523373-mitarbeiter-in-sozialhilfe-hilfe-zur-pflege-m-w-d)).
- Tagesspiegel Background (paywalled, seen via extract only) reports an "AI agent" helping applicants in Köln, Kreis Heinsberg and two Berlin districts ([Tagesspiegel](https://background.tagesspiegel.de/smart-city-und-stadtentwicklung/briefing/wie-der-agentic-ai-hub-zum-erfolg-werden-kann)). A second search could not confirm the Köln deployment.
- Factoring firms such as SozialFactoring sell into the care-home liquidity problem. Factoring firms typically advance 80–90% of an invoice ([ecovis](https://ecovis-kso.com/blog/factoring-in-der-pflege/); [SozialFactoring 2026 article](https://www.sozialfactoring.de/app/uploads/2026/07/PflegeManagement_Warum-Forderungsmanagement-zur-Fuehrungsaufgabe-wird.pdf); [Agicap](https://agicap.com/de/artikel/factoring/)).
- Direct consumer willingness to pay: **no evidence found for any of the three finalist pains.**

**Inferences**
- Homes already pay to fix the cash side of the problem (factoring) but not the paperwork side. That suggests a budget line exists for this pain.

**Gaps**
- Whether care-home ERPs (for example Medifox DAN or Connext Vivendi) handle Hilfe zur Pflege application packets. Not checked.
- Myosotis pricing.

#### Which pain–payer combination gives the clearest payer and a cheap, named channel?

**Takeaway.** Care homes in NRW. They have a quantified money reason, public directories, associations, and pilots can be priced below the level that needs formal purchasing approval.

Runner-ups:
- SBVs: reachable through public-sector SBV web pages and the 1 Oct – 30 Nov 2026 election wave.
- Housing companies: the payer is clear, but sales are slow.

**Cited findings**
- About 16,500 SGB XI care facilities were licensed in 2023 ([KBV](https://www.kbv.de/infothek/zahlen-und-fakten/gesundheitsdaten/pflegeheime-und-personal)).
- 16,505 nursing homes in 2023, of which 11,250 offer long-term care ([Curacon/Destatis](https://www.curacon.de/fileadmin/user_upload/Curacon/Downloads/Produktbeispiel_sAHBenchmark_Max.pdf)).
- SBV elections run from 1 October to 30 November 2026 ([DGB](https://www.dgb.de/fileadmin/download_center/Aufrufe/Aufruf_SBV-Wahl_2026.pdf); [NGG](https://www.ngg.net/fileadmin_new/7_Themen/SBV-Wahl-Grundlagen_vereinfachtes_Wahlverfahren.pdf)).
- Public-sector SBVs publish their contacts online, for example [Uni Bamberg](https://www.uni-bamberg.de/sbv/), [Uni Oldenburg](https://uol.de/schwerbehindertenvertretung/aufgaben), [Uni Bielefeld](https://uni-bielefeld.de/sbv) and [TU Dortmund](https://sbv.tu-dortmund.de/storages/sbv/w/Dateien/SBV_Faltblatt_Wickelfalz_DIN-A4_SC_Druckdaten_ZV.pdf).

**Gaps**
- Quality of the care-home directories as a contact source.
- Number of SBVs in Germany.
- Number of GdW (housing-company federation) members.

---

## (2) FINALIST IDEA CARDS

### F1 — "Heimkosten-Lotse": case manager for care-home financing paperwork (Hilfe zur Pflege, Pflegewohngeld, Wohngeld). Launch: NRW, Germany. The care home pays.

**Who suffers.** Care-home residents whose savings have run out, and their adult children or legal guardians (Betreuer). They must collect income and asset evidence and answer the Sozialamt's follow-up requests. Meanwhile invoices, and sometimes dunning letters, keep arriving.

**Who pays.** The care-home operator.

**The payer's money reason, quantified**
- 55% of homes name the Sozialamt as their largest debtor; 1 in 5 homes has at least €100k outstanding; homes spend 8.3 staff hours a week on open items; 46% have no standard dunning process ([PwC, 12 Jun 2026](https://www.pwc.de/de/pressemitteilungen/2026/fehlende-liquiditaet-in-pflegeheimen-gefaehrdet-die-versorgung.html)).
- 60% of the homes naming the Sozialamt blame missing documents ([Apotheken Umschau](https://www.apotheken-umschau.de/gesundheitspolitik/pflegeheime-warten-monatelang-auf-hilfe-zur-pflege-von-sozialaemtern-1539809.html)).
- Each month of delay means the home pre-finances about **€3,108–3,427** per resident ([vdek](https://www.vdek.com/presse/pressemitteilungen/2025/pflegeheim-monatliche-eigenbeteiligung-steigt-stationaere-pflege.html); [vdek NRW](https://www.vdek.com/LVen/NRW/Presse/Pressemitteilungen/2025/stationaere-pflege-nrw.html)).
- In NRW, Pflegewohngeld is paid **directly to the home** and starts from the application date. If the application is filed within 3 months of eligibility, payment is backdated to the day eligibility began. Approvals last 12 months, so a lapsed renewal is the home's lost revenue ([recht.nrw.de](https://recht.nrw.de/system/files/BH/5196-21888.htm); [Kreis Euskirchen](https://kreis-euskirchen.de/fileadmin/user_upload/1946-Z.I.P._-_Merkblatt_Heimplatzfinanzierung_neu.pdf)).

#### Q1 — Who suffers, when, how often, and at what cost?

When a parent's savings run out in a German care home, the family must assemble dozens of income and asset documents for the Sozialamt, plus an annual Pflegewohngeld application in NRW. All the while €3,100–3,400 a month keeps accruing. More than a quarter of the offices that answered ARD take 6–12 months or longer to decide, and aid generally starts only from the application date. So every missing paper costs the family stress, and costs the home cash it has pre-financed.

- **Frequency.** One intense episode per resident when the money runs out, then annual renewals and reviews.
- **Cost.** €3,108/month first-year co-payment nationally on 1 July 2025 ([vdek](https://www.vdek.com/presse/pressemitteilungen/2025/pflegeheim-monatliche-eigenbeteiligung-steigt-stationaere-pflege.html)).
- **Delay.** About 27% of answering offices take 6–12 months and about 5% take more than 12 months. Some Berlin-Pankow cases took 2–3 years ([Ärzteblatt](https://www.aerzteblatt.de/news/antragsstau-zur-pflege-in-sozialamtern-affb0712-f301-4506-b133-ea19da7c2365)).
- **Risk.** Residents risk losing their place because homes are paid only after approval ([Ärzteblatt](https://www.aerzteblatt.de/news/antragsstau-zur-pflege-in-sozialamtern-affb0712-f301-4506-b133-ea19da7c2365)). Hilfe zur Pflege is generally granted only from the application date ([gegen-hartz](https://www.gegen-hartz.de/news/pflegegeld-pflegeheim-kosten-drei-fehler-die-familien-jetzt-teuer-bezahlen)).
- **Family fear.** Many families fear having to pay for their parent (Elternunterhalt). In fact only children with more than €100k gross income must contribute, and the Sozialamt presumes income is below that line ([biallo](https://www.biallo.de/soziales/news/elternunterhalt-freibetrag-pflegeheim-kosten/); [Pflegestützpunkte Berlin](https://www.pflegestuetzpunkteberlin.de/wp-content/uploads/2025/04/DE-IB-34-Unterhaltspflicht-von-Kinder-gegebenueber-pflegebeduerftigen-Eltern.pdf)).
- **Paper only.** In Berlin, applications for people in a care home are paper-only ([service.berlin.de](https://service.berlin.de/dienstleistung/324474/pdf/)).
- **Scale.** €5.3bn of net Hilfe zur Pflege spending in 2024 ([Destatis via presseportal](https://www.presseportal.de/pm/32102/6098431)). About 354,000 recipients lived in facilities in 2024 (secondary source, unclear provenance: [medi-karriere](https://www.medi-karriere.de/magazin/pflegeheime-bewohner-auf-sozialhilfe-angewiesen/)). Bavaria alone had 41,670 recipients in 2024 ([Bayerischer Landtag](https://www.bayern.landtag.de/www/ElanTextAblage_WP19/Drucksachen/Basisdrucksachen/0000009500/0000009618_039.pdf)).

#### Q2 — What is the one thing the app does?

It gives each resident one shared case file. The file:
- tells the family exactly which documents to upload, using deterministic rules based on income, assets and guardianship;
- generates a date-securing informal application on day one;
- fills the Sozialamt, Pflegewohngeld and Wohngeld forms from the same data;
- tracks every Sozialamt follow-up request and renewal date;
- shows the home one board of open receivables per payer.

#### Q3 — Who already solves it?

Searched in German and English, globally and in Germany.

| Name | Country | Price | What it does | Gap vs F1 |
|---|---|---|---|---|
| Myosotis "formfix" | DE (Berlin) | Not public | Digital application aid for Hilfe zur Pflege, used on the Sozialamt side. Described as a "logic tree" ([Berliner Zeitung](https://www.berliner-zeitung.de/article/berliner-start-up-erleichtert-antraege-auf-sozialhilfe-leute-verstehen-die-komplizierten-fragestellungen-nicht-2338994), paywalled) and as an "AI agent" ([Tagesspiegel](https://background.tagesspiegel.de/smart-city-und-stadtentwicklung/briefing/wie-der-agentic-ai-hub-zum-erfolg-werden-kann), paywalled, extract only). | Sold to public offices, not homes. Uses AI. Not shown to manage home receivables, Pflegewohngeld or Wohngeld renewals, or family document chasing (assumption; the product page was not reachable). |
| Myosotis "myo" app | DE / UK | Not public | Care-home app for communicating with relatives. 400+ customers in DACH and England (vendor claim, [job posting](https://join.com/companies/myo/16523373-mitarbeiter-in-sozialhilfe-hilfe-zur-pflege-m-w-d)). Series A in Feb 2024 of €8–12m ([startbase](https://www.startbase.de/news/105-millionen-euro-fuer-myosotis/); [TVM](https://tvm-capital.com/?p=6430)). | Doesn't handle financing workflows, but gives a funded player a ready channel into homes. **This is the main copy threat.** |
| Care-home ERPs (for example Medifox DAN, Connext Vivendi) | DE | Not public | Resident billing to care insurers and self-payers. | **Not verified** whether they support Hilfe zur Pflege packets or family uploads. Research gap. |
| SozialFactoring GmbH and other factoring firms | DE | Fee-based; 80–90% advance typical ([Agicap](https://agicap.com/de/artikel/factoring/)) | Buy receivables to fix liquidity ([ecovis](https://ecovis-kso.com/blog/factoring-in-der-pflege/)). | Don't fix missing documents or months lost before the application. Cost fees. Unclear whether they buy Sozialamt claims from residential homes. |
| SNF Metrics AR Tracker, Aidace, AR Proactive, ExaCare | US | Not public | Tracking of "Medicaid pending" receivables for US nursing homes ([SNF Metrics](https://snfmetrics.com/ar-tracker-dashboard/); [Aidace](https://www.capterra.co.uk/software/1238013/Aidace), which claims a 44% cut in aged balances (vendor claim); [AR Proactive](https://www.arproactive.com/nursing-homes); [ExaCare](https://www.exacare.com/article/medicaid-pending-nursing-homes)). | Shows the B2B model works abroad. No German offering was found. |

#### Q4 — Why is it still unsolved? Root-cause class: **(c) primary, plus (b) and (e)**

- **(c)** The family suffers but won't pay for back-office software. The party that could fix it, the Sozialamt, is a slow public buyer. Its funded vendor (Myosotis) sells there, not to homes.
- **(b)** The field is fragmented. Report Mainz wrote to 478 Sozialämter ([Ärzteblatt](https://www.aerzteblatt.de/news/antragsstau-zur-pflege-in-sozialamtern-affb0712-f301-4506-b133-ea19da7c2365)), and Pflegewohngeld exists only in some states (NRW confirmed: [Verbraucherzentrale NRW](https://www.verbraucherzentrale.nrw/wissen/gesundheit-pflege/pflege-im-heim/pflegewohngeld-in-nrw-finanzielle-hilfe-in-stationaeren-einrichtungen-86793)).
- **(e)** It is an unglamorous back-office job.
- **Not (f).** Homes already pay for liquidity fixes such as factoring.
- **Not (g).** Everything is deterministic web software.

#### Q5 — Is it profitable?

| Item | Value | Status |
|---|---|---|
| Price per home (average) | €179/month. Tiers: €129 for ≤60 beds, €179 for 61–120, €249 for >120 | ASSUMPTION |
| Price benchmarks | DMRZ care billing from €49.99/month | VERIFIED [OLD 2019] ([DMRZ](https://www.dmrz.de/fileadmin/Presse/DMRZ_PM_Individuelle-Service-und-Tarifwahl-2019.pdf)) |
| | Care-cost calculator widget for home websites: €20/month per site | VERIFIED ([smart-rechner](https://www.smart-rechner.de/pflegekosten/rechner.php)) |
| Cost per customer | ~€18/month: encrypted hosting and storage €4, email/SMS to families €6, payment fees €2, support tooling €6 | ASSUMPTION |
| Gross margin | ~90% | ASSUMPTION (derived) |
| Fixed business costs | ~€1,800/month: data-protection and legal counsel spread over time, insurance, accounting, travel and marketing, tools | ASSUMPTION |
| Customers needed for €8k/month profit | **61 homes** = (8,000 + 1,800) / (179 − 18) | Derived from assumptions |
| Reachable pool | 16,505 nursing homes, of which 11,250 offer long-term care | VERIFIED ([Curacon/Destatis](https://www.curacon.de/fileadmin/user_upload/Curacon/Downloads/Produktbeispiel_sAHBenchmark_Max.pdf); [KBV](https://www.kbv.de/infothek/zahlen-und-fakten/gesundheitsdaten/pflegeheime-und-personal)) |
| Share of pool needed | ~0.5% of long-term-care homes | Derived |
| Value: staff time | 8.3 h/week on open items | VERIFIED ([PwC](https://www.pwc.de/de/pressemitteilungen/2026/fehlende-liquiditaet-in-pflegeheimen-gefaehrdet-die-versorgung.html)) |
| | Cutting this by 25% saves ~9 h/month, worth ~€315 at €35/h | ASSUMPTION |
| Value: cash per case | €3,108–3,427 pre-financed per resident for each month of delay | VERIFIED ([vdek](https://www.vdek.com/presse/pressemitteilungen/2025/pflegeheim-monatliche-eigenbeteiligung-steigt-stationaere-pflege.html)) |
| | ~10 new financing cases per 80-bed home per year, each 1 month faster → ~€31k of cash released earlier | ASSUMPTION |
| CAC | ~€500 (outbound founder time plus travel) | ASSUMPTION |
| Monthly churn | 1.5% | ASSUMPTION |
| LTV | ~€10,700 = €161 × 66.7 months | Derived |
| LTV/CAC | ~21; still ≥10 at 3% monthly churn | Derived |

#### Q6 — How to build it

**MVP scope**
1. A resident case file with a map of all payers: care-insurance grade, co-payment, Hilfe zur Pflege, NRW Pflegewohngeld, Wohngeld.
2. A rules-based document checklist. Rules cover pensions and widow's pensions, accounts, life insurance, prepaid funeral plans, property, power of attorney or guardianship, and the last home address, which decides the responsible Sozialamt.
3. A family portal: magic-link login, uploads, status, reminders.
4. A date-securing informal application letter with a proof-of-sending log.
5. Form filling for the most common NRW Sozialamt forms, the Pflegewohngeld forms, and the Wohngeld (rent subsidy) form for care-home residents.
6. A tracker for Sozialamt follow-up requests with deadlines.
7. A renewal engine for 12-month Pflegewohngeld approvals and Wohngeld periods.
8. A receivables board and dunning templates for the home's own claims.
9. A monthly PDF report.

**Out of scope:** OCR, AI, financing or factoring, legal opinions, and ERP integration (CSV import only).

**Stack:** Django or Rails with Postgres. AcroForm PDF filling (pdf-lib or pdftk). Postmark for email; a German SMS provider. Hosting in Germany (Hetzner or IONOS) with encrypted S3-compatible storage. SEPA billing through GoCardless or Stripe. All off-the-shelf.

**12-week build outline**
- **W1:** 10 discovery calls with NRW homes, run in parallel. Data model (resident, case, payer, document, request, deadline). Roles: home admin, relative, guardian.
- **W2:** Case wizard and checklist rules, version 1.
- **W3:** Family portal, email and SMS notifications.
- **W4:** Generator for the informal application and send log. Directory of Sozialämter, starting with NRW's Kreise and kreisfreie Städte (count not verified).
- **W5–6:** Form library: the 10 most-used NRW Hilfe zur Pflege forms, Pflegewohngeld, and Wohngeld for care-home residents.
- **W7:** Follow-up request tracker and "status enquiry" letter templates.
- **W8:** Receivables board, CSV import, dunning templates.
- **W9:** Renewal engine and calendar.
- **W10:** Security: encryption, 2FA, audit log, retention and deletion rules. Data-processing agreement (AVV), technical and organisational measures (TOMs), and a DPIA template.
- **W11:** Onboard 2–3 pilots and fix issues.
- **W12:** SEPA billing, pricing page, onboarding checklist. Launch.

#### Q7 — Where to launch first: **NRW, Germany**

Evidence for the choice:
1. NRW has one of the highest first-year co-payments: €3,427 against €3,108 nationally, so more residents need Hilfe zur Pflege ([vdek NRW](https://www.vdek.com/LVen/NRW/Presse/Pressemitteilungen/2025/stationaere-pflege-nrw.html)).
2. NRW Pflegewohngeld is paid directly to homes and renewed every 12 months. That gives the payer a recurring workflow tied straight to its revenue ([recht.nrw.de](https://recht.nrw.de/system/files/BH/5196-21888.htm)).
3. The German problem is quantified by recent independent sources: PwC 2026 and ARD 2025.
4. The US version of the problem is already served by at least four vendors (kill log #12).
5. The only funded German player sells to Sozialämter, not to homes.

Expansion path: other German states for Hilfe zur Pflege, then other states with Pflegewohngeld (not verified which), then Austria, Switzerland or France equivalents (not researched).

#### Q8 — How it makes money

- SaaS subscription per home, priced by bed band and paid monthly by SEPA direct debit.
- A 3-month paid pilot at €99/month. Annual prepay gets 2 months free.
- **No success fees.** These would reward pushing residents into aid.
- **No financing products** (keeps clear of H3 and H6).

**First 10 paying customers (plan)**
1. Build a list of NRW homes from public care-home directories. That the directories work as a contact source is assumed, not verified. Prioritise independent operators with 1–3 homes, where the administrator decides quickly.
2. Lead magnets:
   - a "Hilfe zur Pflege document checklist for relatives" in German;
   - an "open items with the Sozialamt" self-check spreadsheet that quotes the PwC numbers.
3. Outbound: 25 emails and 10 calls a day. Target: 20 conversations → 8 demos → 5 paid pilots at ≥€99 by day 75 → 10 paying homes by day 120.
4. Referral partners, offered 20% of first-year revenue (assumption): factoring firms, because complete files lower their risk, and care-home consultancies.
5. After 60 days, publish a pilot case study: days to a complete file, follow-up requests per case, and receivables reduced.

#### Q9 — How one person runs it

- **Support load.** Estimate 2–4 tickets per home per month, from relatives and staff. At 60 homes that is 10–20 hours a month with a help centre and templates (ASSUMPTION).
- **Form library upkeep.** About 1 day a month for quarterly form checks.
- **Failure modes and mitigations:**
  - Wrong checklist leads to a Sozialamt follow-up request → versioned rules plus the follow-up tracker.
  - Breach of special-category data (the care grade is health data) → encryption, 2FA, audit logs, German hosting, DPIA.
  - Email deliverability problems.
  - Bus factor of one founder → runbooks and managed database backups.

#### Q10 — What did I miss? Kill tests

- **Platform kill.** No big-tech risk. Government digitisation (OZG) could make form-filling a commodity. Berlin is online only for home-care cases so far. If that happens, the core value shifts to document chasing, renewals and receivables.
- **Incumbent copy.** Myosotis could bundle formfix into myo for homes (400+ customers, vendor claim). ERPs could add the feature too. Defence: deterministic rules, NRW depth (Pflegewohngeld), receivables first.
- **Liability.** Whether this counts as a legal service under the RDG (Legal Services Act) must be confirmed by counsel. This is ASSUMPTION/GAP: I believe document-generator software is not a legal service, but did not verify that this session. Special-category data under GDPR Art. 9 adds risk.
- **False assumptions.**
  1. Delays may be caused mainly by office capacity, not documents. Against that, 60% of homes blame missing documents.
  2. A home's own social-services staff may already handle this well.
  3. Cost-squeezed homes may not be willing to pay.
- **Churn and seasonality.** Low and none respectively. One unofficial report says more than 1,000 care facilities have closed since 2023 (employers' association via Bild, [Business Punk](https://www.business-punk.com/pflege-kollaps-in-deutschland-ueber-1000-heime-dicht/)).
- **Policy.**
  - A 2026 care reform (PNOG) is in progress ([biallo](https://www.biallo.de/soziales/news/elternunterhalt-freibetrag-pflegeheim-kosten/)). Any cap on co-payments would shrink Hilfe zur Pflege caseloads. **Not researched; gap.**
  - The bad association proposes a "provisional cost commitment" within 3 weeks of a complete file. As of 14 Sep 2026 it was still only a lobby-register entry ([Lobbyregister](https://www.lobbyregister.bundestag.de/media/e0/57/841831/Lobbyregister-Regelungsvorhaben-Detailansicht-RV0017741-2026-09-14_16-05-13.pdf)). If enacted it would ease the cash pain but make complete files worth more.

**Kill tests (≤90 days, ≤€2,000)**
- **KT1 (discovery).** By week 6, ≥15 NRW home administrators interviewed. If fewer than 50% have ≥3 Hilfe zur Pflege or Pflegewohngeld cases open longer than 3 months → kill.
- **KT2 (money).** By day 90, ≥5 homes paying ≥€99/month, or signed letters of intent with a price → else kill.
- **KT3 (efficacy).** Within 3 months of pilots, ≥30% fewer Sozialamt follow-up requests, or ≥30% fewer days to a complete file → else kill.
- **KT4 (competitor).** If Myosotis offers formfix free to NRW homes and pilots switch → stop.
- **KT5 (legal).** For ≤€1,000, counsel confirms the RDG and GDPR model. If not, narrow the product to a tool for home staff only.

---

### F2 — "SBV-Lotse": confidential case manager for Schwerbehindertenvertretungen plus employee self-service. Launch: Germany. The employer pays.

The Schwerbehindertenvertretung (SBV) is the elected representative of severely disabled employees in a German workplace.

**Who suffers**
- Employees with disabilities or chronic illness who need a disability degree (GdB) or "equal status" decision, or who are going through workplace reintegration (BEM) or a dismissal hearing.
- The SBV itself, a part-time volunteer who tracks these cases.

**Who pays.** The employer. It must bear the SBV's necessary costs under §179(8) SGB IX. The SBV decides what is necessary, subject to labour-court review ([LAG Berlin-Brandenburg decision](https://gerichtsentscheidungen.brandenburg.de/gerichtsentscheidung/21268); [betriebsrat.de](https://www.betriebsrat.de/betriebsratslexikon/sbv/kosten-der-amtsfuehrung)).

**The employer's money reason**
- The quota levy is €155–815 per unfilled place per month from 2025 ([IHK Chemnitz](https://www.ihk.de/chemnitz/standortpolitik/fachkraefte/beratungsangebote/ausgleichsabgabe-2024-6024450)). Each additional employee who is recognised or given equal status cuts the levy by **€1,860–9,780 a year** (derived from the tiers × 12).
- Only 39% of obligated employers met the quota in 2021 [OLD] ([Ärzteblatt](https://www.aerzteblatt.de/news/arbeitsmarkt-quote-fuer-menschen-mit-schwerbehinderung-unzureichend-erfuellt-e7959c48-814b-4bf8-a368-b3471d5064ba)).

#### Q1 — Who suffers, when, how often, and at what cost?

An employee with a chronic illness who applies for a disability degree waits months for the decision: 5–6 in Berlin, more than 9 on average in Sachsen-Anhalt. If the degree is set too low, the objection deadline is short (statutory one month under §84 SGG; not fetched this session). Meanwhile the elected SBV, a part-time volunteer, tracks these cases, BEM and dismissal hearings in spreadsheets. A missed step can cost the employee:
- 5 extra days of leave (§208 SGB IX);
- a €1,140 tax allowance at GdB 50;
- dismissal protection, which requires prior consent from the Integrationsamt (integration office).

Sources: [service.berlin.de](https://service.berlin.de/dienstleistung/326173/pdf/); [gegen-hartz on processing times](https://www.gegen-hartz.de/news/schwerbehinderung-der-gang-bis-zum-bescheid-ist-wahnsinn); [gegen-hartz on entitlements](https://www.gegen-hartz.de/news/schwerbehinderung-15-ansprche-bei-einem-grad-der-behinderung-von-50-oder-mehr); [Bundestag petition reply](https://epetitionen.bundestag.de/petitionen/_2023/_01/_13/Petition_144661.abschlussbegruendungpdf.pdf).

- **Frequency.** Episodic for each employee; continuous for the SBV.
- **Scale.** More than 1 million severely disabled or equal-status employees are represented by SBVs ([DGB](https://www.dgb.de/fileadmin/download_center/Aufrufe/Aufruf_SBV-Wahl_2026.pdf)).
- **Legal basis.** Supporting applications for a disability degree and for equal status is part of the SBV's statutory role ([Uni Bamberg](https://www.uni-bamberg.de/sbv/); [Uni Oldenburg](https://uol.de/schwerbehindertenvertretung/aufgaben)), and the list of tasks is open-ended ([betriebsrat.de](https://www.betriebsrat.de/fachartikel/schwerbehindertenvertretung/die-aufgaben-rechte-und-pflichten-einer-schwerbehindertenvertretung-3122842)).

#### Q2 — What is the one thing the app does?

It gives the SBV a confidential case file driven by deadlines, plus a self-service page that walks employees through disability-degree and equal-status applications and objections, generating letters and reminders. Only the SBV can see the data. The employer has no access.

#### Q3 — Who already solves it?

Two German searches for SBV case-management software returned only descriptions of SBV tasks and **no products** ([search set incl. Uni Bamberg, TU Dortmund, betriebsrat.de](https://www.betriebsrat.de/fachartikel/schwerbehindertenvertretung/die-aufgaben-rechte-und-pflichten-einer-schwerbehindertenvertretung-3122842)).

| Name | Country | Price | What it does | Gap vs F2 |
|---|---|---|---|---|
| Excel, Outlook and paper | — | €0 | Today's default (assumption, from SBV task descriptions) | No deadlines, templates or confidential employee self-service |
| Works-council software suites | DE | Not verified | Case and meeting management for works councils | **Not verified** whether they include SBV modules. Research gap and main copy risk. |
| Public advisory services (integration services, employer contact points) | DE | Free | Advice to employers and employees | **Not verified** this session. External advice, not an SBV case tool. |
| Social associations such as VdK and SoVD | DE | Membership fee (not verified) | Help individuals with disability-degree applications and objections | **Not verified.** Serves individuals, not SBV workflow. If true, it does show that individuals pay for this kind of help. |

#### Q4 — Why is it still unsolved? Root-cause class: **(c) + (a) + (e), with a (d) trigger**

- **(c)** The sufferer (employee or SBV) doesn't hold a budget. The employer pays only through the statutory cost rule.
- **(a)** The niche is too small for funded companies.
- **(e)** It is unglamorous.
- **(d) trigger.** SBV elections are running now, from 1 October to 30 November 2026, and will bring in a wave of new office-holders ([DGB](https://www.dgb.de/fileadmin/download_center/Aufrufe/Aufruf_SBV-Wahl_2026.pdf)). The new €815 levy tier for employers with zero quota fulfilment raises employer interest ([LAGeSo Berlin](https://www.berlin.de/lageso/behinderung/inklusionsamt-arbeit-und-behinderung/ausgleichsabgabe/)).

#### Q5 — Is it profitable?

| Item | Value | Status |
|---|---|---|
| Price | €39/month per SBV (≤50 represented employees), invoiced yearly at €468 to the employer. €79 tier for larger SBVs. | ASSUMPTION |
| Cost per customer | ~€4/month (hosting, email, payment fees) | ASSUMPTION |
| Gross margin | ~90% | ASSUMPTION (derived) |
| Fixed business costs | ~€1,200/month | ASSUMPTION |
| Customers needed for €8k/month profit | **~263 SBVs** = (8,000 + 1,200) / (39 − 4) | Derived |
| Reachable pool | >1M represented employees | VERIFIED ([DGB](https://www.dgb.de/fileadmin/download_center/Aufrufe/Aufruf_SBV-Wahl_2026.pdf)) |
| | 20,000–40,000 SBVs. Derived from >1M employees, ~60% in workplaces with ≥5 such employees, ÷ 15–30 per SBV | ASSUMPTION |
| Share of pool needed | ~0.7–1.3% | Derived |
| Payer value per success | €1,860–9,780 a year in levy saved per additional counted employee | VERIFIED tiers ([IHK Chemnitz](https://www.ihk.de/chemnitz/standortpolitik/fachkraefte/beratungsangebote/ausgleichsabgabe-2024-6024450)); derived total |
| Employee value | 5 extra leave days; €1,140 tax allowance at GdB 50 | VERIFIED ([gegen-hartz](https://www.gegen-hartz.de/news/schwerbehinderung-15-ansprche-bei-einem-grad-der-behinderung-von-50-oder-mehr)) |
| CAC | ~€80 (content plus a 20% first-year seminar affiliate fee) | ASSUMPTION |
| Monthly churn | 1.2% (SBV terms last 4 years) | ASSUMPTION |
| LTV | ~€2,900 | Derived |
| LTV/CAC | ~36 | Derived |

#### Q6 — How to build it

**MVP scope**
- Case types: disability-degree application, objection, equal-status application, BEM, prevention procedure, dismissal hearing.
- A deadline engine. The rule for presumed receipt of official letters may have changed in 2025; **verify before build.**
- A letter and template generator.
- An anonymous employee self-service page with booking of SBV consultations.
- SBV duties calendar: hearings, annual assembly, activity report.
- Access only for the SBV and deputies. No employer admin.
- A generator for the SBV's request to the employer to cover the tool's cost under §179(8).

**Stack:** same as F1. Optional client-side encryption of case notes.

**12-week build outline**
- **W1:** 15 SBV interviews; data-protection design reviewed by counsel.
- **W2–3:** Case file and deadline engine.
- **W4–5:** Templates and checklists.
- **W6–7:** Employee self-service.
- **W8:** SBV duties calendar.
- **W9:** Security hardening.
- **W10:** Cost-request generator and invoicing.
- **W11–12:** 5 pilots, fixes, launch.

#### Q7 — Where to launch first: **Germany**

The SBV is a German statutory institution, so there is no other market for this exact product.

Timing evidence: the 1 Oct – 30 Nov 2026 elections produce new SBVs who need tools from December onward. The levy hike sharpens employer interest.

Start with **public-sector SBVs**. They list themselves online, which gives a named and reachable list: [Uni Bamberg](https://www.uni-bamberg.de/sbv/), [Uni Oldenburg](https://uol.de/schwerbehindertenvertretung), [Uni Bielefeld](https://uni-bielefeld.de/sbv), [TU Dortmund](https://sbv.tu-dortmund.de/storages/sbv/w/Dateien/SBV_Faltblatt_Wickelfalz_DIN-A4_SC_Druckdaten_ZV.pdf), [Ostfalia](https://www.ostfalia.de/fileadmin/user_upload/Einrichtungen/Schwerbehindertenvertretung/dokumente/sbv-infobrief/75-SBV-InfoBrief_Januar-2026.pdf), [TiHo Hannover](https://www.tiho-hannover.de/fileadmin/03_Personalrat/Personalversammlungen/6_Grages_SBV.pdf).

#### Q8 — How it makes money

- Annual subscription per SBV, invoiced to the employer and justified under §179(8).
- No success fees: this avoids the incentive conflict in kill #4.
- No data monetisation.

**First 10 paying customers (plan)**
1. Collect a list of ~300 public-sector SBV contacts by hand from university, hospital and municipal websites (not scraping).
2. Offer a "starter pack for newly elected SBVs": 60-day free trial plus templates, with an objection-deadline calculator as the lead magnet.
3. Run affiliate or bundle deals with SBV seminar providers, for example AAS Seminare ([aas-seminare](https://www.aas-seminare.de/wp-content/uploads/print/50940/7282d5088682425dcdf4ba598ecf9280.pdf)).
4. Include a ready-made §179(8) cost-request letter so the SBV can get the employer's approval quickly.
5. Target: 30 trials → 10 paid, employer-approved accounts by day 90–120.

#### Q9 — How one person runs it

- **Support.** Mostly "how do I" questions. Templates and a help centre cover most of it. Estimate under 10 hours a month at 250 SBVs (ASSUMPTION).
- **Failure modes and mitigations:**
  - A wrong deadline calculation → the rule set is reviewed by counsel; clear warnings in the app.
  - Employer pressure to see the data → architecture gives the employer no access.
  - Health-data breach → encryption, 2FA, logging.
- **Seasonality.** Elections every 4 years cause demand spikes.

#### Q10 — What did I miss? Kill tests

- **Payer refusal.** Employers may dispute that the software is "necessary", and the cost rule depends on necessity and proportionality ([betriebsrat.de](https://www.betriebsrat.de/betriebsratslexikon/sbv/kosten-der-amtsfuehrung)). This is the key risk.
- **Incumbent copy.** Works-council suites could add an SBV module (not verified).
- **Liability and GDPR.** Special-category data; SBVs have a confidentiality duty under §179(7) ([TU Dortmund](https://sbv.tu-dortmund.de/storages/sbv/w/Dateien/SBV_Faltblatt_Wickelfalz_DIN-A4_SC_Druckdaten_ZV.pdf)).
- **False assumption.** The number of SBVs, and how many handle ≥10 cases a year, is unknown.
- **Churn and seasonality.** Low churn within a term; the 4-year election cycle drives demand.

**Kill tests (≤90 days, ≤€2,000)**
- **KT1.** By week 4, 20 SBV interviews. If fewer than 8 have ≥10 active cases a year and confirm spreadsheet pain → kill.
- **KT2.** By day 90, ≥5 employers have issued a purchase order or paid an invoice → else kill.
- **KT3.** For ≤€800, counsel approves the data-protection model, deciding who is controller: the SBV or the employer.
- **KT4.** If a works-council suite bundles a free SBV module during the pilots → stop.

---

### F3 — "Fristen-Lotse": benefit-deadline assistant for tenants, triggered by the landlord's utility statements and rent changes. Launch: Germany. The landlord pays.

**Who suffers**
- Tenants on Grundsicherung (basic income support). There were ~2.8 million benefit households in May 2026 ([Bundestag Drucksache](https://dserver.bundestag.de/btd/21/068/2106855.pdf)).
- Low-income workers whose annual utility back-payment the Jobcenter can cover through a one-month claim, even if they don't otherwise draw benefits ([gegen-hartz](https://www.gegen-hartz.de/news/buergergeld-kaum-bekannt-jobcenter-zahlt-betriebskostennachzahlung-auch-ohne-buergergeld-bezug)).

The Bundestag source is an answer to a parliamentary question, seen via extract; the exact document among the listed answers is uncertain.

**Who pays.** Housing companies and property managers.

**The landlord's money reason.** A back-payment the Jobcenter doesn't cover becomes rent arrears. The average back-payment is €907 ([inFranken/WiWo](https://www.infranken.de/ratgeber/karriere-geld/3000-euro-nebenkosten-warum-wohnen-in-deutschland-immer-teurer-wird-art-6350661)). Housing costs paid for a benefit household averaged €594/month in March 2025 (same Bundestag answer). How much landlords actually lose is **not quantified** (gap).

#### Q1 — Who suffers, when, how often, and at what cost?

A tenant on Grundsicherung receives the annual utility statement with a back-payment of about €900. Unless it reaches the Jobcenter in the month the payment falls due, coverage is lost ([gegen-hartz](https://www.gegen-hartz.de/buergergeld-nachzahlung-fuer-nebenkosten-und-heizung-was-zahlt-das-jobcenter)). The tenant then owes money they don't have, which leads to dunning letters, arrears and, in the worst case, eviction proceedings.

- **Frequency.** Once a year per tenant, plus rent increases.
- **New confusion.** The "Neue Grundsicherung" replaced Bürgergeld from 1 July 2026 and changed the housing-cost rules. Municipalities can now set caps per square metre, and the waiting period allows rent up to 1.5× the appropriate limit ([Stuttgarter Zeitung](https://www.stuttgarter-zeitung.de/wirtschaft/neue-grundsicherung-juli-wer-bekommt-wie-viel-mhsd-79231920.html); [LaDaDi brochure](https://www.ladadi.de/medien/pdfs/fb-520-2-esc-kfb/buergergeld/grundsicherung-praesentation.pdf)).

#### Q2 — What is the one thing the app does?

Every utility statement or rent-change letter carries a QR code. It leads to a tenant page that asks three questions, shows the exact deadline, generates the cover letter to the right Jobcenter or Sozialamt, and sends SMS reminders until the tenant confirms they have submitted it.

#### Q3 — Who already solves it?

One German search on this pain returned only advocacy and information pages ([gegen-hartz](https://www.gegen-hartz.de/news/buergergeld-nebenkostennachzahlung-das-muessen-die-jobcenter-jetzt-zahlen-grundsicherung)). No tool surfaced.

| Name | Country | Price | What it does | Gap vs F3 |
|---|---|---|---|---|
| Housing ERPs such as Aareon (Wodis) | DE | Not verified | Produce utility statements | Could add a notice or QR code cheaply. **Main H4 risk; not verified.** |
| Tenant apps and portals | DE | Not verified | Communication with tenants | Not verified |
| Advocacy sites (gegen-hartz.de) | DE | Free | Explain the rules | No deadline tracking or pre-filled letters |
| Mineko | DE | Consumer fee (not verified) | Checks utility statements. Claims 93% contain errors and tenants overpay €515 on average (vendor claim, [web.de](https://web.de/magazine/ratgeber/finanzen-verbraucher/nebenkostenabrechnungen-fehlerhaft-verbraucher-41352500)). | Adjacent: a consumer-paid check, not a deadline service. Partly legal services. |

#### Q4 — Why is it still unsolved? Root-cause class: **(c) + (d) + (b) + (e)**

- **(c)** The tenant suffers; the landlord would have to pay.
- **(d)** The Neue Grundsicherung of 1 July 2026 changed the housing-cost rules, adding fresh confusion.
- **(b)** Hundreds of Jobcenters and Sozialämter, each with its own address and forms.
- **(e)** Boring.

#### Q5 — Is it profitable?

| Item | Value | Status |
|---|---|---|
| Price | €0.08 per rental unit per month, minimum €99. A 4,000-unit customer pays ~€320/month. | ASSUMPTION |
| Cost per customer | ~€25/month. SMS: 12% of 4,000 tenants × 3 messages a year × €0.08 ≈ €10; hosting and support €15. | ASSUMPTION |
| Gross margin | ~92% | ASSUMPTION (derived) |
| Fixed business costs | ~€1,500/month | ASSUMPTION |
| Customers needed for €8k/month profit | **~33 companies** = 9,500 / 295 | Derived |
| Reachable pool | ~3,000 GdW member companies plus property managers | ASSUMPTION (not verified) |
| Household pool | ~2.8M benefit households (May 2026) | VERIFIED ([Bundestag](https://dserver.bundestag.de/btd/21/068/2106855.pdf), via extract) |
| Payer value illustration | 480 benefit tenants × 10% missing the deadline × €907 ≈ €43.5k at risk a year; halving misses protects ~€21.8k vs €3.8k price | €907 VERIFIED; the rest ASSUMPTION |
| CAC | ~€2,500 (slow B2B sales, events) | ASSUMPTION |
| Monthly churn | 1% | ASSUMPTION |
| LTV | ~€29,500 | Derived |
| LTV/CAC | ~12 | Derived |

#### Q6 — How to build it

**MVP scope**
- A rules engine. Inputs: benefit type (SGB II, SGB XII, Wohngeld, or none but low-income) and event (back-payment, credit, rent increase). Output: the deadline (end of the due month) and the responsible office, looked up by postcode from public data.
- A tenant page with no login: plain language in 7 languages, translated by freelancers.
- A PDF cover-letter generator.
- Opt-in SMS and email reminders and a "submitted" confirmation.
- Landlord side: CSV batch upload from ERP exports, QR codes for print inserts, and a dashboard showing confirmations only.

**12-week build outline**
- **W1:** 10 interviews and a legal check.
- **W2–3:** Rules engine.
- **W4–5:** Tenant page and letters.
- **W6:** Landlord batch upload and QR codes.
- **W7–8:** Translations.
- **W9:** ERP CSV mappings.
- **W10:** Security and DPA.
- **W11–12:** Pilot on a real statement batch.

#### Q7 — Where to launch first: **Germany**

The due-month rule and the July 2026 reform are German-specific.

Start with cooperatives and municipal housing companies of 500–5,000 units in cities with many benefit households. That concentration is not verified. Smaller companies decide faster.

#### Q8 — How it makes money

- A per-unit subscription for the landlord, minimum €99/month, invoiced annually.
- The tenant never pays.
- The landlord sees only confirmations that the tenant chose to share.

**First 10 paying customers (plan)**
1. Contact the heads of collections and social management at ~150 cooperatives and municipal companies through LinkedIn and phone.
2. Offer a free pilot on their next statement batch. Measure the share of tenants who submit on time, and arrears from back-payments, against last year.
3. Speak at regional housing-association meetings (not verified as available).
4. Target: 3 pilots by day 90 and 10 paying by month 9. Statement seasonality slows proof.

#### Q9 — How one person runs it

- Mostly automated.
- Rule maintenance after every change to the benefit rules: high in 2026–27, given the July 2026 reform and court rulings ([heidelberg24](https://www.heidelberg24.de/verbraucher/millionen-betroffene-aufgepasst-gericht-kassiert-neue-grundsicherungsregel-ein-zr-94453739.html)).
- Tenant questions are routed to a FAQ. The tool gives no individual advice.

#### Q10 — What did I miss? Kill tests

- **H4 exposure.** Highest of the three finalists: an ERP vendor can add a notice and QR code cheaply.
- **Regulatory volatility.** The Neue Grundsicherung is new and courts are still reinterpreting it.
- **False assumptions.**
  - The share of tenants who miss the deadline is unknown.
  - Landlords may prefer their normal dunning process.
  - Some Jobcenters may accept late submissions in practice. The due-month rule comes from an advocacy source.
- **Liability.** RDG: the tool gives general information plus a letter, not an assessment of the tenant's claim (ASSUMPTION; needs counsel). No debt collection.
- **Seasonality.** Strong, because utility statements cluster in certain months.

**Kill tests**
- **KT1.** By week 6, in 10 interviews, ≥4 landlords confirm measurable arrears from uncovered back-payments → else kill.
- **KT2.** By day 90, ≥2 signed paid pilots or letters of intent with a price → else kill.
- **KT3.** In a pilot, ≥30% fewer misses than the prior year → else kill.

---

## (3) PROVISIONAL SCORES

Weights: C1 10, C2 15, C3 10, C4 15, C5 15, C6 5, C7 10, C8 10, C9 5, C10 5. Weighted score = sum(score × weight) / 10.

The baseline was scored by me with the same rubric, for comparison only.

| Criterion (weight) | Baseline (daily check-in call, DE) | F1 Care-home financing | F2 SBV-Lotse | F3 Tenant deadlines |
|---|---|---|---|---|
| C1 Pain (10) | 6 | 8 | 6 | 6 |
| C2 Willingness to pay and payer clarity (15) | 6 | 7 | 5 | 5 |
| C3 Gap realness (10) | 6 | 7 | 6 | 5 |
| C4 Distribution (15) | 4 | 6 | 6 | 5 |
| C5 Unit economics (15) | 6 | 8 | 6 | 7 |
| C6 Market sufficiency (5) | 9 | 9 | 7 | 8 |
| C7 Solo operability (10) | 7 | 6 | 7 | 7 |
| C8 Durability (10) | 4 | 6 | 5 | 4 |
| C9 Risk, inverse (5) | 5 | 6 | 5 | 6 |
| C10 Speed to proof (5) | 7 | 6 | 5 | 4 |
| **Weighted total** | **57.5** | **69.0** | **58.0** | **56.5** |
| **Verdict** | KILL (<60) | **TEST** (60–74) | KILL by score; ties baseline | KILL by score; below baseline |

**Baseline justifications (one line each)**
- C1 6: the fear of lying undiscovered is real, but the event is rare and the daily friction small.
- C2 6: the family pays €9.90; US services at $14.99 and Hausnotruf at €27–40 show willingness to pay (both given in the brief).
- C3 6: plausible gap for a phone-only service without a care grade.
- C4 4: business-to-consumer marketing to adult children with no cheap named channel.
- C5 6: ~70% margin; acquisition cost and churn uncertain.
- C6 9: ~1,000 families out of millions of people aged 65+.
- C7 7: automated telephony; alarm handling adds support.
- C8 4: trivial to copy; low switching costs.
- C9 5: liability for a missed alert.
- C10 7: cheap landing-page pre-sales.

**F1 justifications**
- C1 8: €3,108–3,427 a month at stake and 6–12+ month decisions with risk of losing the place. Intense, though episodic.
- C2 7: the payer is clear and quantified by PwC 2026 (55% largest debtor, 1 in 5 ≥€100k, 8.3 h/week). No direct proof yet that homes will pay for this tool, only factoring spend.
- C3 7: 60% of homes blame missing documents and 46% lack a process. No product on the home side found; the only funded player sells to public offices.
- C4 6: ~11,250 long-term care homes in public directories plus associations, but cold B2B outreach is needed and chains buy centrally.
- C5 8: ~90% margin at €179/month; LTV/CAC above 10 under conservative assumptions.
- C6 9: needs ~61 homes, about 0.5% of the pool.
- C7 6: variation across ~478 offices, questions from relatives, and Art. 9 data, but no real-time operations.
- C8 6: Myosotis or ERPs could copy, and a care reform could cut caseloads. Case history creates switching costs.
- C9 6: sensitive data and an open RDG question, mitigated by positioning as a tool, not advice.
- C10 6: €99 paid pilots within 90 days are plausible; some homes will take longer.

**F2 justifications**
- C1 6: 3–9-month procedures and lost protections are real, but episodic per employee.
- C2 5: the employer must pay the SBV's necessary costs and has a levy motive, but software "necessity" must be argued and there is no spend evidence.
- C3 6: no SBV-specific product found; works-council suites not checked.
- C4 6: the 2026 election wave plus public-sector SBV pages and seminar providers. No complete list of SBVs.
- C5 6: high margin but low revenue per customer and indirect value attribution.
- C6 7: ~263 needed out of an assumed 20–40k SBVs. The pool size is uncertain.
- C7 7: simple case management and templates; low operations load.
- C8 5: works-council suites could add a module; 4-year terms help retention.
- C9 5: health data and pressure from employers to see it, handled by architecture.
- C10 5: employer approval slows pre-sales.

**F3 justifications**
- C1 6: ~€900 a year can turn into arrears for 2.8M benefit households, but the deadline-miss rate is unknown.
- C2 5: the landlord's loss is real but not quantified.
- C3 5: no tool found, but only one search was run.
- C4 5: housing companies are reachable but sales cycles are slow.
- C5 7: high margin and few customers needed.
- C6 8: ~33 companies needed.
- C7 7: rules plus letters; rule churn in 2026–27.
- C8 4: easy for an ERP vendor to copy; regulatory volatility.
- C9 6: minimal data; RDG framing as general information.
- C10 4: statement seasonality and committee decisions slow proof.

**Does any finalist beat the baseline?**
- **F1: yes.** 69.0 vs 57.5, a TEST verdict. It is the only finalist with a clear margin.
- **F2: no meaningful margin.** 58.0 is within noise of the baseline.
- **F3: no.** 56.5.

If evaluators score the baseline above ~60, only F1 remains ahead.

**Open gaps that could move scores**
- Care-home ERP features (C3/C8 for F1).
- PNOG care-reform content (C8 for F1).
- Number of SBVs (C6 for F2).
- Landlord loss data and ERP features (C2/C8 for F3).
- An RDG legal opinion (C9 for all three).

---

## (4) SOURCES

Method note: most pages were confirmed via search-engine extracts attributed to these URLs. Direct fetching was blocked (DNS errors or proxy 403). **[OLD]** marks evidence from before 2024.

**Care-home financing (F1)**
- PwC/Strategy& press release, 12 Jun 2026: https://www.pwc.de/de/pressemitteilungen/2026/fehlende-liquiditaet-in-pflegeheimen-gefaehrdet-die-versorgung.html
- PwC topic page: https://www.pwc.de/de/gesundheitswesen-und-pharma/liquiditaet-in-pflegeeinrichtungen.html
- Apotheken Umschau (60% blame missing documents): https://www.apotheken-umschau.de/gesundheitspolitik/pflegeheime-warten-monatelang-auf-hilfe-zur-pflege-von-sozialaemtern-1539809.html
- Ärzteblatt on ARD Report Mainz (May 2025): https://www.aerzteblatt.de/news/antragsstau-zur-pflege-in-sozialamtern-affb0712-f301-4506-b133-ea19da7c2365
- bpa newsletter, 13 May 2025: https://www.bpa.de/fileadmin/News___Fachinformationen/bpa.newsletter/mailing_13-05-2025.pdf
- vdek national co-payment figures, July 2025: https://www.vdek.com/presse/pressemitteilungen/2025/pflegeheim-monatliche-eigenbeteiligung-steigt-stationaere-pflege.html
- vdek NRW: https://www.vdek.com/LVen/NRW/Presse/Pressemitteilungen/2025/stationaere-pflege-nrw.html
- cash-online (January 2026 figure): https://www.cash-online.de/a/pflegeheimkosten-steigen-weiter-eigenanteil-erreicht-3-245-euro-im-ersten-jahr-710392/
- Destatis social-assistance spending 2024, via presseportal: https://www.presseportal.de/pm/32102/6098431
- Ärzteblatt on the same Destatis release: https://www.aerzteblatt.de/news/sozialhilfetrager-geben-mehr-geld-aus-85df9e1c-bc46-4920-82d3-20b4222c0f99
- medi-karriere (~354k recipients in facilities; secondary, provenance unclear): https://www.medi-karriere.de/magazin/pflegeheime-bewohner-auf-sozialhilfe-angewiesen/
- Bayerischer Landtag (41,670 recipients in 2024): https://www.bayern.landtag.de/www/ElanTextAblage_WP19/Drucksachen/Basisdrucksachen/0000009500/0000009618_039.pdf
- service.berlin.de, Hilfe zur Pflege (paper only for care homes): https://service.berlin.de/dienstleistung/324474/pdf/
- KBV, number of care facilities: https://www.kbv.de/infothek/zahlen-und-fakten/gesundheitsdaten/pflegeheime-und-personal
- Curacon, home counts from Destatis: https://www.curacon.de/fileadmin/user_upload/Curacon/Downloads/Produktbeispiel_sAHBenchmark_Max.pdf
- Pflegewohngeld NRW rules:
  - Verbraucherzentrale NRW: https://www.verbraucherzentrale.nrw/wissen/gesundheit-pflege/pflege-im-heim/pflegewohngeld-in-nrw-finanzielle-hilfe-in-stationaeren-einrichtungen-86793
  - recht.nrw.de: https://recht.nrw.de/system/files/BH/5196-21888.htm
  - Kreis Euskirchen: https://kreis-euskirchen.de/fileadmin/user_upload/1946-Z.I.P._-_Merkblatt_Heimplatzfinanzierung_neu.pdf
  - Kreis Warendorf: https://serviceportal.kreis-warendorf.de/detail/-/vr-bis-detail/dokument/136331/download
- Parental-support (Elternunterhalt) threshold:
  - biallo: https://www.biallo.de/soziales/news/elternunterhalt-freibetrag-pflegeheim-kosten/
  - Pflegestützpunkte Berlin: https://www.pflegestuetzpunkteberlin.de/wp-content/uploads/2025/04/DE-IB-34-Unterhaltspflicht-von-Kinder-gegebenueber-pflegebeduerftigen-Eltern.pdf
- Aid granted only from application date (gegen-hartz): https://www.gegen-hartz.de/news/pflegegeld-pflegeheim-kosten-drei-fehler-die-familien-jetzt-teuer-bezahlen
- bad lobby proposal (provisional cost commitment):
  - Register entry: https://www.lobbyregister.bundestag.de/inhalte-der-interessenvertretung/regelungsvorhabensuche/RV0017741/195234
  - Printout dated 14 Sep 2026: https://www.lobbyregister.bundestag.de/media/e0/57/841831/Lobbyregister-Regelungsvorhaben-Detailansicht-RV0017741-2026-09-14_16-05-13.pdf
- Myosotis:
  - Job posting (vendor claims): https://join.com/companies/myo/16523373-mitarbeiter-in-sozialhilfe-hilfe-zur-pflege-m-w-d
  - startbase funding report: https://www.startbase.de/news/105-millionen-euro-fuer-myosotis/
  - TVM investor page: https://tvm-capital.com/?p=6430
  - Tagesspiegel Background (paywalled): https://background.tagesspiegel.de/smart-city-und-stadtentwicklung/briefing/wie-der-agentic-ai-hub-zum-erfolg-werden-kann
  - Berliner Zeitung (paywalled): https://www.berliner-zeitung.de/article/berliner-start-up-erleichtert-antraege-auf-sozialhilfe-leute-verstehen-die-komplizierten-fragestellungen-nicht-2338994
- Factoring:
  - ecovis: https://ecovis-kso.com/blog/factoring-in-der-pflege/
  - SozialFactoring (2026): https://www.sozialfactoring.de/app/uploads/2026/07/PflegeManagement_Warum-Forderungsmanagement-zur-Fuehrungsaufgabe-wird.pdf
  - Agicap: https://agicap.com/de/artikel/factoring/
- US Medicaid-pending vendors (vendor pages):
  - SNF Metrics: https://snfmetrics.com/ar-tracker-dashboard/
  - Aidace: https://www.capterra.co.uk/software/1238013/Aidace
  - AR Proactive: https://www.arproactive.com/nursing-homes
  - ExaCare: https://www.exacare.com/article/medicaid-pending-nursing-homes
- Pricing benchmarks:
  - DMRZ [OLD 2019]: https://www.dmrz.de/fileadmin/Presse/DMRZ_PM_Individuelle-Service-und-Tarifwahl-2019.pdf
  - smart-rechner widget: https://www.smart-rechner.de/pflegekosten/rechner.php
- Care-facility closures (unofficial): https://www.business-punk.com/pflege-kollaps-in-deutschland-ueber-1000-heime-dicht/

**Disability, SBV and quota levy (F2; kill #4)**
- SBV elections 2026:
  - DGB: https://www.dgb.de/fileadmin/download_center/Aufrufe/Aufruf_SBV-Wahl_2026.pdf
  - NGG: https://www.ngg.net/fileadmin_new/7_Themen/SBV-Wahl-Grundlagen_vereinfachtes_Wahlverfahren.pdf
- Employer bears SBV costs:
  - LAG decision: https://gerichtsentscheidungen.brandenburg.de/gerichtsentscheidung/21268
  - betriebsrat.de lexicon: https://www.betriebsrat.de/betriebsratslexikon/sbv/kosten-der-amtsfuehrung
- SBV tasks:
  - betriebsrat.de article: https://www.betriebsrat.de/fachartikel/schwerbehindertenvertretung/die-aufgaben-rechte-und-pflichten-einer-schwerbehindertenvertretung-3122842
  - Uni Bamberg: https://www.uni-bamberg.de/sbv/
  - Uni Oldenburg: https://uol.de/schwerbehindertenvertretung/aufgaben
  - Uni Bielefeld: https://uni-bielefeld.de/sbv
  - TU Dortmund: https://sbv.tu-dortmund.de/storages/sbv/w/Dateien/SBV_Faltblatt_Wickelfalz_DIN-A4_SC_Druckdaten_ZV.pdf
  - Ostfalia: https://www.ostfalia.de/fileadmin/user_upload/Einrichtungen/Schwerbehindertenvertretung/dokumente/sbv-infobrief/75-SBV-InfoBrief_Januar-2026.pdf
  - TiHo Hannover: https://www.tiho-hannover.de/fileadmin/03_Personalrat/Personalversammlungen/6_Grages_SBV.pdf
  - AAS Seminare: https://www.aas-seminare.de/wp-content/uploads/print/50940/7282d5088682425dcdf4ba598ecf9280.pdf
- Quota levy tiers:
  - IHK Chemnitz: https://www.ihk.de/chemnitz/standortpolitik/fachkraefte/beratungsangebote/ausgleichsabgabe-2024-6024450
  - LAGeSo Berlin: https://www.berlin.de/lageso/behinderung/inklusionsamt-arbeit-und-behinderung/ausgleichsabgabe/
  - IHK Ostwestfalen: https://www.ihk.de/ostwestfalen/newsportal/ausgleichsabgabe-2026-6964718
- Quota fulfilment 2021 [OLD]: https://www.aerzteblatt.de/news/arbeitsmarkt-quote-fuer-menschen-mit-schwerbehinderung-unzureichend-erfuellt-e7959c48-814b-4bf8-a368-b3471d5064ba
- Disability-degree processing times:
  - service.berlin.de: https://service.berlin.de/dienstleistung/326173/pdf/
  - gegen-hartz (MDR figures): https://www.gegen-hartz.de/news/schwerbehinderung-der-gang-bis-zum-bescheid-ist-wahnsinn
  - Landtag BW: https://www.landtag-bw.de/resource/blob/583480/33e870282b2ece8283f9bb7144051c59/17_9140_D.pdf
- GdB 50 entitlements:
  - gegen-hartz: https://www.gegen-hartz.de/news/schwerbehinderung-15-ansprche-bei-einem-grad-der-behinderung-von-50-oder-mehr
  - Bundestag petition reply: https://epetitionen.bundestag.de/petitionen/_2023/_01/_13/Petition_144661.abschlussbegruendungpdf.pdf
- Employer disclosure programmes (none found): https://www.forum-verlag.com/fachwissen/personalmanagement/schwerbehinderung-arbeitsplatz

**Tenant benefit deadlines (F3; kill #15)**
- Due-month rule and one-month claims (gegen-hartz):
  - https://www.gegen-hartz.de/buergergeld-nachzahlung-fuer-nebenkosten-und-heizung-was-zahlt-das-jobcenter
  - https://www.gegen-hartz.de/news/buergergeld-kaum-bekannt-jobcenter-zahlt-betriebskostennachzahlung-auch-ohne-buergergeld-bezug
  - https://www.gegen-hartz.de/news/buergergeld-nebenkostennachzahlung-das-muessen-die-jobcenter-jetzt-zahlen-grundsicherung
- Average back-payment €907: https://www.infranken.de/ratgeber/karriere-geld/3000-euro-nebenkosten-warum-wohnen-in-deutschland-immer-teurer-wird-art-6350661
- Mineko (vendor claim): https://web.de/magazine/ratgeber/finanzen-verbraucher/nebenkostenabrechnungen-fehlerhaft-verbraucher-41352500
- Deutscher Mieterbund operating-cost index: https://mieterbund.de/aktuelles/meldungen/mieterbund-veroeffentlicht-aktuellen-betriebskostenspiegel-fuer-deutschland/
- Benefit households and housing costs (Bundestag answers; exact document uncertain):
  - https://dserver.bundestag.de/btd/21/068/2106855.pdf
  - https://dserver.bundestag.de/btd/21/065/2106544.pdf
- Neue Grundsicherung:
  - Stuttgarter Zeitung: https://www.stuttgarter-zeitung.de/wirtschaft/neue-grundsicherung-juli-wer-bekommt-wie-viel-mhsd-79231920.html
  - LaDaDi brochure: https://www.ladadi.de/medien/pdfs/fb-520-2-esc-kfb/buergergeld/grundsicherung-praesentation.pdf
  - heidelberg24 (court ruling): https://www.heidelberg24.de/verbraucher/millionen-betroffene-aufgepasst-gericht-kassiert-neue-grundsicherungsregel-ein-zr-94453739.html
- Wohngeld take-up data gap:
  - Bremen: https://www.bremische-buergerschaft.de/dokumente/wp21/land/drucksache/D21L1816.pdf
  - IWU [OLD 2021]: https://www.iwu.de/fileadmin/publikationen/vortrag/2021-06-14_Wohngeld-Fachgespr%C3%A4ch_Cischinsky_Slides_Zur-Inanspruchnahme-des-Wohngelds.pdf

**Kill-log evidence**
- Nurse recruitment:
  - Ankaadia: https://www.ankaadia.com/en/functions/international-recruitment
  - OMR alternatives list: https://omr.com/de/reviews/product/ankaadia/alternatives
  - Recruitroo: https://www.recruitroo.com/how-it-works
  - der-betrieb (up to four authorities): https://der-betrieb.de/meldungen/fachkraeftemangel-stolperfallen-mit-medizinischen-fachkraeften-aus-dem-ausland/
  - KDA position paper on the 24-month window [OLD 2023]: https://kda.de/wp-content/uploads/2023/01/Positionen-zur-erleichterten-Fachkraefte-Einwanderung.pdf
  - Gütesiegel holders [OLD 2022]: https://www.bundestag.de/presse/hib/kurzmeldungen-916382
  - Triple Win fee [OLD 2023]: https://www.staedteregion-aachen.de/fileadmin/user_upload/A_53/Pflegeoffensive/Workshop4_Praesentation_Arbeitsagentur.pdf
  - Recognitions 2024: https://www.bmbfsfj.bund.de/bmbfsfj/aktuelles/pressemitteilungen/anerkennung-auslaendischer-berufsqualifikationen-2024-neue-hoechstwerte-erneut-deutlicher-zuwachs-bei-gesundheitsberufen--269962
- UK sponsor compliance:
  - SMS System: https://www.capterra.com/p/10048254/SMS-SYSTEM/
  - CloudNet UKVI: https://www.capterra.co.uk/software/1108137/UKVI-Sponsor-Licence-Compliance-Software
  - UK Immigration law firm service: https://www.ukimmigration.law/sponsor-compliance-service/
- UK 30-hours childcare codes [OLD 2017–2023]:
  - Bolton: https://www.bolton.gov.uk/downloads/file/3309/30-hours-funding-things-to-remember-parents-
  - Coventry: https://www.coventry.gov.uk/downloads/file/31305/2-reconfirmation-of-funding-codes
  - Devon: https://www.devon.gov.uk/eycs/?p=14452
- UK free school meals:
  - Gloucestershire (June 2026): https://www.gloucestershire.gov.uk/media/y25fdrvs/schoolsnet-free-school-meals-and-pupil-premium-opt-out-auto-award-june-2026.docx
  - Wokingham FOI: https://www.wokingham.gov.uk/foi/auto-enrolment-free-school-meals
  - APSE: https://www.apse.org.uk/sites/apse/assets/File/Ashlee%20and%20Cressida.pdf
- Columba [OLD]:
  - t-online: https://www.t-online.de/digital/aktuelles/id_84818402/neue-helfer-regeln-den-digitalen-nachlass.html
  - WinFuture: https://winfuture.de/news,76351.html
- Fortuna Health:
  - HC Innovation Group: https://www.hcinnovationgroup.com/policy-value-based-care/medicare-medicaid/news/55304442/fortuna-gets-funding-to-expand-medicaid-enrollment-solution
  - Fierce Healthcare: https://fiercehealthcare.com/health-tech/medicaid-navigation-startup-fortuna-health-picks-4m-investment-backed-a16z-cityblock
- Entlastungsbetrag:
  - AOK: https://www.aok.de/pk/pflegeleistungen/entlastungsbetrag/
  - test.de: https://www.test.de/Entlastungsbetrag-pflege-6242425-0/
  - Niedersachsen billing form: https://soziales.niedersachsen.de/download/184112
  - gegen-hartz (unnamed survey): https://www.gegen-hartz.de/news/pflegegeld-rentnerin-mit-pflegegrad-3-verliert-1572-euro-obwohl-das-pflegegeld-weiterluft
- Chimney sweep:
  - haustechnikdialog: https://www.haustechnikdialog.de/SHKwissen/1492/Feuerstaettenschau
  - Handwerksblatt: https://www.handwerksblatt.de/betriebsfuehrung/bei-schoellgen-haustechnik-koennen-kunden-ihre-wartungstermine-entspannt-online-buchen
  - softwareabc24: https://www.softwareabc24.de/schornsteinfeger-software
- School aides [OLD]:
  - SH ombudsman: https://eno.ombudsman.europa.eu/home/news/archives-2016/maincontent/schulbegleitung-auch-das-sozialg.html
  - Langerwehe concept: https://www.ge-langerwehe.de/wp-content/uploads/2021/12/Konzept-zur-Schulbegleitung-an-der-ES-Langerwehe.pdf
