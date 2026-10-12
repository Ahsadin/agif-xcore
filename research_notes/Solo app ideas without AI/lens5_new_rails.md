# Lens 5: New technical rails (2024–2026) as enablers of non-AI solo-founder apps

*Prepared 2026-10-12. Lens: technical rails (payment, identity, messaging and data infrastructure) that recently became available, cheap, mandatory or widespread. Ideas mainly driven by a new compliance obligation were excluded, as instructed.*

**Research limits (read first)**

- **Search budget.** The shared web-search budget ran out after about 31 searches by this researcher. The limit is shared by all agents in the run.
- **No page fetching.** WebFetch could not resolve any host. The egress proxy also refused direct page fetches (for example, gesetze-im-internet.de got a 403).
- **What that means for the facts below.**
  - Every fact is cited to the URL that the search returned.
  - I could not open the pages to re-check exact wording.
  - Figures from secondary sources, vendors or forums are labelled as such.
- **Not researched in this pass (no evidence gathered):**
  - FedNow/RTP adoption
  - UPI international links
  - Peppol network growth
  - RCS business messaging
  - Apple/Google Wallet passes
  - EU High-Value-Dataset APIs
  - Open-banking aggregator price lists
  - FiDA status
  - Germany's WhatsApp rate card
- **Cross-check with other lenses.** Lens 1 and Lens 3 had already killed German self-managed condominium (WEG) software on H8, with evidence. I adopted that kill (K08). Otherwise my finalist slot would have gone to that idea.

**Takeaway**

- **Most 2025 rails commoditise.** SEPA Instant with Verification of Payee, Wero, Tap to Pay in about 43 countries, and WhatsApp's per-message pricing mostly turn payment and messaging features into commodities. Banks, payment providers and Meta ship the obvious features for free. As a result, 16 of my 27 raw candidates died on H4 or H8 (11 of those on verified evidence; the rest are flagged as unverified).
- **Where the rails do pay off for one founder:**
  1. A local rail has just matured, but global tools ignore it. Example: Romania's RoPay (2024–2026) versus India's mature apps that convert cash-on-delivery (COD) orders into prepaid orders. This is **Finalist 1, the only clear win.**
  2. Cheap two-way messaging plus instant deposits fix a small, unglamorous workflow (food-craft pre-orders). This is **Finalist 2. It is marginal and rests on unverified market data.**
  3. A new data-access right opens up device data (the EU Data Act and heat pumps). This is **Finalist 3. It is the weakest, because maker APIs are still rate-limited, paid or missing.**
- **Against the baseline.** On my provisional scoring, the baseline gets 57.5:
  - Finalist 1 beats it clearly (66.0).
  - Finalist 2 beats it narrowly, within scoring noise (60.0).
  - Finalist 3 does not beat it (55.0).

---

## (1) KILL LOG

### 1a. Rail scan: what actually changed in 2024–2026 (verified status)

