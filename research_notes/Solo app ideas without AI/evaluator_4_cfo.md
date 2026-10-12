# Evaluator 4 ("the CFO"): independent full-business evaluation of the 15 finalists and the BASELINE

Date: 2026-10-12. Role: former CFO and pricing lead at subscription-software companies. I scored every criterion for every idea myself, using the coordinator's RULEBOOK exactly (H1–H8, C1–C10, weights 10/15/10/15/15/5/10/10/5/5, weighted score = Σ(score × weight)/10, verdict ≥ 75 BUILD, 60–74 TEST, < 60 KILL). I did not open any other evaluator file.

**Evidence labels used throughout**
- **[V]** = I verified it this session from a search-result extract that attributes it to the cited URL. Every page fetch failed on DNS, so I never opened a page itself.
- **[L]** = reported by the lens researcher (mostly extract-verified by them). I did not re-check it.
- **JUDGEMENT** = my professional expertise, not verified this session.
- **[M]** = output of my own unit-economics and cash model (method in section 1).
- **Benchmark** = a public SaaS benchmark, not data about the idea itself.

**Budget used:** 15 of 15 web searches. 5 page fetches (AlternativeTo, App Store, Stripe, EinfachSTWEG, HealthExec) all failed with DNS errors and were not retried.

---

## (1) Summary table

### Takeaway
- **Nothing reaches BUILD.** Three ideas reach TEST:
  - **L4-F1** care-home financing case manager: **66.5**
  - **L3-A** biogas evidence log: **62.5**
  - **L1-A** vet preventive-care plans: **60.5**
- **The other 12 finalists and the BASELINE are in the KILL band.** I scored the BASELINE at **42.5**, below every lens researcher's score (51–57.5).
- **No hard-rule violation is proven for any ID.** Most IDs carry a watch item (a risk, not a violation; see the table). Two are near-violations:
  - **L5-F2: H8.** Shopify sells butcher shops with click-and-collect, and white-label butcher pre-order apps exist [V].
  - **L5-F3: H4.** Heat-pump makers control both the data and the free apps.
- **On the CFO test**, only **L4-F1** and **L2-F1** reach €8,000/month run-rate profit inside 24 months on €10,000 as proposed. Both reach it in month 21 [M], and both leave less than €1,200 of cash at the low point. Three more get there with a fix:
  - L1-A, with a fixed platform fee: month 21.
  - L3-A, with a higher price: month 18.
  - L3-B, if the umbrella channel works: month 21.

### Cited Findings — summary table (16 rows)
Hard-rule column: "none" means no violation is proven. Text in brackets is a watch item, not a violation.

