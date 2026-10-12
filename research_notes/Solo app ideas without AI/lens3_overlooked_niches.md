# Lens 3 — Overlooked niche industries, trades and organisations: non-AI app ideas one solo founder can build and run

Research date: 2026-10-12. Scope: trades, specialised services and organisations that are "too small for funded companies, big enough for one person". The METHOD (Q1–Q10) and RULEBOOK (H1–H8, C1–C10) were applied as given. Every raw idea started from a concrete operator's pain (Q1), not from a technology.

**How the evidence was gathered, and its limits (read first):**
- I ran searches in German, English, Finnish, Swedish and Spanish through a web-search tool. That tool returns search-engine extracts of the pages it finds.
- Direct page fetching was blocked by the network proxy for almost every domain. Examples: lobbyregister.bundestag.de, softguide.de, topagrar.com, gesetze-im-internet.de, nzz.ch, einfachstweg.ch, nabisy-software.de and biotaktix.de.
- So each fact below comes from the search extract of the cited URL, not from my own reading of the full page. Open the page before relying on any exact number.
- The shared web-search budget ran out before I finished. I could not run several planned checks. They are listed in the Gaps sections.
- Vendor pages and directory listings built from vendor input are labelled **vendor claim**. Evidence from before 2024 is flagged **(older: year)**.
- "Not found" means not found in my local-language searches. It is not proof that something does not exist.

> **Bottom line.** I generated 25 raw candidates. 22 were killed and 3 finalists remain:
> - **(A)** An audit-ready substrate and EEG-bonus evidence log for German biogas plants. **66.5 (TEST)**.
> - **(B)** Parent-duty rosters, an hours ledger and a board handover tool for German parent-run daycares (Elterninitiativen). **65.0 (TEST)**.
> - **(C)** Self-administration for small Swiss condominium communities (STWEG): QR-bills, bank matching and annual accounts. **61.0 (TEST, marginal)**.
>
> I scored the BASELINE at **55.0**. All three beat it on my scoring, but only by 6–11.5 points, and none reaches BUILD (75 or more).
>
> **The main finding of this lens:** the "absent software" premise rarely holds. Almost every niche I checked in Germany, Switzerland or the Nordics with 5,000 or more operators already has three or more small vertical vendors. That includes allotment associations, hunting co-operatives, childminders, Finnish private-road associations and German self-managed condominium owners' associations (WEGs). The survivors are a niche-within-a-niche (B), a compliance diary that is only now going digital (A), and a market next door to a crowded one (C).

---

## (1) KILL LOG

### Takeaway
I applied H8 literally: an idea is killed only if 3 or more **funded or clearly profitable** competitors sell the same thing at a similar price. Read that way, most niches were not killed by H8 alone. They died earlier, at one of three points:
- **Q4 ("already solved").** The trade associations that would be the cheap channel already sell their own tool (Jagdgenossenschaften), or cheap tools are already widespread (Finnish road associations).
- **Q5.** Free or €3–5/month price anchors push the number of customers needed above a realistic share of the pool (allotment associations, childminders).
- **H3/H4.** The rails are controlled by others: health-IT (TI) billing, chimney-sweep data standards, free regional-government apps in Spain, and a free tool bundled by an insurer for UK leasehold blocks.

### Kill log — one line per raw candidate