| Rail | What changed and when | Access cost for a solo founder | Licence / certification | Risk the rail owner ships it free (H4) | Pain it newly makes cheap |
|---|---|---|---|---|---|
| **SEPA Instant Credit Transfer + Verification of Payee (VoP), EU Instant Payments Regulation (IPR)** | **Euro-area payment providers:** must receive instant payments by 9 Jan 2025, and send them plus offer VoP by 9 Oct 2025. **Non-euro states:** receive by 9 Jan 2027, send plus VoP by 9 Jul 2027. **E-money and payment institutions:** 9 Apr 2027 ([ECB](https://www.ecb.europa.eu/paym/retail/instant_payments/html/instant_payments_regulation.ro.html)). Instant transfers may cost no more than standard transfers, and VoP is free ([BTA](https://www.bta.bg/en/news/1072635-bulgarian-banks-99-ready-for-instant-payments-rollout-in-2027)). **Bulgaria** (euro since 1 Jan 2026): the IPR applies there from 1 Jan 2027, and VoP is still being implemented ([BTA](https://www.bta.bg/en/news/1072635-bulgarian-banks-99-ready-for-instant-payments-rollout-in-2027); [ECB news](https://www.ecb.europa.eu/press/intro/news/html/ecb.mipnews260102.en.html)). | Free to use with any business account. Reading incoming payments needs a licensed account-information provider or the bank's own API (prices not verified). | None, as long as the app never holds funds. VoP is a check run by the payer's payment provider ([ECB](https://www.ecb.europa.eu/paym/retail/instant_payments/html/instant_payments_regulation.ro.html)), so a non-provider cannot sell it (inference). | **Very high.** Banks give instant payments and VoP for free. | Instant, name-checked bank payments for prepayments, deposits and handovers. |
| **Wero (European Payments Initiative)** | **Germany:** online-shop payments live since Nov 2025 via Sparkassen and Volksbanken. Deutsche Bank, Postbank, ING and Revolut follow in Q1 2026. **Supporting payment providers** include Stripe, Unzer, PAYONE, Nexi and Worldline ([The Paypers](https://thepaypers.com/payments/news/wero-ecommerce-is-now-live-in-germany); [Nexi, Apr 2026](https://www.nexigroup.com/en/media-relations/news/2026/04/wero-for-ecommerce-in-germany/)). **Next:** online payments in Belgium, France, Luxembourg and the Netherlands in 2026; in-store from end-2026 ([banking.vision](https://banking.vision/en/development-wero-2025-2026)). | Through the payment provider's pricing (not verified). | Not needed (the payment provider is licensed). | **Kills generic bank-to-bank checkout and payment-link ideas in Germany.** | Card-free online payment. |
| **Open banking: account information (AIS) and payment initiation (PIS) via licensed aggregators. PSD2 now, PSD3/PSR next.** | **PSD3/PSR:** provisional agreement on 27 Nov 2025; final texts published 23 Apr 2026. They add a list of prohibited obstacles and more prescriptive API duties, and are likely effective in late 2027 ([Hogan Lovells](https://www.hoganlovells.com/en/publications/final-texts-for-psd3-and-psr-awaited-as-european-parliament-and-council-of-eu-announce-provisional); [JD Supra](https://www.jdsupra.com/legalnews/psd3-and-the-payment-services-4770204/); [Dudkowiak](https://www.dudkowiak.com/blog/psd3-and-psr-final-texts-agreed-new-obligations-for-payment-institutions/)). **FiDA:** status not found. | **Aggregator prices:** not verified. **GoCardless:** still offers Bank Account Data; another, unnamed product was discontinued on 18 Dec 2023 ([GoCardless](https://gocardless.com:443/bank-account-data/announcement)). | Founder can usually work under the aggregator's licence (common model; verify per vendor). | Medium | Automatic payment matching. |
| **WhatsApp Business Platform (Cloud API)** | **Per-message pricing** since 1 Jul 2025. **Free:** utility templates inside an open 24-hour customer-service window, and all messages for 72 hours inside a free entry-point window. **Discounts:** volume tiers ([Meta](https://developers.facebook.com/docs/whatsapp/pricing)). **Romania (secondary sources):** <br>• Marketing €0.0712 per message <br>• Utility, authentication and service €0.0239 per message <br>• Service messages charged from 1 Oct 2026 beyond 1,000 free per number per month <br>([Profit.ro](https://profit.ro/romania-conectata/schimbare-la-whatsapp-apare-plata-pentru-mesajele-de-asistenta-pe-whatsapp-business-api-22793043); [Zernio](https://zernio.com/whatsapp-api-pricing)). | Cents per business-initiated template message. | Meta business verification, template approval and recipient opt-in. | **Medium.** Meta can reclassify templates or ban accounts, so keep an SMS/email fallback. | Two-way order and appointment flows without building an app. |
| **Tap to Pay on iPhone (and Android SoftPOS)** | **43 countries** by Sep 2025 ([MacTech](https://www.mactech.com/2025/09/23/apple-expands-tap-to-pay-on-iphone-to-five-more-countries-across-europe/amp/)). **Added Mar 2025:** Bulgaria, Finland, Hungary, Liechtenstein, Poland, Portugal, Slovakia, Slovenia, Switzerland ([Apple](https://www.apple.com/pt/newsroom/2025/03/apple-introduces-tap-to-pay-on-iphone-in-more-european-countries)). **Added Sep 2025:** Estonia, Latvia, Lithuania, Monaco, Norway. **Providers** include SumUp, Revolut, Adyen, myPOS, Viva, Stripe, PayPal and Nexi ([Apple](https://www.apple.com/uk/newsroom/2025/09/apple-expands-tap-to-pay-on-iphone-to-five-more-countries-across-europe/)). | Free app; card fees set by each provider (not verified). | The provider is the licensed acquirer. | **Very high** for generic point-of-sale apps. | Card acceptance without hardware. |
| **EU Data Act** | **12 Sep 2025:** applicable. Users can access their product data and have it shared with third parties. **12 Sep 2026:** products placed on the market from this date must be designed for data access ([SCL](https://www.scl.org/eu-data-act-in-force-from-12-september-2025/); [Clifford Chance](https://www.cliffordchance.com/insights/resources/blogs/talking-tech/en/articles/2025/09/eu-data-act--a-new-era-for-data-sharing-has-begun.html)). **Heat-pump makers today:** <br>• Viessmann, Vaillant and iDM publish Data Act pages. <br>• Vaillant: no official third-party API found; the community uses a reverse-engineered one. <br>• Daikin: official API limited to 200 calls per day. <br>• Viessmann: free Basic API tier with 1,450 calls per 24 hours, plus paid plans. <br>(Details in Finalist 3.) | Free to low; paid tiers exist. | None | **Medium-high.** Makers can ship the same insight. | Independent analysis of a household's own device data. |
| **Germany: dynamic electricity tariffs and smart meters** | **§41a EnWG:** every electricity supplier must offer a dynamic tariff from 1 Jan 2025 to customers with an intelligent meter. Previously this applied only to suppliers with more than 100,000 customers. **Smart-meter cost:** about €20–50 per year (sources differ) ([preisvergleich.de](https://strom.preisvergleich.de/news/40421/das-aendert-sich-2025/); [greenox](https://greenox-group.de/dynamischer-stromtarif/)). | — | Access to meter data needs energy-market roles (not verified). | **Very high.** Suppliers' own apps. | Shifting electricity use to cheap hours. |
| **EU Digital Identity Wallet** | **End-2026:** each member state must offer a wallet. **End-2027:** regulated relying parties must accept it (finance and anti-money-laundering firms, and very large online platforms). **Registration:** relying parties register per member state ([Heuking](https://www.heuking.de/en/news-events/newsletter-articles/detail/the-new-eu-digital-identity-wallet-eudi.html); [Arthur Cox](https://www.arthurcox.com/knowledge/the-eu-digital-identity-wallet-what-companies-need-to-know/); [eIDEasy, vendor](https://eideasy.com/blog/eu-digital-identity-wallet-acceptance-2027)). | Unknown | Relying-party registration | Not live yet | Remote identity checks (future). |
| **Pix Automático (Brazil)** | Launched 16 Jun 2025 under Resolução BCB 402. Banks must offer it, and individuals pay no fee ([Canaltech](https://canaltech.com.br/mercado/bc-confirma-lancamento-do-pix-automatico-em-junho-de-2025-296277/); [Correio da Manhã](https://digital.correiodamanha.com.br/jornalcorreiodamanha/2025/06/05/0006d8/pdf/0506cmanha06.pdf)). | Through payment providers | The payment provider is licensed. | High | Recurring billing without boleto payment slips or cards. |
| **RoPay (Romania)** | **Oct 2024:** live with CEC Bank and Libra. **Apr 2025:** ING person-to-person payments by QR. **BRD:** online-shop payments with the processor EuPlătesc (date unconfirmed). **24 Aug 2026:** EuPlătesc connected directly to TransFonD's RoPay infrastructure, so its merchants can integrate. Free for individuals; ING caps person-to-person payments at 49,999 lei. Sources: [revistabiz](https://www.revistabiz.ro/s-a-lansat-ropay-serviciul-de-plati-instant-cu-mobilul-intre-conturi-ce-banci-l-au-implementat-deja/); [economica](https://www.economica.net/?p=832404); [capital.ro](https://www.capital.ro/anunt-pentru-clientii-brd-cum-se-vor-face-platile-vestea-bancii-venita-azi-18-decembrie-extinde-optiunile-de-plata.html); [revistabiz, Aug 2026](https://www.revistabiz.ro/euplatesc-se-conecteaza-direct-la-infrastructura-transfond-acces-la-ropay-simplificat-pentru-comercianti/). | Through the merchant's payment processor (merchant fee not found). | The processor or bank is licensed. | Medium | Instant, card-free prepayment in Romanian lei. |
| **Not researched in this pass** | FedNow/RTP, UPI international links, Peppol growth, RCS, Apple/Google Wallet passes, EU High-Value-Dataset APIs | — | — | — | — |

### 1b. Key-question answers and inferences

- **Which rails changed?**
  - **Verified:**
    - IPR: euro area 2025, non-euro 2027, Bulgaria 2027
    - Wero online payments in Germany (Nov 2025)
    - PSD3/PSR agreed (Nov 2025)
    - WhatsApp per-message pricing (Jul 2025)
    - Tap to Pay expansion (2025)
    - EU Data Act (Sep 2025)
    - German dynamic-tariff duty (Jan 2025)
    - EU Digital Identity Wallet timeline (2026/2027)
    - Pix Automático (Jun 2025)
    - RoPay (Oct 2024 to Aug 2026)
  - **Not verified:** FedNow/RTP, UPI, Peppol, RCS, Wallet passes, High-Value-Dataset APIs.
- **Do founders need their own licence?** Not when the money flows straight from payer to merchant through licensed parties, or when bank data comes through a licensed aggregator.
  - VoP checks can only be run by payment providers.
  - Acting as a merchant acquirer needs a partner.
- **Rail-owner risk is the dominant killer.** Banks (instant payments, VoP, Wero), card-acceptance providers (Tap to Pay), suppliers (dynamic tariffs) and Meta (WhatsApp Business app) all ship the obvious features free.
- **Inference: the best pattern is a "playbook port".** Take a tool category proven where a rail matured earlier (India: UPI, then apps that convert cash-on-delivery orders to prepaid). Move it to a market where the matching rail has just arrived (Romania: RoPay), and where global vendors do not support that rail.
- **Inference: the Data Act is a real right but not yet a usable API layer.** Device-data products stay fragile until access-by-design (products from 12 Sep 2026) reaches the installed base.
- **Inference: PSD3/PSR (likely late 2027) should make bank-data products more robust.** This helps durability but does not create demand.

### 1c. Kill log (27 raw candidates; each started from a Q1 pain)

| # | Raw candidate (Q1 pain → new rail → app) | Killed by | Why (evidence) |
|---|---|---|---|
| K01 | Small German web-shop owner matching prepayment ("Vorkasse") transfers by hand → SCT Inst + EPC QR + account data → instant-prepay checkout with auto-confirmation | **H4** | The rail owner ships it: Wero online payments (bank-owned, instant, bank to bank) are live in Germany since Nov 2025, supported by Stripe, Unzer, PAYONE, Nexi and Worldline ([The Paypers](https://thepaypers.com/payments/news/wero-ecommerce-is-now-live-in-germany); [Nexi](https://www.nexigroup.com/en/media-relations/news/2026/04/wero-for-ecommerce-in-germany/)). |
| K02 | Sole trader whose trading name differs from the account name loses payments to VoP "no match" warnings → VoP (9 Oct 2025) → "VoP readiness checker" | **H3 / H4** | VoP is run by the payer's payment provider ([ECB](https://www.ecb.europa.eu/paym/retail/instant_payments/html/instant_payments_regulation.ro.html)). A non-provider cannot query it (inference), and banks show the result free at payment time. |
| K03 | Club treasurer at a summer festival with 10 cash stands → Tap to Pay (EU rollout 2024–25) → multi-stand volunteer point-of-sale app | **H4** | The providers Apple lists (SumUp, Revolut, myPOS, Viva, Adyen, Stripe, PayPal, Nexi) already ship free Tap-to-Pay apps ([Apple, Mar 2025](https://www.apple.com/pt/newsroom/2025/03/apple-introduces-tap-to-pay-on-iphone-in-more-european-countries); [Apple, Sep 2025](https://www.apple.com/uk/newsroom/2025/09/apple-expands-tap-to-pay-on-iphone-to-five-more-countries-across-europe/)). If cash is also recorded, German cash-register security rules (certified signing module) add cost (ASSUMPTION, not verified). |
| K04 | German heat-pump owner overpaying without knowing why → EU Data Act + official maker APIs + open weather data → efficiency watchdog | **SURVIVED → Finalist 3** | Passes H4 only narrowly, and only with a design where maker APIs are optional. Scores below the baseline. |
| K05 | Small solar installer checking four inverter-maker portals → brand-independent fleet monitoring (Data Act) | **H8** | Brand-independent portals are already sold to installers: smartblue Smart Monitor ([vendor](https://www.smartblue.de/produkte/smart-monitor/)), Solar-Log with real-time alarms ([rfp.wiki](https://www.rfp.wiki/vendors/solar-log)) and Papendorf SOL.Connect ([ikz, undated and older](https://www.ikz.de/uploads/media/PV-Ueberwachung.pdf)). Makers also offer free fleet portals ([Fronius](https://www.fronius.com/de/solarenergie/solarloesungen/apps-software)). Several sources date from 2010–2019 (flagged as old). |
| K06 | Household on a new dynamic tariff unsure when to run appliances → §41a EnWG duty (Jan 2025) → "cheapest hours" alerts | **H4 / H5** | Every supplier must offer the tariff ([preisvergleich.de](https://strom.preisvergleich.de/news/40421/das-aendert-sich-2025/)), and the price signal comes with it. Consumers will not pay for a price feed (ASSUMPTION). |
| K07 | Heat-pump installer fielding "my bill is too high" calls → installer fleet monitoring | **H4** | Depends on maker goodwill. Vaillant publishes no third-party API; the community uses a reverse-engineered one, whose quota was cut in Oct 2025 ([myPyllant](https://pypi.org/project/myPyllant/0.0.8); [Home Assistant forum](https://community.home-assistant.io/t/myvaillant-integration/542610?page=24)). Makers also run their own installer tools (ASSUMPTION). |
| K08 | Volunteer owner running a small self-managed condominium (WEG) in Germany → bank data + SCT Inst/VoP + e-voting → treasurer autopilot | **H8** | Funded and profitable tools already sell to self-managers (evidence gathered by Lens 1 and Lens 3): <br>• Dotega: €1.3m pre-seed, targets WEGs with 2–20 units at a reported €9.80 per unit per month ([HTGF](https://www.htgf.de/dotega-pre-seed-finanzierung/); [startup-seeker](https://startup-seeker.com/company/dotega~de)) <br>• Win-CASA: from €398, for self-managing WEGs (vendor claim via [softwareabc24](https://www.softwareabc24.de/vergleiche/intex-hausverwaltung-vs-win-casa)) <br>• selbstverwalten.com ([GetApp](https://www.getapp.sg/software/2143724/selbstverwalten)) <br>• Lexware hausverwaltung ([data sheet](https://lex-blog.de/wp-content/uploads/2024/06/20240606_2025_Lexware_hausverwaltung_Datenblatt.pdf)) <br>Germany has 1,771,291 WEGs ([Census 2022 via EWiR](https://ewir.jura.uni-koeln.de/sites/ewir/user_upload/Praesentation_Storm.pdf)). |
| K09 | Adult child fearing an elderly parent's scam transfer → read-only bank-data alerts | **Q2** | The app's one action cannot prevent the loss. Euro-area instant transfers (send duty since 9 Oct 2025) settle in seconds ([ECB](https://www.ecb.europa.eu/paym/retail/instant_payments/html/instant_payments_regulation.ro.html)). Background bank-data refreshes without the user present are capped (PSD2 technical standard, 4 per day; background knowledge, not verified). The payer and target group are also close to the baseline's. |
| K10 | Elderly person living alone → daily WhatsApp check-in (calling or utility templates) | **Baseline rule** | Substantively the same as the BASELINE: a daily check-in with a family alert. |
| K11 | Romanian web-shop owner paying couriers twice for refused cash-on-delivery parcels → RoPay + WhatsApp Cloud API → converter from cash-on-delivery to prepaid | **SURVIVED → Finalist 1** | See card. |
| K12 | Same owner wanting WhatsApp order confirmations → plain WhatsApp confirmation bot for cash-on-delivery orders (Romania) | **H8** | Already sold locally and globally: <br>• Caty (Romania; plans €10–499/month, vendor claim) ([article](https://aws.plainenglish.io/clientul-tău-a-comandat-cine-îi-spune-că-a-plecat-coletul-caty-ecf9f9f49316)) <br>• Zarina CRM (Romania) ([site](https://www.zarinacrm.ro/automatizare-comenzi-online/)) <br>• WAPI (reports 85% average acceptance of cash-on-delivery parcels in Romania from internal, unaudited data; page attribution unconfirmed, likely [capital.ro](https://www.capital.ro/coletul-refuzat-la-livrare-o-problema-ignorata-care-costa-imm-urile-mii-de-lei-pe-an.html)) <br>• Shopify apps Confirmify (from $9.99/month) and Confirm Bot (free plan) ([Confirmify](https://apps.shopify.com/confirmify); [Confirm Bot](https://apps.shopify.com/confirm-bot)) <br>Folded into Finalist 1 as a feature. |
| K13 | Romanian merchant whose own delivery drivers carry cash → RoPay QR or Tap to Pay at the door | **H4** | Banks and processors already offer this to merchants: BRD with EuPlătesc online, and EuPlătesc's direct RoPay link from Aug 2026 ([capital.ro](https://www.capital.ro/anunt-pentru-clientii-brd-cum-se-vor-face-platile-vestea-bancii-venita-azi-18-decembrie-extinde-optiunile-de-plata.html); [revistabiz](https://www.revistabiz.ro/euplatesc-se-conecteaza-direct-la-infrastructura-transfond-acces-la-ropay-simplificat-pentru-comercianti/)). Tap-to-Pay providers cover card payments. |
| K14 | Buyer who returned a cash-on-delivery item waits weeks because the shop must ask for an IBAN → refunds to the buyer's phone number via RoPay's alias | **Q1 / Q2** | Real but low-frequency: returns are 5–15% of cash-on-delivery orders ([Packeta via economica](https://www.economica.net/alexandr-jeleascov-packeta-romania-rata-de-retur-la-magazinele-online-din-romania-este-in-crestere_625270.html/amp)). A banking app with the RoPay alias already handles it ([revistabiz](https://www.revistabiz.ro/s-a-lansat-ropay-serviciul-de-plati-instant-cu-mobilul-intre-conturi-ce-banci-l-au-implementat-deja/)). This is a feature of Finalist 1, not a business. |
| K15 | Bulgarian web shop where about 80% of orders are cash on delivery → same converter in Bulgaria | **Q7 (not a separate idea)** | Same product. Bulgaria's instant-euro obligations apply only from 1 Jan 2027, and VoP is still being implemented ([BTA](https://www.bta.bg/en/news/1072635-bulgarian-banks-99-ready-for-instant-payments-rollout-in-2027)). The roughly 80% figure is indicative, not verified ([ECDB](https://ecdb.com/blog/cash-on-delivery-is-most-used-in-middle-and-central-europe/5096)). Bulgaria is Finalist 1's second market. |
| K16 | Allotment-association treasurer billing 100 plots once a year → bank-data matching + EPC QR | **H8** | Lens 3 found three or more vertical vendors serving allotment associations ([Lens 3 notes](lens3_overlooked_niches.md)). The rails used are not new. |
| K17 | German butcher swamped by Christmas pre-orders and no-shows → WhatsApp Cloud API + instant deposits via Wero or SCT Inst → pre-order desk | **SURVIVED → Finalist 2** | Evidence is thin; see card. |
| K18 | Landlord wanting to verify a tenant's identity remotely → EU Digital Identity Wallet → wallet-based tenant pack | **H2 / Q10** | Wallets are only due by end-2026, acceptance duties by end-2027, and relying parties must register per member state ([Heuking](https://www.heuking.de/en/news-events/newsletter-articles/detail/the-new-eu-digital-identity-wallet-eudi.html); [Arthur Cox](https://www.arthurcox.com/knowledge/the-eu-digital-identity-wallet-what-companies-need-to-know/)). Nothing is sellable in 12 weeks and there is no money signal in 90 days. |
| K19 | Brazilian gym or language-school owner chasing monthly fees → Pix Automático (16 Jun 2025) → recurring-billing micro-SaaS | **Q7 / H8 (unverified)** | Banks must offer Pix Automático ([Canaltech](https://canaltech.com.br/mercado/bc-confirma-lancamento-do-pix-automatico-em-junho-de-2025-296277/)), so Brazilian payment providers bundle it. A founder with no Portuguese and no network has no evidence-based edge. Competitor density was not researched. |
| K20 | Small landlord with rooftop solar wanting to share it with tenants → smart-meter data → allocation and billing | **H2** | Needs 15-minute meter data via German energy-market roles (background knowledge, not verified). Not buildable by one person in 12 weeks. |
| K21 | Indian tourist unable to pay a small EU shop by UPI → UPI acceptance app | **H3 / H2** | Acceptance requires a licensed acquiring partner, and the app adds no deterministic value (reasoning; not researched). |
| K22 | Micro-business moving to Peppol e-invoicing → simple Peppol inbox | **Scope + H8** | Compliance-driven (covered by another researcher's lens). Many Peppol access points already exist (not researched). |
| K23 | Café owner with paper stamp cards → Apple/Google Wallet loyalty passes | **H8 (unverified)** | Crowded category, and the rail is not new (not researched in this pass). |
| K24 | Friends collecting money for a shared trip → Wero person-to-person payments | **H4 / H5** | Banks provide it free through Wero ([banking.vision](https://banking.vision/en/development-wero-2025-2026)), and organisers do not pay. |
| K25 | US contractor waiting weeks for paper checks → FedNow/RTP request-for-payment invoicing | **H2 / H4 (unverified)** | Access only through participating banks, and bank-owned person-to-person payments are free (background knowledge; FedNow not researched). |
| K26 | Caretaker who must prove snow-clearing duty → open weather data trigger + timestamped log | **Q4 / Q10** | Liability- and compliance-driven (out of this lens), winter-only, and official weather warnings are free (not researched). |
| K27 | Small salon whose SMS reminders get filtered → RCS business messaging | **H8 (unverified)** | Reminder tools are crowded, and the rail only adds branding (not researched). |

---

## (2) FINALIST IDEA CARDS

### Finalist 1: "RambursFlip" (working name). Turn cash-on-delivery orders into instantly paid orders for Romanian web shops

**Hard-rule check: all pass**

- **H1 (no AI):** deterministic rules only, no machine learning.
- **H2 (solo-buildable):** a Shopify app, a WooCommerce plugin, the WhatsApp Cloud API and payment links from payment processors, all within 12 weeks.
- **H3 (no licence):** money moves from the buyer to the merchant's own licensed processor or bank. We never hold funds.
- **H4 (platform-proof):** no single gatekeeper. We use the official WhatsApp API with an SMS/email fallback, several shop platforms and several processors.
- **H5 (real payer):** the merchant pays and saves money.
- **H6 (ethics):** messages are consented and honest, with no fake urgency.
- **H7 (no cold-start marketplace):** single-sided SaaS.
- **H8 (not crowded):** pass, on available evidence. Local tools only confirm orders. I found no tool that converts cash-on-delivery orders to prepaid ones on Romanian payment rails. The wedge is RoPay plus courier-cost economics.

**Rails used**

| Rail | What it is | Since when | Access cost to founder | Licence / certification | Verification status |
|---|---|---|---|---|---|
| RoPay | Romania's instant bank-to-bank payment service, built by TransFonD with the Romanian Banking Association. Payments by QR code, deep link, NFC or a phone-number alias. | Oct 2024 live; ING person-to-person Apr 2025; BRD online-shop payments with EuPlătesc; EuPlătesc direct connection 24 Aug 2026 | None directly. The merchant enables RoPay or cards through its processor, and we create payment links through the processor's API. EuPlătesc/Netopia API availability is an ASSUMPTION. | None: we never touch funds. | Press reports only ([revistabiz](https://www.revistabiz.ro/s-a-lansat-ropay-serviciul-de-plati-instant-cu-mobilul-intre-conturi-ce-banci-l-au-implementat-deja/), [economica](https://www.economica.net/?p=832404), [capital.ro](https://www.capital.ro/anunt-pentru-clientii-brd-cum-se-vor-face-platile-vestea-bancii-venita-azi-18-decembrie-extinde-optiunile-de-plata.html), [revistabiz Aug 2026](https://www.revistabiz.ro/euplatesc-se-conecteaza-direct-la-infrastructura-transfond-acces-la-ropay-simplificat-pentru-comercianti/)). TransFonD's own documentation was not accessible. **Merchant fees: not found.** |
| WhatsApp Business Platform (Cloud API) | Official API for business message templates and replies | Per-message pricing since 1 Jul 2025 | **Romania:** utility €0.0239 and marketing €0.0712 per message. **Service messages:** charged beyond 1,000 free per number per month from 1 Oct 2026. | Meta business verification, template approval and recipient opt-in | Pricing model verified on [Meta's docs](https://developers.facebook.com/docs/whatsapp/pricing). Romanian rates are secondary only ([Profit.ro](https://profit.ro/romania-conectata/schimbare-la-whatsapp-apare-plata-pentru-mesajele-de-asistenta-pe-whatsapp-business-api-22793043); [Zernio](https://zernio.com/whatsapp-api-pricing)). |
| Card payment links | Through the merchant's existing processor | — | Processor fees are paid by the merchant (not verified). | Processor is licensed | Stripe's payment-link API is background knowledge. Romanian processors' APIs: ASSUMPTION. |
| SMS/email fallback | — | — | About €0.03–0.05 per SMS (ASSUMPTION) | — | Not verified |

**Q1. Who suffers, when, how often, and at what cost?**

*In one sentence:* a Romanian web-shop owner who ships about 1,000 cash-on-delivery parcels a month pays the courier twice for every parcel a buyer refuses at the door, plus a cash-collection fee on the rest. Together, that can exceed €1,000 a month.

- **How often parcels fail:**
  - Returns are 5–15% of cash-on-delivery orders, depending on product category (Packeta Romania, company statement, [economica](https://www.economica.net/alexandr-jeleascov-packeta-romania-rata-de-retur-la-magazinele-online-din-romania-este-in-crestere_625270.html/amp)).
  - WAPI reports an average acceptance rate of 85% (internal, unaudited data).
- **What a parcel costs.** These are third-party 2026 estimates for FAN Courier, not official tariffs ([infocontact.ro](https://www.infocontact.ro/cat-costa-livrarea-fan-courier-2026/)):
  - A parcel up to 1 kg costs about 25–30 lei door to door.
  - The cash-on-delivery fee is about 5–9 lei.
- **Other losses:** refused parcels come back within 15 days ([BZI](https://www.bzi.ro/atentie-la-coletele-surpriza-livrate-de-fan-courier-este-incredibil-ce-teapa-era-sa-ia-un-iesean-481524)), so stock is tied up. Capital.ro reports that refusals cost small sellers thousands of lei a year ([capital.ro](https://www.capital.ro/coletul-refuzat-la-livrare-o-problema-ignorata-care-costa-imm-urile-mii-de-lei-pe-an.html)).
- **Worked example (calculation; assumptions: 1,000 orders a month, 1 € ≈ 5 lei):**
  - Refusals: 10% × about 55 lei round trip ≈ €1,100 a month.
  - Collection fees: up to about €1,400 a month, if the merchant pays them.
- **Frequency:** daily.

**Q2. What is the one thing the app does?**

Seconds after a cash-on-delivery order, the buyer gets a WhatsApp message (or SMS): confirm the order, and pay now by instant bank payment (RoPay) or card to get a small perk set by the merchant. If the buyer pays, the order switches to "prepaid" in the shop automatically. If the buyer does not confirm, the order is flagged before it ships.

**Q3. Who already solves it?**

| Name | Country | Price | What it does | Gap |
|---|---|---|---|---|
| Caty (CatyAI) | Romania | €10–€499/month (vendor's own article; not checked on a price page) | Automatic WhatsApp messages when an order is placed, when the courier waybill is generated, and on dispatch. Works with GoMag and others ([article](https://aws.plainenglish.io/clientul-tău-a-comandat-cine-îi-spune-că-a-plecat-coletul-caty-ecf9f9f49316)). VENDOR CLAIM | Evidence shows confirmation and notification only; no prepaid conversion or RoPay found. Says it does not use Meta's Cloud API, which suggests an unofficial channel with ban risk. |
| Zarina CRM | Romania | Not found | Online-shop CRM with pre-filled WhatsApp templates for order confirmation and shipping notices, plus "WhatsApp-based recovery of unpaid cash-on-delivery orders" ([site](https://www.zarinacrm.ro/automatizare-comenzi-online/)). VENDOR CLAIM | A broad CRM suite; instant-payment conversion not evidenced |
| WAPI | Romania (inferred) | Not found | WhatsApp API provider; publishes Romanian acceptance data for cash-on-delivery parcels (search summary) | Not researched |
| Confirmify (WhatsApp COD Verify) | Shopify app (global) | From $9.99/month; Starter includes 500 confirmations ([listing](https://apps.shopify.com/confirmify)) | Confirms cash-on-delivery orders via WhatsApp | Shopify-only; no Romanian payment rails |
| Confirm Bot | Shopify app (global) | Free plan + trial ([listing](https://apps.shopify.com/confirm-bot)) | Buyer replies "Confirm" or "Cancel"; the order is tagged | No payment conversion |
| CODFLIP | Shopify app (India) | Free to install; paid tiers after a free message quota; per-message rate in rupees ([listing](https://apps.shopify.com/codflip)) | Sizes a per-order discount from shipping rate, margin, destination and history; sends a WhatsApp offer with a prepaid link; supports partial cash-on-delivery and OTP | Built on Indian rails (UPI, Razorpay) |
| CashFlip | Shopify app (India) | Not found ([listing](https://apps.shopify.com/cashflip)) | WhatsApp/SMS discount offers to pay online; OTP | Focused on India |
| Verify COD | Shopify app | Not found; rated 3.2 from 20 reviews ([listing](https://apps.shopify.com/cash-on-delivery-cod-verification)) | IVR or WhatsApp confirmation plus prepaid conversion | Weak reviews; focused on India |
| DelightChat | India | Not found ([help page](https://www.delightchat.io/help-center/automatically-convert-cod-orders-to-prepaid)) | Automatic conversion to prepaid over the official WhatsApp API; creates a Shopify draft order and cancels the cash-on-delivery order once paid | Assumes Razorpay or Shopify Checkout |
| Couriers (e.g., FAN Courier) | Romania | Collection fee estimated at 5–9 lei per parcel | Collect cash; return refused parcels within 15 days | They earn the collection fee, so they have no incentive to convert |

- **Demand signal (vendor claims, India):**
  - About 15–30% of buyers convert from cash on delivery to prepaid in WhatsApp flows.
  - About 70% of those conversions happen within the first hour.
  - Sources: [bot.space](https://www.bot.space/blog/how-to-convert-cod-orders-to-prepaid-shopify), [retentionly](https://retentionly.io/post/convert-cod-to-prepaid), [hillteck](https://www.hillteck.com/blog/convert-cod-to-prepaid-shopify.html).
- **Not known:** the traction of the Romanian players.

**Q4. Why is it still unsolved? Root-cause class (b) + (d), secondarily (a)**

- **(d) A new rail.** In India this tool category matured because UPI made instant prepayment a single tap. Romania only got a comparable bank rail in Oct 2024 (RoPay). It reached online-shop processors in 2025–2026 (BRD with EuPlătesc; EuPlătesc's direct link in Aug 2026).
- **(b) Local fragmentation.** The market is local:
  - Romanian language
  - Romanian couriers
  - Local shop platforms such as GoMag and MerchantPro
  Global cash-on-delivery apps assume Indian rails and price in rupees. Local tools grew out of order confirmation, not payment conversion.
- **(a) Too small for funded global players.** The market is small for them.

**Q5. Is it profitable?**

| Line | Number | Status |
|---|---|---|
| Price: Starter | €39/month, up to 600 cash-on-delivery orders | ASSUMPTION |
| Price: Growth | €89/month, up to 2,000 cash-on-delivery orders | ASSUMPTION |
| Price: Pro | €179/month, up to 5,000 cash-on-delivery orders | ASSUMPTION |
| Meta message fees | Passed through at cost. Romania: utility €0.0239, marketing €0.0712 per message | Secondary ([Profit.ro](https://profit.ro/romania-conectata/schimbare-la-whatsapp-apare-plata-pentru-mesajele-de-asistenta-pe-whatsapp-business-api-22793043)); not checked on Meta's rate card |
| Blended revenue per customer (excluding pass-through) | €75/month | ASSUMPTION |
| Cost per customer | About €10/month: <br>• Infrastructure €3 <br>• SMS fallback €3 (about 75 SMS × €0.04) <br>• Card fee on our subscription about €1.40 <br>• Support €2.50 | ASSUMPTION |
| Rail fees paid by the merchant | RoPay or card fees on converted orders | **Not found (gap)** |
| Gross margin | (75 − 10) / 75 ≈ 87% | Calculation on ASSUMPTIONS |
| Merchant value per converted order | €1.5–3.6: <br>• Cash-collection fee of 5–9 lei (≈ €1.0–1.8) <br>• Plus avoided refusal cost: 5–15% × about 50–60 lei round trip (≈ €0.5–1.8) | Inputs are secondary estimates ([infocontact.ro](https://www.infocontact.ro/cat-costa-livrarea-fan-courier-2026/); [Packeta via economica](https://www.economica.net/alexandr-jeleascov-packeta-romania-rata-de-retur-la-magazinele-online-din-romania-este-in-crestere_625270.html/amp)). Exchange rate 1 € ≈ 5 lei is an ASSUMPTION. |
| Conversion rate to prepaid | 15–30% claimed in India; Romanian planning value 10% | India: VENDOR CLAIM ([bot.space](https://www.bot.space/blog/how-to-convert-cod-orders-to-prepaid-shopify)). Romania: ASSUMPTION |
| Merchant return on investment (worked example) | 1,000 orders × 10% × €2.50 = €250/month of value. <br>Minus the €89 price and about €34 of utility messages (1,400 × €0.0239). <br>Net to the merchant: about €127/month. | Calculation |
| Fixed business costs | €2,300/month: <br>• Romanian-speaking support and sales freelancer €600 <br>• Marketing €900 <br>• Tools and infrastructure €300 <br>• Accounting and legal €300 <br>• Events €200 | ASSUMPTION |
| **Customers needed for €8k/month profit** | (8,000 + 2,300) ÷ (75 × 0.87) ≈ 158, so **about 160 merchants** | Calculation |
| Reachable pool | Market size: <br>• Romanian online retail above €8bn in 2025 ([GoMag report via bursa.ro](https://www.bursa.ro/raport-piata-de-ecommerce-din-romania-a-depasit-8-miliarde-de-euro-in-2025-68566858)) <br>• €8.1bn per [MerchantPro via Forbes](https://forbes.ro/piata-de-ecommerce-din-romania-depaseste-8-miliarde-de-euro-in-2025-si-se-indreapta-spre-13-miliarde-pana-in-2032-492528) <br>Cash-on-delivery share: <br>• About two-thirds of orders ([Forbes RO](https://www.forbes.ro/?p=518750); an estimate without an official source) <br>• About 31bn lei of cash-on-delivery payments reported to the tax authority (ANAF) for 2024, and 18.5bn lei for Jan–Jul 2025 (secondary; page not isolated, likely [Puterea](https://www.puterea.ro/?p=526571)) <br>Number of active shops: not found. **ASSUMPTION: 10,000–20,000, so 160 merchants is 0.8–1.6%.** | Mixed |
| Lifetime value vs acquisition cost | Lifetime value ≈ €65 × 24 months ≈ €1,560 (monthly churn about 4%, ASSUMPTION). <br>Acquisition cost ≈ €250–400 (sales freelancer plus pilot, ASSUMPTION). <br>Ratio about 4–6×. | ASSUMPTION |

**Q6. How to build it**

- **MVP scope, in:**
  - A Shopify app and a WooCommerce plugin.
  - WhatsApp Cloud API templates: confirmation, payment link and one reminder. SMS fallback.
  - Payment links through Stripe and one Romanian processor that supports RoPay. If no API exists, use a bank-transfer QR with manual confirmation.
  - Automatically switch the order to "prepaid" when paid; tag unconfirmed orders as "hold".
  - A deterministic rules engine:
    - Offer the perk only above an order-value threshold.
    - Cap the perk by margin.
    - Send at most one reminder.
    - Keep quiet hours from 21:00 to 08:00.
  - A savings dashboard.
  - A consent snippet for the shop's checkout.
- **MVP scope, out:**
  - Courier waybill creation
  - Returns
  - Any AI or risk scoring
  - Holding funds
- **Stack and time:**
  - TypeScript (Node/NestJS), Postgres, a Redis job queue, a React admin, EU hosting and Stripe Billing for our own subscriptions.
  - 12 weeks.
- **12-week build outline:**
  - **W1:** 10 merchant interviews with a paid Romanian interpreter. Meta business verification. Draft Romanian templates.
  - **W2:** Shopify app skeleton (OAuth, order webhooks), data model, consent capture.
  - **W3:** WhatsApp Cloud API send and receive, template management, SMS fallback.
  - **W4:** Stripe payment-link flow. A webhook switches the order to paid. Make the updates idempotent.
  - **W5:** Romanian processor and RoPay payment link (ASSUMPTION that an API exists; fallback: bank-transfer QR).
  - **W6:** Rules engine (perk sizing, thresholds, quiet hours, reminder) and the "hold" tag.
  - **W7:** WooCommerce plugin and backend API.
  - **W8:** Dashboard showing conversion rate, refusals avoided and estimated savings. The merchant enters its own collection fee and courier price.
  - **W9:** GoMag and MerchantPro bridges if public APIs exist (ASSUMPTION); otherwise a CSV or webhook bridge.
  - **W10:** Paid pilots with 3–5 shops. Test template categories (utility vs marketing).
  - **W11:** Hardening: retries, monitoring, GDPR data-processing agreement, data retention, Romanian user interface.
  - **W12:** Shopify App Store submission, WordPress.org listing, pricing page, first case study.

**Q7. Where to launch first: Romania. Evidence:**

- **Cash on delivery dominates:**
  - About two-thirds of online orders are still paid on delivery ([Forbes RO](https://www.forbes.ro/?p=518750); an estimate).
  - About 31bn lei of cash-on-delivery payments were reported to the tax authority for 2024 (secondary).
- **The market is big and growing:**
  - Above €8bn in 2025, with about 7–8% growth and a forecast of about €13bn by 2032.
  - Online sales are only about 8.5% of retail ([bursa.ro](https://www.bursa.ro/raport-piata-de-ecommerce-din-romania-a-depasit-8-miliarde-de-euro-in-2025-68566858)).
- **Losses are measurable:** 5–15% of cash-on-delivery orders come back (Packeta), and refusals cost small sellers thousands of lei a year (capital.ro).
- **The rail is new:** RoPay since Oct 2024; online shops via processors in 2025–2026.
- **There is a gap:** local tools only confirm orders, and the Indian apps do not support Romanian payment rails.
- **Second market, Bulgaria (2027):** about 80% cash on delivery (indicative, [ECDB](https://ecdb.com/blog/cash-on-delivery-is-most-used-in-middle-and-central-europe/5096)). Its instant-euro obligations and VoP start 1 Jan 2027 ([BTA](https://www.bta.bg/en/news/1072635-bulgarian-banks-99-ready-for-instant-payments-rollout-in-2027)).
- **Third market, Greece:** 85.6% of shops accept cash on delivery. That is a share of merchants, not of orders ([Payments Industry Intelligence](https://paymentsindustryintelligence.com/?p=56417)).

**Q8. How it makes money**

- **Model:** monthly SaaS, tiered by the number of cash-on-delivery orders. WhatsApp fees are passed through at cost.
- **Payer:** the merchant, by card or SEPA direct debit through Stripe Billing. EU business-to-business reverse-charge VAT applies (ASSUMPTION).
- **Trial and pilot:** 14-day trial. A paid pilot costs €99 for 60 days, refundable if measured savings are below the fee.

**Q9. How one person runs it**

- **Support load:** about 0.2 hours per merchant per month (ASSUMPTION). That is about 32 hours a month at 160 merchants, about 10 of which go to a Romanian freelancer.
- **Automation:**
  - Self-serve onboarding
  - A pre-approved template library
  - Per-shop health checks
  - Automatic alerts when a template is rejected
- **Failure modes and mitigations:**
  1. Meta rejects or recategorises a template → SMS fallback.
  2. A processor webhook is delayed → never mark an order as paid without the webhook.
  3. A buyer pays after the parcel has shipped → cut-off rules.
  4. Meta bans the account → SMS and email keep working.
  5. A platform API changes → monitoring.
- **Peaks:** Black Friday and Christmas (ASSUMPTION).

**Q10. What did I miss? Kill tests**

- **What if the rail's owner launches the same feature?**
  - **TransFonD and banks (RoPay):** they build rails, not shop workflows. Risk: low.
  - **Processors (EuPlătesc, Netopia):** could add "pay your cash-on-delivery order now" links. Risk: medium. Mitigation: stay processor-agnostic and partner with them.
  - **Meta:** has no order-conversion logic, but it can change prices. Risk: medium. Mitigation: pass costs through.
  - **Couriers:** they earn the collection fee. Risk: low.
  - **Shop platforms (GoMag, MerchantPro, Shopify):** could add a native feature. Risk: medium-high. Mitigation: be their app partner.
- **Incumbent copy:** Caty, Zarina or WAPI could add payment links. Likelihood: high. Our edge would be RoPay depth, courier-cost analytics and speed. Switching costs are low.
- **Liability:** low, because we never hold money.
  - **GDPR and e-privacy:** marketing-type WhatsApp messages need opt-in, which is captured at checkout.
- **False assumption: Romanian buyers may pick cash on delivery because they distrust prepaying, so conversion could be below 5%.**
  - Pilot kill threshold: below 5% conversion across 1,000 cash-on-delivery orders in three shops.
  - WhatsApp reach in Romania is also an ASSUMPTION.
- **Margin trap:** if Meta classes the offer as marketing (€0.0712 per message), message costs can eat about a third of the merchant's gain.
  - Mitigation: pass costs through, and use neutral, order-related wording.
- **Churn:** merchants leave if savings are invisible. Mitigation: a monthly savings report.
- **Seasonality:** a Q4 peak, absorbed by volume tiers.

**First 10 paying customers (within 90 days, at most €2,000)**

1. Build a free Romanian "cash-on-delivery loss calculator" as the hook.
2. Hand-pick 300 Romanian Shopify or WooCommerce shops that show cash on delivery at checkout. Do this manually, so the product does not depend on scraping.
3. Have a Romanian-speaking freelance sales rep book about 30 demos (about €800).
4. Offer the €99 refundable pilot and aim for 10 paying pilots.
5. Sign 2–3 Romanian Shopify or WooCommerce agencies for a 20% referral share for 12 months.
6. Post pilot results in Romanian e-commerce communities.

Budget: about €800 sales freelancer, €400 translation and €300 ads.

---

### Finalist 2: "Vorbestell-Desk" (working name). WhatsApp pre-orders with pickup slots and instant deposits for German butchers, bakeries and farm shops

**Evidence warning:** the market and competitor facts for this card were not researched, because the search budget was exhausted. Only the rail facts are verified. Treat the H8 pass and every market number as provisional.

**Hard-rule check**

- **H1 (no AI):** rules and schedules only.
- **H2 (solo-buildable):** a web order form, the WhatsApp Cloud API, Stripe Checkout with Wero, cards and SEPA, and EPC QR as a fallback.
- **H3 (no licence):** deposits go to the shop's own Stripe account or IBAN. We never hold funds.
- **H4 (platform-proof):** narrow pass. Meta's free WhatsApp Business app has catalogues and carts but, per my ASSUMPTION, no slot capacity, production lists or deposit checks. The web form works without WhatsApp.
- **H5 (real payer):** the shop pays.
- **H6 (ethics):** pass.
- **H7 (no cold-start marketplace):** single-sided.
- **H8 (not crowded):** pass on absence of evidence only (not researched).

**Rails used**

| Rail | What it is | Since when | Access cost | Licence | Verification |
|---|---|---|---|---|---|
| Wero via a payment provider such as Stripe | Bank-owned instant bank-to-bank payment at checkout | German online payments live since Nov 2025; Stripe is among the supporting payment providers | Payment-provider fees: not verified | None (payment provider licensed) | [The Paypers](https://thepaypers.com/payments/news/wero-ecommerce-is-now-live-in-germany); [Wero](https://wero-wallet.eu/news/wero-ecommerce-germany) |
| SEPA Instant + VoP | The deposit arrives in seconds; the payer sees the shop's verified name | Euro area since 9 Oct 2025 | Priced no higher than a standard transfer | None | [ECB](https://www.ecb.europa.eu/paym/retail/instant_payments/html/instant_payments_regulation.ro.html); [BTA](https://www.bta.bg/en/news/1072635-bulgarian-banks-99-ready-for-instant-payments-rollout-in-2027) |
| WhatsApp Cloud API | Customers order where they already chat | Per-message pricing since 1 Jul 2025. Utility templates are free inside a 24-hour window opened by the customer. Service messages are charged beyond 1,000 free per month from 1 Oct 2026 (secondary). | German rates: not verified (ASSUMPTION €0.03–0.05 per utility template) | Meta verification | [Meta](https://developers.facebook.com/docs/whatsapp/pricing); [Zernio](https://zernio.com/whatsapp-api-pricing) |
| EPC QR ("GiroCode") | Bank-transfer QR code read by banking apps | Long-standing standard (background) | Free | None | Not verified in this pass |

**Q1. Who suffers?**

*In one sentence:* a German butcher who sells hundreds of Christmas roasts, geese and platters spends the four weeks before the holidays writing phone orders on paper slips. Meat and money are lost when customers do not collect, and the queue on 23 December drives regulars away.

- Every number in this description is an ASSUMPTION.
- The pain is highest at Christmas and Easter, plus year-round party-platter orders.

**Q2. The one thing**

Customers order by WhatsApp or a link, pick a pickup slot with limited capacity, and pay a deposit instantly (Wero, bank transfer or card). The shop gets one production list per day and automatic pickup reminders.

**Q3. Who already solves it?**

Not researched. The H8 call rests on absence of evidence.

| Name | Country | Price | What it does | Gap |
|---|---|---|---|---|
| WhatsApp Business app (Meta) | Global | Free (background) | Catalogue, cart, quick replies | No slot capacity, deposit check or production list (ASSUMPTION) |
| Online-shop builders (Shopify and similar) | Global | Not researched | Online ordering | Not built for slots, deposits or production lists (ASSUMPTION) |
| Pre-order modules from point-of-sale or scale vendors | Germany | Not researched | Possibly pre-ordering | Unknown; **the biggest open risk** |
| Phone plus paper | — | Free | Status quo | Errors, no-shows, queues |

**Q4. Root-cause class (a) + (e) + (d)**

- **(a) and (e) Small and unglamorous.** By hypothesis, butchers are too small and too seasonal for funded SaaS companies, and ordering platforms target restaurants and delivery.
- **(d) New rails.** The rails only recently made the fix cheap:
  - An official per-message WhatsApp API that a solo founder can use directly (2025)
  - Instant, name-checked bank deposits (Oct 2025)
  - Wero at checkout (Nov 2025)

**Q5. Is it profitable?**

| Line | Number | Status |
|---|---|---|
| Price | €35/month billed yearly (€420/year), or €59/month billed monthly; a €149 Christmas-season pilot | ASSUMPTION |
| Cost per customer | About €7/month: <br>• About 600 business-initiated reminders a year × €0.04 ≈ €2/month <br>• Hosting €1 <br>• Subscription payment fees about €1 <br>• Support €3 (peak-heavy) | ASSUMPTION |
| Rail fees paid by the shop | Wero, card or SEPA fees on deposits | Not verified |
| Gross margin | (35 − 7) / 35 = 80% | Calculation on ASSUMPTIONS |
| Fixed business costs | €1,800/month | ASSUMPTION |
| **Customers needed for €8k/month profit** | (8,000 + 1,800) ÷ 28 ≈ **350 shops** | Calculation |
| Reachable pool | About 10,000 butchers + about 9,000 bakeries + farm shops ≈ 20,000; so 350 shops is about 1.75% | ASSUMPTION (craft counts are background knowledge, not verified) |
| Lifetime value vs acquisition cost | Churn about 2.5%/month on yearly billing gives about €1,120 lifetime value. Acquisition cost about €150–300 (guild talks, demos). Ratio about 4–7×. | ASSUMPTION |

**Q6. How to build it**

- **MVP:**
  - Shop setup: products, slots and capacity.
  - Customer order flow by web link and WhatsApp.
  - Deposit through Stripe Checkout (Wero, card, SEPA) or EPC QR.
  - Automatic confirmation, plus a reminder the day before pickup.
  - A daily production list as PDF or print.
  - Pickup check-off on a tablet.
- **Stack and time:** Django or Node, Postgres, the WhatsApp Cloud API and Stripe. 12 weeks.
- **12-week outline:**
  - **W1:** Interview 10 butchers or bakeries. Run a concierge pilot using forms and the WhatsApp Business app, aimed at Christmas 2026.
  - **W2–3:** Products, slots and capacity data model; shop admin.
  - **W4:** Customer order flow on the web.
  - **W5:** WhatsApp Cloud API: inbound order intent and outbound utility templates.
  - **W6:** Stripe Checkout with Wero, cards and SEPA; EPC QR fallback; deposit status.
  - **W7:** Production lists and pickup check-off.
  - **W8:** Reminders and no-show handling (deposit kept or refunded by shop policy).
  - **W9:** Billing and onboarding wizard.
  - **W10–11:** Pilot hardening at Easter 2027.
  - **W12:** Launch for Christmas 2027 sales.

**Q7. Where to launch first: Germany**

- **Verified evidence:** Wero is live for online payments first in Germany (Nov 2025), and euro-area instant payments with VoP are mandatory (Oct 2025).
- **Background, not verified:** Germany has a dense craft-food retail sector and a preference for bank payments.
- **Caveat:** the gap itself is unverified.

**Q8. How it makes money**

- Annual subscription paid by the shop, by SEPA direct debit or card.
- The paid concierge "season pilot" doubles as the speed-to-proof test.

**Q9. How one person runs it**

- **Support load:** low most of the year, and peaking in November–December and before Easter. So onboarding must close by October.
- **Failure modes and fallbacks:**
  - WhatsApp is down or a template is rejected → the web form still works.
  - Payment provider issues → EPC QR.
  - Capacity bugs → a manual override.

**Q10. Kill tests**

- **What if the rail's owner launches the same feature?**
  - **Meta** adds slots or deposits to WhatsApp Business. Risk: low-medium.
  - **Wero or payment providers** add payment links (likely), but these cover only the deposit, not slots or production lists.
- **Incumbent copy:** point-of-sale and scale vendors add pre-order modules. Risk: medium-high. **This is unverified and must be checked first.**
- **Seasonality:** churn after Christmas. Mitigation: yearly billing plus year-round platter orders.
- **False assumption:** older customers may refuse to prepay a local butcher. The pilot will measure the deposit rate.
- **Data protection:** WhatsApp use in Germany needs a data-processing agreement and consent.
- **Liability:** low.

**First 10 paying customers (within 90 days, at most €2,000)**

Today is 12 Oct 2026, so Christmas 2026 is about 10 weeks away. The plan:

1. Sell a **€149 concierge "Christmas 2026" pilot** to shops within 50 km.
2. Run it on Google Forms, Stripe/Wero payment links, the WhatsApp Business app and a manually built production list.
3. Ask regional butcher and baker guilds for 15-minute slots at member meetings.
4. Cold-visit shops with a printed demo.

Target: 10 paid pilots by mid-November. Budget: about €600 travel and €300 print and ads.

---

### Finalist 3: "WP-Wächter" (working name). Monthly efficiency check and fix list for German heat-pump owners

**Hard-rule check**

- **H1 (no AI):** deterministic rules: coefficient-of-performance calculation, compressor-start counting, backup-heater runtime, and heating curve against outdoor temperature.
- **H2 (solo-buildable):** a web app, manual meter entry and two official maker APIs.
- **H3 (no licence):** pass.
- **H4 (platform-proof): narrow pass.**
  - Only official maker APIs are used; Vaillant's reverse-engineered API is excluded.
  - A manual-entry path works for every brand.
  - Multiple makers, plus the Data Act right, reduce revocability.
  - **Remaining risk:** makers' apps could add the same diagnosis.
- **H5 (real payer):** the homeowner.
- **H6 (ethics):** pass.
- **H7 (no cold-start marketplace):** pass.
- **H8 (not crowded):** not researched. Pass on absence of evidence only.

**Rails used**

| Rail | What it is | Since when | Access cost | Licence | Verification |
|---|---|---|---|---|---|
| EU Data Act | Users can access their product data and have it sent to a third party they choose | Applicable 12 Sep 2025; access-by-design for products placed on the market from 12 Sep 2026 | Free to the user; third-party compensation rules not verified | None | Law-firm summaries ([SCL](https://www.scl.org/eu-data-act-in-force-from-12-september-2025/), [Clifford Chance](https://www.cliffordchance.com/insights/resources/blogs/talking-tech/en/articles/2025/09/eu-data-act--a-new-era-for-data-sharing-has-begun.html)). Maker Data Act pages: [Viessmann](https://developer.viessmann-climatesolutions.com/start/EU-Data-Act.html), [Vaillant](https://vaillant.com/eu-data-act/), [iDM](https://www.idm-energie.at/en/eu-data-act/) |
| Viessmann API | Official developer portal using the ViCare login | Available now | **Basic (free):** a 24-hour block after 120 calls in 10 minutes or 1,450 calls in 24 hours. **Paid plans:** 3,000 calls per 24 hours. **Some consumption data points** only appear on the paid "Advanced" plan, reported at €19.99/month in a forum. | Developer registration; **commercial multi-user terms unknown** | [Home Assistant docs](https://www.home-assistant.io/integrations/vicare); [Viessmann community](https://community.viessmann.de/t5/The-Viessmann-API/heating-power-consumption-dhw-via-API/m-p/427483); [Homey forum](https://community.homey.app/t/app-pro-viessmann-vicare-app-for-homey-pro/118749?page=2) |
| Daikin Onecta Cloud API | Official cloud API | Available now | Default 200 calls per day and 20 per minute; business partners get 200 calls per user per day. EMEA only. "Not suitable for reactive control." | Developer or partner registration | [Homey forum](https://community.homey.app/t/app-pro-and-cloud-daikin-onecta/54088/338); [GitHub library](https://github.com/Apollon77/daikin-controller-cloud); [Daikin portal](https://www.daikinmea.com/en_us/product-group/control-systems/daikin-developer-portal.html) |
| Vaillant (excluded) | Data Act notice lists data types with intervals from "on change" to daily, but publishes no third-party interface | — | — | Only a reverse-engineered API exists, so it is **not used** (H4) | [Vaillant](https://vaillant.com/eu-data-act/); [myPyllant](https://pypi.org/project/myPyllant/0.0.8); [Home Assistant forum, quota cut Oct 2025](https://community.home-assistant.io/t/myvaillant-integration/542610?page=24) |
| Manual monthly readings + open weather data from the German weather service (DWD) | The user types in meter values once a month; heating degree-days come from the weather service | Background | Free | None | DWD open data not verified in this pass |

**Q1. Who suffers?**

*In one sentence:* a German homeowner who swapped a gas boiler for a heat pump cannot tell whether a heating curve set too high, short-cycling or a running backup heater is quietly wasting part of a four-figure electricity bill. Installers rarely come back, and the maker's app shows numbers, not a diagnosis.

- **Verified:** about 299,000 heat pumps were sold in Germany in 2025 alone ([solarserver/BWP](https://www.solarserver.de/2026/01/27/bwp-waermepumpen-absatz-um-55-prozent-in-2025-gestiegen/)).
- **ASSUMPTION:** the size of the bill and the share wasted.
- **Frequency:** monthly bills, heating season.

**Q2. The one thing**

Every month the app calculates the heat pump's real efficiency, adjusted for weather. It sends a short fix list ("heating curve 4 K too high", "backup heater ran 14 h") that the owner can hand to the installer.

**Q3. Who already solves it?**

| Name | Country | Price | What it does | Gap |
|---|---|---|---|---|
| ViCare app (Viessmann) | Germany | Free (ASSUMPTION) | Control; users report consumption is visible in the app | Diagnosis not evidenced. Some API consumption data needs a paid plan. |
| myVAILLANT app | Germany | Free (ASSUMPTION) | Control and data; Data Act notice | No official third-party API |
| Daikin Onecta app | Japan/EU | Free (ASSUMPTION) | Control; official API | API is rate-limited |
| Home Assistant + ViCare / myPyllant integrations | Global | Free (do-it-yourself) | Dashboards | Needs technical skill; the Vaillant route is unofficial |
| Installer maintenance contract | Germany | Not verified | Yearly service | Data-driven tuning is rare (ASSUMPTION) |

**Q4. Root-cause class (d) + (c) + (a)**

- **(d) A new right:** the Data Act (Sep 2025) and official maker APIs only recently made third-party analysis legal and possible.
- **(c) Pain and payer split:** the homeowner feels the pain, but the installer controls the settings.
- **(a) Too small:** the opportunity is small for funded companies.

**Q5. Is it profitable?**

| Line | Number | Status |
|---|---|---|
| Price | €4.99/month or €49/year, VAT included (net €4.19/month) | ASSUMPTION |
| Cost per customer | About €0.88/month: <br>• Payment fee €0.33 <br>• Hosting €0.15 <br>• Share of the API plan €0.10 <br>• Support €0.30 | ASSUMPTION |
| Gross margin | About 79% | Calculation on ASSUMPTIONS |
| Fixed business costs | €1,800/month | ASSUMPTION |
| **Customers needed for €8k/month profit** | 9,800 ÷ 3.31 ≈ **3,000 subscribers** | Calculation |
| Reachable pool | **Units sold 2023–2025 ≈ 846k–848k (VERIFIED by summing):** <br>• 354k–356k in 2023 ([EMA](https://ema-energiewelt.de/wissen/waermepumpen-markt-2026-bwp-absatz-prognose); [ingenieur.de](https://www.ingenieur.de/fachmedien/hlh/die-talsohle-ist-erreicht/)) <br>• 193k in 2024 <br>• 299k in 2025 <br>About 80% of installs are in existing buildings, and 95% are air-to-water ([solarserver](https://www.solarserver.de/2026/05/22/heizungsbestand-2025-waermewende-stockt/)). **ASSUMPTION:** 25–40% are supported, online brands, so 3,000 subscribers is about 1–1.4% of the pool. | Mixed |
| Lifetime value vs acquisition cost | Churn about 5%/month (the value is front-loaded), so lifetime value ≈ €66. Acquisition cost via communities and YouTube ≈ €15–30. Ratio about 2–4×. | ASSUMPTION |

**Q6. How to build it**

- **MVP:**
  - Manual monthly readings plus weather adjustment (degree-days).
  - Daikin and Viessmann connectors with rate-limit schedulers.
  - Rules engine v1, a monthly PDF report and alerts.
- **12-week outline:**
  - **W1:** Interviews; weather-data pipeline.
  - **W2:** Manual-reading flow and efficiency calculation.
  - **W3:** Viessmann connector (check Basic vs paid plan and commercial terms).
  - **W4:** Daikin connector (scheduler within 200 calls per day).
  - **W5:** Rules v1.
  - **W6:** Monthly report.
  - **W7:** Benchmarks and alerts.
  - **W8:** Billing.
  - **W9:** A third official API if one exists (ASSUMPTION).
  - **W10:** 30-user beta.
  - **W11:** Templates for Data Act data requests to unsupported makers (experimental).
  - **W12:** Launch.

**Q7. Where to launch first: Germany**

- **Largest recent install base:** about 847k units sold in 2023–2025, mostly retrofits where settings matter most.
- **API scope:** Daikin's API is EMEA-only.
- **Why not the UK:** not researched.

**Q8. How it makes money**

- Consumer subscription billed on the web, avoiding app-store fees.
- The yearly plan is pushed before the heating season.

**Q9. How one person runs it**

- **Main operational risk:** API rate limits.
- **Viessmann scaling risk:** if the 1,450-calls-per-day Basic limit applies per app rather than per user, it caps the business at about 60 hourly-polled users. A commercial agreement would then be required (unknown).
- **Support:** answering technical questions; keep scope to "recommendations to discuss with your installer".

**Q10. Kill tests**

- **What if the rail's owner launches the same feature?** Makers (the data holders under the Data Act) add efficiency diagnosis to their free apps. Risk: high. This is the main reason the C8 score is 3.
- **Data access:**
  - Vaillant (a top brand) has no official API.
  - Viessmann's consumption data may require a paid plan.
  - Daikin is capped at 200 calls per day.
  - The Data Act's practical machinery is still request-based.
- **Churn:** high once the first fixes are applied.
- **Seasonality:** summer cancellations.
- **Liability:** if the user changes settings and causes damage. Mitigation: route changes through the installer.

**First 10 paying customers**

1. Post a free "heating curve check" in German heat-pump owner communities (forums such as [haustechnikdialog](https://www.haustechnikdialog.de/Forum/t/271077/Auslesen-Daten-Vaillant-Arotherm-Plus); Facebook groups not verified).
2. Sponsor two German heat-pump YouTubers at about €300 each (ASSUMPTION).
3. Pre-sell a €39 "founding season".

---

## (3) PROVISIONAL SCORES (C1–C10; weighted total = sum of score × weight ÷ 10)

**Baseline (reference, scored the same way). Daily check-in call for people aged 65+ in Germany: 57.5 → KILL band (just under the 60 TEST line)**

| Criterion (weight) | Score | One-line justification |
|---|---|---|
| C1 Pain (10) | 6 | Rare but catastrophic risk for the senior, plus daily low-level worry for the family. |
| C2 Willingness to pay (15) | 6 | The family pays €9.90; payer is clear, but the free substitute is "I'll call Mum myself". |
| C3 Gap realness (10) | 6 | Device-based Hausnotruf costs €27–40 and is subsidised only with a care grade; a phone-only gap is plausible. |
| C4 Distribution (15) | 5 | No cheap named channel to adult children of over-65s. |
| C5 Unit economics (15) | 5 | €9.90 including VAT is €8.32 net; with €3 cost, gross margin is about 64% (below 70%). |
| C6 Market sufficiency (5) | 9 | About 1,000 families out of millions. |
| C7 Solo operability (10) | 6 | Simple telephony, but false alarms and an expectation of 24/7 reliability. |
| C8 Durability (10) | 5 | Easy to copy; Hausnotruf providers could add a phone-only tier. |
| C9 Risk, inverse (5) | 5 | Liability if an alert is missed. |
| C10 Speed to proof (5) | 7 | A landing page and pre-sale are feasible. |
| **Weighted total** | **57.5** | |

**Finalist 1: RambursFlip (Romania) → 66.0, TEST**

| Criterion (weight) | Score | One-line justification |
|---|---|---|
| C1 Pain (10) | 7 | Daily, measurable losses: 5–15% of cash-on-delivery orders come back, and each parcel pays a collection fee. |
| C2 Willingness to pay (15) | 8 | The merchant pays from savings; paid local tools (Caty from €10/month) show willingness to pay. |
| C3 Gap realness (10) | 6 | Proven in India, but no Romanian prepaid converter found and RoPay only reached processors in 2025–26; search coverage was limited. |
| C4 Distribution (15) | 6 | Shopify and WordPress directories, agencies and Romanian e-commerce communities; but a language barrier and no network. |
| C5 Unit economics (15) | 7 | About 87% gross margin with message pass-through; lifetime value about 4–6× acquisition cost on assumptions. |
| C6 Market sufficiency (5) | 7 | Needs about 160 merchants out of an assumed 10–20k shops (0.8–1.6%). |
| C7 Solo operability (10) | 6 | Several integrations, plus Romanian-language support through a freelancer. |
| C8 Durability (10) | 5 | Easy for Caty, Zarina or GoMag to copy; switching costs are low. |
| C9 Risk, inverse (5) | 7 | No funds handled; the main risk is GDPR consent for messages. |
| C10 Speed to proof (5) | 7 | Paid €99 pilots with 3–5 shops within 60–90 days for under €2k. |
| **Weighted total** | **66.0** | **Beats the baseline by 8.5 points.** |

**Finalist 2: Vorbestell-Desk (Germany) → 60.0, TEST (marginal; evidence-thin)**

| Criterion (weight) | Score | One-line justification |
|---|---|---|
| C1 Pain (10) | 6 | Intense at Christmas and Easter, moderate the rest of the year (ASSUMPTION). |
| C2 Willingness to pay (15) | 6 | The shop owner pays to avoid no-shows and phone chaos; the €35/month price is untested. |
| C3 Gap realness (10) | 4 | Competitors were not researched, so there is no evidence of a gap. |
| C4 Distribution (15) | 6 | Guild meetings and local cold visits are cheap and named, but slow. |
| C5 Unit economics (15) | 6 | About 80% gross margin; seasonal churn risk. |
| C6 Market sufficiency (5) | 7 | About 350 shops out of an assumed 20k (about 1.75%). |
| C7 Solo operability (10) | 7 | Simple product; support peaks before holidays. |
| C8 Durability (10) | 5 | Point-of-sale or scale vendors could add pre-ordering. |
| C9 Risk, inverse (5) | 8 | Payment providers handle funds; low liability. |
| C10 Speed to proof (5) | 7 | A concierge Christmas 2026 pilot can be sold within 90 days. |
| **Weighted total** | **60.0** | **Beats the baseline by 2.5 points, which is within scoring noise.** |

**Finalist 3: WP-Wächter (Germany) → 55.0, KILL band**

| Criterion (weight) | Score | One-line justification |
|---|---|---|
| C1 Pain (10) | 6 | Real money, but invisible to the owner; monthly. |
| C2 Willingness to pay (15) | 5 | Homeowner willingness to pay for €4.99/month is uncertain, and the value is front-loaded. |
| C3 Gap realness (10) | 5 | Maker apps and do-it-yourself tools exist; the diagnosis gap is unverified. |
| C4 Distribution (15) | 6 | Active owner forums and YouTube are cheap channels. |
| C5 Unit economics (15) | 6 | About 79% gross margin, but churn after the first fixes limits lifetime value. |
| C6 Market sufficiency (5) | 8 | About 3,000 users out of about 847k units sold 2023–25. |
| C7 Solo operability (10) | 5 | Fragile API limits and paid tiers. |
| C8 Durability (10) | 3 | Makers can ship the same feature, and data access is controlled per maker. |
| C9 Risk, inverse (5) | 7 | Advice routed through the installer. |
| C10 Speed to proof (5) | 6 | Community pre-sales are feasible. |
| **Weighted total** | **55.0** | **Does not beat the baseline.** |

**Plain verdict against the baseline**

- **Only Finalist 1 beats the baseline by a margin larger than scoring noise.**
- **Finalist 2's lead (2.5 points) depends on unverified competitor and market data.**
- **Finalist 3 does not beat the baseline.**
- **Sensitivity:** if the evaluators score the baseline at 60 or higher, only Finalist 1 beats it. If they score it at 66 or higher, none of my finalists beats it.

---

## (4) SOURCES

Labels: official, law firm, press, vendor claim, forum, older, secondary.

**Payment rails and regulation**

- ECB, Instant Payments Regulation deadlines (official): https://www.ecb.europa.eu/paym/retail/instant_payments/html/instant_payments_regulation.ro.html
- BTA, Bulgarian banks and the IPR from 1 Jan 2027, price parity and free VoP (press): https://www.bta.bg/en/news/1072635-bulgarian-banks-99-ready-for-instant-payments-rollout-in-2027
- ECB news, Bulgarian banks connected to T2/TIPS (official): https://www.ecb.europa.eu/press/intro/news/html/ecb.mipnews260102.en.html
- BORICA, VoP provider in Bulgaria: https://www.borica.bg/en/latest
- Hogan Lovells, PSD3/PSR provisional agreement (law firm): https://www.hoganlovells.com/en/publications/final-texts-for-psd3-and-psr-awaited-as-european-parliament-and-council-of-eu-announce-provisional
- JD Supra, PSD3/PSR timeline (law firm): https://www.jdsupra.com/legalnews/psd3-and-the-payment-services-4770204/
- Dudkowiak, PSD3/PSR final texts (law firm): https://www.dudkowiak.com/blog/psd3-and-psr-final-texts-agreed-new-obligations-for-payment-institutions/
- European Parliament Legislative Train, PSD3 (official): https://www.europarl.europa.eu/legislative-train/theme-an-economy-that-works-for-people/file-payment-services-and-electronic-money-services-(directive)
- GoCardless, Bank Account Data announcement (vendor): https://gocardless.com:443/bank-account-data/announcement
- The Paypers, Wero online payments live in Germany (press): https://thepaypers.com/payments/news/wero-ecommerce-is-now-live-in-germany
- Wero, online payments in Germany (vendor): https://wero-wallet.eu/news/wero-ecommerce-germany
- Nexi, Wero for German online shops, Apr 2026 (vendor): https://www.nexigroup.com/en/media-relations/news/2026/04/wero-for-ecommerce-in-germany/
- banking.vision, Wero 2025–2026 (press): https://banking.vision/en/development-wero-2025-2026
- Canaltech, Pix Automático June 2025 (press): https://canaltech.com.br/mercado/bc-confirma-lancamento-do-pix-automatico-em-junho-de-2025-296277/
- Correio da Manhã, Pix Automático launch event (press PDF): https://digital.correiodamanha.com.br/jornalcorreiodamanha/2025/06/05/0006d8/pdf/0506cmanha06.pdf
- Mercado&Consumo, Pix Automático modalities (press, 2024): https://mercadoeconsumo.com.br/20/09/2024/meios-de-pagamento/pix-automatico-sera-mais-flexivel-e-tera-quatro-possibilidades-de-contratacao/
- RoPay launch (revistabiz, Oct 2024): https://www.revistabiz.ro/s-a-lansat-ropay-serviciul-de-plati-instant-cu-mobilul-intre-conturi-ce-banci-l-au-implementat-deja/
- RoPay at ING (economica.net): https://www.economica.net/?p=832404
- RoPay at BRD for online shops (capital.ro): https://www.capital.ro/anunt-pentru-clientii-brd-cum-se-vor-face-platile-vestea-bancii-venita-azi-18-decembrie-extinde-optiunile-de-plata.html
- EuPlătesc direct RoPay connection (revistabiz, Aug 2026): https://www.revistabiz.ro/euplatesc-se-conecteaza-direct-la-infrastructura-transfond-acces-la-ropay-simplificat-pentru-comercianti/
- RoPay participating banks (Mobilissimo): https://www.mobilissimo.ro/stiri-telefoane/platile-devin-instant-cu-ropay-ce-banci-participa-si-care-sunt-avantajele-noului-sistem-de-plati-romanesc

**Messaging, card acceptance, identity**

- Meta, WhatsApp Business Platform pricing (official): https://developers.facebook.com/docs/whatsapp/pricing and https://developers.facebook.com/documentation/business-messaging/whatsapp/pricing
- Profit.ro, Romanian WhatsApp rates from 1 Oct 2026 (press, secondary): https://profit.ro/romania-conectata/schimbare-la-whatsapp-apare-plata-pentru-mesajele-de-asistenta-pe-whatsapp-business-api-22793043
- Zernio, WhatsApp pricing calculator (vendor): https://zernio.com/whatsapp-api-pricing
- Kommo, WhatsApp rate changes on 1 Jul 2026 (vendor): https://support.kommo.com/docs/updated-pricing-rules-for-whatsapp-business.md
- Apple Newsroom, Tap to Pay expansion Sep 2025 (official): https://www.apple.com/uk/newsroom/2025/09/apple-expands-tap-to-pay-on-iphone-to-five-more-countries-across-europe/
- Apple Newsroom, Tap to Pay expansion Mar 2025 (official): https://www.apple.com/pt/newsroom/2025/03/apple-introduces-tap-to-pay-on-iphone-in-more-european-countries
- MacTech, 43 countries (press): https://www.mactech.com/2025/09/23/apple-expands-tap-to-pay-on-iphone-to-five-more-countries-across-europe/amp/
- Heuking, EU Digital Identity Wallet (law firm): https://www.heuking.de/en/news-events/newsletter-articles/detail/the-new-eu-digital-identity-wallet-eudi.html
- Arthur Cox, EU Digital Identity Wallet (law firm): https://www.arthurcox.com/knowledge/the-eu-digital-identity-wallet-what-companies-need-to-know/
- eIDEasy, wallet acceptance 2027 (vendor): https://eideasy.com/blog/eu-digital-identity-wallet-acceptance-2027

**Data Act, energy, heat pumps**

- SCL, Data Act applicable from 12 Sep 2025 (legal): https://www.scl.org/eu-data-act-in-force-from-12-september-2025/
- Clifford Chance, Data Act (law firm): https://www.cliffordchance.com/insights/resources/blogs/talking-tech/en/articles/2025/09/eu-data-act--a-new-era-for-data-sharing-has-begun.html
- Servitly, Data Act in heating and cooling (vendor): https://www.servitly.com/post/the-impact-of-the-eu-data-act-in-the-hvac-industry-an-analysis-for-manufacturers-and-third-parties
- iDM, Data Act page (maker): https://www.idm-energie.at/en/eu-data-act/
- Viessmann, Data Act page (maker): https://developer.viessmann-climatesolutions.com/start/EU-Data-Act.html
- Vaillant, Data Act page (maker): https://vaillant.com/eu-data-act/
- Home Assistant, ViCare integration and rate limits (docs): https://www.home-assistant.io/integrations/vicare
- Viessmann community, consumption data on the Basic plan (forum): https://community.viessmann.de/t5/The-Viessmann-API/heating-power-consumption-dhw-via-API/m-p/427483
- Homey forum, Viessmann Advanced plan €19.99 (forum): https://community.homey.app/t/app-pro-viessmann-vicare-app-for-homey-pro/118749?page=2
- Homey forum, Daikin limits (forum): https://community.homey.app/t/app-pro-and-cloud-daikin-onecta/54088/338
- GitHub, daikin-controller-cloud (developer): https://github.com/Apollon77/daikin-controller-cloud
- Daikin developer portal page (maker): https://www.daikinmea.com/en_us/product-group/control-systems/daikin-developer-portal.html
- myPyllant, reverse-engineered Vaillant API (developer): https://pypi.org/project/myPyllant/0.0.8
- Home Assistant forum, myVAILLANT quota cut Oct 2025 (forum): https://community.home-assistant.io/t/myvaillant-integration/542610?page=24
- haustechnikdialog, Vaillant data readout (forum): https://www.haustechnikdialog.de/Forum/t/271077/Auslesen-Daten-Vaillant-Arotherm-Plus
- Solarserver/BWP, 2025 heat-pump sales (press): https://www.solarserver.de/2026/01/27/bwp-waermepumpen-absatz-um-55-prozent-in-2025-gestiegen/
- EMA Energiewelt, 2023 and 2024 sales (press): https://ema-energiewelt.de/wissen/waermepumpen-markt-2026-bwp-absatz-prognose
- ingenieur.de, 2023 sales (press): https://www.ingenieur.de/fachmedien/hlh/die-talsohle-ist-erreicht/
- Solarserver, heating stock 2025 (press): https://www.solarserver.de/2026/05/22/heizungsbestand-2025-waermewende-stockt/
- preisvergleich.de, §41a EnWG 2025 (secondary): https://strom.preisvergleich.de/news/40421/das-aendert-sich-2025/
- greenox, dynamic tariffs and smart-meter cost (vendor): https://greenox-group.de/dynamischer-stromtarif/
- smartblue Smart Monitor (vendor): https://www.smartblue.de/produkte/smart-monitor/
- rfp.wiki, Solar-Log (review site): https://www.rfp.wiki/vendors/solar-log
- ikz, solar monitoring overview (older, undated): https://www.ikz.de/uploads/media/PV-Ueberwachung.pdf
- Fronius, apps and software (maker): https://www.fronius.com/de/solarenergie/solarloesungen/apps-software

**Cash on delivery and Romanian online retail**

- Forbes România, about two-thirds of orders paid cash on delivery (press; estimate): https://www.forbes.ro/?p=518750
- Capital.ro, refused parcels cost small sellers (press): https://www.capital.ro/coletul-refuzat-la-livrare-o-problema-ignorata-care-costa-imm-urile-mii-de-lei-pe-an.html
- Economica.net, Packeta: 5–15% returns on cash-on-delivery orders (press; company statement): https://www.economica.net/alexandr-jeleascov-packeta-romania-rata-de-retur-la-magazinele-online-din-romania-este-in-crestere_625270.html/amp
- Puterea.ro, Temu/Shein and cash-on-delivery volume; likely source of the tax-authority figures, unconfirmed (press): https://www.puterea.ro/?p=526571
- Fiscalitatea.ro, emergency ordinance 67/2022: couriers report cash-on-delivery payers to the tax authority (press, older 2022): https://www.fiscalitatea.ro/oug-672022-curierii-vor-transmite-la-anaf-informatii-despre-persoanele-care-au-platit-ramburs-comenzile-facute-online-21870/
- Infocontact.ro, FAN Courier price estimates 2026 (third-party estimate): https://www.infocontact.ro/cat-costa-livrarea-fan-courier-2026/
- BZI.ro, refused parcels returned within 15 days (press): https://www.bzi.ro/atentie-la-coletele-surpriza-livrate-de-fan-courier-este-incredibil-ce-teapa-era-sa-ia-un-iesean-481524
- Wall-street.ro, FAN Courier 2025 revenue of 1.5bn lei (press): https://www.wall-street.ro/articol/ecommerce/fan-courier-rezultate-financiare.html
- Bursa.ro, GoMag eCommerce Pulse 2026 (press; vendor report): https://www.bursa.ro/raport-piata-de-ecommerce-din-romania-a-depasit-8-miliarde-de-euro-in-2025-68566858
- Forbes.ro, MerchantPro report: €8.1bn (press; vendor report): https://forbes.ro/piata-de-ecommerce-din-romania-depaseste-8-miliarde-de-euro-in-2025-si-se-indreapta-spre-13-miliarde-pana-in-2032-492528
- Agerpres, 2025 forecast (press): https://agerpres.ro/economic/2025/03/12/piata-ecommerce-din-romania-va-depasi-valoarea-de-8-8-miliarde-de-euro-in-acest-an-estimari--1430016
- ECDB, cash on delivery in middle and central Europe (data vendor): https://ecdb.com/blog/cash-on-delivery-is-most-used-in-middle-and-central-europe/5096
- Payments Industry Intelligence, cash on delivery across Europe (press): https://paymentsindustryintelligence.com/?p=56417
- BigArena, cash on delivery as the default in Romania, Bulgaria and Greece (vendor): https://bigarena.net/en/blog/cash-on-delivery-europe-guide
- DHL cash-on-delivery table (vendor; column misalignment, so unreliable): https://www.dhl.de/en/geschaeftskunden/paket/leistungen-und-services/internationaler-versand/paket-international/nachnahme-export.html

**Competitors for cash-on-delivery tools**

- Caty article (vendor): https://aws.plainenglish.io/clientul-tău-a-comandat-cine-îi-spune-că-a-plecat-coletul-caty-ecf9f9f49316
- Zarina CRM (vendor): https://www.zarinacrm.ro/automatizare-comenzi-online/
- Confirmify: https://apps.shopify.com/confirmify
- Confirm Bot: https://apps.shopify.com/confirm-bot
- CODFLIP: https://apps.shopify.com/codflip
- CashFlip: https://apps.shopify.com/cashflip
- Verify COD: https://apps.shopify.com/cash-on-delivery-cod-verification
- DelightChat (vendor): https://www.delightchat.io/help-center/automatically-convert-cod-orders-to-prepaid
- bot.space, 15–30% conversion claim (vendor): https://www.bot.space/blog/how-to-convert-cod-orders-to-prepaid-shopify
- retentionly (vendor): https://retentionly.io/post/convert-cod-to-prepaid
- hillteck (vendor): https://www.hillteck.com/blog/convert-cod-to-prepaid-shopify.html
- YCloud, cash-on-delivery confirmation (vendor docs): https://helpdocs.ycloud.com/help-center/integrations/e-commerce/shopify/cod-order-confirmation
- Returino, Romanian returns plugin for WooCommerce: https://ml.wordpress.org/plugins/?p=337180

**WEG kill (K08), evidence from Lens 1 and Lens 3 plus my searches**

- EWiR / University of Cologne, census 2022: 1,771,291 WEGs: https://ewir.jura.uni-koeln.de/sites/ewir/user_upload/Praesentation_Storm.pdf
- test.de, small WEGs hardly find administrators: https://www.test.de/Wohnungseigentum-Neues-Baurecht-fuer-Eigentuemer-5662026-0/
- Wohnen im Eigentum, self-management becomes hard above 10–15 units: https://www.wohnen-im-eigentum.de/media/168/download?inline=
- Lexware hausverwaltung 2025 data sheet (vendor): https://lex-blog.de/wp-content/uploads/2024/06/20240606_2025_Lexware_hausverwaltung_Datenblatt.pdf
- Immoware24 WEG manual (vendor): https://www.immoware24.de/wp-content/uploads/2025/01/11_AbrechnungWEG-Verwaltung.pdf
- SoftGuide, WEG administration directory: https://www.softguide.de/funktion/weg-verwaltung
- HTGF, Dotega pre-seed (via Lens 1): https://www.htgf.de/dotega-pre-seed-finanzierung/
- startup-seeker, Dotega pricing (aggregator; via Lens 1): https://startup-seeker.com/company/dotega~de
- GetApp, selbstverwalten.com (via Lens 1): https://www.getapp.sg/software/2143724/selbstverwalten
- softwareabc24, Win-CASA (vendor claim; via Lens 3): https://www.softwareabc24.de/vergleiche/intex-hausverwaltung-vs-win-casa

### Gaps (what could not be answered, and why)

**Not researched (search budget exhausted):**

- FiDA status
- FedNow/RTP adoption and request-for-payment availability
- UPI international linkages
- Peppol growth figures
- RCS business messaging on iOS
- Apple/Google Wallet pass economics
- EU High-Value-Dataset APIs

**Pricing not found:**

- Open-banking aggregators (GoCardless Bank Account Data, Enable Banking, finAPI)
- RoPay merchant fees
- EuPlătesc and Netopia fees and API availability
- Germany's WhatsApp rate card

**Finalist 1 (Romania):**

- Number of active Romanian online shops, and platform shares (GoMag, MerchantPro, Shopify, WooCommerce)
- Funding and traction of Caty, Zarina and WAPI
- Whether Romanian merchants or buyers pay the cash-on-delivery fee
- WhatsApp penetration in Romania
- The exact page behind the tax-authority figures (31bn lei in 2024; 18.5bn lei in Jan–Jul 2025)

**Finalist 2 (Germany):**

- Competitors for butcher and bakery pre-ordering (point-of-sale and scale vendors, shop builders)
- Number of butcher, bakery and farm shops
- Deposit acceptance by customers

**Finalist 3 (Germany):**

- The total German heat-pump stock and brand shares
- Whether makers' apps already show efficiency or diagnoses
- Whether Viessmann's API limits apply per app or per user, and its commercial terms
- DWD open-data terms

**WEG law details (German condominium law):**

- Virtual owners' meetings (2024) and text-form resolutions were not verified here.
- These details only matter for K08, which is killed on H8 anyway.