| ID | Idea (short) | Hard-rule flags | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 | C9 | C10 | Weighted | Verdict |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L1-A | Vet preventive-care plans (DE) | none (H3: needs legal opinion on GOT, insurance boundary and medicine pricing) | 5 | 6 | 7 | 5 | 7 | 8 | 6 | 6 | 5 | 6 | **60.5** | TEST |
| L1-B | Boarding-stable billing (DE) | none (H8/H4 watch: Stabley "free incl. billing", unverified) | 5 | 4 | 5 | 4 | 6 | 6 | 7 | 4 | 8 | 6 | **52.0** | KILL |
| L1-C | Music-teacher admin (DE) | none | 5 | 4 | 5 | 5 | 5 | 6 | 8 | 4 | 8 | 6 | **53.0** | KILL |
| L2-F1 | CRA Logbook (EU, launch DE) | none (H4 watch: GitHub/Microsoft and free EU-funded toolkits) | 6 | 5 | 4 | 6 | 7 | 7 | 6 | 4 | 6 | 6 | **56.5** | KILL |
| L2-F2 | CRA importer/distributor vault (EU) | none (H4 watch: Amazon) | 4 | 4 | 4 | 4 | 6 | 6 | 7 | 3 | 6 | 3 | **46.5** | KILL |
| L2-F3 | Battery Passport Lite (EU) | none (H8 watch: funded passport vendors) | 6 | 5 | 4 | 3 | 7 | 4 | 4 | 6 | 3 | 6 | **49.0** | KILL |
| L3-A | Biogas substrate/EEG evidence log (DE) | none (H8 watch: 3+ small vendors, funding unknown) | 7 | 7 | 5 | 6 | 7 | 7 | 6 | 5 | 5 | 7 | **62.5** | TEST |
| L3-B | Parent-duty rosters, parent-run daycares (DE) | none | 5 | 4 | 5 | 7 | 7 | 4 | 8 | 4 | 8 | 7 | **58.5** | KILL |
| L3-C | Swiss condominium self-administration (CH) | none (H8 watch: EinfachSTWEG at the same price) | 6 | 6 | 4 | 3 | 4 | 7 | 5 | 6 | 6 | 4 | **49.0** | KILL |
| L4-F1 | Care-home financing case manager (NRW) | none (H3: needs counsel on the Legal Services Act (RDG) and GDPR Art. 9) | 8 | 7 | 7 | 6 | 7 | 8 | 6 | 6 | 5 | 6 | **66.5** | TEST |
| L4-F2 | SBV case tool, employer pays (DE) | none (H5 weak: employer must accept "necessity") | 5 | 4 | 5 | 6 | 7 | 8 | 6 | 5 | 5 | 5 | **55.5** | KILL |
| L4-F3 | Tenant benefit-deadline assistant, landlord pays (DE) | none (H4 watch: housing-ERP incumbent) | 5 | 4 | 4 | 4 | 4 | 6 | 6 | 3 | 5 | 3 | **43.0** | KILL |
| L5-F1 | RambursFlip, COD to prepaid (RO) | none (H4 watch: Meta API, shop platforms, processors) | 6 | 5 | 6 | 5 | 5 | 5 | 5 | 4 | 7 | 6 | **52.5** | KILL |
| L5-F2 | Vorbestell-Desk pre-orders (DE) | none (**H8 borderline**: Shopify and white-label butcher apps [V]) | 5 | 4 | 3 | 5 | 4 | 7 | 7 | 3 | 8 | 7 | **48.5** | KILL |
| L5-F3 | WP-Wächter heat-pump check (DE) | none (**H4 borderline**: makers control data and free apps) | 5 | 3 | 4 | 5 | 3 | 6 | 5 | 2 | 6 | 6 | **41.5** | KILL |
| BASE | Daily check-in call 65+ (DE) | none (H6: the senior's own consent must be designed in) | 6 | 4 | 5 | 3 | 2 | 9 | 5 | 4 | 3 | 6 | **42.5** | KILL |

### How the numbers were built (applies to every ID)
- **Prices are net of VAT.**
  - Consumer prices in Germany include 19% VAT (JUDGEMENT). So the BASELINE's €9.90 is **€8.32** net, and WP-Wächter's €4.99 is **€4.19** net.
  - Business prices are treated as net.
- **Cost to serve per customer per month** includes:
  - hosting
  - messaging and telephony
  - payment fees on my own subscription billing
  - support time, priced at €35/hour as if outsourced, so the margin holds at scale
- **Payment fees (JUDGEMENT; stripe.com could not be fetched):**
  - Stripe standard EEA cards: 1.5% + €0.25
  - Non-EEA (incl. Swiss) cards: 3.25% + €0.25
  - SEPA Direct Debit: €0.35
  - Stripe Billing: +0.7%
  - GoCardless: about 1% + €0.20, capped. The lens cites an older "1% capped at €2" ([t3n](https://t3n.de/news/?p=653634)) [L].
- **Telephony and messaging:**
  - Twilio Germany, outbound voice [V]:
    - about $0.028/min to landlines
    - about $0.042/min to mobiles from an EEA origin
    - about $0.376/min to mobiles at the general rate
    - local number $1.35/month
    - Source: [Twilio DE pricing](https://www.twilio.com/en-us/voice/pricing/de); Plivo is similar ([Plivo DE](https://www.plivo.com/voice/pricing/de/)).
  - WhatsApp Germany, secondary rate cards [V]: utility about **€0.0456**, marketing about **€0.1131** per message ([ChatMaxima, July 2026](https://chatmaxima.com/whatsapp-api-pricing/germany/); [whautomate](https://whautomate.com/whatsapp-business-api-pricing-germany)).
  - WhatsApp Romania: utility €0.0239 [L] ([Profit.ro](https://profit.ro/romania-conectata/schimbare-la-whatsapp-apare-plata-pentru-mesajele-de-asistenta-pe-whatsapp-business-api-22793043)).
- **Churn benchmark.** ChartMogul [V] (Benchmark): median monthly customer churn is **6.1% for ARPA under $25**, falling to 2.2% above $500 ARPA. Gross MRR churn should stay under 3.5% for ARPA under $100 ([ChartMogul](https://chartmogul.com/blog/good-customer-churn-rate/); [cheat sheet](https://chartmogul.com/resources/churn-cheat-sheet)). Secondary compilations put SMB SaaS at 3–7%/month ([focus-digital](https://focus-digital.co/average-churn-rate-by-industry-saas/)) [V]. I set each idea's churn against this, adjusted for lock-in.
- **CAC.**
  - "Cash CAC" = upfront marketing, travel and materials per new customer.
  - "Fully loaded CAC" adds founder sales hours at €50/hour (JUDGEMENT). LTV/CAC uses the fully loaded figure.
  - Referral fees paid out of revenue are not upfront CAC.
- **Overhead.** Tools €200–300, tax adviser €250, insurance €80–250, legal reserve €50–150 and bank €15 per month. Idea-specific additions:
  - external data-protection officer €150 (L4-F1)
  - Romanian freelancer €600 (L5-F1)
  - Swiss fiscal representative €150 plus native-speaker support €400 (L3-C)
  - continuity escrow €100 (L2-F3)
- **One-off set-up.** Company formation about €800 plus legal templates and opinions: €1,600–3,500 per idea. This is paid before launch, together with 3 build months at €300/month.
- **Customers needed for €8,000/month** = (8,000 + overhead) ÷ (net ARPA − cost to serve − monthly churn × cash CAC). The last term is the marketing needed just to replace churned customers. The lens files left it out, and for consumer ideas it changes the answer by 2–5×.
- **LTV** = monthly gross margin × min(1/churn, 60 months).
- **24-month model [M]:**
  - Launch is January 2027, after a 12-week build from today.
  - Starting capital is €10,000 and there is no outside money. Acquisition stops whenever cash cannot pay for it.
  - Overhead runs at 50% in months 1–6, 75% in months 7–12, 100% after.
  - Annual-prepay plans collect 12 months of cash at signing.
  - "Run-rate profit" = recurring gross margin − full overhead − replacement marketing. It is the profit the founder could take each month while keeping the customer base flat.
  - Founder living costs sit outside the €10,000.
  - Profit is before any income tax. A German UG would also pay corporate and trade tax of about 30% (JUDGEMENT), so a sole proprietorship fits the "before personal income tax" goal better.
  - Model code and full output are in the scratchpad: `cfo/model.py`, `cfo/report_tables.py`, `cfo/tables.md`.

### Inferences
- **The lenses were systematically optimistic in the same three places:**
  1. They left out VAT on consumer prices.
  2. They left out the marketing needed to replace churn.
  3. They counted CAC without the founder's time.

  Once those are added, every consumer-priced idea (BASE, L5-F3, L1-C solo tier) fails the 3× LTV/CAC test or needs thousands of payers.
- **Only B2B ideas with ARPA of €65–250/month and churn ≤ 1.8%/month reach €8k inside 24 months on €10k:**
  - as proposed: L4-F1 and L2-F1
  - with a pricing fix: L1-A and L3-A
  - only if its channel over-delivers: L3-B
- **Annual prepay is the strongest CFO lever available.** It turns L3-A, L4-F2, L5-F2 and L3-C cash-positive at signing.

### Gaps
- I could not open any page (DNS failures), so even my [V] items rest on search-engine extracts.
- Current Stripe and GoCardless price lists, SMS prices to Germany and Swiss VAT rules are JUDGEMENT.
- My ramp assumptions (new customers per month) are judgement calibrated to each channel. The scenario table in section 2 shows how sensitive the verdicts are to them.

---

## (2) Per-idea notes

### Takeaway
- **The three TEST ideas share three traits:**
  - a payer with a quantified money reason
  - a price of €65–250 per month per account
  - churn at or below 1.2%/month
- **The KILL ideas fail mostly on four things:**
  - consumer-level ARPA (BASE, L5-F3, L1-C)
  - a missing cheap channel (L3-C, L2-F3, L4-F3)
  - competitors the lens missed (L5-F2, L2-F1)
  - customer ROI too thin after hidden costs (L5-F1)

### Cross-idea unit economics (all 16 IDs) [M]
| ID | Price as proposed | Net ARPA €/mo | Cost to serve €/mo | Gross margin | Cash CAC € | Fully loaded CAC € | Payback (months) | Monthly churn | LTV € | LTV/CAC | Overhead €/mo | Customers for €8k/mo | Pool used | Share of pool |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L1-A | €2.50/active plan/month, €99 min after 6 months | 250.00 (at 100 plans) | 26.10 | 90% | 300 | 1,050 | 4.7 | 1.2% | 13,434 | 12.8 | 850 | 41 | 4,500 | 0.9% |
| L1-B | €39 / €59 per month | 45.00 | 7.90 | 82% | 150 | 350 | 9.4 | 2.5% | 1,484 | 4.2 | 600 | 258 | 7,000 | 3.7% |
| L1-C | €12 solo / €49 studio per month | 15.70 | 2.35 | 85% | 55 | 80 | 6.0 | 4.2% | 318 | 4.0 | 600 | 779 | 25,000 | 3.1% |
| L2-F1 | €49 / €99 / €199 per month | 85.00 | 13.60 | 84% | 250 | 500 | 7.0 | 1.8% | 3,967 | 7.9 | 950 | 134 | 8,000 | 1.7% |
| L2-F2 | €29 / €69 / €149 per month | 55.00 | 7.00 | 87% | 150 | 300 | 6.2 | 2.5% | 1,920 | 6.4 | 850 | 200 | 10,000 | 2.0% |
| L2-F3 | €99/month + €0.40/passport | 180.00 | 30.00 | 83% | 500 | 1,000 | 6.7 | 1.0% | 9,000 | 9.0 | 1,050 | 63 | 2,000 | 3.1% |
| L3-A | €790/plant/year | 65.83 | 10.80 | 84% | 300 | 550 | 10.0 | 1.0% | 3,302 | 6.0 | 800 | 170 | 6,500 | 2.6% |
| L3-B | €49/month | 49.00 | 7.20 | 85% | 100 | 250 | 6.0 | 2.0% | 2,090 | 8.4 | 600 | 217 | 3,600 | 6.0% |
| L3-C | CHF 350/year (CHF 35/month option) | 30.92 | 11.00 | 64% | 300 | 450 | 22.6 | 1.0% | 1,195 | 2.7 | 1,300 | 550 | 24,000 | 2.3% |
| L4-F1 | €129–249/month (avg 179), €99 pilot | 179.00 | 23.90 | 87% | 400 | 1,200 | 7.7 | 1.2% | 9,306 | 7.8 | 1,100 | 61 | 4,000 | 1.5% |
| L4-F2 | €39 / €79 per month, invoiced yearly | 45.00 | 6.30 | 86% | 120 | 300 | 7.8 | 1.0% | 2,322 | 7.7 | 800 | 235 | 30,000 | 0.8% |
| L4-F3 | €0.08/unit/month, min €99, yearly | 160.00 | 18.00 | 89% | 1,500 | 3,000 | 21.1 | 1.0% | 8,520 | 2.8 | 900 | 71 | 3,000 | 2.3% |
| L5-F1 | €39 / €89 / €179 per month + Meta fees | 75.00 | 13.20 | 82% | 300 | 450 | 7.3 | 4.5% | 1,373 | 3.1 | 1,300 | 193 | 3,000 | 6.4% |
| L5-F2 | €35/month yearly (€59 monthly) | 35.00 | 7.80 | 78% | 150 | 300 | 11.0 | 3.5% | 777 | 2.6 | 600 | 392 | 15,000 | 2.6% |
| L5-F3 | €4.99/month or €49/year incl. VAT | 3.81 | 0.75 | 80% | 25 | 30 | 9.8 | 5.0% | 61 | 2.0 | 600 | 4,752 | 250,000 | 1.9% |
| BASE | €9.90/month incl. VAT | 8.32 | 2.70 | 68% | 80 | 90 | 16.0 | 5.0% | 112 | 1.2 | 850 | 5,463 | 4,000,000 | 0.1% |

### 24-month view on €10,000 [M]
| ID | Cash at launch € | Cash low point M1–M24 (€, month) | Customers M12 | Run-rate profit M12 € | Customers M24 | Run-rate profit M24 € | P&L profit M24 € | First month run-rate ≥ €8k | Plausible in 24 months on €10k? |
|---|---|---|---|---|---|---|---|---|---|
| L1-A | 5,600 | 510 (M7) | 18 | 555 | 59 | 5,449 | 4,463 | M28 | No as proposed (plans mature slowly); **yes with fix (M21)** |
| L1-B | 7,500 | 4,288 (M8) | 68 | 1,677 | 190 | 5,733 | 4,195 | M34 | No |
| L1-C | 7,300 | 2,643 (M10) | 215 | 1,714 | 518 | 5,117 | 4,828 | not by M36 | No |
| L2-F1 | 6,800 | 518 (M7) | 79 | 3,760 | 150 | 9,106 | 7,782 | **M21** | Yes, but fragile (half the sales pace → no) |
| L2-F2 | 7,100 | 2,849 (M11) | 50 | 1,353 | 121 | 4,486 | 3,738 | not by M36 | No |
| L2-F3 | 6,800 | 3,206 (M3) | 26 | 2,769 | 46 | 5,630 | 4,861 | M36 | No (pool-limited) |
| L3-A | 7,300 | never below launch (prepay) | 68 | 2,338 | 163 | 7,696 | 2,786 | M25 | Almost; **yes at €1,190/yr (M18)** |
| L3-B | 7,500 | 5,943 (M5) | 67 | 1,982 | 188 | 6,893 | 6,570 | M29 | No as modelled; yes if umbrella channel works (M21) |
| L3-C | 6,300 | **−3,616 (M13)** | 88 | 109 | 276 | 3,369 | −1,203 | not by M36 | No; €10k runs out around M9 |
| L4-F1 | 6,600 | 1,110 (M7) | 37 | 3,498 | 77 | 9,507 | 8,276 | **M21** | **Yes** (tight cash; safe with annual prepay) |
| L4-F2 | 6,800 | never below launch (yearly invoices) | 57 | 1,338 | 166 | 5,407 | 4,406 | M33 | No |
| L4-F3 | 5,800 | 2,956 (M15) | 15 | 1,005 | 37 | 3,837 | 1,396 | not by M36 | No |
| L5-F1 | 6,800 | **−8,579 (M24)** | 13 | −692 | 7 | −950 | −853 | not by M36 | No; cash runs out around M12 |
| L5-F2 | 7,500 | never below launch (prepay) | 100 | 1,595 | 202 | 3,839 | 4,150 | not by M36 | No |
| L5-F3 | 7,300 | 500 (M16) | 345 | 25 | 367 | 64 | −2 | not by M36 | No |
| BASE | 6,800 | **−9,889 (M24)** | 44 | −779 | 24 | −812 | −718 | not by M36 | No; cash runs out around M8 |

**Monthly run-rate profit, € thousands [M]** (M1 = January 2027)

| Month | L1-A | L1-B | L1-C | L2-F1 | L2-F2 | L2-F3 | L3-A | L3-B | L3-C | L4-F1 | L4-F2 | L4-F3 | L5-F1 | L5-F2 | L5-F3 | BASE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M1 Jan 27 | -0.9 | -0.5 | -0.5 | -0.9 | -0.8 | -0.6 | -0.7 | -0.5 | -1.3 | -1.0 | -0.7 | -0.9 | -1.2 | -0.6 | -0.5 | -0.8 |
| M2 Feb 27 | -0.8 | -0.4 | -0.4 | -0.7 | -0.7 | -0.0 | -0.6 | -0.4 | -1.2 | -0.9 | -0.7 | -0.9 | -1.1 | -0.5 | -0.3 | -0.7 |
| M3 Mar 27 | -0.8 | -0.2 | -0.2 | -0.6 | -0.6 | 0.4 | -0.5 | -0.3 | -1.1 | -0.7 | -0.5 | -0.9 | -1.0 | -0.4 | -0.2 | -0.7 |
| M4 Apr 27 | -0.7 | -0.1 | -0.0 | -0.1 | -0.5 | 0.7 | -0.4 | -0.1 | -1.0 | -0.4 | -0.4 | -0.8 | -0.8 | -0.3 | -0.1 | -0.7 |
| M5 May 27 | -0.6 | 0.1 | 0.1 | 0.2 | -0.4 | 0.9 | -0.3 | 0.1 | -0.9 | -0.0 | -0.2 | -0.6 | -0.7 | -0.3 | -0.1 | -0.7 |
| M6 Jun 27 | -0.4 | 0.3 | 0.2 | 0.4 | -0.4 | 1.2 | -0.2 | 0.3 | -0.8 | 0.4 | -0.1 | -0.5 | -0.5 | -0.2 | -0.1 | -0.8 |
| M7 Jul 27 | -0.3 | 0.5 | 0.3 | 0.7 | -0.2 | 1.5 | -0.1 | 0.4 | -0.7 | 0.9 | 0.1 | -0.3 | -0.6 | -0.2 | -0.0 | -0.8 |
| M8 Aug 27 | -0.1 | 0.7 | 0.5 | 1.1 | -0.0 | 1.7 | 0.0 | 0.8 | -0.6 | 1.4 | 0.3 | -0.0 | -0.6 | -0.2 | -0.0 | -0.8 |
| M9 Sep 27 | 0.0 | 0.9 | 1.0 | 1.6 | 0.1 | 2.0 | 0.2 | 1.2 | -0.4 | 1.9 | 0.6 | 0.2 | -0.6 | 0.4 | -0.0 | -0.8 |
| M10 Oct 27 | 0.2 | 1.1 | 1.3 | 2.3 | 0.5 | 2.3 | 0.9 | 1.6 | -0.2 | 2.4 | 0.8 | 0.5 | -0.6 | 0.9 | -0.0 | -0.8 |
| M11 Nov 27 | 0.4 | 1.4 | 1.6 | 3.0 | 1.0 | 2.5 | 1.6 | 1.9 | -0.1 | 3.0 | 1.0 | 0.8 | -0.7 | 1.5 | 0.0 | -0.8 |
| M12 Dec 27 | 0.6 | 1.7 | 1.7 | 3.8 | 1.4 | 2.8 | 2.3 | 2.0 | 0.1 | 3.5 | 1.3 | 1.0 | -0.7 | 1.6 | 0.0 | -0.8 |
| M13 Jan 28 | 0.8 | 2.0 | 2.2 | 4.4 | 1.7 | 3.0 | 3.2 | 2.3 | 0.4 | 4.0 | 1.6 | 1.3 | -0.7 | 1.6 | 0.0 | -0.8 |
| M14 Feb 28 | 1.0 | 2.3 | 2.5 | 5.0 | 1.9 | 3.3 | 4.1 | 2.7 | 0.7 | 4.6 | 1.9 | 1.5 | -0.7 | 1.7 | 0.0 | -0.8 |
| M15 Mar 28 | 1.3 | 2.6 | 2.8 | 5.6 | 2.2 | 3.5 | 4.3 | 3.0 | 1.0 | 5.1 | 2.2 | 1.8 | -0.8 | 1.8 | 0.0 | -0.8 |
| M16 Apr 28 | 1.7 | 2.9 | 3.1 | 6.0 | 2.5 | 3.8 | 4.4 | 3.4 | 1.3 | 5.6 | 2.6 | 2.0 | -0.8 | 1.8 | 0.0 | -0.8 |
| M17 May 28 | 2.1 | 3.2 | 3.3 | 6.4 | 2.8 | 4.0 | 4.6 | 3.7 | 1.5 | 6.1 | 3.0 | 2.2 | -0.8 | 1.9 | 0.0 | -0.8 |
| M18 Jun 28 | 2.5 | 3.6 | 3.5 | 6.8 | 3.0 | 4.2 | 4.7 | 4.1 | 1.7 | 6.6 | 3.3 | 2.5 | -0.8 | 1.9 | 0.0 | -0.8 |
| M19 Jul 28 | 2.9 | 3.9 | 3.6 | 7.2 | 3.3 | 4.5 | 4.8 | 4.3 | 2.0 | 7.1 | 3.7 | 2.7 | -0.9 | 2.0 | 0.0 | -0.8 |
| M20 Aug 28 | 3.4 | 4.3 | 3.8 | 7.6 | 3.5 | 4.7 | 5.0 | 5.0 | 2.2 | 7.6 | 4.0 | 2.9 | -0.9 | 2.0 | 0.0 | -0.8 |
| M21 Sep 28 | 3.8 | 4.7 | 4.4 | 8.0 | 3.8 | 4.9 | 5.1 | 5.7 | 2.5 | 8.1 | 4.4 | 3.2 | -0.9 | 2.6 | 0.1 | -0.8 |
| M22 Oct 28 | 4.3 | 5.0 | 4.8 | 8.4 | 4.0 | 5.2 | 6.0 | 6.3 | 2.8 | 8.6 | 4.7 | 3.4 | -0.9 | 3.2 | 0.1 | -0.8 |
| M23 Nov 28 | 4.9 | 5.4 | 5.1 | 8.7 | 4.3 | 5.4 | 6.8 | 6.8 | 3.1 | 9.0 | 5.1 | 3.6 | -0.9 | 3.8 | 0.1 | -0.8 |
| M24 Dec 28 | 5.4 | 5.7 | 5.1 | 9.1 | 4.5 | 5.6 | 7.7 | 6.9 | 3.4 | 9.5 | 5.4 | 3.8 | -1.0 | 3.8 | 0.1 | -0.8 |

**Month-end cash balance, € thousands [M]** (starts from €10,000 minus set-up and build costs)

| Month | L1-A | L1-B | L1-C | L2-F1 | L2-F2 | L2-F3 | L3-A | L3-B | L3-C | L4-F1 | L4-F2 | L4-F3 | L5-F1 | L5-F2 | L5-F3 | BASE |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Launch | 5.6 | 7.5 | 7.3 | 6.8 | 7.1 | 6.8 | 7.3 | 7.5 | 6.3 | 6.6 | 6.8 | 5.8 | 6.8 | 7.5 | 7.3 | 6.8 |
| M1 Jan 27 | 4.6 | 6.9 | 6.3 | 5.4 | 6.5 | 5.2 | 7.4 | 7.0 | 5.6 | 5.7 | 7.2 | 5.3 | 5.4 | 7.7 | 5.2 | 4.1 |
| M2 Feb 27 | 3.6 | 6.2 | 5.5 | 4.0 | 5.9 | 3.7 | 7.4 | 6.5 | 4.9 | 4.6 | 7.6 | 4.9 | 3.8 | 7.9 | 3.2 | 0.9 |
| M3 Mar 27 | 2.3 | 5.7 | 4.8 | 2.4 | 5.5 | 3.2 | 7.8 | 6.2 | 4.2 | 3.3 | 8.5 | 4.5 | 2.1 | 9.2 | 1.6 | 0.5 |
| M4 Apr 27 | 1.2 | 5.2 | 4.3 | 0.9 | 5.1 | 3.5 | 8.2 | 6.0 | 3.8 | 2.3 | 9.7 | 4.4 | 0.7 | 9.3 | 1.4 | 0.5 |
| M5 May 27 | 0.8 | 4.9 | 4.0 | 0.6 | 4.9 | 4.0 | 8.6 | 5.9 | 3.2 | 1.7 | 10.9 | 4.3 | 0.6 | 9.5 | 1.1 | 0.4 |
| M6 Jun 27 | 0.5 | 4.7 | 3.9 | 0.7 | 4.7 | 4.8 | 9.0 | 6.0 | 2.6 | 1.5 | 12.0 | 4.3 | 0.6 | 9.6 | 1.0 | 0.3 |
| M7 Jul 27 | 0.5 | 4.4 | 4.0 | 0.5 | 4.2 | 5.6 | 9.1 | 6.3 | 1.7 | 1.1 | 13.4 | 4.3 | 0.6 | 9.5 | 0.7 | 0.0 |
| M8 Aug 27 | 0.6 | 4.3 | 3.7 | 0.5 | 3.8 | 6.7 | 9.2 | 6.3 | 0.8 | 1.3 | 15.1 | 4.4 | 0.6 | 9.5 | 0.5 | -0.3 |
| M9 Sep 27 | 0.6 | 4.3 | 2.7 | 0.6 | 3.6 | 8.1 | 9.3 | 6.7 | -0.2 | 1.9 | 16.8 | 4.4 | 0.5 | 15.4 | 0.5 | -0.7 |
| M10 Oct 27 | 0.8 | 4.6 | 2.6 | 0.6 | 3.0 | 9.7 | 15.2 | 7.5 | -1.3 | 3.1 | 18.4 | 4.3 | 0.4 | 21.2 | 0.5 | -1.1 |
| M11 Nov 27 | 0.5 | 5.0 | 3.1 | 1.2 | 2.8 | 11.6 | 20.8 | 8.9 | -2.4 | 4.9 | 20.5 | 4.3 | 0.2 | 26.7 | 0.5 | -1.4 |
| M12 Dec 27 | 0.7 | 5.6 | 4.3 | 2.5 | 3.1 | 13.8 | 26.4 | 10.7 | -3.6 | 7.3 | 22.9 | 4.2 | 0.0 | 26.8 | 0.5 | -1.8 |
| M13 Jan 28 | 0.7 | 6.3 | 4.5 | 5.3 | 3.8 | 15.9 | 35.7 | 12.3 | -3.6 | 9.9 | 26.0 | 3.8 | -0.5 | 26.5 | 0.5 | -2.4 |
| M14 Feb 28 | 0.6 | 7.3 | 5.6 | 8.6 | 4.7 | 18.3 | 45.0 | 14.1 | -3.4 | 13.1 | 29.0 | 3.4 | -1.1 | 26.2 | 0.5 | -3.1 |
| M15 Mar 28 | 0.9 | 8.5 | 6.9 | 12.7 | 6.0 | 21.0 | 46.0 | 16.3 | -3.0 | 16.8 | 32.9 | 3.0 | -1.8 | 28.6 | 0.5 | -3.7 |
| M16 Apr 28 | 1.5 | 10.0 | 8.7 | 17.2 | 7.6 | 23.9 | 47.0 | 18.9 | -2.4 | 21.0 | 37.7 | 4.2 | -2.4 | 28.5 | 0.5 | -4.4 |
| M17 May 28 | 2.5 | 11.7 | 10.9 | 22.1 | 9.5 | 27.1 | 48.0 | 21.7 | -2.6 | 25.8 | 42.4 | 5.4 | -3.1 | 28.3 | 0.5 | -5.0 |
| M18 Jun 28 | 3.9 | 13.8 | 13.5 | 27.5 | 11.7 | 30.6 | 48.9 | 24.9 | -2.8 | 31.1 | 47.0 | 6.5 | -3.8 | 28.2 | 0.5 | -5.7 |
| M19 Jul 28 | 5.8 | 16.1 | 16.8 | 33.3 | 14.1 | 34.2 | 49.8 | 28.6 | -2.8 | 36.9 | 52.0 | 9.4 | -4.5 | 28.0 | 0.5 | -6.4 |
| M20 Aug 28 | 8.1 | 18.8 | 19.5 | 39.5 | 16.8 | 38.1 | 50.6 | 32.0 | -2.6 | 43.2 | 57.5 | 12.2 | -5.3 | 27.9 | 0.5 | -7.1 |
| M21 Sep 28 | 11.0 | 21.8 | 21.0 | 46.1 | 19.8 | 42.3 | 51.5 | 36.0 | -2.2 | 50.0 | 62.9 | 14.9 | -6.1 | 42.4 | 0.5 | -7.8 |
| M22 Oct 28 | 14.3 | 25.2 | 23.9 | 53.1 | 23.1 | 46.7 | 67.9 | 40.7 | -2.0 | 57.3 | 68.2 | 17.7 | -6.9 | 56.8 | 0.5 | -8.5 |
| M23 Nov 28 | 18.2 | 29.0 | 27.7 | 60.5 | 26.6 | 51.3 | 84.1 | 46.4 | -1.6 | 65.1 | 74.0 | 20.4 | -7.7 | 70.9 | 0.5 | -9.2 |
| M24 Dec 28 | 22.6 | 33.2 | 32.5 | 68.3 | 30.3 | 56.2 | 100.2 | 53.0 | -1.0 | 73.4 | 80.2 | 23.1 | -8.6 | 71.5 | 0.5 | -9.9 |

Cash for annual-prepay ideas (L3-A, L4-F2, L5-F2) includes prepaid revenue for future months. That is a liability, not profit.

**Scenarios (what flips the CFO answer) [M]**
| Scenario | Change vs as proposed | Cash low point | Customers M24 | Run-rate profit M24 | First month ≥ €8k | Customers needed |
|---|---|---|---|---|---|---|
| L1-A fix | €99/month platform minimum from month 1 + €290 set-up fee | €5,210 (M2) | 79 | €10,652 | **M21** | 41 |
| L1-A low uptake | as proposed, but owner uptake caps at 60 plans/practice | €192 (M8) | 15 | €346 | not by M36 | 71 |
| L4-F1 fix | no €99 pilot; annual prepay with 2 months free | never below €6,600 | 82 | €8,747 | **M23** | 76 |
| L4-F1 stress | as proposed, churn 2%/month, 3 new homes/month | €1,514 (M8) | 53 | €5,996 | M32 | 62 |
| L3-A fix | price €1,190/plant/year, tiered by plant size | never below €7,300 | 163 | €13,138 | **M18** | 104 |
| L3-A stress | two-thirds of the sales pace, churn 2%/month | €6,213 (M9) | 101 | €4,150 | not by M36 | 180 |
| L2-F1 stress | half the sales pace (free EU toolkits absorb demand) | €622 (M8) | 85 | €4,741 | not by M36 | 134 |
| L3-B optimistic | umbrella channel delivers up to 20 associations/month | €5,867 (M4) | 282 | €10,606 | **M21** | 217 |
| L5-F1 optimistic | cash CAC €150 (app-store organic), churn 3%/month | €2,000 (M7) | 246 | €11,949 | **M19** | 163 |
| L3-C optimistic | cash CAC €150 (SEO templates instead of paid search) | €6,236 (M1) | 276 | €3,783 | not by M36 | 505 |
| BASE optimistic | cash CAC €40, churn 3%/month | €501 (M30) | 293 | €444 | not by M36 | 2,003 |

---

### L1-A — Vet preventive-care plans (Germany) — 60.5, TEST

| C | Score | One-line justification |
|---|---|---|
| C1 | 5 | Owners face lumpy prevention bills after vet fees rose about 22% ([t-online](https://www.t-online.de/nachrichten/panorama/tiere/id_101219134/hoehere-tierarztkosten-belasten-tierheime.html)) [L]. But the payer, the practice, sees an opportunity (recurring revenue) rather than an acute pain. |
| C2 | 6 | Abroad, practices pay per plan: Petly charges USD 4.35–4.95 per plan per month plus USD 1,249 set-up ([IDEXX](https://idexx-prod-base.django-aws.idexx.com/en/veterinary/software-services/petly-plans/getting-started/pricing)) [L]. German practice WTP and owner uptake are untested. |
| C3 | 7 | Proven at scale in the UK: CVS has 519k members ([FCA RNS](https://data.fca.org.uk/artefacts/NSM/RNS/5850272.html)) [L]. My German search again found no practice-run monthly plan [V]. The GOT 1× floor explains why foreign players have not copied it [L]. |
| C4 | 5 | About 4,500 listable independent practices and only about 41 needed, but vets are hard to reach ([VetStage](https://www.vetstage.de/pdf/vetstage-agenturvorstellung.pdf)) [L]. Sales are founder-led field sales. |
| C5 | 7 | Gross margin 90%; LTV/CAC 12.8 at 100 plans and 7.3 at 60 plans [M]. Per-practice revenue takes about 17 months to mature. |
| C6 | 8 | About 41 practices ≈ 0.9% of about 4,500 (JUDGEMENT pool from [BTK 2024](https://bundestieraerztekammer.de/btk/statistik/downloads/2024.pdf) [L]). |
| C7 | 6 | Each practice needs plan-design help, staff training and legal-template upkeep. The payment partner automates collections. |
| C8 | 6 | Active plans and mandates create switching costs. Risks: IDEXX or PVA entering Germany (PVA entered Spain in 2025, [VetClick](https://vetclick.com/news/premier-vet-alliance-expands-into-spain-with-preventative-pet-health-plans-p11248.php) [L]), chains, and practice-management vendors. |
| C9 | 5 | Exposure under the vet fee schedule (GOT), consumer-subscription law, the insurance boundary and medicine-pricing rules. |
| C10 | 6 | A paid onboarding deposit or a signed LOI with a price from 2–3 practices within 90 days for under €2k is plausible. |

**Hard-rule findings**
- **H1 pass.** The core is plan rules, a SEPA ledger and reminders.
- **H2 pass.** The 12-week plan is credible.
- **H3 conditional pass.**
  - Owners pay into the practice's own Stripe Connect or GoCardless account, so the founder never holds money [L].
  - A plan covering only scheduled preventive services, with no risk transfer, is not insurance (JUDGEMENT).
  - With no interest or fees it is not consumer credit (JUDGEMENT).
  - A vet-law opinion is still mandatory.
- **H4 pass.** No big-tech or bank feature replaces it.
- **H5–H7 pass.**
- **H8 pass.** No German competitor was found by lens 1 or by my search [V].

**What the researcher missed**
1. **Cash design.**
   - "Free for 3 months, then €99 minimum only after 6 months", combined with slow owner uptake, leaves just **€510** of cash in month 7. Run-rate profit reaches €8k only in **M28** [M].
   - A €99/month platform minimum from month 1 plus a €290 set-up fee reaches €8k in **M21**, with a €5.2k cash floor [M].
2. **Uptake is the whole business.** At 60 plans per practice the requirement rises to about 71 practices. Under the cash limit, growth stalls: run-rate is €0.3k at M24 [M].
3. **The 1× floor may not bind in practice.** A plan priced at 1× GOT can still save money against a practice's usual multiplier (JUDGEMENT). The lens treated the floor only as a constraint.
4. **Medicines.** Bundling prescription antiparasitics with discounts runs into the vet drug-pricing ordinance (AMPreisV) (JUDGEMENT). The lens listed this only as an open question.
5. **Insurer substitutes are live.**
   - HanseMerkur offers up to €100/year for prevention checks [V] ([HanseMerkur cats](https://www.hansemerkur.de/haustiere/vorsorge-katze)).
   - Dalma offers €70–100/year ([Dalma](https://intercom.help/dalma/de/articles/6145270-was-ist-das-vorsorge-budget)) [L].
   - Useful price anchor: a basic cat check costs about **€23.62 at 1× GOT** [V].
6. **Chains already operate in Germany.** AniCura publishes owner guidance ([AniCura](https://www.anicura.de/globalassets/de-DE/pdfs/tkv_broschure_web_202006.pdf)) [V]. BTK reports a trend toward employed vets ([BTK](https://www.bundestieraerztekammer.de/presse/2024/08/PM-BTK_Tieraerztestatistik_Deutlicher-Trend-zum-Angestelltenverhaeltnis.pdf)) [L]. Both shrink the independent pool.
7. **Missed channel.** Animal-health pharma field forces (vaccines, antiparasitics) have a reason to promote compliance plans (JUDGEMENT).

**Recomputed unit economics [M]**
- **Revenue:** €250/practice/month at 100 plans × €2.50.
- **Cost to serve:** €26.10 = reminders €10 + payment €2.10 + hosting €6 + support €8. Gross margin 90%.
- **CAC:** €300 cash; €1,050 fully loaded (15 founder hours).
- **Churn:** 1.2%/month. LTV €13.4k; LTV/CAC 12.8.
- **Payback:** 4.7 months at maturity. In reality about 12 months, because plans ramp.
- **Requirement:** overhead €850 → **41 practices (≈4,100 owner plans)**.
- **24 months:** 59 practices and €5.4k run-rate at M24.

**Top 3 risks**
1. German owners do not enrol without UK-style discounts.
2. A GOT, AMPreisV or insurance-boundary challenge (chamber complaint or cease-and-desist letter).
3. Slow sales to vets, plus chain consolidation or entry by IDEXX or PVA.

**Cheapest 30-day money test (≤ €1,500)**
- Commission a short written vet-law opinion (about €800, JUDGEMENT price).
- In parallel, call 60 independent small-animal practices in one region with a GOT-safe plan calculator.
- Ask for a €290 paid onboarding deposit, refundable if the legal opinion is negative.
- **Pass:** ≥ 3 deposits. **Kill:** ≤ 1.

### L1-B — Boarding-stable billing (Germany) — 52.0, KILL

| C | Score | One-line justification |
|---|---|---|
| C1 | 5 | Month-end invoicing of about 35 boarders plus extras ([Göttingen](https://www.uni-goettingen.de/de/document/download/6d9e2af4c09df3d5f60a5fe3a5d2c79f.pdf/Gille_und_Spiller_OEGA2008__Jahrbuch.pdf), older) [L]. Lost extras are not quantified. |
| C2 | 4 | Price-sensitive farm owners. A directory says a free platform (Stabley) includes billing ([AlternativeTo](https://alternativeto.net/software/stabley/about/)) [V]. Generic invoicing plus SEPA add-ons already exist ([sevDesk SEPApro](https://sevdesk.de/integrationen/sepapro/)) [V]. |
| C3 | 5 | Neither lens 1 nor my German search found a stable-specific billing tool [V]. The free-billing claim is still open. |
| C4 | 4 | No association or newsletter channel is verified; only visits, Facebook groups and boarder referrals. |
| C5 | 6 | Gross margin 82%; LTV/CAC 4.2; payback 9.4 months on ARPA €45 [M]. |
| C6 | 6 | About 258 stables ≈ 3.7% of about 7,000 with 15+ boarders (JUDGEMENT; lens: about 16k of all sizes, from dated inputs). |
| C7 | 7 | Self-serve, with a month-end support peak and VAT set-up. |
| C8 | 4 | Free stable apps (e.g. [Stall Manager](https://apps.apple.com/de/app/stall-manager/id6751195329) [L]) or invoicing incumbents can add billing. |
| C9 | 8 | Low liability; tax responsibility stays with the stable. |
| C10 | 6 | Pre-sales through stable visits within 90 days are feasible. |

**Hard-rule findings**
- No violation is proven.
- **H8:** one free product of unknown funding does not make three funded or profitable competitors.
- **H4:** Stabley is not shown to be the niche's dominant incumbent. Watch it.

**What the researcher missed**
- Stabley's billing claim (lens 1 did not find Stabley).
- A lower price anchor: Stable Secretary (UK/US) includes billing from **$6.95** ([Capterra AT](https://www.capterra.at/software/129021/stable-secretary)) [V].
- Generic tools already create SEPA XML from recurring invoices ([sevDesk SEPApro](https://sevdesk.de/integrationen/sepapro/); [B2B Router](https://www.b2brouter.net/de/funktionen/)) [V].
- The ChartMogul churn benchmark suggests about 3%/month at this ARPA, against the lens's 2% [V].

**Recomputed unit economics [M]**
- **Unit:** ARPA €45; cost to serve €7.90 (support €5.25, payment €0.67, hosting/PDF €2); gross margin 82%.
- **CAC and churn:** CAC €150 cash / €350 fully loaded; churn 2.5%; LTV €1,484; LTV/CAC 4.2.
- **Requirement:** **258 stables**.
- **24 months:** 190 stables and €5.7k run-rate at M24; €8k only at **M34**.

**Top 3 risks**
1. A free billing app.
2. Low WTP.
3. No cheap channel.

**Cheapest 30-day money test (≤ €500)**
- **Day 1:** sign up to Stabley and run one month of test invoices.
- Then visit 15 stables with 20–60 boarders and sell 5 three-month prepayments (€117).
- **Kill:** fewer than 3, or Stabley already handles extras plus SEPA well.

### L1-C — Music-teacher admin (Germany) — 53.0, KILL

| C | Score | One-line justification |
|---|---|---|
| C1 | 5 | Weekly but modest admin pain; standing orders already cover much of the payment side. |
| C2 | 4 | Self-employed teachers are cost-sensitive. Most cannot reclaim VAT, so €12 net really costs them €14.28 (JUDGEMENT). German WTP is unproven. |
| C3 | 5 | No German-language product was found except a dated desktop tool [L]. The North American leaders could localise. |
| C4 | 5 | Teacher groups, SEO and associations are plausible but unverified. |
| C5 | 5 | Gross margin 85%, but ARPA is €15.70 and churn 4.2% → LTV €318, LTV/CAC 4.0 [M]. |
| C6 | 6 | About 779 customers ≈ 3.1% of about 25,000 self-employed teachers ([MIZ](https://miz.org/de/statistiken/version/2025-beschaeftigung-und-arbeitslosigkeit-in-musikberufen)) [L, derived]. |
| C7 | 8 | Fully self-serve. |
| C8 | 4 | Low switching cost. My Music Staff has already localised into French ([MMS FR](https://www.mymusicstaff.com/fr/wp-json/wp/v2/posts/31729)) [L]. |
| C9 | 8 | Low risk (GDPR for minors' data). |
| C10 | 6 | Founding annual pre-sales at €99 are feasible. |

**Hard-rule findings:** none. H8 passes on available evidence.

**What the researcher missed**
- **Churn.** The low-ARPA churn benchmark is a 6.1%/month median for ARPA under $25 ([ChartMogul](https://chartmogul.com/blog/good-customer-churn-rate/)) [V]. The lens used 3%.
- **VAT.** Teachers cannot reclaim it, which raises their effective price.
- **Customers needed.** Once replacement marketing is counted, the requirement rises from the lens's 655 to **779**.

**Recomputed unit economics [M]**
- **Unit:** blended ARPA €15.70 (90% solo at €12 / 10% studios at €49); cost to serve €2.35; gross margin 85%.
- **CAC and churn:** CAC €55 cash / €80 fully loaded; churn 4.2%; LTV €318; LTV/CAC 4.0.
- **24 months:** 518 customers and €5.1k run-rate at M24; €8k not reached by M36.

**Top 3 risks**
1. Low WTP.
2. High churn among part-time teachers.
3. My Music Staff or TutorBird adds German ([pricing](https://www.capterra.com/p/148451/My-Music-Staff/pricing/); [TutorBird](https://tutorbird.com/pricing)) [L].

**Cheapest 30-day money test (≤ €300)**
- German landing page, 3 teacher-group posts and 30 direct messages, selling a €99 founding year.
- **Pass:** ≥ 30 sales. **Kill:** < 10.

### L2-F1 — CRA Logbook (EU, launch Germany) — 56.5, KILL

| C | Score | One-line justification |
|---|---|---|
| C1 | 6 | Cyber Resilience Act (CRA) Art. 14 reporting has been live since 11 Sep 2026, and the Dec 2027 CE deadline is coming ([EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=OJ%3AL_202402847); [ENISA](https://www.enisa.europa.eu/news/the-cra-single-reporting-platform-is-launched)) [L]. But exploited-vulnerability events are rare, and micro and small firms are not fined for missing the 24-hour warning [L]. |
| C2 | 5 | Makers pay to keep EU market access, with sbomify at $159–199/month as an anchor ([sbomify](https://sbomify.com/pricing/)) [L]. Free EU-funded SME toolkits (OCCTET, OSCRAT) cap WTP [V]. |
| C3 | 4 | The field is filling. Verimu is free until 1 Sep 2026 and billing since ([Verimu](https://verimu.com/), vendor claim) [V]. CRA Evidence (Senda Tech) is listed "from €1", flat rate ([GetApp](https://www.getapp.com.au/software/2141675/cra-evidence)) [V]. sbomify too [L]. |
| C4 | 6 | Open-source lead magnet, maker communities, IHK/BSI events; English works EU-wide. All unvalidated. |
| C5 | 7 | Gross margin 84%; LTV/CAC 7.9; payback 7 months [M]. |
| C6 | 7 | 134 customers ≈ 1.7% of about 8,000 EU micro/small connected-hardware makers (JUDGEMENT). Germany has 7,860 computer/electronics manufacturers (NACE C26) ([Statista](https://statista.com/statistics/383747/enterprises-manufacturing-computer-electronic-optical-products-germany)) [L]. |
| C7 | 6 | Regulatory-interpretation questions, alert reliability and feed upkeep. |
| C8 | 4 | Free EU-funded tools ([OCCTET](https://cybermagazine.com/globenewswire/3359273); [OSCRAT](https://www.bta.bg/en/created-bg/1202158-bulgarian-innovation-hub-joins-european-consortium-launching-cyber-resilience-pl)) [V], and GitHub (Microsoft) could add CRA packs (JUDGEMENT). The 10-year records help retention. |
| C9 | 6 | False-negative liability. Document generators are not legal services under German case law (BGH 2021, I ZR 113/20; JUDGEMENT). |
| C10 | 6 | €490 founding pre-sales are feasible. |

**Hard-rule findings**
- No violation is proven.
- **H4 watch:** GitHub/Microsoft could make it redundant for free, and EU-funded free toolkits are a "free from the authority" substitute.
- **H8 watch:** at least 3 SME-priced tools now exist, but none is shown to be funded or profitable.

**What the researcher missed**
- **New entrants:** Verimu, CRA Evidence and OSCRAT [V]. "Only sbomify is comparable" is out of date.
- **Launch market.** Non-EU makers who sell into the EU (UK and US maker communities) are an English-language segment. EU-wide, English-first is the better launch (see issue (c)).

**Recomputed unit economics [M]**
- **Unit:** ARPA €85; cost to serve €13.60 (support €7.50, payment €2.10, compute €3, alerts €1); gross margin 84%.
- **CAC and churn:** CAC €250 cash / €500 fully loaded; churn 1.8%; LTV €3,967; LTV/CAC 7.9.
- **Requirement:** **134 customers**.
- **24 months, as modelled** (8–12 sales/month into the Dec 2027 deadline): 150 customers, €9.1k run-rate at M24, €8k in M21. But the cash low point is only €518 (M7).
- **At half the pace:** €4.7k at M24, and €8k not reached by M36.

**Top 3 risks**
1. Postponement or simplification of the CRA.
2. Free EU toolkits or GitHub features.
3. Micro-maker WTP.

**Cheapest 30-day money test (≤ €300)**
- Publish a free open-source "cra-clock" CLI.
- Send 100 personalised emails to EU makers, including Tindie and Crowd Supply sellers.
- Sell 5 × €490 founding plans. **Kill:** < 2.

### L2-F2 — CRA importer/distributor vault (EU) — 46.5, KILL

| C | Score | One-line justification |
|---|---|---|
| C1 | 4 | A real per-SKU chore, but it binds only from 11 Dec 2027 ([Springlex Art. 19](https://www.springlex.eu/en/packages/cra/cra-regulation/article-19/)) [L]. |
| C2 | 4 | The shop owner would pay, but CRA awareness is low; there is no WTP evidence. |
| C3 | 4 | No priced deterministic tool was found [L]. Adjacent product-safety (GPSR) and legal-text services can extend into this. |
| C4 | 4 | Agencies ([xictron](https://www.xictron.com/de/blog/cyber-resilience-act-online-shops-pflichten-2026/)) [L], IHK and shop communities are all unvalidated. |
| C5 | 6 | Gross margin 87%; LTV/CAC 6.4. The value stays unproven until enforcement starts [M]. |
| C6 | 6 | About 200 customers out of an unverified pool of about 10,000 (2%). |
| C7 | 7 | Simple CRUD, reminders and exports. |
| C8 | 3 | Easy to copy for GPSR services and marketplaces. |
| C9 | 6 | Risk of giving false comfort. |
| C10 | 3 | Pre-selling 14 months before the duty starts is hard. |

**Hard-rule findings**
- No violation is proven.
- **H4 watch:** Amazon, which H4 names, could extend its compliance-document collection to CRA (JUDGEMENT).

**What the researcher missed**
- The Amazon risk.
- Own-brand importers become manufacturers, which moves them to L2-F1.
- 100% of the revenue is back-loaded behind the Dec 2027 date.

**Recomputed unit economics [M]**
- **Unit:** ARPA €55; cost to serve €7; gross margin 87%.
- **CAC and churn:** CAC €150 cash / €300 fully loaded; churn 2.5%; LTV €1,920; LTV/CAC 6.4.
- **Requirement:** **200 customers**.
- **24 months:** 121 customers, €4.5k at M24; €8k not reached by M36.

**Top 3 risks**
1. CRA postponement.
2. Copying by adjacent services.
3. Low awareness.

**Cheapest 30-day money test (≤ €300)**
- 50 shop emails plus 2 agency partners; sell 5 × €290 founding plans.
- **Kill:** < 2. I expect it to fail.

### L2-F3 — Battery Passport Lite (EU) — 49.0, KILL

| C | Score | One-line justification |
|---|---|---|
| C1 | 6 | A hard market-access gate from 18 Feb 2027 for every light-vehicle (LMT) and industrial (> 2 kWh) battery ([Battery-Tech](https://battery-tech.net/the-eu-battery-passport-belongs-to-whoever-finishes-the-battery-four-months-before-it-becomes-mandatory/)) [L]. |
| C2 | 5 | The assembler pays, and the fee per battery is small. But suppliers and enterprise passport vendors may bundle it. |
| C3 | 4 | Several passport vendors exist (Scantrust, Circuland, dpp-tool, Tracepas); their SME pricing is unknown [L]. |
| C4 | 3 | Niche workshops and trade fairs; no cheap channel. |
| C5 | 7 | Gross margin 83%; LTV/CAC 9.0 thanks to low churn (on assumptions) [M]. |
| C6 | 4 | 63 customers out of an unverified 1,000–3,000 (2–6%). |
| C7 | 4 | Moving standards, uptime and long-term data availability. |
| C8 | 6 | High switching cost once passports are issued. |
| C9 | 3 | Customers' market access depends on one founder's uptime and continuity. |
| C10 | 6 | The deadline makes pre-sales possible. |

**Hard-rule findings**
- No violation is proven.
- **H8 watch:** funded passport vendors (Circulor, Minespider, listed as [U] in lens 2).
- **H2:** buildable, but standards are still moving.

**What the researcher missed**
- **Timing.** A 12-week build from today ends in about January 2027, only weeks before 18 Feb 2027. The buying window may close before launch.
- **Continuity duty.** Passports must outlive the founder's business, a structural liability for a solo founder (JUDGEMENT).

**Recomputed unit economics [M]**
- **Unit:** ARPA €180; cost to serve €30; gross margin 83%.
- **CAC and churn:** CAC €500 cash / €1,000 fully loaded; churn 1%; LTV €9,000; LTV/CAC 9.0.
- **Requirement:** **63 customers**.
- **24 months:** 46 customers, €5.6k at M24; €8k only in M36. The pool is the limit.

**Top 3 risks**
1. The pool is too small.
2. Supplier or vendor bundling.
3. Continuity liability.

**Cheapest 30-day money test (≤ €500)**
- 30 calls to German and Dutch battery assemblers; sell 3 × €990 founding plans.
- **Kill:** 0.

### L3-A — Biogas substrate and EEG-bonus evidence log (Germany) — 62.5, TEST

| C | Score | One-line justification |
|---|---|---|
| C1 | 7 | Daily logging plus a 28 Feb deadline; the bonus lapses permanently if conditions are missed ([WEMAG/Kremp](https://www.wemag.com/sites/default/files/4_kremp_ug_im_eeg_2017_wemag_2019.pdf), older) [L]. HkRNDV §42 also requires a feedstock diary kept 5 years, with verifier plausibility checks ([gesetze-im-internet](https://www.gesetze-im-internet.de/hkrndv/__42.html)) [V]. |
| C2 | 7 | The sufferer is the payer. A plant averages about 3.1 GWh/year ([topagrar census](https://www.topagrar.com/energie/news/biogasbranche-2025-neue-zahlen-zeigen-grosses-potenzial-politik-bremst-ausbau-a-20023918.html)) [L]. One plant reports verifier costs of about €15k/year ([topagrar](https://www.topagrar.com/betriebsleitung/news/biogas-im-wuergegriff-der-buerokratie-b-20001963.html), anecdote) [L]. |
| C3 | 5 | Excel is still the standard, but the gap is closing. Players: Nabisy Software, TerraVis and Biotaktix [L]; Biotaktix "Liefermanager" ([topagrar](https://www.topagrar.com/energie/news/liefermanager-fur-biogasanlagen-digitale-logistik-fur-substrate-und-gulle-20026352.html)) [V]; agriportance for biomethane certification ([WBA](https://www.worldbiogasassociation.org/agriportance-award-winning-software-for-automating-biomethane-and-liquid-co₂-certification/)) [V]. |
| C4 | 6 | The Marktstammdatenregister lists every plant with its operator (JUDGEMENT). Environmental verifiers can refer customers ([UGA guideline](https://www.emas.de/fileadmin/user_upload/4-pub/UGA-Aufgaben-LL_EEG.pdf)) [L]. Competitors use the same channels. |
| C5 | 7 | Gross margin 84%; LTV/CAC 6.0. Annual prepay covers CAC at signing [M]. The price is too low for the value. |
| C6 | 7 | About 170 plants ≈ 2.6% of about 6,500 independents (1.8% of all 9,605). |
| C7 | 6 | Rules differ by EEG version, support peaks in Jan–Feb, and the law needs yearly upkeep. |
| C8 | 5 | Copyable. The pool shrinks as 20-year EEG terms expire (JUDGEMENT). Switching cost builds after one season. |
| C9 | 5 | Diary errors could cost a bonus and lead to claims; the verifier remains the certifier. |
| C10 | 7 | The selling season (Oct–Feb) starts now; founding prepaid sales through verifiers are feasible. |

**Hard-rule findings**
- No violation is proven.
- **H1:** the competitor Nabisy uses OCR; this design deliberately does not [L].
- **H8 watch:** 3+ small vendors with unknown funding and prices. Check them in the 30-day test.

**What the researcher missed**
- The HkRNDV duty [V].
- The additional players listed under C3 [V].
- The free, complete public plant list (Marktstammdatenregister) (JUDGEMENT).
- **Underpricing.** €790/year against about €15k of verifier fees. At **€1,190/year** the requirement falls to 104 plants and €8k arrives in **M18** [M].
- The EEG expiry wave, which slowly shrinks the pool.

**Recomputed unit economics [M]**
- **Unit:** ARPA €65.83; cost to serve €10.80 (support 2.5 h/year ≈ €7.30, hosting/backups €3, payment €0.50); gross margin 84%.
- **CAC and churn:** CAC €300 cash / €550 fully loaded; churn 1%; LTV €3,302; LTV/CAC 6.0.
- **Requirement:** **170 plants**.
- **24 months:** with only two selling seasons inside the window, 163 plants and €7.7k at M24; €8k in **M25**.
- **Cash** never falls below the launch balance.
- **Stress** (two-thirds of the pace, churn 2%): €8k not reached by M36.

**Top 3 risks**
1. Operators stay with Excel plus their verifier.
2. Competitors with hardware links or OCR.
3. Seasonality leaves only two sales windows inside 24 months.

**Cheapest 30-day money test (≤ €600)**
- From the plant register, pick 60 plants in two Länder and approach 15 verifiers.
- Offer a €390 founding first year, prepaid, for the Feb 2027 audit pack, with a free import of last year's Excel.
- **Pass:** ≥ 8 prepaid. **Kill:** < 3.

### L3-B — Parent-duty rosters for parent-run daycares (Germany, Berlin first) — 58.5, KILL

| C | Score | One-line justification |
|---|---|---|
| C1 | 5 | Weekly duty coordination, monthly hours reconciliation and board turnover. The intensity is assumed, not evidenced [L]. |
| C2 | 4 | The association has a budget, but volunteer boards and free tools (Doodle, Spond, WhatsApp) anchor the price low; €49/month is untested. |
| C3 | 5 | Neither lens 3 nor I found a product. The kitaplus parent app has a notice board, mailbox and consent forms but no duty roster ([kitaplus guide](https://www.kita-ggmbh-trier.de/export/sites/kitas/katholische-kita-ggmbh-trier/.galleries/dokumente/5.-Eltern-App-Kurzanleitung-Eltern-Deutsch.pdf)) [V]. Free tools may be "good enough". |
| C4 | 7 | Dense umbrella channels: DaKS (about 800 Berlin initiatives; [DaKS](https://www.daks-berlin.de/system/files/media/files/PM_Warnstreik_final.pdf), older) and BAGE's 29 member organisations ([BAGE](https://www.lobbyregister.bundestag.de/suche/R003613)) [L]. |
| C5 | 7 | Gross margin 85%; LTV/CAC 8.4; payback 6 months [M]. |
| C6 | 4 | About 217 associations ≈ 6% of about 3,600 that run duty systems (JUDGEMENT on 5,000–7,500 initiatives [L]). |
| C7 | 8 | Simple domain, low support, no child data. |
| C8 | 4 | Daycare apps can copy it; board turnover drives churn. |
| C9 | 8 | Low risk. |
| C10 | 7 | Berlin's density makes paid pilots within 90 days plausible. |

**Hard-rule findings:** none. Munich confirms that parents carry the non-staff tasks themselves ([München](https://stadt.muenchen.de/infos/eltern-kind-initiativen.html)) [V].

**What the researcher missed**
- **Berlin alone is too small.** About 800 × 60% ≈ 480 initiatives would need about 45% penetration, so a national roll-out is needed early.
- **Board turnover.** Yearly board changes put about 2%/month churn risk on every account.
- **Alternative market.** US parent-participation co-op preschools have the same "co-op hours" problem (JUDGEMENT, unverified).

**Recomputed unit economics [M]**
- **Unit:** ARPA €49; cost to serve €7.20; gross margin 85%.
- **CAC and churn:** CAC €100 cash / €250 fully loaded; churn 2%; LTV €2,090; LTV/CAC 8.4.
- **Requirement:** **217 associations**.
- **24 months:** 188 associations and €6.9k at M24; €8k in M29. If the umbrella channel delivers up to 20 associations a month: **M21**.

**Top 3 risks**
1. Free tools set the price at zero.
2. The pool is small.
3. Board churn.

**Cheapest 30-day money test (≤ €300)**
- Offer DaKS a free board workshop; call 20 boards; sell 5 annual plans at €490.
- **Kill:** < 2.

### L3-C — Self-administration for small Swiss condominium communities — 49.0, KILL

| C | Score | One-line justification |
|---|---|---|
| C1 | 6 | Monthly billing, annual accounts and owners' meetings; administrators refuse small mandates ([NZZ](https://www.nzz.ch/wirtschaft/hoher-aufwand-wenig-ertrag-viel-streit-warum-kleine-eigentuemergemeinschaften-kaum-noch-verwalter-finden-ld.1892411)) [L]. |
| C2 | 6 | Owners pay. A professional administrator costs CHF 350–500 per unit per year plus a CHF 2,500 base fee ([Beobachter](https://www.beobachter.ch/beratung/rechtsratgeber/wohnen/stockwerkeigentum/der-verwalter-der-stockwerkeigentuemergemeinschaft/was-kostet-ein-stockwerkeigentumsverwalter)) [V]. Cheaper tools also exist (CHF 30/month; CHF 195 one-off) [L]. |
| C3 | 4 | EinfachSTWEG sells the same thing at a similar price ([EinfachSTWEG](https://einfachstweg.ch/)) [L]. Also LIMMOBI, an Excel tool, and ImmoTop2 through HEV [L]. |
| C4 | 3 | No neutral channel: HEV, the main owners' association, distributes ImmoTop2 ([HEV](https://www.hev-schweiz.ch/vermieten/verwalten/immobilien-software/software-immotop2/)) [L]. A foreign founder must rely on paid search. |
| C5 | 4 | On the annual plan: gross margin 64% (below 70%), LTV/CAC 2.7 (below 3), payback about 23 months [M]. |
| C6 | 7 | About 550 communities ≈ 2.3% of about 24,000 self-administered ones (JUDGEMENT on about 97,000 in total [L]). |
| C7 | 5 | Swiss bookkeeping support, with a January–April peak; French and Italian later. |
| C8 | 6 | Strong lock-in once the ledger lives in the app. |
| C9 | 6 | Bookkeeping errors turn into neighbour disputes. |
| C10 | 4 | A foreign, unknown founder in a trust-sensitive market. |

**Hard-rule findings:** none proven. H8 watch: only one same-price competitor is confirmed, and its funding or profitability is unknown.

**What the researcher missed**
- **Card fees.** Swiss cards count as international for an EU Stripe account (3.25% + €0.25; JUDGEMENT).
- **Swiss VAT.** Registration with a fiscal representative once worldwide turnover reaches CHF 100k (JUDGEMENT).
- **Support.** Lay bookkeepers need much more help than the lens assumed.
- **ARPA.** The proposed annual price (CHF 350) gives ARPA **€30.92**, not €37, so the requirement is **550 communities, not 362**.

**Recomputed unit economics [M]**
- **Unit:** cost to serve €11; gross margin 64%.
- **CAC and churn:** CAC €300 cash / €450 fully loaded; churn 1%; LTV €1,195; LTV/CAC 2.7.
- **24 months:** the €10k runs out around **M9**, with a low point of −€3.6k at M13. 276 communities and €3.4k run-rate at M24; €8k not reached by M36.

**Top 3 risks**
1. EinfachSTWEG plus the captured HEV channel.
2. CAC for a foreign founder.
3. Support load.

**Cheapest 30-day money test (≤ CHF 700)**
- Publish 5 German templates, spend CHF 500 on search ads and make 15 calls; sell 5 prepaid founding years at CHF 290.
- **Kill:** < 2.

### L4-F1 — Care-home financing case manager (NRW; the home pays) — 66.5, TEST (rank 1)

| C | Score | One-line justification |
|---|---|---|
| C1 | 8 | €3,108–3,427 a month pre-financed per resident ([vdek](https://www.vdek.com/presse/pressemitteilungen/2025/pflegeheim-monatliche-eigenbeteiligung-steigt-stationaere-pflege.html); [vdek NRW](https://www.vdek.com/LVen/NRW/Presse/Pressemitteilungen/2025/stationaere-pflege-nrw.html)) [L]. 27% of answering welfare offices take 6–12 months and 5% take more than 12 ([Ärzteblatt](https://www.aerzteblatt.de/news/antragsstau-zur-pflege-in-sozialamtern-affb0712-f301-4506-b133-ea19da7c2365)) [L]. |
| C2 | 7 | The payer's pain is quantified: 55% of homes name the welfare office as their largest debtor; 1 in 5 has ≥ €100k outstanding; staff spend 8.3 hours a week on open items ([PwC](https://www.pwc.de/de/pressemitteilungen/2026/fehlende-liquiditaet-in-pflegeheimen-gefaehrdet-die-versorgung.html)) [L]. There is no proof yet that homes will pay for this tool. |
| C3 | 7 | Neither lens 4 nor my search found a product on the home's side [V]. The funded player, Myosotis, sells to welfare offices ([startbase](https://www.startbase.de/news/105-millionen-euro-fuer-myosotis/)) [L]. 60% of homes blame missing documents ([Apotheken Umschau](https://www.apotheken-umschau.de/gesundheitspolitik/pflegeheime-warten-monatelang-auf-hilfe-zur-pflege-von-sozialaemtern-1539809.html)) [L]. |
| C4 | 6 | Homes are listable and concentrated in NRW; sales are outbound B2B; chains buy centrally. |
| C5 | 7 | Gross margin 87%; LTV/CAC 7.8; payback 7.7 months [M]. |
| C6 | 8 | About 61 homes ≈ 1.5% of about 4,000 independent decision units (JUDGEMENT on 11,250 long-term-care homes ([Curacon/Destatis](https://www.curacon.de/fileadmin/user_upload/Curacon/Downloads/Produktbeispiel_sAHBenchmark_Max.pdf)) [L]). |
| C7 | 6 | Form-library upkeep across hundreds of welfare offices (ARD's Report Mainz wrote to 478), relatives' questions and Art. 9 data security. |
| C8 | 6 | Myosotis or care-home ERPs could copy it, and online applications are spreading [V]. Case history creates lock-in. |
| C9 | 5 | Special-category (health) data, an open Legal Services Act (RDG) question (document generators are not legal services per BGH 2021, JUDGEMENT), and reputational exposure. |
| C10 | 6 | Paid pilots within 90 days are plausible. |

**Hard-rule findings**
- No violation is proven.
- **H3:** the founder holds no money and gives no advice. Confirm the RDG and GDPR Art. 9 position with counsel before launch.
- **H4:** no big-tech or bank threat. The care-home ERPs (e.g. Medifox DAN) are a copy risk, not a free-feature kill.
- **H6/H7:** no financing products and no marketplace.

**What the researcher missed**
1. **Online application channels already exist in some districts.** Rhein-Berg accepts online uploads up to 85 MB in total and 3 MB per file ([RBK FAQ](https://www.rbk-direkt.de/download/429/hilfe-zur-pflege-in-einem-pflegeheim---fragen-und-antworten)) [V]. So form-filling is commoditising faster than the lens assumed. The value must sit in:
   - chasing documents from families
   - the date-securing notice
   - renewals
   - receivables
2. **An informal advance notice secures the start date** of aid ([RBK FAQ](https://www.rbk-direkt.de/download/429/hilfe-zur-pflege-in-einem-pflegeheim---fragen-und-antworten); [gegen-hartz](https://www.gegen-hartz.de/urteile/sozialhilfe-formloser-antrag-sichert-anspruch-auf-hilfe-zur-pflege)) [V]. This is the cheapest high-value first feature. Families should also plan about 2 months to gather documents [V].
3. **Processing times vary from weeks to months between offices** ([Landtag BW](https://www.landtag-bw.de/resource/blob/585070/cf26fb5af1795d9bc21e527dfa3bf5bd/17_9244_D.pdf)) [V].
4. **Missing cost lines and CAC.**
   - The lens left out an external data-protection officer, cyber insurance and a data-protection impact assessment (DPIA).
   - The lens's €500 CAC excludes founder time; fully loaded it is about €1,200.

**Recomputed unit economics [M]**
- **Unit:** ARPA €179; cost to serve €23.90 (support €12.30, SMS/e-mail €6, storage €4, payment €1.60); gross margin 87%.
- **CAC and churn:** CAC €400 cash / €1,200 fully loaded; churn 1.2%; LTV €9,306; LTV/CAC 7.8.
- **Requirement:** **61 homes**.
- **24 months:** 77 homes and €9.5k run-rate at M24; €8k in **M21**. Cash low point €1.1k (M7).
- **Fix** (annual prepay, no €99 pilot): cash never falls below €6.6k; €8k in M23.
- **Stress** (churn 2%, 3 homes/month): M32.
- **Value check:** a 25% cut in the 8.3 weekly hours saves about 9 hours a month, worth about €315 at €35/hour (lens assumption), plus earlier cash. At €179/month that is at least a 2× return.

**Top 3 risks**
1. Myosotis bundles a home-side module into its care-home app "myo", which claims 400+ customers ([job post](https://join.com/companies/myo/16523373-mitarbeiter-in-sozialhilfe-hilfe-zur-pflege-m-w-d)) [L].
2. A data breach or an RDG challenge.
3. Cost-squeezed homes decide slowly.

**Cheapest 30-day money test (≤ €1,500)**
- 40 calls and 10 visits to independent NRW homes.
- Offer a 3-month paid pilot at €179/month, or an annual prepay with 2 months free.
- In parallel, buy a counsel check of the RDG and GDPR model for about €1,000 (JUDGEMENT price).
- **Pass:** ≥ 3 paid or signed with a price. **Kill:** < 2, or a negative counsel opinion.

### L4-F2 — SBV case tool (Germany; the employer pays) — 55.5, KILL

| C | Score | One-line justification |
|---|---|---|
| C1 | 5 | Disability-degree (GdB) procedures take 3–9 months ([service.berlin](https://service.berlin.de/dienstleistung/326173/pdf/)) [L]. Real pain, but episodic per employee. |
| C2 | 4 | The employer pays only what is "necessary" under §179(8) SGB IX ([betriebsrat.de](https://www.betriebsrat.de/betriebsratslexikon/sbv/kosten-der-amtsfuehrung)) [L]. IT and data-protection approval adds friction (JUDGEMENT). |
| C3 | 5 | No SBV-specific product was found [L]; works-council software suites were not checked. |
| C4 | 6 | The SBV elections run 1 Oct–30 Nov 2026 ([DGB](https://www.dgb.de/fileadmin/download_center/Aufrufe/Aufruf_SBV-Wahl_2026.pdf)) [L]. Public-sector SBVs list themselves online; seminar providers could refer. |
| C5 | 7 | Gross margin 86%; LTV/CAC 7.7; yearly invoicing [M]. |
| C6 | 8 | About 235 of an assumed 20,000–40,000 SBVs (about 0.8%). |
| C7 | 6 | Simple case management, but data-protection questions differ by employer. |
| C8 | 5 | Works-council suites could add a module; 4-year terms help retention. |
| C9 | 5 | Employee health data and pressure from employers to see it. |
| C10 | 5 | Employer approval slows the money signal. |

**Hard-rule findings**
- No violation is proven.
- **H5 is the weakest pass:** the payer is obliged by law, but only after accepting "necessity". The levy motive (€155–815 per unfilled place per month, [IHK Chemnitz](https://www.ihk.de/chemnitz/standortpolitik/fachkraefte/beratungsangebote/ausgleichsabgabe-2024-6024450) [L]) is real but indirect.

**What the researcher missed**
- **Controller question.** Under GDPR the employer is likely the controller for SBV data, which triggers IT approval cycles (JUDGEMENT).
- **Conversion lag.** Employer conversion will trail SBV enthusiasm. I moderated the ramp to at most 10 new SBVs a month.

**Recomputed unit economics [M]**
- **Unit:** ARPA €45; cost to serve €6.30; gross margin 86%.
- **CAC and churn:** CAC €120 cash / €300 fully loaded; churn 1%; LTV €2,322; LTV/CAC 7.7.
- **Requirement:** **235 SBVs**.
- **24 months:** 166 SBVs, €5.4k at M24; €8k in M33. Cash is always positive (yearly invoices).

**Top 3 risks**
1. The employer refuses to pay.
2. Data-protection blockers.
3. Works-council software adds a module.

**Cheapest 30-day money test (≤ €300)**
- Send a free starter pack to 100 newly elected public-sector SBVs; count cost requests filed and purchase orders issued.
- **Pass:** ≥ 2 purchase orders within 60 days. **Kill:** 0.

### L4-F3 — Tenant benefit-deadline assistant (Germany; the landlord pays) — 43.0, KILL

| C | Score | One-line justification |
|---|---|---|
| C1 | 5 | The average utility back-payment is about €907 ([inFranken](https://www.infranken.de/ratgeber/karriere-geld/3000-euro-nebenkosten-warum-wohnen-in-deutschland-immer-teurer-wird-art-6350661)) [L], and the Jobcenter only covers it if claimed in the month it falls due ([gegen-hartz](https://www.gegen-hartz.de/buergergeld-nachzahlung-fuer-nebenkosten-und-heizung-was-zahlt-das-jobcenter), advocacy) [L]. How often tenants miss it is unknown. |
| C2 | 4 | The landlord's loss is not quantified. |
| C3 | 4 | Only one search was run; housing ERPs could add a notice. |
| C4 | 4 | Committee-driven sales to housing companies are slow. |
| C5 | 4 | LTV/CAC 2.8; payback 21 months [M]. |
| C6 | 6 | 71 of an assumed ~3,000 companies (2.3%). |
| C7 | 6 | Rules keep changing after the July 2026 benefit reform and new court rulings ([heidelberg24](https://www.heidelberg24.de/verbraucher/millionen-betroffene-aufgepasst-gericht-kassiert-neue-grundsicherungsregel-ein-zr-94453739.html)) [L]. |
| C8 | 3 | A housing-ERP incumbent can add a QR notice cheaply. |
| C9 | 5 | A wrong deadline means the tenant loses coverage, which is reputational exposure. |
| C10 | 3 | Utility statements are seasonal and decisions go through committees. |

**Hard-rule findings**
- No violation is proven.
- **H4 watch:** the dominant housing-ERP vendor (Aareon, JUDGEMENT) could ship the same notice.

**What the researcher missed**
- **Customer size.** The typical customer is smaller than the lens's 4,000-unit example. At about 2,000 units (JUDGEMENT) revenue is €160/month, so about 71 customers are needed.
- **Cash CAC** of about €1,500 per company.

**Recomputed unit economics [M]**
- **Unit:** ARPA €160; cost to serve €18; gross margin 89%.
- **CAC and churn:** CAC €1,500 cash / €3,000 fully loaded; churn 1%; LTV €8,520; LTV/CAC 2.8.
- **24 months:** 37 customers, €3.8k at M24; €8k not reached by M36.

**Top 3 risks**
1. ERP copy.
2. The landlord's loss is unproven.
3. Rule volatility.

**Cheapest 30-day money test (≤ €500)**
- 10 interviews with housing companies, then 1 paid pilot on the next statement batch.
- **Kill:** if no landlord can quantify arrears from uncovered back-payments.

### L5-F1 — RambursFlip: cash-on-delivery to prepaid (Romania) — 52.5, KILL

| C | Score | One-line justification |
|---|---|---|
| C1 | 6 | Daily losses: 5–15% of COD orders come back ([Packeta via economica](https://www.economica.net/alexandr-jeleascov-packeta-romania-rata-de-retur-la-magazinele-online-din-romania-este-in-crestere_625270.html/amp)) [L], plus collection fees of 5–9 lei ([infocontact](https://www.infocontact.ro/cat-costa-livrarea-fan-courier-2026/), estimate) [L]. |
| C2 | 5 | Merchants already pay for confirmation tools (Caty €10–499, vendor claim [L]). But the extra value of converting to prepaid is thin once the buyer's incentive and payment fees are paid. |
| C3 | 6 | No Romanian COD-to-prepaid converter was found, by the lens or by my Romanian search [V]. Proof exists in India ([CODFLIP](https://apps.shopify.com/codflip)) [L]. |
| C4 | 5 | App stores, agencies and a Romanian freelancer; a language barrier remains. |
| C5 | 5 | Gross margin 82%, but LTV/CAC only 3.1 at 4.5% churn. On prepay alone, the merchant gets back roughly what it pays [M]. |
| C6 | 5 | 193 of about 3,000 shops big enough to benefit (6.4%) (JUDGEMENT). |
| C7 | 5 | Shopify, WooCommerce and local platforms, WhatsApp template operations and Romanian support. |
| C8 | 4 | Caty, Zarina, GoMag or the processors can copy it. RoPay is spreading at checkout (eMAG, Dedeman) [V]. |
| C9 | 7 | No funds handled; messaging consent is the main risk. |
| C10 | 6 | €99 pilots within 60–90 days, though "refundable" weakens the signal. |

**Hard-rule findings**
- No violation is proven.
- **H4 watch:** it relies on Meta's official API (SMS fallback planned) and on shop-platform app stores.

**What the researcher missed**
1. **The merchant's net gain is much smaller than the lens's €2.50 per converted order.** The lens left out:
   - the buyer's incentive, about €0.5–2 (JUDGEMENT)
   - the payment fee on the now-prepaid order. RoPay merchant fees are negotiated case by case ([ZF](https://www.zf.ro/business-hi-tech/video-emag-parte-proiectul-ropay-schema-plata-fac-parte-12-banci-22329513)) [V]; cards cost about 1.5–2% (JUDGEMENT).

   The net gain is about €0.4–2.2 per converted order. At 10% conversion on 1,000 COD orders, the prepay feature is worth about €95/month, against an €89 fee plus about €34 of Meta messages. Most of the value is order confirmation, which incumbents already sell.
2. **Large merchants are adding RoPay at checkout:**
   - eMAG with ING ([bursa](https://www.bursa.ro/emag-lanseaza-platile-prin-ropay-cu-ing-49685952))
   - Dedeman in July 2026, citing lower processing costs and settlement within 10 seconds ([revistabiz](https://www.revistabiz.ro/ing-si-dedeman-implementeaza-ropay-in-platforma-online-a-magazinului/))
   - RoPay is free for consumers ([economica](https://www.economica.net/brd-extinde-functionalitatile-ropay-plati-pe-net-prin-scanare-de-cod-qr-platile-prin-ropay-sunt-necomisionate_948769.html))

   All [V]. Processors may therefore push prepaying natively.
3. **Growth burns cash.** The Romanian freelancer is a fixed cost from day 1. With 4.5% churn, growth consumes cash faster than revenue replaces it.

**Recomputed unit economics [M]**
- **Unit:** ARPA €75, excluding Meta fees passed through; cost to serve €13.20; gross margin 82%.
- **CAC and churn:** CAC €300 cash / €450 fully loaded; churn 4.5%; LTV €1,373; LTV/CAC 3.1.
- **Requirement:** **193 merchants**.
- **24 months, as proposed:** cash runs out around M12 and growth stalls at about 7–13 merchants (−€8.6k by M24).
- **Optimistic** (CAC €150, churn 3%): €8k in M19. The idea is very sensitive to CAC.

**Top 3 risks**
1. Conversion below 5%, because Romanian buyers choose COD out of distrust.
2. Copying by incumbents.
3. Meta pricing or template recategorisation.

**Cheapest 30-day money test (≤ €1,000)**
- Concierge test at 2–3 shops: send WhatsApp prepay links on 300 COD orders through a provider's trial of the official API, and measure conversion.
- Charge €99/month.
- **Pass:** ≥ 8% conversion and ≥ 3 paying shops. **Kill:** < 5% conversion.

### L5-F2 — Vorbestell-Desk: pre-orders for butchers, bakeries and farm shops (Germany) — 48.5, KILL

| C | Score | One-line justification |
|---|---|---|
| C1 | 5 | Intense at Christmas and Easter, moderate otherwise (an assumption) [L]. |
| C2 | 4 | €35/month is untested; phone and paper or existing apps already do the job. |
| C3 | 3 | Competitors already sell the core: white-label butcher pre-order apps where customers pick a pickup time and branch, the order prints in the shop, and they pay at the till ([Lotter](https://apps.apple.com/app/id1508324294), [Schreder](https://apps.apple.com/app/id1482256245), [Breidert](https://apps.apple.com/app/id1536133403), [Metzler](https://apps.apple.com/app/id1551760911), [Steinleitner](https://apps.apple.com/app/id1596895369)) [V]; and Shopify's butcher shops with local pickup and prepayment ([Shopify](https://www.shopify.com/de/metzger)) [V]. |
| C4 | 5 | Guilds and cold visits are cheap but slow. |
| C5 | 4 | Gross margin 78%; LTV/CAC 2.6; churn after the season [M]. |
| C6 | 7 | About 392 of about 15,000 shops (2.6%) (JUDGEMENT). |
| C7 | 7 | A simple product with seasonal peaks. |
| C8 | 3 | Easy to copy; POS and scale vendors could add it. |
| C9 | 8 | Low liability. |
| C10 | 7 | A Christmas 2026 concierge pilot can be sold now. |

**Hard-rule findings**
- **H8 is borderline.** Two of the three competitors H8 needs are confirmed:
  - Shopify: clearly profitable, similar price, and markets to German butchers [V].
  - The white-label app vendor(s): about 7 butchers use the same app model; funding is unknown [V].

  The third would be WooCommerce pickup-slot plugins (JUDGEMENT, unverified). I do not count it as a violation on this evidence.

**What the researcher missed**
- The whole competitor check (now done; see issue (d)).
- **German WhatsApp rates.** Utility templates cost about €0.0456 and marketing about €0.1131 per message ([ChatMaxima](https://chatmaxima.com/whatsapp-api-pricing/germany/)) [V]. One source says free service and in-window utility messages become chargeable from 1 Oct 2026 (unconfirmed) [V].
- **Deposit fees.** A card deposit costs the shop about 1.5% + €0.25 (JUDGEMENT).

**Recomputed unit economics [M]**
- **Unit:** ARPA €35; cost to serve €7.80 (WhatsApp €2.30, support €4.20, hosting €1, payment €0.30); gross margin 78%.
- **CAC and churn:** CAC €150 cash / €300 fully loaded; churn 3.5%; LTV €777; LTV/CAC 2.6.
- **Requirement:** **392 shops**.
- **24 months:** 202 shops, €3.8k at M24; €8k not reached by M36.

**Top 3 risks**
1. Existing apps and Shopify.
2. Churn after the season.
3. Older customers refuse to pay deposits.

**Cheapest 30-day money test (≤ €900)**
- Sell a €149 "Christmas 2026" concierge pilot to 10 shops within 50 km, run on forms, payment links and the WhatsApp Business app.
- **Pass:** ≥ 5 paid. **Kill:** < 3.

### L5-F3 — WP-Wächter: monthly heat-pump efficiency check (Germany) — 41.5, KILL

| C | Score | One-line justification |
|---|---|---|
| C1 | 5 | Real but invisible waste; seasonal. |
| C2 | 3 | Consumer WTP for €4.99 is unproven, and the value is front-loaded. |
| C3 | 4 | Maker apps and do-it-yourself dashboards exist [L]; the gap in diagnosis is unverified. |
| C4 | 5 | Owner forums and YouTube are cheap channels. |
| C5 | 3 | Gross margin 80%, but LTV €61 against a €30 CAC gives 2.0 [M]. |
| C6 | 6 | About 4,750 subscribers ≈ 1.9% of about 250,000 supported units (JUDGEMENT; about 847k heat pumps sold 2023–25 [L]). The share willing to pay is small. |
| C7 | 5 | API rate limits and paid tiers ([Home Assistant ViCare](https://www.home-assistant.io/integrations/vicare); [Homey Daikin](https://community.homey.app/t/app-pro-and-cloud-daikin-onecta/54088/338)) [L]. |
| C8 | 2 | The makers hold the data and can ship the same feature free. Vaillant has no official API, and the quota on its reverse-engineered API was cut ([HA forum](https://community.home-assistant.io/t/myvaillant-integration/542610?page=24)) [L]. |
| C9 | 6 | Setting changes go through the installer. |
| C10 | 6 | Community pre-sales are feasible. |

**Hard-rule findings**
- **H4 is borderline.** The niche's incumbents (the makers) control both the data and free apps, and Viessmann's free tier may be capped per app rather than per user [L]. A manual-entry path exists, so I do not count it as a violation.

**What the researcher missed**
- VAT: the net price is €4.19.
- The ChartMogul benchmark for ARPA under $25 is 6.1% churn a month [V].
- Counting the marketing that replaces churned users, the requirement is **about 4,750 subscribers**, not about 3,000.

**Recomputed unit economics [M]**
- **Unit:** ARPA €3.81 (blend of monthly and annual); cost to serve €0.75; gross margin 80%.
- **CAC and churn:** CAC €25 cash / €30 fully loaded; churn 5%; LTV €61; LTV/CAC 2.0.
- **24 months:** about 360 subscribers, run-rate about €0. The €10k bottoms out at about €0.5k.

**Top 3 risks**
1. Makers ship the feature.
2. API access is withdrawn or capped.
3. Churn once the first fixes are made.

**Cheapest 30-day money test (≤ €400)**
- Pre-sell a €39 "founding season" in 3 forums and 1 YouTube sponsorship (€300).
- **Pass:** ≥ 100. **Kill:** < 30.

### BASE — Daily automated check-in call for people 65+ living alone (Germany) — 42.5, KILL

| C | Score | One-line justification |
|---|---|---|
| C1 | 6 | Lying undiscovered is a grave but rare event; the family worries every day. |
| C2 | 4 | The family pays. US prices run from $14.99 (IamFine, per the brief) to $34.95 a month (FineThanx, search extract; attribution uncertain, [Senior Housing News](https://seniorhousingnews.com/?p=2537)) [V]. HealthExec reports that "enrollment in check-in services for seniors remains low" (headline only, [HealthExec](https://healthexec.com/topics/patient-care/precision-medicine/enrollment-check-services-seniors-remains-low)) [V]. Free substitutes exist. |
| C3 | 5 | No German phone-only check-in service was found [V] ([web.de](https://web.de/magazine/ratgeber/kind-familie/notrufsysteme-senioren-moeglichkeiten-34479312) names only device-based providers). The gap may be a lack of demand rather than of supply. |
| C4 | 3 | Paid consumer acquisition aimed at adult children; no cheap named channel. |
| C5 | 2 | €9.90 including VAT is €8.32 net. With €2.70 cost to serve, gross margin is 68% (below 70%), LTV/CAC 1.2 and payback 16 months [M]. |
| C6 | 9 | About 5,460 families needed out of roughly 4 million people (JUDGEMENT). |
| C7 | 5 | Telephony reliability, escalations and support for elderly users. |
| C8 | 4 | Trivial to copy; alarm-service providers could add a phone-only tier. |
| C9 | 3 | A missed alert followed by a death is severe reputational and legal exposure. |
| C10 | 6 | Landing-page pre-sales are easy to run. |

**Hard-rule findings**
- **No violation.**
- **H6:** the senior's own consent must be built into the flow, because the family pays.
- **H8:** no German competitor was found. The Maryland state programme is free, which shows the US model ([Maryland Senior Call Check](https://aging.maryland.gov/Pages/senior-call-check.aspx)) [V].

**What the brief's assumptions missed**
1. **"About 1,000 paying families" is wrong.** 1,000 × (€8.32 − €2.70) = €5,620 a month of gross margin, below €8,000 before any overhead. With €850 overhead and the marketing needed to replace 5% churn at €80 CAC, the requirement is **about 5,460 families**. Even the optimistic case (CAC €40, churn 3%) needs 2,003.
2. **The €3 cost holds only with EEA-origin call routing.** Twilio lists calls to German mobiles at about $0.376/min at the general rate, against about $0.042/min from an EEA origin and about $0.028/min to landlines ([Twilio](https://www.twilio.com/en-us/voice/pricing/de)) [V]. Thirty billed minutes a month to a mobile at the general rate would cost more than the net price.
3. **Churn is high.** The ChartMogul median is 6.1% a month for ARPA under $25 [V], before deaths and moves into care.

**Recomputed unit economics [M]**
- **Unit:** ARPA €8.32; cost to serve €2.70 (calls about €1.00, retries €0.20, alert SMS €0.24, payment €0.47, hosting €0.10, support €0.70); gross margin 68%.
- **CAC and churn:** CAC €80 cash / €90 fully loaded; churn 5%; LTV €112; LTV/CAC 1.2.
- **24 months:** the €10k is gone around M8 with only about 70 customers acquired. Cash is at −€9.9k by M24.
- **Optimistic** (CAC €40, churn 3%): still about 290 customers at M24 and about €0.4k run-rate. A cheap product with expensive acquisition cannot fund its own growth.

**Top 3 risks**
1. Low WTP and high churn.
2. Life-safety liability.
3. Copying by alarm-service providers.

**Cheapest 30-day money test (≤ €700)**
- Landing page plus €500 of social and search ads aimed at adult children; sell the first month at €9.90 or a year at €99.
- **Pass:** CAC ≤ €40 and ≥ 20 paid. **Kill:** anything worse.

### Known issues (a)–(d), resolved

**(a) Boarding-stable billing: lens 1 finalist (L1-B) vs lens 3 kill (Stabley).**
- **Neither verdict was proven, and each is half right.**
  - **Lens 1 is right that no hard rule is violated.**
    - One free product of unknown funding is not "3 or more funded or clearly profitable competitors" (H8).
    - Stabley is not shown to be the niche's dominant incumbent (H4).
  - **Lens 3 is right that a free product claiming billing is a serious commercial threat.**
- **Evidence on Stabley:**
  - The only source for its billing is a directory listing ([AlternativeTo](https://alternativeto.net/software/stabley/about/)) [V]. My search returned the same listing, and the page fetch failed.
  - My German search for stable billing found no stable-specific tool, only generic invoicing with SEPA add-ons [V].
- **Consequence:** L1-B stays alive under the hard rules but scores 52.0 (KILL band) on CFO grounds: ARPA €45, LTV/CAC 4.2, €8k only in M34.
- **The decisive check costs one day:** sign up to Stabley and run a month of boarder invoices.

**(b) Does the German condominium (WEG) "crowded" logic apply to Swiss L3-C?**
- **Partly.** The German kill rested on two things:
  - at least 3 funded or profitable tools selling to self-managers (Dotega, pre-seed €1.3m ([HTGF](https://www.htgf.de/dotega-pre-seed-finanzierung/)); Win-CASA ([softwareabc24](https://www.softwareabc24.de/vergleiche/intex-hausverwaltung-vs-win-casa)); Lexware; selbstverwalten.com) [L]
  - a captured owners' association channel (Wohnen im Eigentum → Dotega, [it-boltwise](https://www.it-boltwise.de/?p=1548390)) [L]
- **In Switzerland:**
  - **Channel capture applies.** HEV distributes ImmoTop2 [L].
  - **The "3 funded competitors" part is not shown.** There is one same-price direct competitor (EinfachSTWEG at CHF 30/month), one with an unknown price (LIMMOBI), and one CHF 195 Excel tool [L].
- **Result:** no H8 kill. But L3-C fails on CFO numbers: GM 64%, LTV/CAC 2.7, 550 communities needed, and cash below zero by M9.
- **The value proposition itself is real.** Professional administration costs CHF 350–500 per unit per year plus a CHF 2,500 base fee ([Beobachter](https://www.beobachter.ch/beratung/rechtsratgeber/wohnen/stockwerkeigentum/der-verwalter-der-stockwerkeigentuemergemeinschaft/was-kostet-ein-stockwerkeigentumsverwalter)) [V]. What is missing is a cheap channel.

**(c) Twelve of fifteen finalists launch in Germany. Evidence-driven or anchored by the German baseline?**

| ID | Launch market | Evidence-driven or anchored? | Clearly better market? |
|---|---|---|---|
| L1-A | Germany | **Evidence-driven:** France, Spain and the Netherlands are already served; no German practice plans found in 4 searches; the GOT floor explains the gap [L][V] | No (AT/CH later) |
| L1-B | Germany | **Partly anchored:** no cross-country comparison was made | Not evidenced (France unchecked) |
| L1-C | Germany | **Evidence-driven:** the language gap; largest German-speaking pool [L] | No |
| L2-F1 | EU, launch Germany | **Partly anchored:** the duty is EU-wide and the product is English-first; Germany was chosen only on a firm count | **Yes:** launch EU-wide, English-first, including non-EU makers who sell into the EU (UK/US maker communities). Keep Germany as one outbound region |
| L2-F2 | EU, launch Germany | **Anchored** (the lens itself calls the evidence weak) | Netherlands equally plausible; none better evidenced |
| L3-A | Germany | **Evidence-driven:** the EEG regime is German-only; about 9,600 plants [L] | No |
| L3-B | Germany (Berlin) | **Evidence-driven:** parent-run daycares are a German institution; Berlin is the densest [L] | US parent co-op preschools possible (JUDGEMENT), not clearly better |
| L4-F1 | NRW | **Evidence-driven:** highest co-payments; Pflegewohngeld paid to homes; the US is already served [L] | No |
| L4-F2 | Germany | **Forced:** the SBV is a German statutory institution | — |
| L4-F3 | Germany | **Forced:** a German benefit rule | — |
| L5-F2 | Germany | **Partly anchored:** Wero launched in Germany first [L]; shop density is background knowledge | Not evidenced |
| L5-F3 | Germany | **Partly anchored:** largest recent install base [L]; UK and Nordics unchecked | Unverified alternatives |

Seven of the twelve are evidence-driven or forced by German law. Five are partly anchored. Only **L2-F1** has a clearly better launch plan (EU-wide, English-first). I scored every idea as proposed. (L2-F3 is "EU, Germany + Netherlands", based on an assumption.)

**(d) L5-F2's competitor check was incomplete.**
- **Now done, and the result is negative for the idea.**
  - Butcher-specific pre-order apps with pickup times already run under at least 7 butcher brands [V].
  - Shopify markets butcher shops with local pickup and prepayment in Germany [V].
  - The remaining wedge (WhatsApp ordering, instant deposits, slot capacity, production lists) is copyable.
- C3 falls to 3 and H8 is borderline. The score is 48.5, KILL.

### Inferences
- **Small sales capacity, not small markets, is the binding constraint for the B2B finalists.**
  - In high-touch sales (vets, care homes) a solo founder closes about 4 accounts a month. So only ideas needing ≤ ~70 such accounts reach €8k inside 24 months.
  - Lower-touch ideas need a channel that delivers 10+ accounts a month. L2-F1 does so only under my assumption that the Dec 2027 CE deadline drives buying.
- **Pricing structure matters as much as the idea.**
  - A minimum platform fee (L1-A) or a higher list price (L3-A) moves the €8k month about 7 months earlier in my model.
  - Annual prepay mainly removes cash risk. For L4-F1 it lifts the cash floor from €1.1k to €6.6k, at the cost of reaching €8k 2 months later.

### Gaps
- **Competitor facts I could not establish:**
  - funding and prices of Nabisy Software, TerraVis, Biotaktix, EinfachSTWEG, LIMMOBI, Verimu and CRA Evidence
  - Stabley's billing depth
  - the identity of the white-label butcher-app vendor
- **Pool sizes I could not establish:**
  - the number of SBVs
  - the number of Romanian online shops
  - the self-administered share of Swiss communities

---

## (3) Ranking of all 16 IDs and which beat BASE

### Takeaway
**14 of 15 finalists score above my BASELINE (42.5), but only 3 reach TEST.**
- **Beat BASE by more than an evaluator-noise band of ±5 points:** 12 ideas.
- **Tie with BASE:** L2-F2 (+4.0) and L4-F3 (+0.5).
- **Below BASE:** L5-F3 (−1.0).

### Cited Findings — ranking
| Rank | ID | Score | Verdict | Δ vs BASE | €8k run-rate (as proposed) [M] | One-line reason |
|---|---|---|---|---|---|---|
| 1 | L4-F1 | 66.5 | TEST | +24.0 | M21 | Quantified payer pain (PwC 2026); 61 homes needed; LTV/CAC 7.8 |
| 2 | L3-A | 62.5 | TEST | +20.0 | M25 (M18 at €1,190) | Sufferer = payer, annual prepay, season starts now; competitors closing the gap |
| 3 | L1-A | 60.5 | TEST | +18.0 | M28 (M21 with fix) | Proven abroad, no German player; owner uptake untested |
| 4 | L3-B | 58.5 | KILL | +16.0 | M29 | Dense umbrella channel, but needs ~6% of a small pool |
| 5 | L2-F1 | 56.5 | KILL | +14.0 | M21 (fragile) | Live duty; but new entrants and free EU toolkits |
| 6 | L4-F2 | 55.5 | KILL | +13.0 | M33 | Clear statutory payer route, but a reluctant employer |
| 7 | L1-C | 53.0 | KILL | +10.5 | not by M36 | Low ARPA, high churn |
| 8 | L5-F1 | 52.5 | KILL | +10.0 | not by M36 | Thin merchant ROI; growth burns cash |
| 9 | L1-B | 52.0 | KILL | +9.5 | M34 | Free-billing claim; low WTP |
| 10 | L2-F3 | 49.0 | KILL | +6.5 | M36 | Small unverified pool; continuity liability |
| 11 | L3-C | 49.0 | KILL | +6.5 | not by M36 | GM 64%, LTV/CAC 2.7; cash runs out (ranked below L2-F3 on cash) |
| 12 | L5-F2 | 48.5 | KILL | +6.0 | not by M36 | Competitors exist (apps, Shopify) |
| 13 | L2-F2 | 46.5 | KILL | +4.0 | not by M36 | Value starts only in Dec 2027 |
| 14 | L4-F3 | 43.0 | KILL | +0.5 | not by M36 | CAC €1,500+, ERP copy risk |
| 15 | BASE | 42.5 | KILL | 0 | not by M36 | GM 68%, LTV/CAC 1.2; cash gone by M8 |
| 16 | L5-F3 | 41.5 | KILL | −1.0 | not by M36 | LTV €61; makers own the data |

### Inferences
- **The BASELINE scores lower here than in any lens** (51–57.5). The lenses priced it at €9.90 without VAT and without the marketing needed to replace 5% monthly churn. Even with generous scores on C4 and C5, it stays below 50.
- **The top three are within 6 points of each other.** Their order depends on a few untested numbers, each resolvable within 90 days:
  - homes' willingness to pay (L4-F1)
  - plant operators' willingness to leave Excel (L3-A)
  - owner uptake per practice (L1-A)

---

## (4) My €10,000 bet and my never-fund pick

### Takeaway
I would bet on **L4-F1 (care-home financing case manager, NRW)**, run with CFO pricing and staged spending. I would never fund **L5-F3 (WP-Wächter)**. I would not fund the BASELINE either.

### Why L4-F1
- **The payer's money reason is the best evidenced of all 16.** It is quantified by an independent 2026 survey: 55% of homes name the welfare office as their largest debtor, 1 in 5 has ≥ €100k outstanding, and staff spend 8.3 hours a week on it ([PwC](https://www.pwc.de/de/pressemitteilungen/2026/fehlende-liquiditaet-in-pflegeheimen-gefaehrdet-die-versorgung.html)) [L]. Each month of delay pre-finances €3.1–3.4k per resident [L].
- **It needs the fewest customers of any idea that reaches €8k: 61 homes** (1.5% of the reachable pool). ARPA is €179, gross margin 87%, LTV/CAC 7.8 [M].
- **It is the only idea that reaches €8k run-rate inside 24 months in both the base case (M21) and the cash-safe version (M23).**
  - The cash-safe version uses annual prepay, keeping cash ≥ €6.6k [M].
  - The stress case (churn 2%, 3 homes/month) still gets there by M32.
- **No home-side competitor was found in two separate searches** [V][L]. The funded player sells to the authorities instead.

**How I would spend the €10,000 (JUDGEMENT)**
1. **Days 1–30, about €1.5k.** Counsel check on the Legal Services Act (RDG) and GDPR Art. 9; 40 calls and 10 visits to NRW homes; target ≥ 3 paid commitments at list price.
2. **Weeks 5–16, about €2.5k.** Build the core: case file, family document chasing, date-securing notice, renewals, receivables board. Set up company, insurance and DPO.
3. **Keep ≥ €5k in reserve.** Sell annual prepay with 2 months free; do not offer the discounted €99 pilot.

**Walk-away triggers**
- Counsel says no.
- Fewer than half of the interviewed homes have ≥ 3 financing cases open for more than 3 months.
- Myosotis offers a free home-side module.

**My subjective odds of €8k/month by month 24:** about 30% for L4-F1, about 25% for L3-A at €1,190, about 15% for L1-A (JUDGEMENT).

**Runner-up: L3-A at €1,190 per plant per year.** It is the cash-safest idea: annual prepay means cash never falls below the launch balance, and the selling season starts this month. I would switch to it if the RDG or GDPR check on L4-F1 fails.

### Never fund: L5-F3 (and the BASELINE as specified)
**L5-F3 is structurally unfundable.**
- At €4.99 including VAT (€3.81 net blended), LTV is about €61 against a €30 CAC (LTV/CAC 2.0).
- It needs about **4,750 paying households** [M].
- The makers hold the data and the free apps. Vaillant has no official API, and the quota on its unofficial one has been cut [L]. Viessmann's free tier may be capped per app [L].
- Any success would invite the makers to ship the same check for free.

**The BASELINE fails every CFO test.**
- Gross margin 68%, LTV/CAC 1.2, payback 16 months.
- The €10k is gone around month 8, and €8k is never reached, even in the optimistic case [M].

### Inferences
- **Every idea I would fund sells a ≥ €65/month (€790+ a year) workflow** to a business that loses money visibly when the workflow fails.
- **Every idea I would refuse sells a < €10/month reassurance or optimisation** to consumers or volunteers.

---

## (5) Verification log

### Takeaway
I checked 16 claims with 15 searches (rows 1–16). Results:
- **confirmed:** 8, mostly "nothing found" absence checks
- **contradicted:** 3
- **new evidence for an open question:** 2
- **unverifiable:** 3

Four more lens or brief numbers were contradicted by recomputation rather than search (rows 17–20). All five page fetches failed (rows 21–25).

### Cited Findings — log
| # | Claim checked (source lens) | Result | Evidence / URL |
|---|---|---|---|
| 1 | Stabley is free and includes boarder billing (lens 3 kill #4) | **Unverifiable.** Only the same directory listing; the official site was not reachable | [AlternativeTo](https://alternativeto.net/software/stabley/about/) [V] |
| 2 | No German stable-specific billing tool exists (lens 1, L1-B) | **Confirmed** (absence). Only generic invoicing + SEPA tools; Stable Secretary (UK/US) bills from $6.95 | [sevDesk SEPApro](https://sevdesk.de/integrationen/sepapro/); [B2B Router](https://www.b2brouter.net/de/funktionen/); [Capterra AT](https://www.capterra.at/software/129021/stable-secretary) [V] |
| 3 | Swiss self-administration value and competitors (lens 3, L3-C) | **New evidence:** administrator fees CHF 350–500/unit/yr + CHF 2,500 base; no new software competitor found | [Beobachter](https://www.beobachter.ch/beratung/rechtsratgeber/wohnen/stockwerkeigentum/der-verwalter-der-stockwerkeigentuemergemeinschaft/was-kostet-ein-stockwerkeigentumsverwalter); [WEKA](https://www.weka.ch/bau-immobilien/immobilien/immobilienverwaltung/rechner-heiz-und-nebenkostenabrechnung-im-stockwerkeigentum.html) [V] |
| 4 | L5-F2 H8 pass "on absence of evidence" (lens 5) | **Contradicted.** White-label butcher pre-order apps (≥ 7 brands) and Shopify butcher shops with local pickup and prepayment exist | [Lotter](https://apps.apple.com/app/id1508324294); [Schreder](https://apps.apple.com/app/id1482256245); [Shopify](https://www.shopify.com/de/metzger); [inFranken](https://www.infranken.de/lk/wuerzburg/grillabend-ohne-stress-mit-dieser-app-kannst-du-beim-metzger-grillgut-bestellen-art-2802701) [V] |
| 5 | German WhatsApp utility template ≈ €0.03–0.05 (lens 5 assumption) | **Confirmed (secondary):** utility ≈ €0.0456, marketing ≈ €0.1131. One source claims a free-tier change on 1 Oct 2026 (unconfirmed) | [ChatMaxima](https://chatmaxima.com/whatsapp-api-pricing/germany/); [whautomate](https://whautomate.com/whatsapp-business-api-pricing-germany); [Chatarmin](https://chatarmin.com/en/blog/whats-app-api-pricing) [V] |
| 6 | BASE cost ≈ €3/customer/month (brief) | **Confirmed only with EEA-origin routing:** landline ≈ $0.028/min, EEA-origin mobile ≈ $0.042/min; general mobile rate ≈ $0.376/min would exceed the price | [Twilio DE](https://www.twilio.com/en-us/voice/pricing/de); [Plivo DE](https://www.plivo.com/voice/pricing/de/) [V] |
| 7 | BASE: German phone-only competitors; demand | **Confirmed absence in Germany.** US: Maryland's free programme; FineThanx $34.95/month; "enrollment remains low" (headline) | [Maryland](https://aging.maryland.gov/Pages/senior-call-check.aspx); [HealthExec](https://healthexec.com/topics/patient-care/precision-medicine/enrollment-check-services-seniors-remains-low); [web.de](https://web.de/magazine/ratgeber/kind-familie/notrufsysteme-senioren-moeglichkeiten-34479312) [V] |
| 8 | SMB churn assumptions of 0.8–3%/month across lenses | **Contradicted for low-ARPA ideas** (Benchmark): median 6.1%/month at ARPA < $25; 2.2% at > $500 | [ChartMogul](https://chartmogul.com/blog/good-customer-churn-rate/); [ChartMogul cheat sheet](https://chartmogul.com/resources/churn-cheat-sheet); [focus-digital](https://focus-digital.co/average-churn-rate-by-industry-saas/) [V] |
| 9 | No practice-run vet plans in Germany (lens 1, L1-A) | **Confirmed** (absence). New anchors: cat check about €23.62 at 1× GOT; insurers' prevention modules up to €100/yr | [HanseMerkur cats](https://www.hansemerkur.de/haustiere/vorsorge-katze); [HanseMerkur dogs](https://www.hansemerkur.de/haustiere/vorsorge-hund); [AniCura](https://www.anicura.de/globalassets/de-DE/pdfs/tkv_broschure_web_202006.pdf) [V] |
| 10 | RoPay merchant fees (lens 5 gap) | **Unverifiable:** negotiated bilaterally; free for consumers; eMAG and Dedeman (July 2026) adopting | [ZF](https://www.zf.ro/business-hi-tech/video-emag-parte-proiectul-ropay-schema-plata-fac-parte-12-banci-22329513); [bursa](https://www.bursa.ro/emag-lanseaza-platile-prin-ropay-cu-ing-49685952); [revistabiz](https://www.revistabiz.ro/ing-si-dedeman-implementeaza-ropay-in-platforma-online-a-magazinului/); [economica](https://www.economica.net/brd-extinde-functionalitatile-ropay-plati-pe-net-prin-scanare-de-cod-qr-platile-prin-ropay-sunt-necomisionate_948769.html) [V] |
| 11 | No parent-duty roster product (lens 3, L3-B) | **Confirmed** (absence). The kitaplus parent app has no duty roster | [kitaplus guide](https://www.kita-ggmbh-trier.de/export/sites/kitas/katholische-kita-ggmbh-trier/.galleries/dokumente/5.-Eltern-App-Kurzanleitung-Eltern-Deutsch.pdf); [München](https://stadt.muenchen.de/infos/eltern-kind-initiativen.html) [V] |
| 12 | No Romanian COD-to-prepaid converter (lens 5, L5-F1) | **Confirmed** (absence). Only generic WhatsApp-commerce tools; WhatsApp in-chat payments are India-only at 360dialog | [WATI](https://www.wati.io/integrations-library/shopify/); [360dialog](https://docs.360dialog.com/docs/messaging/payments/payments-india-only/receive-whatsapp-payments-via-payment-links) [V] |
| 13 | No home-side tool for social-assistance applications (lens 4, L4-F1) | **Confirmed** (absence). New: online application channels exist in some districts; informal notice secures the start date; processing times vary widely | [RBK FAQ](https://www.rbk-direkt.de/download/429/hilfe-zur-pflege-in-einem-pflegeheim---fragen-und-antworten); [Landtag BW](https://www.landtag-bw.de/resource/blob/585070/cf26fb5af1795d9bc21e527dfa3bf5bd/17_9244_D.pdf); [gegen-hartz](https://www.gegen-hartz.de/urteile/sozialhilfe-formloser-antrag-sichert-anspruch-auf-hilfe-zur-pflege) [V] |
| 14 | "Only sbomify sells a comparable CRA tool" (lens 2, L2-F1) | **Contradicted:** Verimu (billing since Sep 2026), CRA Evidence ("from €1", flat rate), and EU-funded OSCRAT and OCCTET for SMEs | [Verimu](https://verimu.com/); [GetApp](https://www.getapp.com.au/software/2141675/cra-evidence); [Cyber Magazine](https://cybermagazine.com/globenewswire/3359273); [BTA](https://www.bta.bg/en/created-bg/1202158-bulgarian-innovation-hub-joins-european-consortium-launching-cyber-resilience-pl) [V] |
| 15 | Biogas: duty and competitor field (lens 3, L3-A) | **New evidence:** HkRNDV §42 feedstock-diary duty with verifier checks; more players (Biotaktix Liefermanager, agriportance, bioGASMAS) | [HkRNDV §42](https://www.gesetze-im-internet.de/hkrndv/__42.html); [topagrar](https://www.topagrar.com/energie/news/liefermanager-fur-biogasanlagen-digitale-logistik-fur-substrate-und-gulle-20026352.html); [WBA](https://www.worldbiogasassociation.org/agriportance-award-winning-software-for-automating-biomethane-and-liquid-co₂-certification/); [ki-syndikat](https://www.ki-syndikat.de/tools/biogasmas/) [V] |
| 16 | Swiss software price anchor CHF 30/month (lens 3) | **Unverifiable** this session (page fetch failed) | [EinfachSTWEG](https://einfachstweg.ch/) |
| 17 | BASE "≈ 1,000 paying families needed" (brief) | **Contradicted by recomputation:** about 5,460 (about 2,000 optimistic) | inputs: rows 6–8; [M] |
| 18 | L5-F1 merchant value €2.50 per converted order (lens 5) | **Contradicted by recomputation:** net about €0.4–2.2 after buyer incentive and payment fee | inputs: [infocontact](https://www.infocontact.ro/cat-costa-livrarea-fan-courier-2026/) [L]; row 10; [M] |
| 19 | L3-C needs 362 communities (lens 3) | **Contradicted by recomputation:** about 550 at the proposed CHF 350/yr annual price | [M] |
| 20 | L1-C needs about 655 customers; churn 3% (lens 1) | **Contradicted:** about 779 with benchmark churn and replacement marketing | row 8; [M] |
| 21 | Stripe/GoCardless fees | **Fetch failed (DNS);** used as JUDGEMENT | https://stripe.com/de/pricing |
| 22 | Identity of the white-label butcher-app vendor | **Fetch failed (DNS)** | https://apps.apple.com/app/id1508324294 |
| 23 | Stabley official details | **Fetch failed (DNS)** | https://alternativeto.net/software/stabley/about/ |
| 24 | HealthExec article body | **Fetch failed (DNS)** | https://healthexec.com/topics/patient-care/precision-medicine/enrollment-check-services-seniors-remains-low |
| 25 | EinfachSTWEG price page | **Fetch failed (DNS)** | https://einfachstweg.ch/ |

### JUDGEMENT items used (unverified this session)
- **Payment fees:** Stripe EEA cards 1.5% + €0.25; non-EEA (incl. Swiss) cards 3.25% + €0.25; SEPA Direct Debit €0.35; Stripe Billing +0.7%. GoCardless about 1% + €0.20, capped.
- **Pricing and tax rules:**
  - German consumer prices must include VAT.
  - Swiss VAT registration with a fiscal representative applies once worldwide turnover reaches CHF 100k.
  - A UG's corporate and trade taxes are about 30%.
- **Legal points:**
  - BGH 9 Sep 2021, I ZR 113/20: a contract-document generator is not a legal service under the RDG.
  - The vet drug-pricing ordinance (AMPreisV) limits discounts on prescription medicines.
  - The employer is the likely GDPR controller for SBV data.
- **Data sources and market structure:**
  - The Marktstammdatenregister lists every biogas plant with its operator.
  - About 6 million people aged 65+ live alone in Germany, roughly two-thirds without a care grade.
  - Aareon is the dominant housing ERP.
  - About 3,000 Romanian shops have ≥ 600 COD orders a month.
  - Pool shares used for independent vet practices, care homes and Swiss self-administered communities.
- **Model inputs:** the ramp of new customers per month for each idea; founder time at €50/hour; support time at €35/hour.

### Gaps
- No page could be opened, so all [V] items rest on search extracts. Recheck exact wording before relying on any single number.
- **Not checked, for lack of budget:**
  - German music-school software in German
  - works-council suites with SBV modules
  - care-home ERP features
  - pricing from battery-passport vendors
  - heat-pump makers' in-app efficiency features
  - Romanian shop counts
  - SMS prices to Germany