| # | Raw candidate (Q1 person and moment → app) | Killed by | Why (evidence) |
|---|---|---|---|
| 1 | Volunteer chair of one of Germany's ~40,000 hunting co-operatives (Jagdgenossenschaften), who must keep the land/owner register (Jagdkataster) and pay each landowner's share of lease income every year → cloud cadastre + payout + meeting app (DE) | **Q4** (solved; channel held by incumbents) + H8 risk | **Pool:** ~40,000 co-operatives and >4 million landowners ([BAGJE statement, 2026](https://www.lobbyregister.bundestag.de/media/23/6e/698363/Stellungnahme-Gutachten-SG2602240021.pdf)).<br>**Incumbents:**<br>• GIS mbH "Jagdpachtverwaltung": used in >1,000 co-operatives, base module €650 (vendor claim, [flyer 09/2025](https://www.bwv-net.de/wp-content/uploads/2026/02/Jagdpachtverwaltung-Flyer_2025-09.pdf)).<br>• The Lower Saxony association ZJEN sells its own PC program: €160–650 one-time plus €38/€58 a year ([ZJEN](https://www.zjen.de/pc-programm-jagdkataster-22-mit-digitaler-karte-gis/)).<br>• The Bavarian farmers' association runs a web service with a payout helper ([BBV](https://www.bayerischerbauernverband.de/jagdkataster)).<br>• Also: [jagdkataster.net](https://www.jagdkataster.net/index.html), [Gaja®Matrix](https://geoinformationssystem.net/jagdkataster/) and [Bauernverband MV](https://www.bauernverband-mv.de/jagdpachtverwaltung-am-pc/).<br>**Public services:** NRW districts offer a cadastre service ([RBK](https://www.rbk-direkt.de/geoportal/beschreibung-kooperationsprojekt-jagdkataster.pdfx)), and the Bavarian survey office produces the cadastre as a CSV file ([LDBV](https://bayernlabs.bayern.de/mam/ldbv/dateien/dfb_jagdkataster_csv_nicht_barrierefrei.pdf)).<br>**Conclusion:** the associations that would be the cheap channel sell competing tools. Price anchors are €38–58 a year. I found no complaints. |
| 2 | Volunteer treasurer of one of 13,155 allotment associations (871,226 plots), who once a year bills each plot for lease, meter-read water and electricity, levies and missed work hours → billing app (DE) | **Q5** (customers needed vs pool) + H8 risk | **Pool:** [BKD report 2023, data as of 03/2024](https://www.lobbyregister.bundestag.de/media/bd/1d/374451/BKD_Geschaeftsbericht_Kassenbericht_2023.pdf).<br>**Specialised tools already sold:**<br>• Laubenmeister: waiting list, meter readings and year-end billing prep, "permanently free" (vendor claim, [features](https://www.laubenmeister.de/features)).<br>• Clubcopilot: €3/month for a 90-plot club; per-plot meter billing is still "on the roadmap" (vendor claim, [Clubcopilot](https://clubcopilot.de/kleingartenverein/)).<br>• Also: [KleingartenAssist](https://kleingartenassist.com/) (SEPA pain.008 export), [Kleingartenverein24](https://kleingartenverein24.de/), [MeinTopVerwalter](https://www.pc-kleingaertner.de/) ("400+ clubs", vendor claim) and [SEWOBE](https://www.sewobe.de/spezialloesungen/kleingartenvereine/).<br>**Arithmetic:** at €10/month you would need ~1,190 clubs (9% of the pool) for €8k profit. At the €3 anchor you would need most of the pool. |
| 3 | Self-employed childminder (Tagespflegeperson) doing monthly attendance, parent extras and tax paperwork → admin app (DE) | **Q5** + H8 risk | **Tools already sold:** KTP Digital Plus at €4.99/month or €49.99/year (vendor claim, [KTP Digital](https://ktp-digital.de/)), [TagespflegeDigital](https://www.tagespflegedigital.eu/tagesmutter-app-verwaltung) and [KitaPflege TPP](https://www.mm-soft.de/KitaPflegeTPP.html).<br>**Shrinking pool:** publicly funded childminders fell ~11% from 2020 to 2024, and children in their care fell from 173,988 to 160,539 ([Bildungsserver](https://www.bildungsserver.de/Kindertagespflege-2463-de.html)).<br>**Arithmetic:** at a ~€5 anchor you need ~2,400 paying carers (~6% of an assumed ~40k). |
| 4 | Boarding-stable owner billing boarders monthly for extras → billing app (DE) | **Q3/Q5** (free incumbent) — *weakest kill* | **Free incumbent:** Stabley is listed as covering occupancy, boarder communication **and billing**, and as free for stables (directory listing, [AlternativeTo](https://alternativeto.net/software/stabley/about/)).<br>**Other apps:** [Stall Manager](https://apps.apple.com/de/app/stall-manager/id6751195329), [StallZeit](https://apps.apple.com/de/app/stallzeit/id6757603739), and Die Pferde App and EquineM ([CB Insights](https://www.cbinsights.com/compare/die-pferde-app-vs-equinem)).<br>**Caveat:** I did not verify how deep Stabley's billing goes. If it is shallow, revisit this idea. |
| 5 | Small provider of everyday support for people with a care grade, billing the care insurers monthly for the €131/month relief amount (§45b SGB XI) → billing app (DE) | **H3** (health-IT certification risk) | **Moving to TI:** Bavarian guidance (05/2026) describes fully electronic billing via the TI/KIM network with electronic proof of service, which needs TI-capable software ([LfP Bayern](https://www.lfp.bayern.de/wp-content/uploads/2026/05/Praxiseinblick_Vorbereitung_vollelektronische_Abrechnung.pdf)).<br>**Today's rails:** an IK identifier plus self-billing or a billing centre ([AOK BW](https://www.aok.de/gp/fileadmin/user_upload/Pflege/Abrechnung/bw_dta_abrechnungsleitfaden.pdf)).<br>**Incumbent:** [komda](https://komda-software.de/produkte/software-betreuungsdienste/).<br>**Caveat:** it is not confirmed that these support-only providers (not licensed care services) must use TI. That is a risk, not a certainty. |
| 6 | Provider of school escorts or ambulatory youth-welfare services billing hours to youth offices → billing app (DE) | **H8** | At least ten established vendors already sell this exact workflow: [MediFox DAN](https://www.medifoxdan.de/software-jugendhilfe/loesungen/ambulante-traeger-und-schulbegleitung), [Kilanka](https://www.kilanka.de/software/schulbegleitung/), [Tau-Office/rocom](https://www.rocom.de/sozial/schulbegleitung-software/), [LAP](https://www.lap-jugendhilfe.de/software-schulbegleiter-und-schulbegleitung/), [Connext](https://connext.de/einsatzfelder/jugendhilfe/ambulante-betreuung.aspx), [i-SOFT](https://www.i-soft.de/jugendhilfe), [SODISYS](https://www.sodisys.de/target/software-fuer-ambulante-kinder-und-jugendhilfe/), [KoJu24](https://koju24.de/software-schulbegleitung/), [Just Manage IT](https://justmanageit.de/) and [acoma](https://schulbegleitung.online/). |
| 7 | Self-employed professional legal guardian (Berufsbetreuer) doing annual accounts and fee claims to the court → practice app (DE) | **Q3** (solved) | **Existing products:** LOGO Datensysteme "BdB at work" ([BdB ebook, older: 2013](https://download.betreuung.de/ebook/BdB_at_work_2013_Fallsteuerung_(eBook).pdf)). A tender reply suggests C&S KlientenManager ([SoftGuide tender](https://www.softguide.de/ausschreibungen/angehender-berufsbetreuer-sucht-software-zur-rechtsbetreuung)).<br>**Buyers are choosing among existing tools** ([SoftGuide tender](https://www.softguide.de/ausschreibungen/software-der-nachweisfuehrung-zur-verwaltung-des-vermoegens-gesucht)).<br>**Not checked:** other known vendors (BtPrax, Butler) were not verified. |
| 8 | Volunteer owner running a small self-managed owners' association (WEG) → annual accounts and resolution register (DE) | **H8** | **Long-established tools at similar prices, several explicitly for self-managers:**<br>• Win-CASA: from €398, explicitly for self-managing WEGs (vendor claim via [softwareabc24](https://www.softwareabc24.de/vergleiche/intex-hausverwaltung-vs-win-casa)).<br>• INtex, Karthago, VS3 ([softwareabc24](https://www.softwareabc24.de/vergleiche/karthago-vs-win-casa)).<br>• Immoware24 WEG module ([manual 2025](https://www.immoware24.de/wp-content/uploads/2025/01/11_AbrechnungWEG-Verwaltung.pdf)).<br>• Aareon Hausverwaltung plus 2026 ([connect-professional](https://www.connect-professional.de/filedownload/documents/900635/aareon-hausverwaltung-plus-2026-tabelle-mit-punktverteilung.pdf)). |
| 9 | Lay manager of one of Finland's ~53,000–60,000 private-road associations (tiekunnat), billing road units yearly → admin app (FI) | **Q4** (solved) | **Pool:** ~60,000 in a 2026 statement ([hankeikkuna](https://api.hankeikkuna.fi/asiakirjat/df500404-bf0f-4be0-b16d-486244c13c9c/de6b3b41-b6e8-47af-b438-15ef21ba3e82/LAUSUNTO_20260312200852.PDF)); ~53,000 in the 2017 government bill ([Edilex](https://www.edilex.fi/he/20170147)).<br>**Already served:**<br>• Tiehoitokunta.fi: €4.99/month (1–9 shareholders) or €14.99/month (vendor claim, [pricing](https://tiehoitokunta.fi/hinnasto/)).<br>• Matriset NetWintie/Wintie: "thousands of road associations" over 25–30 years (vendor claim, [Matriset](https://matriset.fi/)).<br>• Also [Tiekarhu](https://tiekarhu.fi/) and [Helppo Käyttää](https://www.helppokayttaa.fi/). |
| 10 | Board of a Swedish joint-facility or road association (samfällighetsförening) producing the yearly fee roll by share numbers → admin app (SE) | **Q3** (served) + Q5 (pool not sizable) | **Already served:** Boappa is called "Sweden's largest app" for housing co-ops and joint-facility associations ([Hemnet, older: 2022](https://www.hemnet.se/artiklar/guider/2022/05/06/slipp-brf-nytt-pa-hallgolvet)). Sharely sells an asset register, fee roll and accounting integration (vendor claim, [Spiris](https://www.spiris.se/integrationer/partner/sharely)).<br>**Pool:** I found no national count of associations. |
| 11 | Manager of a Spanish hunting estate/society (coto de caza) handling members, quotas and catch reports → admin app (ES) | **H4** | Regional governments run free official systems: Castilla y León's CAPTURCYL app plus a web panel for estate holders (hunters, quotas, dates) ([Agronews CyL](https://www.agronewscastillayleon.com/junta-precinto-digital-caza/); [Orden MAV/258/2025 via CESEFOR](https://redforesta.com/wp-content/uploads/2025/06/repos-caceres/03-Caceres-5jun25.pdf)), and Andalucía's digital-tag panel ([Junta de Andalucía](https://www.juntadeandalucia.es/medioambiente/portal/documents/d/global/andalucia_-manual-precinto-digital-para-titulares-de-cotos-pdf)). |
| 12 | Secretary of a Spanish irrigation community (comunidad de regantes) billing per hectare and rotating watering turns → admin app (ES) | **Q3** (gap unproven) + H2 risk | Industry presentations show existing tools and projects ([MAPA telecontrol](https://mapa.gob.es/images/ca/ponencia-4-telecontrol_tcm34-648096.pdf); [CITA, older: 2018](https://citarea.cita-aragon.es/bitstream/10532/5330/2/GCP2018003700presentacion.pdf)). I could not size the pool or find prices. Telemetry hardware is often part of the solution. |
| 13 | Volunteer director of a UK self-managed block (RMC/RTM) running Section 20 major-works consultations → compliance app (UK) | **H4** + H8 risk | **Insurer-bundled free tool:** Manage Your Block is free to Residentsline insurance customers and £99/year for others (vendor claim, [Manage Your Block](https://manageyourblock.co.uk/?p=2275)).<br>**Others:** S20 Planner £99 ([Payhip](https://payhip.com/b/h239a)); Blockman from £195/month and Landlord Vision ([Landlord Vision blog](https://www.landlordvision.co.uk/blog/best-block-management-software-uk-market/)). |
| 14 | Owner of a German driving school → school management app (DE) | **H8** | AUTOVIO raised more than €3M ([Startbase, older: 2022](https://www.startbase.de/news/autovio-schliesst-finanzierungsrunde-ab/)). ClickClickDrive raised $1M ([Tech.eu, older: 2018](https://tech.eu/2018/11/14/belgian-founded-startup-clickclickdrive-raises-1-million-for-its-driving-school-management-software)). Fahrschulcockpit charges up to 1% of student payments ([KI-Syndikat review](https://www.ki-syndikat.de/tools/fahrschulcockpit/)). |
| 15 | Small German funeral director → case and document management app (DE) | **Q3** (solved) | Cloud BestattungONE from €89 ([GetApp](https://www.getapp.de/software/2100087/bestattungone)). Directories list many funeral-home tools ([Capterra DE](https://www.capterra.com.de/directory/30565/funeral-home/deployment-options/windows/software)). I found no evidence that operators still suffer. |
| 16 | District chimney sweep keeping the legally required electronic sweep book (Kehrbuch) → cloud sweep-book (DE) | **H4** (data standard controlled by the trade body) | The electronic sweep book is mandatory and must be handed over machine-readably ([§19 SchfHwG](https://gesetze.legal/bund/schfhwg/19)). Baden-Württemberg sets minimum software requirements ([VwV BW](https://umwelt-online.de/recht/luft/laender/bw/vwvschornstf.htm)). Mecklenburg-Vorpommern requires the federal association's interface ([MV directive](https://www.nordwestmecklenburg.de/datei/anzeigen/id/10350,1105/richtlinie_ueber_die_fuehrung_vorlage_und_pruefung_von_kehrbuechern.pdf)). Incumbents include digibase connect and HERO ([softwareabc24](https://www.softwareabc24.de/schornsteinfeger-software/saas)). |
| 17 | Volunteer board of a small foundation preparing the yearly report to the state supervisor and charity-law use-of-funds proof → compliance app (DE; 26,349 foundations in 2024) | **Q1** (pain too weak) | **Pool:** 26,349 (2024) and 27,082 (2025) ([BVDS datasheet](https://www.stiftungen.org/fileadmin/stiftungen_org/Stiftungen/Zahlen-Daten/2025/Datenblatt_Niedersachsen_2025.pdf)).<br>**Low burden:** the supervisor accepts a short table ([Bezirksregierung Detmold FAQ](https://www.bezreg-detmold.nrw.de/system/files/media/document/file/2.21_stiftungen-haeufig-gestellte-fragen-und-antworten.doc)).<br>**No forcing event:** the central foundation register is postponed to 2028 ([IHK Dresden](https://www.ihk.de/dresden/servicenavigation/presse-publikationen/meldungen/einfuehrung-eines-zentralen-stiftungsregisters-verspaetet-sich-6799258); [FGS](https://www.fgs.de/news-and-insights/blog/detail/das-neue-stiftungsregister-ist-nicht-mehr-weit-was-gemeinnuetzige-stiftungen-jetzt-und-in-zukunft-beachten-muessen)).<br>**Vendor exists:** [onlinebilanz.de](https://onlinebilanz.de/stiftung/). |
| 18 | Sport shooter who must prove regular training to keep a firearms permit, and the club officer who confirms it → club-verified digital shooting log (DE; ~14,000 clubs, 1.34M members) | **H4** (gatekeeper acceptance) + C9 | **Rule:** proof is a certificate from the shooting-sport federation. "Regular" means once a month or 18 times in 12 months ([§14 WaffG](https://lxgesetze.de/waffg/14)).<br>**Acceptance unknown:** I found no guidance that authorities accept app logs, so the value depends on each federation and authority accepting them.<br>**Apps already exist:** [SchiessLog](https://apps.apple.com/th/app/schiesslog/id6751775923) and [ShootingProof](https://apps.apple.com/bo/app/shootingproof/id6447617371).<br>**Pool:** [DSB, end-2023](https://www.dsb.de/fileadmin/DSB.DE/MIX/MIX_2024/Stiller_Star_03-2024.pdf).<br>Reputational exposure as well. |
| 19 | Certified maintenance firm for small private sewage plants (Kleinkläranlagen) sending protocols to owners and water authorities → field app (DE) | **Pool rule unverified** + Q3 | DiWa has been evaluated as a possible standard tool ([DBU report, older: 2018](https://opac.dbu.de/ab/DBU-Abschlussbericht-AZ-33290-01.pdf)), and DiWapp exists. Certified firms must meet DWA rules ([Ammerland](https://www.ammerland.de/media/custom/2843_2653_1.PDF)). I could not find the number of firms (likely below 5,000). |
| 20 | Volunteer head of a water-and-soil association (Wasser- und Bodenverband) assessing landowner levies → levy app (DE) | **Q5/Q7** (payer often municipal; cannot size) | Levies are often passed through municipalities ([KAG NRW §7 via Haufe](https://www.haufe.de/id/norm/kommunalabgabengesetz-nordrhein-westfalen-7-gebuehren-fuer-beitraege-und-umlagen-der-wasser-und-bodenverbaende-und-zweckverbaende-HI1308275_p7.html); [Uelzen report 2025](https://www.landkreis-osnabrueck.de/sites/default/files/2025-08/kreisverband-der-wub-uelzen-erfahrungsbericht-aus-der-praxis.pdf)). Billing software exists ([Igel Wassergeld](https://www.softguide.de/programm/igel-wassergeld)). I found no national count. |
| 21 | Volunteer treasurer of a German sports club → club admin app (DE) | **H8** (partial evidence) | ClubDesk is free for clubs up to 200 members ([netzwelt](https://www.netzwelt.de/download/25272-clubdesk.html)). Forum users point to vereinsplaner and campai ([administrator.de](https://administrator.de/forum/sql-csv-fotoverwaltung-abrechnungsdaten-678402.html)). A widely crowded category; I did not research it further. |
| 22 | Small therapy practice, e.g. a Heilpraktiker (licensed non-physician health practitioner) → practice app (DE) | **H3** (rule-based; not researched) | Any practice tool that holds clinical notes is a medical record system. A billing-only version would fall into generic invoicing. |
| 23 | **Biogas plant operator** keeping the daily substrate diary for the yearly EEG-bonus audit | **SURVIVED → Finalist A** | See card A. |
| 24 | **Parent board of a parent-run daycare (Elterninitiative)** coordinating parent duties | **SURVIVED → Finalist B** | See card B. |
| 25 | **Volunteer owner running a small Swiss condominium community (STWEG)** | **SURVIVED → Finalist C** | See card C. |

### Inferences
- **Where the overlooked niches are:** in DACH, small vertical vendors (often 1–10 people) have long since entered the organisation niches the brief points to: allotments, hunting co-operatives, road associations, childminders and condominium owners. Several niches have a **trade association selling its own tool** (ZJEN, BBV). That kills the "cheap channel" logic of this lens. The channel exists, but it is owned by a competitor.
- **Price anchors are the real killer** for volunteer organisations. Free, €3/month and €5/month tools make €8k/month profit require 6–70% of the pool.
- **What survived:**
  - a **sub-workflow** that generic vertical tools ignore: parent duties in parent-run daycares;
  - a **B2B compliance diary** that is only now going digital: biogas;
  - a **neighbouring jurisdiction** where the equivalent of a crowded German market is still young: Swiss condominium communities versus German WEGs.

### Gaps
- **Funding and profitability of small vendors** (Nabisy Software, TerraVis, Biotaktix, EinfachSTWEG, LIMMOBI and others) could not be checked. My H8 "pass" calls rest on absence of evidence.
- **Operator complaints.** Facebook, Reddit and app-review complaint mining was not possible because those pages could not be fetched. Complaint evidence is thin. It is limited to:
  - forum threads on allotment meter billing ([finanzfrage.net](https://www.finanzfrage.net/frage/muessen-stromverluste-4500kwhjahr-bei-20-pachtgaerten-im-kleingartenverein-von-den-parzellenpaechtern-ausgeglichen-werden); [DATEV community, older: 2019](https://www.datev-community.de/t5/Betriebliches-Rechnungswesen/Buchhaltungssoftware-Verein/m-p/110010));
  - one topagrar piece on biogas bureaucracy;
  - one NZZ piece on small condominium communities.
- **Not researched because the search budget ran out:** beekeepers, volunteer fire brigades, music associations, village halls (UK), parish councils (UK), US niches.

---

## (2) FINALIST IDEA CARDS

### Finalist A — "Substrat-Tagebuch": an audit-ready substrate and EEG-bonus evidence log for German biogas plants

**Hard-rule check:** H1 pass (deterministic ledger and rules; no OCR). H2 pass (web app plus CSV import; no hardware). H3 pass (no licence; the environmental verifier stays the certifying party). H4 pass (no single gatekeeper; risk from plant-control vendors is noted in Q10). H5 pass (the operator pays). H6 pass. H7 pass. **H8: pass on available evidence only.** Three small specialised vendors exist, but none was shown to be funded or clearly profitable, and their prices are not public.

**Q1 — Who suffers, when, how often, at what cost?**
- **Who:** the operator of one of Germany's **9,605 biogas plants**, usually a farm business. The count is end-2025: 9,315 on-site combined heat-and-power plants plus 290 biomethane plants ([topagrar, FvB/Fraunhofer IEE census, 03/2026](https://www.topagrar.com/energie/news/biogasbranche-2025-neue-zahlen-zeigen-grosses-potenzial-politik-bremst-ausbau-a-20023918.html)). [EnBW](https://www.enbw.com/unternehmen/themen/klimaschutz/biogas.html) also cites 9,315 and [ZfK](https://www.zfk.de/energie/waermewende/so-gelingt-der-biomethan-hochlauf-wenn-berlin-die-bremsen-loest) cites ~9,600.
- **When and how often:** every day, when substrates are fed. Then once a year, by **28 February**, the substrate diary (Einsatzstofftagebuch) must reach the grid operator (EEG 2009 §27(3), per a verifier's presentation ([WEMAG/Kremp](https://www.wemag.com/sites/default/files/4_kremp_ug_im_eeg_2017_wemag_2019.pdf); [WEMAG/Kremp 2](https://www.wemag.com/sites/default/files/5_Kremp_Was%20ist%20aus%20Sicht%20des%20Umweltgutachters%20zu%20beachten.pdf), older: 2019)).
- **What is at stake:** "once the conditions are no longer met, the bonus claim lapses permanently" (EEG 2009 Annex 2 VII(2), same source).
- **Proof required:** grid operators' forms accept "substrate diary **or** environmental verifier's report" as proof for bonuses ([SWK EEG 2012 form](https://cdn.swk.de/assets/download/Konformitätserklärung%20Bio%20EEG%202012.pdf); [EWE Netz](https://www.ewe-netz.de/-/media/ewe-netz/downloads/konformitaetserklaerung/konfo_neu/erklrung-der-konformitt-zum-eeg-ibn-bis-2011-eeg-2009.pdf)). The verifier compares delivery receipts with the diary entries ([UGA guideline](https://www.emas.de/fileadmin/user_upload/4-pub/UGA-Aufgaben-LL_EEG.pdf)).
- **Cost:** one operator told topagrar that the yearly expert report for bonus calculations rose from ~€1,500 (2006) to ~€15,000 now, plus €2,500 per formaldehyde measurement ([topagrar, "Biogas im Würgegriff der Bürokratie"](https://www.topagrar.com/betriebsleitung/news/biogas-im-wuergegriff-der-buerokratie-b-20001963.html); anecdote, one plant). A trade outlet reports that documentation duties have "risen considerably" ([IKZ](https://www.ikz.de/detail/news/detail/nachweispflicht-fuer-energiewirte-anforderungen-bei-der-dokumentationspflicht-erheblich-gestiegen/); date not visible).
- **In one sentence:** *"A farmer who runs a biogas plant must log every tonne of maize and manure he feeds it, and if that log doesn't match his delivery slips at the yearly audit, he can lose bonus payments for good."*

**Q2 — The one thing the app does.**
It is a tablet-friendly web app:
- The operator logs substrate deliveries (weighbridge tickets typed in or imported as CSV) and daily feeding (typed in, or imported as CSV from the feeding controller).
- The app keeps a running stock and mass balance and flags deviations.
- One button produces the **verifier and grid-operator pack**: a diary in the format for that plant's EEG version, a check on the maximum maize/grain share, and digestate outflows.
- Deterministic rules only. No OCR or AI (the competitor Nabisy uses OCR; this product deliberately does not).

**Q3 — Who already solves it?** Searched in German. The workflow depends on German EEG law, so non-German tools do not apply.

| Name | Country | Price | What it does | Gap |
|---|---|---|---|---|
| Excel/LibreOffice templates ([NQ Anlagentechnik](https://www.nq-anlagentechnik.de/downloads/); verifiers such as [PBNE](https://pbne.de/gutachten/)) | DE | Free | Diary templates by substrate mix | Manual; no stock reconciliation or audit trail (inference) |
| BOGIS ([App Store](https://apps.apple.com/mx/app/bogis/id998939173); [blog, older: 2014](https://biogasbogis.wordpress.com/2014/07/16/16-07-2014-biogas-erfassung-der-futterung-btb/)) | DE | Free app | Feeding diary, maintenance plans | No sign of a current EEG audit pack (unverified) |
| Nabisy Software ([site](https://nabisy-software.de/biogasanlagen-betreiber); [blog 2026](https://nabisy-software.de/blog/massenbilanzierung-biogasanlage-anleitung)) | DE | Not found | Mass balance, OCR of weighbridge tickets, alert at >5% input/output deviation, works with the federal agency's Nabisy portal (vendor claim) | Uses OCR (excluded by H1 for us); focus on sustainability/Nabisy; price unknown |
| TerraVis DokuManager Biomasse ([TerraVis](https://www.terravis-biogas.de/dienstleistungen/gocero2/digitale-massenbilanzierung)) | DE | Not found; 90-day trial | Web app from feeding diary to mass balance (vendor claim) | Page appears ~592 days old (may be stale) |
| Biotaktix ([site](https://www.biotaktix.de/en/)) | DE | Not found | Weighbridge tickets sent from the scale over LTE, RED III sustainability proofs, maintenance, feeding log, delivery manager (vendor claim) | Needs a hardware link; price unknown |
| Environmental verifiers (e.g. [Normec](https://certification.normecgroup.com/environmental-reports-for-biogas-plants-in-accordance-with-the-eeg)) | DE | ~€15,000/yr (one anecdote) | Certify EEG compliance | A service, not a tool. They are partners, not rivals |
| Free calculators ([LfL Biogas-Rechner](https://www.lfl.bayern.de/biogasrechner); KTBL substrate calculator via [agrarheute](https://www.agrarheute.com/energie/biogas-tool-hilft-landwirten-substratspektrum-erweitern-622497)) | DE | Free | Gas yield and feeding plans | Not diaries |

**What operators use and pay today:** Excel templates plus verifier fees. One anecdote puts verifier fees at ~€15,000 a year. I found no published price for any of the three software vendors.

**Q4 — Why do people still suffer? Root cause:**
- **Primary (b), regulatory fragmentation.** Bonus rules differ by EEG version (2004, 2009, 2012 and later), and verifier practice is German-only.
- **Primary (a), too small for funded SaaS.** At most ~9,600 plants.
- **Contributing (e), unglamorous.**
- **Partly (d), rising documentation load.** Examples are RED III sustainability proofs (vendor claim, Biotaktix) and the IKZ report.

The niche is only now going digital: three small vendors are visible in 2024–2026. That confirms demand, but it also means the window is closing.

**Q5 — Is it profitable?**

| Item | Value | Status |
|---|---|---|
| Price | €790 per plant per year (≈€66/month) | ASSUMPTION |
| Cost per customer | €10/month (hosting €2, backups/e-mail €1, payment fees ~€1, support time ~€6) | ASSUMPTION |
| Gross margin | ≈85% | Derived from assumptions |
| Fixed business costs | €2,000/month (professional liability insurance, accounting, tools, travel to regional meetings, marketing) | ASSUMPTION |
| Customers needed for €8k/month profit | (8,000 + 2,000) / (66 − 10) ≈ **180 plants** | Derived |
| Reachable pool | 9,605 plants (end-2025) | VERIFIED ([topagrar/FvB](https://www.topagrar.com/energie/news/biogasbranche-2025-neue-zahlen-zeigen-grosses-potenzial-politik-bremst-ausbau-a-20023918.html)) |
| Share of pool needed | ≈1.9% | Derived |
| Average plant size | ~356 kW rated output (3,316 MW ÷ 9,315 plants) and ~3.1 GWh of electricity a year (29 TWh ÷ 9,315 plants) | VERIFIED inputs ([topagrar/FvB](https://www.topagrar.com/energie/news/biogasbranche-2025-neue-zahlen-zeigen-grosses-potenzial-politik-bremst-ausbau-a-20023918.html)); division derived |
| Current spend on proof | ~€15,000/yr for the bonus expert report at one plant | VERIFIED as an anecdote ([topagrar](https://www.topagrar.com/betriebsleitung/news/biogas-im-wuergegriff-der-buerokratie-b-20001963.html)) |
| Customer acquisition cost (CAC) | €400 (verifier referrals plus regional meetings) | ASSUMPTION |
| Churn | 1%/month (2%/month in the stress case) | ASSUMPTION |
| Lifetime value (gross margin basis) | €56 × 100 months ≈ €5,600 (≈€2,800 in the stress case) | Derived |
| LTV/CAC | ≈14 (≈7 in the stress case) | Derived; optimistic |

**Q6 — How to build it.** Stack: a TypeScript or Rails web app (PWA, works offline on a tablet), Postgres, server-side PDF/XLSX generation, EU hosting, and SEPA direct debit through a licensed payment service provider (PSP). No licensed rails are needed.

12-week outline:
- **Weeks 1–2:** interview 5 operators and 3 verifiers; collect real diaries and verifier checklists. Data model: plant, EEG version, substrate catalogue with categories, suppliers, deliveries, feedings, stock, outputs.
- **Weeks 3–4:** delivery and feeding entry forms; CSV import for 2 common feeding-controller exports; duplicate checks.
- **Weeks 5–6:** stock and mass-balance engine (opening stock + deliveries − feedings − losses ± corrections); deviation alerts; maize/grain share monitor with thresholds set per EEG version.
- **Weeks 7–8:** annual pack (PDF + XLSX) mirroring verifier checklists; entries that cannot be overwritten (corrections are logged); read-only verifier link.
- **Week 9:** digestate outflow log and delivery-note export.
- **Week 10:** importer for last year's Excel; onboarding wizard; billing.
- **Weeks 11–12:** paid pilot with 3–5 plants and 2 verifiers; fixes; public launch before the Q4 run-up to the 28 February deadline.

**Q7 — Where to launch first, and why.**
- **Launch market: Germany.** It has ~9,600 plants, and the EEG diary and verifier regime is German-specific (sources above).
- **Where operators gather (cheap channels):**
  - **Fachverband Biogas (FvB):** it describes itself as Germany's and Europe's largest biogas body and aims to build an advisory network of members across regions ([FvB statement to the NRW parliament](https://opal.landtag.nrw.de/portal/WWW/dokumentenarchiv/Dokument/MMST18-161.pdf)).
  - **Environmental verifiers:** they already compare receipts with diaries and would gain from cleaner input ([UGA guideline](https://www.emas.de/fileadmin/user_upload/4-pub/UGA-Aufgaben-LL_EEG.pdf)).
  - **Trade press:** topagrar covers biogas bureaucracy.
- **First 10 paying customers:**
  1. List 15–20 verifiers active in biogas (public EEG-verifier directories; ASSUMPTION that these lists are usable). Offer each a free reviewer portal and co-designed export format.
  2. Ask each verifier for 2–3 introductions to plants that send messy diaries.
  3. Offer a founding price (€390 for the first year, prepaid) and import last year's Excel for free.
  4. Attend 2 FvB regional meetings (cost ASSUMPTION: under €500).
  5. Target: 10 prepaid plants before 31 January.

**Q8 — How it makes money.** An annual subscription per plant (€790) with a 20% discount from the second plant. The operating company pays (often a GmbH & Co. KG or the farm), by SEPA direct debit or invoice. Verifiers get free read access, which is the referral engine.

**Q9 — How one person runs it.**
- **Support load:** low most of the year, with a spike in January–February. Pre-built import mappings and an in-app checklist keep it down.
- **Legal maintenance:** once a year, check the EEG rules table and update thresholds when the law changes.
- **Data safety:** daily backups; corrections are logged rather than overwriting entries.
- **Failure modes:** unmapped substrate names in CSV imports; operators forgetting daily entries (fix: weekly summary e-mail); disputes over who is liable (fix: terms making clear the verifier certifies and the app only records).

**Q10 — What did I miss? Kill tests.**
- **Platform kill:** plant-control or feeding-controller vendors could add EEG export packs. This is plausible but fragmented by manufacturer. Mitigate with vendor-neutral imports.
- **Incumbent copy:** three young competitors are already in the space. The differentiation (no hardware, no OCR, verifier co-designed exports) is copyable. **This is the largest risk.**
- **Liability:** a wrong pack could cost an operator a bonus. Mitigate with terms, verifier review and professional liability insurance (in the fixed costs).
- **False assumptions:** operators may be content with Excel plus the verifier, and willingness to pay €790 is unproven. Test it with 10 prepaid founding customers within 90 days.
- **Churn:** plants leave as their 20-year EEG terms end (inference; not quantified). Some move to tenders that still need evidence (unverified).
- **Seasonality:** sales and usage peak before 28 February. Plan the cash flow for it.

---

### Finalist B — "Elterndienst-Planer": parent-duty rosters, an hours ledger and board handover for parent-run daycares (Elterninitiativen)

**Hard-rule check:** H1 pass. H2 pass. H3 pass. H4 pass (no dominant incumbent; generic daycare apps could copy it, see Q10). H5 pass (the association pays from its budget). H6 pass (no child data needed; parents consent). H7 pass. H8 pass (I found no product that sells this workflow).

**Q1 — Who suffers, when, how often, at what cost?**
- **Who:** the volunteer parent board (Vorstand) of a parent-run daycare association. Germany has about 5,000 such facilities according to the national umbrella body BAGE ([lobby register entry](https://www.lobbyregister.bundestag.de/suche/R003613)), or more than 7,500 according to [Bildungsserver](https://www.bildungsserver.de/seite_de.php?seite=3362) (undated). The sources conflict. BAGE groups 29 umbrella and advisory organisations ([BAGE statement 2026](https://www.lobbyregister.bundestag.de/media/c5/04/830045/Stellungnahme-Gutachten-SG2608120005.pdf)).
- **When and how often:**
  - **Every week**, cleaning, cooking, laundry, repair and emergency-cover duties must be assigned and chased.
  - **Every month or year**, each family's owed and served duty hours, and any compensation payments, must be reconciled under the association's own rules.
  - **At every board change**, know-how leaves with the departing parents.
- **City-specific funding rules add admin work.** Munich's model caps parent fees and reimburses the difference through a city procedure ([Munich EKI-Plus](https://stadt.muenchen.de/service/info/erstattung-von-entgeltermassigung-nach-ekiplus/10315711/); [guideline as of 01/2026](https://www.muenchen-transparent.de/dokumente/9178772/datei)).
- **Cost:** unpaid evening hours, conflict between families, and gaps in staff cover. The specific hours and penalty amounts are an **ASSUMPTION**; I found no source.
- **In one sentence:** *"In a daycare run by its parents, two volunteer parents spend their evenings working out who cleans, cooks or covers for a sick teacher this week and which families still owe hours."*

**Q2 — The one thing the app does.**
A duty roster and hours ledger for parent-run daycares:
- Families sign up for and swap shifts, and get reminders.
- A rules engine keeps a monthly ledger of owed versus served hours, following the association's own quota, carry-over, exemption and €-per-missed-hour rules.
- An emergency-cover call-out cascades by push or SMS.
- A board handover vault holds role checklists, a calendar and documents.

**Q3 — Who already solves it?** Searched in German. No product that sells this workflow was found.

| Name | Country | Price | What it does | Gap |
|---|---|---|---|---|
| Kindy ([App Store](https://apps.apple.com/us/app/id1424121474)) | DE | Not found | Parent communication, dates, absence reports | No duty rosters or board admin |
| Kita-Manager, Kirchhoff ([SoftGuide](https://www.softguide.de/programm/kita-manager)) | DE | Not found | Child admin, attendance, automated fee billing | No parent-duty planning listed |
| COM.kita ([SoftGuide](https://www.softguide.de/programm/comkita/vorschau)) | DE | Not found | SaaS admin and billing; "Dienstplan 2.0" | Staff rostering, not parent duties |
| Kita-Abrechnung ([SoftGuide](https://www.softguide.de/programm/kita-abrechnung)) | DE | €79.90/month + €2.90 per daycare (listing reference 10/2021, older) | Monthly fee billing, master data | No parent duties |
| LiveKid ([pricing page](https://livekid.com/pricing/)) | DE/AT (not verified) | Not read | Billing, parent communication, documentation | No parent-duty economy found |
| DaKS service offer ([guiding principles, older: 2013](https://www.daks-berlin.de/system/files/media/files/leitbild-final.pdf)) | DE (Berlin) | Not found | Advice, training, bookkeeping and HR support for member daycares | A service and potential partner, not software |
| Generic free tools (Doodle, Spond, WhatsApp) | Global | Free | Polls and chat | ASSUMPTION; not researched. Most likely substitute |

**What operators use and pay today:** generic tools plus umbrella-body services. Fees unknown.

**Q4 — Why has nobody solved it? Root cause:**
- **(a) Too small:** about 5,000–7,500 associations.
- **(e) Unglamorous.**
- **(b) Local fragmentation:** each city has its own funding model, e.g. Munich's EKI model.

Daycare-software vendors build for staff-run providers, so the parent-duty economy of parent-run daycares falls between categories.

**Q5 — Is it profitable?**

| Item | Value | Status |
|---|---|---|
| Price | €49 per association per month (up to 50 families) | ASSUMPTION |
| Cost per customer | €7/month (hosting €1, SMS/push €3, payment €1, support €2) | ASSUMPTION |
| Gross margin | ≈86% | Derived |
| Fixed business costs | €1,500/month | ASSUMPTION |
| Customers needed for €8k/month profit | (8,000 + 1,500) / 42 ≈ **227 associations** | Derived |
| Reachable pool | ~5,000 ([BAGE](https://www.lobbyregister.bundestag.de/suche/R003613)) to >7,500 ([Bildungsserver](https://www.bildungsserver.de/seite_de.php?seite=3362)) | VERIFIED; the two sources conflict |
| Share of pool needed | 3.0–4.5% | Derived |
| Price anchor for daycare admin software | €79.90/month + €2.90 per daycare | VERIFIED, older ([SoftGuide, 2021](https://www.softguide.de/programm/kita-abrechnung)) |
| CAC | €150 (umbrella workshops and newsletters) | ASSUMPTION |
| Churn | 1.5%/month (3%/month in the stress case) | ASSUMPTION |
| LTV (gross margin basis) | ≈€2,800 (≈€1,400 in the stress case) | Derived |
| LTV/CAC | ≈19 (≈9 in the stress case) | Derived; optimistic |

**Q6 — How to build it.** Stack: a progressive web app (PWA), Postgres, push notifications, an SMS API, iCal export, and SEPA or card payments through a licensed PSP. No child data is stored.

12-week outline:
- **Weeks 1–2:** interview 10 Berlin boards; collect duty rules and statutes; data model (families, roles, shift types, rules, ledger).
- **Weeks 3–4:** roster templates (cleaning, cooking, laundry, repairs, emergency); sign-up, swap and reminders; iCal feed.
- **Weeks 5–6:** hours-ledger rules engine (quotas, carry-over, exemptions, €-per-missed-hour) and monthly statements with a CSV export for the treasurer.
- **Weeks 7–8:** emergency-cover call-out cascade; availability polls.
- **Weeks 9–10:** board handover vault (role checklists, yearly calendar, documents); German/English interface; GDPR data processing agreement template.
- **Weeks 11–12:** billing and onboarding; paid pilot with 5 associations.

**Q7 — Where to launch first, and why.**
- **Launch market: Germany, Berlin first, then Munich and Hamburg.**
- **Why Berlin:** the Berlin umbrella body DaKS reported "almost 800" small self-managed daycares, after-school groups and free schools ([DaKS press release, older: 2019](https://www.daks-berlin.de/system/files/media/files/PM_Warnstreik_final.pdf)). It runs trainings ([guiding principles, older: 2013](https://www.daks-berlin.de/system/files/media/files/leitbild-final.pdf)) and is still active in 2025 ([Berlin parliament participation](https://pardok.parlament-berlin.de/starweb/adis/citat/VT/19/Lobbyregister/Beteiligungsbeitrag_3105_DaKS.pdf)).
- **Why Munich next:** it has its own funding model for parent-run daycares (EKI), see Q1.
- **Where operators gather (cheap channels):** DaKS trainings and newsletter; BAGE's 29 member organisations; city funding offices that brief boards.
- **First 10 paying customers:**
  1. Offer DaKS a free workshop, "Elterndienste ohne Chaos" (parent duties without chaos), for board members.
  2. Run 20 interviews and offer 5 boards a free setup.
  3. Convert to an annual prepay (€490) after a 30-day trial.
  4. Pay referral credit board-to-board.
  5. Target: 10 paid associations within 90 days, in time for the start of the daycare year in August/September.

**Q8 — How it makes money.** A monthly or annual subscription per association, paid from the association's account by SEPA. No parent-paid tier, which keeps the payer clear.

**Q9 — How one person runs it.**
- **Low support:** parents are mostly digital natives; templates per duty type help; no child data means a low GDPR burden.
- **Failure modes:**
  - SMS delivery failures (fix: fall back to push and e-mail);
  - disputed hour balances (fix: an audit log of who changed what);
  - board turnover (fix: make the app the handover tool, so the new board inherits it).

**Q10 — What did I miss? Kill tests.**
- **Platform or incumbent kill:** daycare apps (Kindy, Kita-Manager, COM.kita) could add parent-duty rosters for free. That is moderately likely, but they target staff-run providers.
- **False assumptions (the largest risk):** whether duty quotas and penalties are common and painful is an **ASSUMPTION**. Kill test: of 20 board interviews, at least 12 confirm weekly duty coordination as a top-3 pain, and at least 5 prepay.
- **Substitutes:** free Doodle, Spond or WhatsApp may be "good enough", which would cap willingness to pay.
- **Churn:** boards change every 1–2 years, but the association persists.
- **Seasonality:** onboarding clusters at the start of the daycare year.
- **Liability:** low.
- **Market drift:** whether the number of parent-run daycares is falling is unknown (see Gaps).

---

### Finalist C — "STWEG selbst verwalten": accounts, QR-bills and meetings for small self-administered Swiss condominium communities

**Hard-rule check:**
- H1 pass. H2 pass. H5 pass (the community pays). H6 pass. H7 pass.
- **H3 pass:** this is software only, and owners pay straight into the community's bank account, so no client money is held. It is an ASSUMPTION that no cantonal fiduciary licence is needed for software; I did not verify it.
- **H4 pass:** banks' free e-banking QR-bill tools overlap only partly; they do no allocation or annual accounts (inference).
- **H8: pass on available evidence only.** EinfachSTWEG sells the same thing at a similar price, but I found no evidence that 3 or more funded or clearly profitable players do.

**Q1 — Who suffers, when, how often, at what cost?**
- **Who:** the volunteer owner who runs a small Swiss condominium community (Stockwerkeigentümergemeinschaft, STWEG), because administrators increasingly refuse small mandates ([NZZ: "high effort, little return, lots of disputes"](https://www.nzz.ch/wirtschaft/hoher-aufwand-wenig-ertrag-viel-streit-warum-kleine-eigentuemergemeinschaften-kaum-noch-verwalter-finden-ld.1892411); date not visible).
- **When and how often:** monthly, when owners' advance payments must be billed and matched. Yearly, when annual accounts with cost allocation, the renewal-fund statement and owners'-meeting minutes are due (legal basis: Swiss Civil Code Art. 712a ff., per [immoverkauf24](https://immoverkauf24.ch/immobilienverkauf/immobilienverkauf-a-z/stockwerkeigentum/); renewal-fund line in a standard Swiss operating statement, [law.ch](https://law.ch/wp-content/uploads/007_schema-betriebsrechnung1.pdf)).
- **Cost:** mistakes turn into disputes between neighbours.
- **In one sentence:** *"In a small Swiss building owned by its residents, one unpaid neighbour has to do the books, the bills and the yearly owners' meeting, because no property manager will take such a small job."*
- **Niche size:** ~970,000 condominium units (Wüest Partner, cited by NZZ), with ~10 units per community on average. That gives **~97,000 communities (derived)**. NZZ speaks of "tens of thousands of small communities". The share that self-administers is unknown.

**Q2 — The one thing the app does.**
- It bills owners' contributions as Swiss QR-bills.
- It imports bank statements and auto-matches payments by QR reference.
- It allocates costs by value quotas and keys, keeps the renewal-fund ledger, and produces each owner's annual statement plus meeting invitation and minutes templates.
- Deterministic accounting rules only.
- QR-bill and bank-statement formats (camt.053/054) are an **ASSUMPTION** about Swiss payment rails; I did not verify them in this research.

**Q3 — Who already solves it?** Searched in German.

| Name | Country | Price | What it does | Gap |
|---|---|---|---|---|
| EinfachSTWEG ([site](https://einfachstweg.ch/)) | CH | From CHF 30/month (vendor claim) | Self-administration software for small and mid-sized communities; "no bookkeeping knowledge needed" (vendor claim) | Direct competitor at the same price. Bank auto-matching depth unknown |
| LIMMOBI ([site](https://limmobi.ch/de/stockwerkeigentum/)) | CH | Not found | Owners' contributions, budget, renewal fund, annual accounts; also for self-administrators (vendor claim) | Price and traction unknown |
| Stockwerkeigentum Digital ([site](https://stockwerkeigentum-buchhaltung.ch/)) | CH | CHF 195 one-time, no subscription (vendor claim) | Excel-based bookkeeping tool | Manual, single-user |
| ImmoTop2 via HEV Schweiz ([HEV](https://www.hev-schweiz.ch/vermieten/verwalten/immobilien-software/software-immotop2/)) | CH | Not found | Professional property software, "also suitable" for condominium communities | Built for professionals; pushed by the big owners' association |
| Fairwalter ([blog](https://blog.fairwalter.com/de-ch/stockwerkeigentum-verwaltung-und-herausforderungen)) | CH | Not found | Property-management platform; writes about condominium administration | Funding and focus not verified |
| softimo ([site](https://softimo.ch/)) | CH | Not found | Property-management software | For professionals (inference) |
| Professional administrators | CH | Not found | Full service | Increasingly refuse small mandates ([NZZ](https://www.nzz.ch/wirtschaft/hoher-aufwand-wenig-ertrag-viel-streit-warum-kleine-eigentuemergemeinschaften-kaum-noch-verwalter-finden-ld.1892411)) |

**What operators use and pay today:** Excel (CHF 195 tool) or subscriptions around CHF 30/month (vendor claims), or a professional administrator (fees not verified).

**Q4 — Why do people still suffer? Root cause:**
- **(b) Local/regulatory:** Swiss Civil Code rules, Swiss payment rails, and three languages.
- **(a) Too small** for funded players.
- **(d) A structural shift:** the shortage of administrators for small communities pushes owners into self-administration.

The gap is being filled, but only by young, fragmented tools. Launch market logic: the German equivalent (self-managed WEGs) is crowded with clearly profitable incumbents (kill #8), while Switzerland is not, on available evidence.

**Q5 — Is it profitable?**

| Item | Value | Status |
|---|---|---|
| Price | CHF 35/month per community (up to 15 units), ≈€37 | ASSUMPTION (anchor: EinfachSTWEG from CHF 30, vendor claim); exchange rate of 1 CHF ≈ €1.06 is an ASSUMPTION |
| Cost per customer | €8/month (hosting €1.5, bank-file processing and e-mail €1, payment €1, support €4.5) | ASSUMPTION |
| Gross margin | ≈78% | Derived |
| Fixed business costs | €2,500/month (native-speaker support/translation freelancer, Swiss VAT handling, base ad budget, insurance, accounting) | ASSUMPTION |
| Customers needed for €8k/month profit | (8,000 + 2,500) / 29 ≈ **362 communities** | Derived |
| Reachable pool | ~97,000 communities (970,000 units ÷ ~10) | Inputs VERIFIED via NZZ citing Wüest Partner ([NZZ](https://www.nzz.ch/wirtschaft/hoher-aufwand-wenig-ertrag-viel-streit-warum-kleine-eigentuemergemeinschaften-kaum-noch-verwalter-finden-ld.1892411)); total derived; self-administered share unknown |
| Share of pool needed | ≈0.4% of all communities | Derived |
| CAC | €250 (search ads plus free templates; €600 in the stress case) | ASSUMPTION |
| Churn | 0.8%/month | ASSUMPTION |
| LTV (gross margin basis) | €29 × 125 ≈ €3,600 | Derived |
| LTV/CAC | ≈14 (≈6 in the stress case) | Derived |
| Swiss VAT registration for a foreign e-service provider (CHF 100k worldwide turnover threshold) | — | ASSUMPTION, not verified |

**Q6 — How to build it.** Stack: a web app, Postgres, a QR-bill PDF generator, a camt/CSV bank parser, and PDF reports. Hosting in the EU or Switzerland. Payments for the subscription through a licensed PSP.

12-week outline:
- **Weeks 1–2:** interview 10 self-administering owners; collect community rules (Reglement) and past accounts; data model (community, units, value quotas, cost keys, owners, budget, accounts).
- **Weeks 3–4:** contribution plan; QR-bill generation and reminders.
- **Weeks 5–6:** bank-statement import (camt.053/054 and CSV); automatic matching by QR reference; manual matching screen.
- **Weeks 7–8:** expense booking with cost keys; renewal-fund ledger; each owner's annual statement; annual accounts PDF.
- **Week 9:** owners'-meeting invitation and minutes templates; read-only owner portal; document vault.
- **Week 10:** importer from Excel; billing and onboarding.
- **Weeks 11–12:** paid pilot with 5 communities; launch in German.

**Q7 — Where to launch first, and why.**
- **Launch market: German-speaking Switzerland.** The evidence: the administrator shortage (NZZ), a large pool, an existing CHF 30/month price point, and the crowded German alternative.
- **Where operators gather.** This is weak. I found no neutral association channel: the owners' association HEV distributes ImmoTop2. Possible routes:
  - SEO with free templates (meeting minutes, budgets) for searches about self-administering;
  - insurer guides such as [Mobiliar's condominium guide](https://www.mobiliar.ch/ratgeber/stockwerkeigentum), as a possible content partner (ASSUMPTION);
  - notaries and estate agents who sell condominium units (ASSUMPTION).
- **First 10 paying customers:**
  1. Publish 5 free templates in German and buy CHF 1,000 of search ads on terms such as "STWEG selbst verwalten".
  2. Book 20 discovery calls and offer a free import of last year's accounts.
  3. Convert at a founding price of CHF 290 for the first year, prepaid.
  4. Pay a referral credit for each new community.

**Q8 — How it makes money.** A subscription per community (CHF 35/month or CHF 350/year), paid from the community's account. Larger communities pay a per-unit add-on.

**Q9 — How one person runs it.**
- **Support:** in German; French and Italian later, through freelancers.
- **No legal advice:** route questions to the Civil Code text or to lawyers (keeps H3 clean).
- **Failure modes:** differences in bank file formats; disputes between owners about allocations (fix: transparent per-owner audit trail); peak load in January–April for annual accounts.

**Q10 — What did I miss? Kill tests.**
- **Incumbent copy (the largest risk):** EinfachSTWEG already sells this at CHF 30/month. A wedge (bank auto-matching, owner portal) must be proven in 10 discovery calls.
- **Platform kill:** banks' free QR-bill tools plus Excel may be enough for very small communities (3–4 units).
- **Liability:** bookkeeping errors cause disputes. Mitigate with clear terms and annual review by an owner-appointed auditor (common practice; ASSUMPTION).
- **False assumptions:** the self-administered share of the ~97,000 communities is unknown, and the CAC of a foreign founder in Switzerland may be much higher than €250.
- **Churn:** low once the ledger lives in the app.
- **Seasonality:** January to April.

---

## (3) PROVISIONAL SCORES C1–C10 (with weighted totals)

### Takeaway
On my scoring all three finalists beat the baseline (55.0): A by 11.5 points, B by 10, C by 6. All three sit in the TEST band. Five independent evaluators should push hardest on:
- **C3 for A** (three young competitors);
- **C1/C2 for B** (pain intensity is assumed, not evidenced);
- **C4 for C** (no cheap named channel).

Weighted score = sum(score × weight) / 10.

### Finalist A — Biogas substrate and EEG-bonus evidence log (Germany): **66.5 → TEST**

| Criterion (weight) | Score | One-line justification |
|---|---|---|
| C1 Pain (10) | 7 | Daily logging plus a hard 28 February deadline. A bonus can lapse permanently. One plant reports verifier costs up from €1.5k to €15k a year. |
| C2 Willingness to pay (15) | 8 | The sufferer is the payer: a business producing ~3.1 GWh a year that already pays verifiers. €790 a year is trivial against that. |
| C3 Gap realness (10) | 5 | Excel templates are still standard, but three young vendors (Nabisy Software, TerraVis, Biotaktix) show the gap is closing. |
| C4 Distribution (15) | 6 | Named channels exist (FvB regional network, verifiers, topagrar), but the founder has no contacts and competitors use the same channels. |
| C5 Unit economics (15) | 8 | ~85% gross margin; ~180 customers; LTV/CAC ≥7 even in the stress case. |
| C6 Market sufficiency (5) | 9 | Needs ~1.9% of 9,605 plants. |
| C7 Solo operability (10) | 6 | Rules for several EEG versions, deadline support peaks and legal upkeep. |
| C8 Durability (10) | 5 | Copyable by competitors or control-system vendors. The pool slowly shrinks as EEG terms end. Switching cost rises after one season of data. |
| C9 Risk, inverse (5) | 6 | Errors could cost bonuses, creating liability claims. The verifier remains the certifier. |
| C10 Speed to proof (5) | 6 | Prepaid founding customers before the deadline are feasible through verifiers, but a stranger faces a trust barrier. |
| **Weighted total** | **66.5** | 70 + 120 + 50 + 90 + 120 + 45 + 60 + 50 + 30 + 30 = 665 |

### Finalist B — Parent-duty and board tool for parent-run daycares (Germany): **65.0 → TEST**

| Criterion (weight) | Score | One-line justification |
|---|---|---|
| C1 Pain (10) | 6 | Weekly coordination plus yearly board handover. Intensity is plausible but evidenced only indirectly (ASSUMPTION-heavy). |
| C2 Willingness to pay (15) | 6 | The association has a budget and a clear payer, but free generic tools anchor low. |
| C3 Gap realness (10) | 6 | No product for this workflow found. Daycare apps target staff-run providers. |
| C4 Distribution (15) | 7 | 29 umbrella organisations; ~800 parent-run daycares in Berlin under DaKS, with trainings. Dense and cheap. |
| C5 Unit economics (15) | 7 | ~86% gross margin and low CAC through umbrellas, offset by churn from board turnover. |
| C6 Market sufficiency (5) | 5 | Needs 3.0–4.5% of a 5,000–7,500 pool. |
| C7 Solo operability (10) | 8 | Simple domain, low support, minimal personal data. |
| C8 Durability (10) | 5 | Copyable by daycare apps. The handover vault adds some switching cost. |
| C9 Risk, inverse (5) | 8 | Low liability; no child data. |
| C10 Speed to proof (5) | 7 | Berlin density makes 5–10 paid pilots in 90 days plausible. |
| **Weighted total** | **65.0** | 60 + 90 + 60 + 105 + 105 + 25 + 80 + 50 + 40 + 35 = 650 |

### Finalist C — Self-administration for small Swiss condominium communities: **61.0 → TEST (marginal)**

| Criterion (weight) | Score | One-line justification |
|---|---|---|
| C1 Pain (10) | 7 | Monthly billing, annual accounts and owners' meetings. Administrators refuse small mandates (NZZ). Neighbour disputes. |
| C2 Willingness to pay (15) | 7 | Owners are both payers and sufferers. A CHF 30/month price point already exists (vendor claim). |
| C3 Gap realness (10) | 5 | Tools exist (EinfachSTWEG, LIMMOBI, an Excel tool) but are young and fragmented. |
| C4 Distribution (15) | 4 | No neutral association channel (HEV pushes ImmoTop2). Depends on SEO, ads and referrals. |
| C5 Unit economics (15) | 7 | ~78% gross margin and long lifetimes, but the Swiss CAC for a foreign founder is unknown. |
| C6 Market sufficiency (5) | 9 | ~362 of ~97,000 communities (0.4%). |
| C7 Solo operability (10) | 6 | Swiss accounting and legal nuances; more languages later. |
| C8 Durability (10) | 6 | High switching cost once the ledger lives in the app; competitors are similar. |
| C9 Risk, inverse (5) | 6 | Bookkeeping errors become owner disputes. No licence needed. |
| C10 Speed to proof (5) | 5 | A foreign unknown founder in a trust-sensitive market; pre-sales will be slower. |
| **Weighted total** | **61.0** | 70 + 105 + 50 + 60 + 105 + 45 + 60 + 60 + 30 + 25 = 610 |

### BASELINE — Daily automated check-in call for people 65+ living alone without a care grade (Germany, €9.90/month): **55.0 → KILL band** (my score)

| Criterion (weight) | Score | One-line justification |
|---|---|---|
| C1 Pain (10) | 6 | A real but rare catastrophic risk; daily reassurance value is moderate. |
| C2 Willingness to pay (15) | 5 | The family pays, but the person at risk does not. Device-based alarm services (Hausnotruf) are subsidised only with a care grade. |
| C3 Gap realness (10) | 6 | A device-free daily call is rare in Germany, but it is simple to build (US analogues). Why it is still missing is unclear. |
| C4 Distribution (15) | 4 | Sold to adult children; no cheap named channel. |
| C5 Unit economics (15) | 5 | ~70% gross margin at €9.90 against ~€3 cost; consumer CAC; churn through death or moves into care. |
| C6 Market sufficiency (5) | 9 | ~1,000 of millions of people. |
| C7 Solo operability (10) | 7 | Automated telephony; elderly users need support; false alarms. |
| C8 Durability (10) | 5 | Easy for alarm-service providers or telecoms to copy. |
| C9 Risk, inverse (5) | 4 | Liability and reputation if a missed alert coincides with harm. |
| C10 Speed to proof (5) | 7 | Landing page plus ads gives fast pre-sales. |
| **Weighted total** | **55.0** | 60 + 75 + 60 + 60 + 75 + 45 + 70 + 50 + 20 + 35 = 550 |

### Summary

| Idea | Weighted score | Verdict | Beats my baseline (55.0)? | Still beats it if evaluators score the baseline at… |
|---|---|---|---|---|
| A Biogas evidence log (DE) | 66.5 | TEST | Yes (+11.5) | ≤66 |
| B Parent-duty tool (DE) | 65.0 | TEST | Yes (+10.0) | ≤64.5 |
| C Swiss condominium self-admin (CH) | 61.0 | TEST (marginal) | Yes (+6.0) | ≤60.5 |
| BASELINE (DE) | 55.0 | KILL band | — | — |

### Inferences
- **None of the three is a clear BUILD.** All three depend on one unproven point: A, that operators will pay instead of using Excel plus the verifier; B, that parent-duty coordination is a top-3 pain; C, that the CAC is affordable without an association channel. A 90-day test of under €2,000 per idea resolves each one: 10 prepaid founding customers.
- **If evaluators cut A's C3 to 4 and C8 to 4, A drops to 64.5.** It still beats the baseline, but A is the most exposed to competitors entering.

### Gaps
- Prices and traction of Nabisy Software, TerraVis, Biotaktix, EinfachSTWEG and LIMMOBI were not found.
- Fees of professional Swiss condominium administrators were not found.
- The share of self-administered Swiss communities was not found.
- The trend in the number of parent-run daycares was not found.
- The exact current-law consequences of diary errors under EEG 2014–2023 were not found. My sources describe EEG 2009.
- How many plants already use dedicated software was not found.

---

## (4) SOURCES

All URLs below were found through the search tool. Direct fetching was blocked by the network proxy, so facts come from search extracts of these pages. Vendor pages are vendor claims.

**Biogas (Finalist A)**
- FvB/Fraunhofer IEE plant census, end-2025: https://www.topagrar.com/energie/news/biogasbranche-2025-neue-zahlen-zeigen-grosses-potenzial-politik-bremst-ausbau-a-20023918.html
- EnBW biogas facts: https://www.enbw.com/unternehmen/themen/klimaschutz/biogas.html
- ZfK on ~9,600 plants: https://www.zfk.de/energie/waermewende/so-gelingt-der-biomethan-hochlauf-wenn-berlin-die-bremsen-loest
- WEMAG/Kremp verifier presentations (EEG 2009 §27(3), 28 February deadline, bonus lapse; older: 2019): https://www.wemag.com/sites/default/files/4_kremp_ug_im_eeg_2017_wemag_2019.pdf ; https://www.wemag.com/sites/default/files/5_Kremp_Was%20ist%20aus%20Sicht%20des%20Umweltgutachters%20zu%20beachten.pdf
- Grid-operator conformity forms: https://cdn.swk.de/assets/download/Konformitätserklärung%20Bio%20EEG%202012.pdf ; https://www.ewe-netz.de/-/media/ewe-netz/downloads/konformitaetserklaerung/konfo_neu/erklrung-der-konformitt-zum-eeg-ibn-bis-2011-eeg-2009.pdf ; https://www.bayernwerk-netz.de/content/dam/revu-global/bayernwerk-netz/files/Energieeinspeisen/Ihre-Anlage/Bio/20210714-bayernwerk-einsatzstofftagebuch.pdf
- Environmental verifier committee guideline (UGA): https://www.emas.de/fileadmin/user_upload/4-pub/UGA-Aufgaben-LL_EEG.pdf
- Normec, EEG environmental reports: https://certification.normecgroup.com/environmental-reports-for-biogas-plants-in-accordance-with-the-eeg
- TLL leaflet on substrate diary (older): https://www.tll.de/www/daten/publikationen/merkblaetter/biol1005.pdf
- topagrar, 28 February deadline article (date not visible): https://www.topagrar.com/management-und-politik/news/biogas-tagebuch-und-umweltgutachten-bis-28-februar-vorlegen-9608061.html
- topagrar, "Biogas im Würgegriff der Bürokratie" (expert report €1.5k → €15k): https://www.topagrar.com/betriebsleitung/news/biogas-im-wuergegriff-der-buerokratie-b-20001963.html
- IKZ on rising documentation duties: https://www.ikz.de/detail/news/detail/nachweispflicht-fuer-energiewirte-anforderungen-bei-der-dokumentationspflicht-erheblich-gestiegen/
- Templates: https://www.nq-anlagentechnik.de/downloads/ ; https://pbne.de/gutachten/
- BOGIS: https://apps.apple.com/mx/app/bogis/id998939173 ; https://biogasbogis.wordpress.com/2014/07/16/16-07-2014-biogas-erfassung-der-futterung-btb/
- Nabisy Software: https://nabisy-software.de/biogasanlagen-betreiber ; https://nabisy-software.de/blog/massenbilanzierung-biogasanlage-anleitung
- TerraVis: https://www.terravis-biogas.de/dienstleistungen/gocero2/digitale-massenbilanzierung
- Biotaktix: https://www.biotaktix.de/en/
- LfL Biogas-Rechner: https://www.lfl.bayern.de/biogasrechner ; KTBL tool via agrarheute: https://www.agrarheute.com/energie/biogas-tool-hilft-landwirten-substratspektrum-erweitern-622497
- FvB statement to the NRW parliament: https://opal.landtag.nrw.de/portal/WWW/dokumentenarchiv/Dokument/MMST18-161.pdf

**Parent-run daycares (Finalist B)**
- BAGE lobby register entry: https://www.lobbyregister.bundestag.de/suche/R003613 ; BAGE statement 2026: https://www.lobbyregister.bundestag.de/media/c5/04/830045/Stellungnahme-Gutachten-SG2608120005.pdf
- Bildungsserver (>7,500 parent-run daycares): https://www.bildungsserver.de/seite_de.php?seite=3362
- DaKS guiding principles (older: 2013): https://www.daks-berlin.de/system/files/media/files/leitbild-final.pdf ; DaKS press release (older: 2019): https://www.daks-berlin.de/system/files/media/files/PM_Warnstreik_final.pdf ; DaKS participation 2025: https://pardok.parlament-berlin.de/starweb/adis/citat/VT/19/Lobbyregister/Beteiligungsbeitrag_3105_DaKS.pdf
- Munich EKI model: https://stadt.muenchen.de/service/info/erstattung-von-entgeltermassigung-nach-ekiplus/10315711/ ; https://www.muenchen-transparent.de/dokumente/9178772/datei
- Daycare software: https://apps.apple.com/us/app/id1424121474 ; https://www.softguide.de/programm/kita-manager ; https://www.softguide.de/programm/comkita/vorschau ; https://www.softguide.de/programm/kita-abrechnung ; https://livekid.com/pricing/ ; https://kommunal.de/kita-chaos-kita-planer

**Swiss condominium communities (Finalist C)**
- NZZ on small communities and administrators: https://www.nzz.ch/wirtschaft/hoher-aufwand-wenig-ertrag-viel-streit-warum-kleine-eigentuemergemeinschaften-kaum-noch-verwalter-finden-ld.1892411
- EinfachSTWEG: https://einfachstweg.ch/ ; LIMMOBI: https://limmobi.ch/de/stockwerkeigentum/ ; Stockwerkeigentum Digital: https://stockwerkeigentum-buchhaltung.ch/ ; ImmoTop2 (HEV): https://www.hev-schweiz.ch/vermieten/verwalten/immobilien-software/software-immotop2/ ; Fairwalter: https://blog.fairwalter.com/de-ch/stockwerkeigentum-verwaltung-und-herausforderungen ; softimo: https://softimo.ch/
- Legal background: https://immoverkauf24.ch/immobilienverkauf/immobilienverkauf-a-z/stockwerkeigentum/ ; https://www.mobiliar.ch/ratgeber/stockwerkeigentum ; https://law.ch/wp-content/uploads/007_schema-betriebsrechnung1.pdf

**Kill-log evidence**
- Hunting co-operatives: https://www.lobbyregister.bundestag.de/media/23/6e/698363/Stellungnahme-Gutachten-SG2602240021.pdf ; https://www.BFR.bund.de/cm/343/position-der-bagje.pdf ; https://www.bwv-net.de/wp-content/uploads/2026/02/Jagdpachtverwaltung-Flyer_2025-09.pdf ; https://www.zjen.de/pc-programm-jagdkataster-22-mit-digitaler-karte-gis/ ; https://www.bayerischerbauernverband.de/jagdkataster ; https://www.bauernverband-mv.de/jagdpachtverwaltung-am-pc/ ; https://www.jagdkataster.net/index.html ; https://geoinformationssystem.net/jagdkataster/ ; https://www.tvje.de/themen/kataster/ ; https://www.rbk-direkt.de/geoportal/beschreibung-kooperationsprojekt-jagdkataster.pdfx ; https://bayernlabs.bayern.de/mam/ldbv/dateien/dfb_jagdkataster_csv_nicht_barrierefrei.pdf ; https://www.allendorf-eder.de/verwaltung/mitteilungen/amtliche-bekanntmachungen/2025/2025-10-jagdgeldauszahlung-2025/bekanntmachung-jagdgeldauszahlung-2025.pdf?cid=9oi ; Saxony count (1,401 co-operatives): https://medienservice.sachsen.de/medien/medienobjekte/116840/download
- Allotment associations: https://www.lobbyregister.bundestag.de/media/bd/1d/374451/BKD_Geschaeftsbericht_Kassenbericht_2023.pdf ; https://verbraucher.org/media/file/4191.Kleingaerten_Verb_konkret_02_25.pdf ; https://www.laubenmeister.de/features ; https://kleingartenassist.com/ ; https://kleingartenverein24.de/ ; https://www.pc-kleingaertner.de/ ; https://clubcopilot.de/kleingartenverein/ ; https://www.sewobe.de/spezialloesungen/kleingartenvereine/ ; https://vereinsplaner.com/en/v/software-fuer-kleingartenvereine ; https://www.finanzfrage.net/frage/muessen-stromverluste-4500kwhjahr-bei-20-pachtgaerten-im-kleingartenverein-von-den-parzellenpaechtern-ausgeglichen-werden ; https://administrator.de/forum/sql-csv-fotoverwaltung-abrechnungsdaten-678402.html ; https://www.datev-community.de/t5/Betriebliches-Rechnungswesen/Buchhaltungssoftware-Verein/m-p/110010
- Childminders: https://www.bildungsserver.de/Kindertagespflege-2463-de.html ; https://ktp-digital.de/ ; https://www.tagespflegedigital.eu/tagesmutter-app-verwaltung ; https://www.mm-soft.de/KitaPflegeTPP.html ; https://www.nordholz-edv.de/tagespflege.html ; https://www.tagespflege.bayern.de/imperia/md/content/stmas/tagespflege/downloads/iv_fakten_empfehlungen_jan2020.pdf
- Boarding stables: https://alternativeto.net/software/stabley/about/ ; https://apps.apple.com/de/app/stall-manager/id6751195329 ; https://apps.apple.com/de/app/stallzeit/id6757603739 ; https://www.cbinsights.com/compare/die-pferde-app-vs-equinem
- §45b relief-amount billing: https://www.lfp.bayern.de/wp-content/uploads/2026/05/Praxiseinblick_Vorbereitung_vollelektronische_Abrechnung.pdf ; https://www.aok.de/gp/fileadmin/user_upload/Pflege/Abrechnung/bw_dta_abrechnungsleitfaden.pdf ; https://soziales.niedersachsen.de/download/191137/Abrechnungsvordruck_jur._Pers._Einzelunternehmen_.pdf ; https://komda-software.de/produkte/software-betreuungsdienste/
- School escorts and youth welfare: https://www.medifoxdan.de/software-jugendhilfe/loesungen/ambulante-traeger-und-schulbegleitung ; https://www.kilanka.de/software/schulbegleitung/ ; https://www.rocom.de/sozial/schulbegleitung-software/ ; https://www.lap-jugendhilfe.de/software-schulbegleiter-und-schulbegleitung/ ; https://connext.de/einsatzfelder/jugendhilfe/ambulante-betreuung.aspx ; https://www.i-soft.de/jugendhilfe ; https://www.sodisys.de/target/software-fuer-ambulante-kinder-und-jugendhilfe/ ; https://koju24.de/software-schulbegleitung/ ; https://justmanageit.de/ ; https://schulbegleitung.online/ ; https://www.timo24.de/blog/intelligente-zeiterfassung-fuer-schulbegleiter/
- Legal guardians: https://download.betreuung.de/ebook/BdB_at_work_2013_Fallsteuerung_(eBook).pdf ; https://www.softguide.de/ausschreibungen/angehender-berufsbetreuer-sucht-software-zur-rechtsbetreuung ; https://www.softguide.de/ausschreibungen/software-der-nachweisfuehrung-zur-verwaltung-des-vermoegens-gesucht
- WEG (Germany): https://www.softwareabc24.de/vergleiche/karthago-vs-win-casa ; https://www.softwareabc24.de/vergleiche/intex-hausverwaltung-vs-win-casa ; https://www.immoware24.de/wp-content/uploads/2025/01/11_AbrechnungWEG-Verwaltung.pdf ; https://www.connect-professional.de/filedownload/documents/900635/aareon-hausverwaltung-plus-2026-tabelle-mit-punktverteilung.pdf ; https://bau.de/text/250625-weg-selbstverwaltung-hilfe.php
- Finnish road associations: https://api.hankeikkuna.fi/asiakirjat/df500404-bf0f-4be0-b16d-486244c13c9c/de6b3b41-b6e8-47af-b438-15ef21ba3e82/LAUSUNTO_20260312200852.PDF ; https://www.edilex.fi/he/20170147 ; https://tiehoitokunta.fi/hinnasto/ ; https://matriset.fi/ ; https://tiekarhu.fi/ ; https://www.helppokayttaa.fi/ ; https://asteri.fi/tiekunnan-laskutus-laskutusohjelma-tienhoitokunnalle/
- Swedish joint-facility associations: https://www.hemnet.se/artiklar/guider/2022/05/06/slipp-brf-nytt-pa-hallgolvet ; https://www.spiris.se/integrationer/partner/sharely ; https://www.skatteverket.se/foreningar/driva/samfallighetsforening/momsiensamfallighetsforening.4.1657ce2817f5a993c3a7cf8.html
- Spanish hunting estates and irrigation communities: https://www.agronewscastillayleon.com/junta-precinto-digital-caza/ ; https://www.vozpopuli.com/espana/castilla-y-leon/la-junta-de-castilla-y-leon-pone-en-marcha-el-precinto-digital-de-caza-mayor-sg.html ; https://www.juntadeandalucia.es/medioambiente/portal/documents/d/global/andalucia_-manual-precinto-digital-para-titulares-de-cotos-pdf ; https://redforesta.com/wp-content/uploads/2025/06/repos-caceres/03-Caceres-5jun25.pdf ; https://mapa.gob.es/images/ca/ponencia-4-telecontrol_tcm34-648096.pdf ; https://citarea.cita-aragon.es/bitstream/10532/5330/2/GCP2018003700presentacion.pdf
- UK blocks: https://manageyourblock.co.uk/?p=2275 ; https://payhip.com/b/h239a ; https://www.landlordvision.co.uk/blog/best-block-management-software-uk-market/ ; https://www.softomatesolutions.com/block-management-software/
- Driving schools: https://www.startbase.de/news/autovio-schliesst-finanzierungsrunde-ab/ ; https://tech.eu/2018/11/14/belgian-founded-startup-clickclickdrive-raises-1-million-for-its-driving-school-management-software ; https://www.ki-syndikat.de/tools/fahrschulcockpit/
- Funeral homes: https://www.getapp.de/software/2100087/bestattungone ; https://www.capterra.com.de/directory/30565/funeral-home/deployment-options/windows/software
- Chimney sweeps: https://gesetze.legal/bund/schfhwg/19 ; https://umwelt-online.de/recht/luft/laender/bw/vwvschornstf.htm ; https://www.nordwestmecklenburg.de/datei/anzeigen/id/10350,1105/richtlinie_ueber_die_fuehrung_vorlage_und_pruefung_von_kehrbuechern.pdf ; https://www.softwareabc24.de/schornsteinfeger-software/saas
- Foundations: https://www.stiftungen.org/fileadmin/stiftungen_org/Stiftungen/Zahlen-Daten/2025/Datenblatt_Niedersachsen_2025.pdf ; https://www.bezreg-detmold.nrw.de/system/files/media/document/file/2.21_stiftungen-haeufig-gestellte-fragen-und-antworten.doc ; https://www.ihk.de/dresden/servicenavigation/presse-publikationen/meldungen/einfuehrung-eines-zentralen-stiftungsregisters-verspaetet-sich-6799258 ; https://www.fgs.de/news-and-insights/blog/detail/das-neue-stiftungsregister-ist-nicht-mehr-weit-was-gemeinnuetzige-stiftungen-jetzt-und-in-zukunft-beachten-muessen ; https://onlinebilanz.de/stiftung/
- Shooting clubs: https://lxgesetze.de/waffg/14 ; https://gesetze.legal/bund/waffg/14 ; https://www.dsb.de/fileadmin/DSB.DE/MIX/MIX_2024/Stiller_Star_03-2024.pdf ; https://apps.apple.com/th/app/schiesslog/id6751775923 ; https://apps.apple.com/bo/app/shootingproof/id6447617371 ; https://www.bayern.landtag.de/www/ElanTextAblage_WP18/Drucksachen/Basisdrucksachen/0000005000/0000005470.pdf
- Small sewage plants: https://opac.dbu.de/ab/DBU-Abschlussbericht-AZ-33290-01.pdf ; https://www.ammerland.de/media/custom/2843_2653_1.PDF
- Water and soil associations: https://www.softguide.de/programm/igel-wassergeld ; https://www.haufe.de/id/norm/kommunalabgabengesetz-nordrhein-westfalen-7-gebuehren-fuer-beitraege-und-umlagen-der-wasser-und-bodenverbaende-und-zweckverbaende-HI1308275_p7.html ; https://www.landkreis-osnabrueck.de/sites/default/files/2025-08/kreisverband-der-wub-uelzen-erfahrungsbericht-aus-der-praxis.pdf
- Sports clubs: https://www.netzwelt.de/download/25272-clubdesk.html
