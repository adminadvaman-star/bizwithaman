#!/usr/bin/env python3
"""Generates parkash/index.html for bizwithaman.com (static, no build deps)."""
import html, json, re, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else "index.html"
B = "https://5.imimg.com/data5/SELLER/Default/"
def img(p): return f"{B}{p}-500x500.jpg"

PHONE_DISPLAY = "+91 98174 75759"
PHONE = "919817475759"
EMAIL = "admin.advaman@gmail.com"
PLACE = "https://www.google.com/maps/place/?q=place_id:ChIJ77-cZgblDTkReO3T_u5qnZI"
DIRECTIONS = "https://www.google.com/maps/dir/?api=1&destination=29.3936889,76.716061"

# ---------- data ----------
CATS = [
 ("chicken-cage","Chicken cages","Durable cages for growing and housing chickens.","2023/9/347712571/XX/FY/PG/60024860/chicken-cage",[
  ("Poultry Chicken Cage","₹90 / piece","5,000 pcs",["Galvanized iron, hot dip","H-type layer cage","8–10 birds per cage","For hens, layer farms"]),
  ("Chicken Brooder Cage","₹90 / piece","5,000 pcs",["California cage system","2 tier, galvanized iron","15 × 17.5 × 15 in","2 birds per box, breeder use"]),
  ("Galvanized Iron Chicken Cage","₹105 / piece","On request",["California cage, layer","Galvanized iron, hot dip","5 birds per box","Hatchery & commercial farms"]),
  ("GI Chicken Cage","₹95 / piece","On request",["Layer cage, GI","5 birds per box","Commercial & breeding farms"]),
  ("Chicken Farming Cage","₹90 / piece","5,000 pcs",["Layer cage, galvanized iron","3 tier","14 × 21 × 15 in","5 birds per box"])]),
 ("poultry-cage","Poultry cages","Tiered cage systems for every growth stage.","2025/9/545536049/MI/MQ/LZ/60024860/chicken-cage",[
  ("Layer Poultry Cage","₹95 / piece","5,000 pcs",["A-type layer cage","3 tier, metal","For breeder & layer birds"]),
  ("Poultry Chicks Cage","₹95 / piece","5,000 pcs",["Brooder cage, zinc plated","3 tier","14 × 24 × 15 in","6 chicks per box"]),
  ("Poultry Grower Cage","₹85 / piece","5,000 pcs",["A-type, zinc plated","2 tier","2 birds per box"]),
  ("Steel Poultry Chicks Cage","₹80 / piece","1,000 pcs",["A-type, zinc plated","2 tier","15 × 21 × 15 in"]),
  ("Poultry Grower Cage (MS)","₹85 / piece","5,000 pcs",["Mild steel, A-type","2 tier","Blue finish"])]),
 ("chain-link-fencing","Chain link fencing","Farm and boundary fencing in GI wire mesh.","2023/9/347711917/HQ/ZH/UW/60024860/chain-link-fencing",[
  ("Chain Link Fencing","₹100 / kg","1,000 kg",["GI wire, galvanized","3 × 3 in mesh","10 gauge","5 ft height"]),
  ("Chain Link Fencing (fine mesh)","₹15 / sq ft","On request",["GI wire, galvanized","1 × 1 in mesh","16 gauge","10 ft height"]),
  ("Galvanized Wire Fencing","₹100 / kg","On request",["GI, galvanized","250 m roll","40–275 GSM coating"]),
  ("Wire Mesh Fence","₹100 / kg","On request",["Chain link, GI","3 in mesh","10 gauge (3.0 mm)","100 GSM"]),
  ("GI Chain Link Mesh Fence","₹16 / sq ft","On request",["GI, 100 GSM","1 × 1 in mesh","16 gauge (1.6 mm)","6 ft height"])]),
 ("cooling-pad","Cooling pads","Evaporative cooling for sheds through Indian summers.","2024/12/476400797/UG/TG/DG/60024860/evaporative-cooling-pad",[
  ("Evaporative Cooling Pad","₹350 / sq ft","On request",["Honeycomb pad, 45° × 45° flute","150 mm thick","1800 × 300 mm panels"]),
  ("Poultry Cooling Pad","₹280 / sq ft","On request",["Up to 100 mm thick","Brown pad, metal frame","Made in India"])]),
 ("poultry-exhaust-fan","Exhaust fans","Heavy-duty ventilation for clean air in the shed.","2023/8/333916413/SL/LI/YK/60024860/cooling-fan",[
  ("Poultry Exhaust Fan","₹25,000 / piece","On request",["50 in fan","1.5 HP, 3 phase motor","GI steel body"])]),
 ("poultry-feeder","Poultry feeders","Feeders that cut wastage and keep feed clean.","2023/6/317243314/AH/VW/NO/60024860/poultry-feeder",[
  ("Poultry Chicken Feeder","₹350 / piece","On request",["Circular, plastic","4–8 kg feed","Serves about 10 birds"])]),
 ("power-sprayer","Power sprayers","Sprayers for shed sanitation and farm use.","2024/12/476401543/QO/LG/VO/60024860/htp-pump",[
  ("HTP Power Sprayer","₹2,900 / piece","On request",["1.5 HP petrol engine","Portable","Up to 15 bar pressure"]),
  ("HTP Spray Pump","₹8,000 / piece","On request",["30 LPM flow","2 HP","4 piston"]),
  ("Stainless Steel Sprayer","₹8,000 / piece","On request",["SS 304","18 L capacity","Manual operation"])]),
 ("square-pipe","Square pipe","PVC square pipe for poultry setups.","2023/8/333917566/EI/IP/KE/60024860/square-pipe",[
  ("PVC Square Pipe, Poultry","₹140 / piece","On request",["PVC, white","3 m length","2.5 kg/cm² rating"])]),
 ("rubber-mats","Rubber mats","Mats for poultry cages and shed floors.","2023/8/333915834/UV/YS/QN/60024860/rubber-mat-for-poultry-cages",[
  ("Rubber Mat for Poultry Cages","₹85 / piece","On request",["3 × 1 ft","Rubber","Load up to 50 kg"])]),
]
NSKU = sum(len(c[4]) for c in CATS)

GALLERY = [
 ("2025/9/545536046/XA/FD/AE/60024860/chicken-cage","Layer cage system in operation"),
 ("2023/9/347713297/EG/JI/CE/60024860/layer-poultry-cage","Long-row cage shed"),
 ("2024/12/476400797/UG/TG/DG/60024860/evaporative-cooling-pad","Cooling pad wall"),
 ("2025/9/545537570/LJ/RA/AY/60024860/layer-poultry-cage","A-frame layer cages"),
 ("2023/8/333916413/SL/LI/YK/60024860/cooling-fan","50 inch exhaust fan"),
 ("2023/9/347711917/HQ/ZH/UW/60024860/chain-link-fencing","GI chain link fencing"),
]

FAQ = [
 ("What is the minimum order quantity?","Most cage models start at 1,000 to 5,000 pieces. Fencing starts at 1,000 kg for the standard mesh. For other products the minimum is agreed on the quote, so send your quantity and we will confirm."),
 ("Do the prices include GST and delivery?","No. Catalogue prices are indicative ex-works rates and exclude GST and freight. Your written quote shows the final price for your size, quantity and location."),
 ("Can you make custom sizes?","Yes. Share the cage dimensions, number of tiers and birds per box, or the fencing height and mesh size you need, and we will quote for it."),
 ("Do you supply outside India?","Yes. Parkash equipment has reached buyers in Saudi Arabia and we welcome export enquiries. Packing and commercial documents for your port are arranged on order."),
 ("How is the order delivered?","We dispatch by road across India from our factory in Safidon, Jind. Delivery time depends on quantity and is stated on the quote."),
 ("What payment modes do you accept?","Cash, cheque, demand draft and card. Terms for bulk and export orders are agreed on the quote."),
 ("Can I visit the factory?","Yes. The unit in Village Tito Kheri, Safidon is open every day from 8:00 AM to 5:00 PM. Call ahead and we will show you the cages being made."),
]

# ---------- helpers ----------
def esc(s): return html.escape(s, quote=True)
def parse_price(p):
    m = re.match(r"₹([\d,]+)\s*/\s*(.+)", p); return int(m.group(1).replace(",","")), m.group(2)
def parse_moq(m):
    n = re.match(r"([\d,]+)", m); return int(n.group(1).replace(",","")) if n else 0

ICON = {
 "arrow":'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "phone":'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 3h4l2 5-3 2a12 12 0 006 6l2-3 5 2v4a2 2 0 01-2 2A17 17 0 013 5a2 2 0 012-2"/></svg>',
 "mail":'<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>',
 "pin":'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-6.2-7-11a7 7 0 0114 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/></svg>',
 "clock":'<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
 "search":'<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>',
 "check":'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7"/></svg>',
 "factory":'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 21V10l6 4V10l6 4V6h6v15z"/><path d="M7 17h2M12 17h2M17 17h2"/></svg>',
 "layers":'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l9 5-9 5-9-5z"/><path d="M3 13l9 5 9-5"/></svg>',
 "shield":'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/></svg>',
 "doc":'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 3h9l4 4v14H6z"/><path d="M14 3v5h5M9 13h7M9 17h5"/></svg>',
 "globe":'<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/></svg>',
 "x":'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg>',
 "wa":'<svg viewBox="0 0 32 32" aria-hidden="true" class="fill"><path d="M16 3a13 13 0 00-11.2 19.6L3 29l6.6-1.7A13 13 0 1016 3zm0 23.6a10.6 10.6 0 01-5.4-1.5l-.4-.2-3.9 1 1-3.8-.2-.4A10.6 10.6 0 1116 26.6zm5.8-7.9c-.3-.2-1.9-.9-2.2-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7.1a8.7 8.7 0 01-2.6-1.6 9.7 9.7 0 01-1.8-2.2c-.2-.3 0-.5.1-.7l.5-.6.3-.5a.6.6 0 000-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 00-.9.4 3.7 3.7 0 00-1.1 2.7 6.5 6.5 0 001.3 3.4 14.6 14.6 0 005.7 5c2.1.9 2.9 1 4 .8a3.3 3.3 0 002.2-1.5 2.7 2.7 0 00.2-1.5c-.1-.1-.3-.2-.6-.4z"/></svg>',
}
WA_BASE = f"https://wa.me/{PHONE}?text="

# ---------- sections ----------
def product_cards():
    out=[]
    for i,(slug,title,desc,ph,items) in enumerate(CATS):
        lo = min(parse_price(x[1])[0] for x in items); unit = parse_price(items[0][1])[1]
        subs = "".join(f"<li>{esc(x[0])}</li>" for x in items[:3])
        out.append(f'''<a class="pcard rv" style="--d:{(i%3)*80}ms" href="#catalog" data-cat="{slug}">
  <div class="pimg"><img src="{img(ph)}" alt="{esc(title)}" loading="lazy" width="500" height="500" onerror="this.parentNode.classList.add('noimg')"><span class="from">from ₹{lo:,} / {esc(unit)}</span></div>
  <div class="pbody"><span class="pnum">{i+1:02d}</span><h3>{esc(title)}</h3><p>{esc(desc)}</p><ul>{subs}</ul>
  <span class="plink">{len(items)} model{"s" if len(items)>1 else ""} · Specs &amp; price {ICON["arrow"]}</span></div>
</a>''')
    return "\n".join(out)

def catalog():
    tabs = '<button class="tab" role="tab" data-cat="all" aria-selected="true">All <span>'+str(NSKU)+'</span></button>' + "".join(
        f'<button class="tab" role="tab" data-cat="{s}" aria-selected="false">{esc(t)} <span>{len(it)}</span></button>' for s,t,_,_,it in CATS)
    rows=[]
    for s,t,_,ph,items in CATS:
        for n,price,moq,spec in items:
            chips="".join(f"<li>{esc(x)}</li>" for x in spec)
            hay=esc((n+" "+t+" "+" ".join(spec)).lower())
            rows.append(f'''<article class="sku" data-cat="{s}" data-q="{hay}">
  <img class="sku-img" src="{img(ph)}" alt="" loading="lazy" width="80" height="80">
  <div class="sku-main"><span class="sku-cat">{esc(t)}</span><h4>{esc(n)}</h4><ul class="chips">{chips}</ul></div>
  <div class="sku-side"><div class="price">{esc(price)}<small>MOQ: {esc(moq)}</small></div>
  <button class="btn btn-primary btn-sm" type="button" data-pick="{esc(n)}">Get quote</button></div>
</article>''')
    return tabs, "\n".join(rows)

def quote_options():
    opts=[]
    for s,t,_,_,items in CATS:
        opts.append(f'<optgroup label="{esc(t)}">')
        for n,price,moq,_ in items:
            p,u=parse_price(price)
            opts.append(f'<option value="{esc(n)}" data-price="{p}" data-unit="{esc(u)}" data-moq="{parse_moq(moq)}" data-cat="{esc(t)}">{esc(n)} — {esc(price)}</option>')
        opts.append('</optgroup>')
    return "".join(opts)

def gallery():
    return "".join(f'<button class="gitem rv" style="--d:{i*60}ms" type="button" data-full="{img(p)}" data-cap="{esc(c)}" aria-label="View photo: {esc(c)}"><img src="{img(p)}" alt="{esc(c)}" loading="lazy" width="500" height="500"><span>{esc(c)}</span></button>' for i,(p,c) in enumerate(GALLERY))

def faq():
    return "".join(f'<details class="rv"{" open" if i==0 else ""}><summary>{esc(q)}<i aria-hidden="true"></i></summary><p>{esc(a)}</p></details>' for i,(q,a) in enumerate(FAQ))

marquee_items = ["Chicken cages","Layer cages","Brooder cages","Chain link fencing","Cooling pads","Exhaust fans","Poultry feeders","Power sprayers","PVC square pipe","Rubber mats"]
marquee = "".join(f"<span>{esc(x)}</span><i aria-hidden=\"true\">◆</i>" for x in marquee_items)

TABS, SKUS = catalog()

LD = {
 "@context":"https://schema.org","@type":"Organization","name":"Parkash Industries","legalName":"ASN Poultech Private Limited",
 "url":"https://bizwithaman.com/parkash/","logo":"https://bizwithaman.com/parkash/logo.png","telephone":"+91-9817475759","email":EMAIL,
 "foundingDate":"2018",
 "address":{"@type":"PostalAddress","streetAddress":"Plot No. 55, Tito Kheri Road, Village Tito Kheri","addressLocality":"Safidon, Jind","addressRegion":"Haryana","postalCode":"126112","addressCountry":"IN"},
 "location":{"@type":"Place","geo":{"@type":"GeoCoordinates","latitude":29.3936889,"longitude":76.716061},"openingHours":"Mo-Su 08:00-17:00","hasMap":PLACE},
 "makesOffer":[{"@type":"Offer","itemOffered":{"@type":"Product","name":t}} for _,t,_,_,_ in CATS],
}
FAQLD = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ]}

HERO = [img("2025/9/545536046/XA/FD/AE/60024860/chicken-cage"), img("2025/9/545536049/MI/MQ/LZ/60024860/chicken-cage"), img("2024/12/476400797/UG/TG/DG/60024860/evaporative-cooling-pad")]

page = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Parkash Industries | Poultry Cages &amp; Farm Equipment Manufacturer, India</title>
<meta name="description" content="Parkash Industries, a brand of ASN Poultech Pvt. Ltd., Safidon, Jind, Haryana. Manufacturer of layer, brooder and grower poultry cages, chain link fencing, cooling pads, exhaust fans, feeders and sprayers. Prices, specs and export enquiries.">
<link rel="canonical" href="https://bizwithaman.com/parkash/">
<meta name="theme-color" content="#1B1E24">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Parkash Industries">
<meta property="og:title" content="Parkash Industries | Poultry Equipment Manufacturer, India">
<meta property="og:description" content="Cages, fencing, cooling and ventilation for poultry farms. Factory prices from Safidon, Haryana. Export enquiries welcome.">
<meta property="og:url" content="https://bizwithaman.com/parkash/">
<meta property="og:image" content="{HERO[1]}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="favicon.png">
<link rel="apple-touch-icon" href="favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="preconnect" href="https://5.imimg.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<script type="application/ld+json">{json.dumps(LD, ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(FAQLD, ensure_ascii=False)}</script>
<script>document.documentElement.classList.add('js')</script>
<style>
:root{{
  --o:#F07F00;--o2:#FF9A2E;--od:#C96A00;--os:#FFF3E5;--br:#7A4A12;
  --c:#23272E;--c2:#1B1E24;--c3:#2E333B;--ink:#1F232A;--mut:#5B6270;--line:#E5E7EB;--bg:#fff;--alt:#F6F6F4;
  --r:18px;--max:1200px;--ease:cubic-bezier(.2,.7,.2,1);
}}
*{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth;scroll-padding-top:90px;-webkit-text-size-adjust:100%}}
body{{font-family:Inter,system-ui,Arial,sans-serif;color:var(--ink);background:var(--bg);line-height:1.6;-webkit-font-smoothing:antialiased;overflow-x:hidden}}
img{{max-width:100%;display:block}}
a{{color:inherit}}
button{{font:inherit;color:inherit}}
svg{{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;flex:none}}
svg.fill{{fill:currentColor;stroke:none}}
.wrap{{max-width:var(--max);margin:0 auto;padding:0 24px}}
.eyebrow{{display:inline-flex;align-items:center;gap:10px;font-size:12px;font-weight:800;letter-spacing:.2em;text-transform:uppercase;color:var(--o)}}
.eyebrow::before{{content:"";width:28px;height:2px;background:currentColor}}
h1,h2,h3,h4{{line-height:1.08;letter-spacing:-.025em}}
h2{{font-size:clamp(32px,4.4vw,52px);font-weight:900;margin:14px 0 16px}}
h2 em{{font-style:normal;color:var(--o)}}
.lead{{color:var(--mut);font-size:18px;max-width:620px}}
section{{padding:110px 0;position:relative}}
.alt{{background:var(--alt)}}
.head{{margin-bottom:52px}}
.head.split{{display:flex;justify-content:space-between;align-items:flex-end;gap:32px;flex-wrap:wrap}}
.btn{{display:inline-flex;align-items:center;justify-content:center;gap:10px;font-weight:700;font-size:15px;text-decoration:none;padding:15px 24px;border-radius:12px;border:2px solid transparent;cursor:pointer;transition:transform .2s var(--ease),background .2s,border-color .2s,box-shadow .2s;min-height:48px;white-space:nowrap}}
.btn:hover{{transform:translateY(-2px)}}
.btn-primary{{background:var(--o);color:#fff;box-shadow:0 10px 24px -10px rgba(240,127,0,.8)}}
.btn-primary:hover{{background:var(--od)}}
.btn-ghost{{border-color:rgba(255,255,255,.28);color:#fff}}
.btn-ghost:hover{{border-color:#fff;background:rgba(255,255,255,.06)}}
.btn-dark{{background:var(--c);color:#fff}}
.btn-line{{border-color:var(--line);background:#fff}}
.btn-line:hover{{border-color:var(--c)}}
.btn-wa{{background:#1FA855;color:#fff}}
.btn-wa:hover{{background:#178A45}}
.btn-sm{{padding:10px 16px;font-size:14px;min-height:44px;border-radius:10px}}

/* reveal */
.js .rv{{opacity:0;transform:translateY(28px);transition:opacity .8s var(--ease),transform .8s var(--ease);transition-delay:var(--d,0ms)}}
.js .rv.in{{opacity:1;transform:none}}
.js .pcard.rv.in,.js .wcard.rv.in{{transition:box-shadow .35s var(--ease),border-color .35s,transform .35s var(--ease),opacity .8s;transition-delay:0s}}

/* header */
.topbar{{background:var(--c2);color:#AEB4BD;font-size:13px}}
.topbar .wrap{{display:flex;justify-content:space-between;align-items:center;gap:16px;height:38px}}
.topbar a{{color:#fff;text-decoration:none}}
.topbar b{{color:var(--o2);font-weight:600}}
.topbar .tb-r{{display:flex;gap:22px;align-items:center}}
.topbar .tb-r span{{display:inline-flex;gap:6px;align-items:center}}
.topbar svg{{width:14px;height:14px}}
header{{position:sticky;top:0;z-index:50;background:rgba(255,255,255,.88);backdrop-filter:saturate(1.6) blur(14px);-webkit-backdrop-filter:saturate(1.6) blur(14px);border-bottom:1px solid transparent;transition:border-color .3s,box-shadow .3s}}
header.scrolled{{border-color:var(--line);box-shadow:0 10px 30px -20px rgba(0,0,0,.25)}}
.nav{{display:flex;align-items:center;justify-content:space-between;height:78px;gap:20px}}
.brand{{display:flex;align-items:center;gap:14px;text-decoration:none}}
.brand img{{height:52px;width:auto}}
.brand .bar{{width:2px;height:38px;background:var(--o)}}
.brand .name{{font-weight:900;font-size:21px;letter-spacing:.02em;line-height:1}}
.brand .sub{{display:block;font-size:10px;font-weight:700;letter-spacing:.46em;color:var(--o);margin-top:7px}}
nav ul{{display:flex;gap:4px;list-style:none;align-items:center}}
nav a{{text-decoration:none;font-weight:600;font-size:14.5px;padding:10px 12px;border-radius:8px;transition:color .2s,background .2s}}
nav a:hover,nav a.active{{color:var(--o)}}
nav .btn{{margin-left:10px;padding:11px 18px;font-size:14px;min-height:44px}}
nav .btn:hover{{color:#fff}}
.menu-btn{{display:none;background:none;border:0;width:46px;height:46px;cursor:pointer;border-radius:10px}}
.menu-btn span{{display:block;width:22px;height:2px;background:var(--ink);margin:5px auto;transition:.3s var(--ease)}}
.menu-btn[aria-expanded="true"] span:nth-child(1){{transform:translateY(7px) rotate(45deg)}}
.menu-btn[aria-expanded="true"] span:nth-child(2){{opacity:0}}
.menu-btn[aria-expanded="true"] span:nth-child(3){{transform:translateY(-7px) rotate(-45deg)}}
.progress{{position:absolute;left:0;bottom:-1px;height:3px;width:100%;transform-origin:0 50%;transform:scaleX(0);background:linear-gradient(90deg,var(--o),var(--o2))}}

/* hero */
.hero{{background:var(--c2);color:#fff;overflow:hidden;padding:0}}
.hero::before{{content:"";position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.045) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.045) 1px,transparent 1px);background-size:56px 56px;mask-image:radial-gradient(ellipse at 70% 40%,#000 20%,transparent 75%);-webkit-mask-image:radial-gradient(ellipse at 70% 40%,#000 20%,transparent 75%)}}
.hero::after{{content:"";position:absolute;width:720px;height:720px;right:-160px;top:-200px;border-radius:50%;background:radial-gradient(circle,rgba(240,127,0,.35),transparent 65%);pointer-events:none}}
.hero .wrap{{position:relative;z-index:1;display:grid;grid-template-columns:1.08fr .92fr;gap:56px;align-items:center;padding-top:96px;padding-bottom:110px}}
.pill{{display:inline-flex;align-items:center;gap:10px;font-size:13px;font-weight:600;color:#E7E9EC;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.12);padding:7px 14px 7px 8px;border-radius:999px}}
.pill b{{background:var(--o);color:#fff;font-size:11px;letter-spacing:.08em;padding:3px 9px;border-radius:999px}}
.hero h1{{font-size:clamp(42px,5.2vw,68px);font-weight:900;margin:26px 0 22px;letter-spacing:-.035em}}
.rot{{display:grid;color:var(--o2)}}
.rot span{{grid-area:1/1;opacity:0;transform:translateY(40%);transition:opacity .5s var(--ease),transform .5s var(--ease)}}
.rot span.on{{opacity:1;transform:none}}
.rot span.off{{opacity:0;transform:translateY(-40%)}}
.no-js-word{{display:none}}
.hero p.sub{{color:#BCC2CB;font-size:19px;max-width:560px}}
.hero .actions{{display:flex;gap:14px;flex-wrap:wrap;margin-top:34px}}
.trust{{display:flex;gap:28px;flex-wrap:wrap;margin-top:42px;padding-top:28px;border-top:1px solid rgba(255,255,255,.1)}}
.trust div{{font-size:13px;color:#9EA5AF}}
.trust b{{display:block;color:#fff;font-size:17px;font-weight:800}}
.trust b i{{font-style:normal;color:var(--o2)}}
.collage{{position:relative;height:560px}}
.collage .ph{{position:absolute;border-radius:22px;overflow:hidden;box-shadow:0 40px 80px -30px rgba(0,0,0,.7);border:1px solid rgba(255,255,255,.1);background:var(--c3)}}
.collage .ph img{{width:100%;height:100%;object-fit:cover}}
.collage .p1{{left:0;top:30px;width:62%;height:400px}}
.collage .p2{{right:0;top:0;width:44%;height:250px}}
.collage .p3{{right:4%;bottom:0;width:48%;height:270px}}
.badge{{position:absolute;z-index:2;display:flex;align-items:center;gap:12px;background:#fff;color:var(--ink);border-radius:14px;padding:12px 16px;box-shadow:0 20px 40px -16px rgba(0,0,0,.5);font-size:13px;animation:float 6s ease-in-out infinite}}
.badge b{{display:block;font-size:15px}}
.badge small{{color:var(--mut)}}
.badge .bi{{width:38px;height:38px;border-radius:10px;background:var(--os);color:var(--o);display:grid;place-items:center;font-weight:900}}
.badge.b1{{left:-18px;bottom:96px}}
.badge.b2{{right:-10px;top:268px;animation-delay:-3s}}
.logo-chip{{position:absolute;left:46%;top:-14px;z-index:2;background:#fff;border-radius:16px;padding:10px 12px;box-shadow:0 20px 40px -16px rgba(0,0,0,.5)}}
.logo-chip img{{height:62px;width:auto}}
@keyframes float{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-10px)}}}}

/* marquee */
.marquee{{background:var(--o);color:#fff;overflow:hidden;white-space:nowrap;padding:18px 0;font-weight:800;font-size:17px;letter-spacing:.01em}}
.marquee .track{{display:inline-flex;gap:28px;align-items:center;animation:mq 36s linear infinite;padding-right:28px}}
.marquee i{{font-style:normal;opacity:.55;font-size:12px}}
@keyframes mq{{to{{transform:translateX(-50%)}}}}

/* stats */
.stats{{padding:0;background:#fff;border-bottom:1px solid var(--line)}}
.stats .wrap{{display:grid;grid-template-columns:repeat(4,1fr)}}
.stat{{padding:40px 28px;border-left:1px solid var(--line)}}
.stat:first-child{{border-left:0;padding-left:0}}
.stat b{{display:block;font-size:46px;font-weight:900;letter-spacing:-.04em;line-height:1}}
.stat b i{{font-style:normal;color:var(--o)}}
.stat>span{{display:block;margin-top:10px;color:var(--mut);font-size:15px}}

/* products */
.pgrid{{display:grid;grid-template-columns:repeat(3,1fr);gap:24px}}
.pcard{{position:relative;display:flex;flex-direction:column;background:#fff;border:1px solid var(--line);border-radius:var(--r);overflow:hidden;text-decoration:none;transition:box-shadow .35s var(--ease),border-color .35s,transform .35s var(--ease)}}
.pcard:hover{{box-shadow:0 30px 60px -28px rgba(35,39,46,.35);border-color:#F3CFA4}}
.pimg{{position:relative;aspect-ratio:4/3;overflow:hidden;background:var(--os)}}
.pimg img{{width:100%;height:100%;object-fit:cover;transition:transform .7s var(--ease)}}
.pcard:hover .pimg img{{transform:scale(1.07)}}
.pimg.noimg img{{display:none}}
.pimg::after{{content:"";position:absolute;inset:0;background:linear-gradient(180deg,transparent 55%,rgba(27,30,36,.55))}}
.from{{position:absolute;left:14px;bottom:14px;z-index:1;background:#fff;color:var(--ink);font-weight:800;font-size:13px;padding:6px 12px;border-radius:999px}}
.pbody{{padding:24px 26px 26px;display:flex;flex-direction:column;flex:1}}
.pnum{{font-size:12px;font-weight:800;color:var(--o);letter-spacing:.14em}}
.pbody h3{{font-size:22px;font-weight:800;margin:6px 0 8px}}
.pbody p{{color:var(--mut);font-size:15px;margin-bottom:14px}}
.pbody ul{{list-style:none;font-size:14px;margin-bottom:20px;display:grid;gap:4px}}
.pbody li{{padding-left:16px;position:relative}}
.pbody li::before{{content:"";position:absolute;left:0;top:9px;width:6px;height:6px;background:var(--o);transform:rotate(45deg)}}
.plink{{margin-top:auto;display:inline-flex;align-items:center;gap:8px;font-weight:700;font-size:14px;color:var(--o)}}
.plink svg{{width:16px;height:16px;transition:transform .3s var(--ease)}}
.pcard:hover .plink svg{{transform:translateX(4px)}}

/* quote builder */
.qb{{background:var(--c2);color:#fff;overflow:hidden}}
.qb::before{{content:"";position:absolute;left:-200px;bottom:-260px;width:620px;height:620px;border-radius:50%;background:radial-gradient(circle,rgba(240,127,0,.28),transparent 65%)}}
.qb .wrap{{position:relative;display:grid;grid-template-columns:.9fr 1.1fr;gap:56px;align-items:center}}
.qb h2{{color:#fff}}
.qb .lead{{color:#BCC2CB}}
.qb ul.pts{{list-style:none;display:grid;gap:12px;margin-top:28px}}
.qb ul.pts li{{display:flex;gap:12px;align-items:center;color:#DADDE2}}
.qb ul.pts svg{{color:var(--o2)}}
.qcard{{background:#fff;color:var(--ink);border-radius:24px;padding:32px;box-shadow:0 40px 80px -30px rgba(0,0,0,.6)}}
.qcard h3{{font-size:20px;font-weight:800;margin-bottom:20px}}
.qrow{{display:grid;grid-template-columns:1fr 170px;gap:14px}}
label{{display:grid;gap:7px;font-size:13px;font-weight:700;color:var(--mut)}}
input,select,textarea{{font:inherit;font-size:15px;color:var(--ink);border:1.5px solid #D6DAE0;border-radius:12px;padding:13px 14px;background:#fff;width:100%;min-width:0;min-height:48px;transition:border-color .2s,box-shadow .2s}}
input:focus,select:focus,textarea:focus{{outline:none;border-color:var(--o);box-shadow:0 0 0 4px rgba(240,127,0,.18)}}
.qout{{margin-top:20px;background:var(--alt);border-radius:16px;padding:20px 22px;display:grid;gap:10px}}
.qline{{display:flex;justify-content:space-between;gap:12px;font-size:15px;color:var(--mut)}}
.qline b{{color:var(--ink)}}
.qtotal{{display:flex;justify-content:space-between;align-items:baseline;gap:12px;padding-top:12px;border-top:1px dashed #CDD1D7}}
.qtotal span{{font-weight:700}}
.qtotal b{{font-size:34px;font-weight:900;letter-spacing:-.03em;color:var(--o)}}
.qnote{{font-size:13px;color:var(--mut)}}
.qwarn{{font-size:13px;font-weight:600;color:#9A4B00;background:var(--os);border-radius:10px;padding:9px 12px}}
.qwarn[hidden]{{display:none}}
.qbtns{{display:flex;gap:12px;flex-wrap:wrap;margin-top:18px}}
.qbtns .btn{{flex:1}}

/* catalogue */
.cat-tools{{display:flex;gap:16px;align-items:center;justify-content:space-between;flex-wrap:wrap;margin-bottom:22px}}
.searchbox{{position:relative;flex:0 1 340px}}
.searchbox svg{{position:absolute;left:14px;top:50%;transform:translateY(-50%);color:var(--mut)}}
.searchbox input{{padding-left:44px;border-radius:999px;background:#fff}}
.tabs{{display:flex;gap:8px;overflow-x:auto;padding:2px 2px 8px;scrollbar-width:thin;margin-bottom:18px}}
.tab{{flex:none;font-weight:600;font-size:14px;padding:10px 16px;border-radius:999px;border:1px solid var(--line);background:#fff;cursor:pointer;min-height:44px;transition:background .2s,color .2s,border-color .2s}}
.tab span{{display:inline-block;margin-left:4px;font-size:12px;color:var(--mut);font-weight:700}}
.tab:hover{{border-color:var(--c)}}
.tab[aria-selected="true"]{{background:var(--c);color:#fff;border-color:var(--c)}}
.tab[aria-selected="true"] span{{color:var(--o2)}}
.skus{{display:grid;gap:12px}}
.sku{{display:flex;align-items:center;gap:20px;background:#fff;border:1px solid var(--line);border-radius:16px;padding:14px 18px 14px 14px;transition:box-shadow .25s,border-color .25s}}
.sku:hover{{border-color:#F3CFA4;box-shadow:0 16px 34px -24px rgba(35,39,46,.4)}}
.sku[hidden]{{display:none}}
.sku-img{{width:80px;height:80px;border-radius:12px;object-fit:cover;flex:none;background:var(--os)}}
.sku-main{{flex:1;min-width:0}}
.sku-cat{{font-size:11.5px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:var(--o)}}
.sku h4{{font-size:17px;font-weight:800;margin:3px 0 8px;letter-spacing:-.01em}}
.chips{{display:flex;flex-wrap:wrap;gap:6px;list-style:none}}
.chips li{{font-size:12.5px;background:var(--alt);border:1px solid var(--line);border-radius:6px;padding:3px 9px;color:var(--mut)}}
.sku-side{{display:flex;align-items:center;gap:18px;flex:none;text-align:right}}
.price{{font-weight:900;font-size:20px;white-space:nowrap;letter-spacing:-.02em}}
.price small{{display:block;font-weight:500;font-size:12.5px;color:var(--mut);letter-spacing:0}}
.empty{{text-align:center;color:var(--mut);padding:40px;border:1px dashed var(--line);border-radius:16px}}
.empty[hidden]{{display:none}}
.fine{{font-size:13px;color:var(--mut);margin-top:16px}}

/* why */
.why{{display:grid;grid-template-columns:repeat(4,1fr);gap:20px}}
.wcard{{padding:30px 26px;border-radius:var(--r);background:#fff;border:1px solid var(--line);transition:transform .35s var(--ease),box-shadow .35s}}
.wcard:hover{{transform:translateY(-6px);box-shadow:0 30px 50px -30px rgba(35,39,46,.35)}}
.wico{{width:52px;height:52px;border-radius:14px;background:var(--c);color:var(--o2);display:grid;place-items:center;margin-bottom:22px}}
.wico svg{{width:24px;height:24px}}
.wcard h3{{font-size:19px;font-weight:800;margin-bottom:8px}}
.wcard p{{color:var(--mut);font-size:15px}}

/* gallery */
.gal{{display:grid;grid-template-columns:repeat(4,1fr);grid-auto-rows:240px;gap:16px}}
.gitem{{position:relative;border:0;padding:0;border-radius:var(--r);overflow:hidden;cursor:zoom-in;background:var(--c3)}}
.gitem:nth-child(1){{grid-column:span 2;grid-row:span 2}}
.gitem:nth-child(4){{grid-column:span 2}}
.gitem img{{width:100%;height:100%;object-fit:cover;transition:transform .7s var(--ease)}}
.gitem:hover img{{transform:scale(1.06)}}
.gitem span{{position:absolute;left:14px;bottom:14px;background:rgba(27,30,36,.82);backdrop-filter:blur(6px);color:#fff;font-size:13px;font-weight:600;padding:7px 13px;border-radius:999px}}
.lb{{position:fixed;inset:0;z-index:100;background:rgba(12,14,17,.92);display:grid;place-items:center;padding:24px}}
.lb[hidden]{{display:none}}
.lb figure{{max-width:min(92vw,900px);text-align:center}}
.lb img{{max-height:78vh;width:auto;margin:0 auto;border-radius:14px}}
.lb figcaption{{color:#fff;margin-top:14px;font-weight:600}}
.lb-close{{position:absolute;top:18px;right:18px;width:48px;height:48px;border-radius:50%;border:0;background:rgba(255,255,255,.12);color:#fff;cursor:pointer;display:grid;place-items:center}}

/* steps */
.steps{{display:grid;grid-template-columns:repeat(4,1fr);gap:0;counter-reset:s}}
.step{{padding-right:24px;position:relative}}
.step::before{{counter-increment:s;content:"0" counter(s);display:grid;place-items:center;width:58px;height:58px;border-radius:16px;background:var(--o);color:#fff;font-weight:900;font-size:18px;margin-bottom:22px;position:relative;z-index:1;box-shadow:0 14px 28px -12px rgba(240,127,0,.8)}}
.step::after{{content:"";position:absolute;top:29px;left:58px;right:0;height:2px;background:repeating-linear-gradient(90deg,#E0B27E 0 8px,transparent 8px 15px)}}
.step:last-child::after{{display:none}}
.step h3{{font-size:19px;font-weight:800;margin-bottom:8px}}
.step p{{color:var(--mut);font-size:15px}}

/* export */
.export{{background:var(--c);color:#fff;overflow:hidden}}
.export::before{{content:"";position:absolute;right:-6%;top:0;bottom:0;width:38%;background:var(--o);transform:skewX(-14deg);transform-origin:top}}
.export::after{{content:"";position:absolute;right:31%;top:0;bottom:0;width:14px;background:var(--br);transform:skewX(-14deg);transform-origin:top}}
.export .wrap{{position:relative;z-index:1;display:grid;grid-template-columns:1.1fr .9fr;gap:48px;align-items:center}}
.export h2{{color:#fff}}
.export p{{color:#C6CBD2}}
.checks{{list-style:none;margin:28px 0 34px;display:grid;gap:16px}}
.checks li{{display:flex;gap:14px}}
.checks i{{flex:none;width:28px;height:28px;border-radius:50%;background:var(--o);display:grid;place-items:center}}
.checks i svg{{width:15px;height:15px;stroke-width:3}}
.checks b{{display:block}}
.checks span{{color:#B8BEC7;font-size:15px}}
.ex-card{{justify-self:end;background:#fff;color:var(--ink);border-radius:24px;padding:30px;width:min(100%,380px);box-shadow:0 40px 80px -30px rgba(0,0,0,.55)}}
.ex-card .flag{{font-size:13px;font-weight:800;letter-spacing:.14em;color:var(--o);text-transform:uppercase}}
.ex-card h3{{font-size:26px;font-weight:900;margin:8px 0 14px}}
.ex-card dl div{{display:flex;justify-content:space-between;gap:12px;padding:11px 0;border-top:1px solid var(--line);font-size:14.5px}}
.ex-card dt{{color:var(--mut)}}
.ex-card dd{{font-weight:700;text-align:right}}

/* reviews */
.ratings{{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-bottom:20px}}
.rating{{display:flex;align-items:center;gap:18px;background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:24px;text-decoration:none;transition:border-color .25s,box-shadow .25s}}
a.rating:hover{{border-color:#F3CFA4;box-shadow:0 16px 34px -24px rgba(35,39,46,.4)}}
.rating b{{font-size:40px;font-weight:900;line-height:1;letter-spacing:-.03em}}
.rating b span{{color:var(--o);font-size:26px;margin-left:2px}}
.rating strong{{display:block;font-size:16px}}
.rating small{{color:var(--mut);font-size:13.5px}}
.buyers{{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}}
.buyer{{background:var(--c2);color:#fff;border-radius:var(--r);padding:28px;position:relative;overflow:hidden}}
.buyer::after{{content:"\\201C";position:absolute;right:18px;top:-10px;font-size:120px;font-weight:900;color:rgba(240,127,0,.2);line-height:1}}
.stars{{color:var(--o2);letter-spacing:3px}}
.buyer p{{font-weight:700;font-size:17px;margin:12px 0 18px}}
.who{{display:flex;align-items:center;gap:12px}}
.av{{width:40px;height:40px;border-radius:50%;background:var(--o);display:grid;place-items:center;font-weight:800}}
.who small{{display:block;color:#A3A9B3}}

/* faq */
.faq-wrap{{display:grid;grid-template-columns:.8fr 1.2fr;gap:56px;align-items:start}}
.faq-list{{display:grid;gap:12px}}
details{{background:#fff;border:1px solid var(--line);border-radius:14px;transition:border-color .2s,box-shadow .2s}}
details[open]{{border-color:#F3CFA4;box-shadow:0 16px 34px -26px rgba(35,39,46,.4)}}
summary{{list-style:none;cursor:pointer;padding:20px 22px;font-weight:700;font-size:16.5px;display:flex;justify-content:space-between;gap:16px;align-items:center}}
summary::-webkit-details-marker{{display:none}}
summary i{{flex:none;width:28px;height:28px;border-radius:50%;background:var(--os);position:relative}}
summary i::before,summary i::after{{content:"";position:absolute;left:50%;top:50%;width:12px;height:2px;background:var(--o);transform:translate(-50%,-50%);transition:transform .3s var(--ease)}}
summary i::after{{transform:translate(-50%,-50%) rotate(90deg)}}
details[open] summary i::after{{transform:translate(-50%,-50%) rotate(0)}}
details p{{padding:0 22px 22px;color:var(--mut)}}

/* company */
.company{{display:grid;grid-template-columns:1fr 1fr;gap:48px;align-items:start}}
.facts{{background:#fff;border:1px solid var(--line);border-radius:var(--r);overflow:hidden}}
.facts div{{display:grid;grid-template-columns:150px 1fr;gap:14px;padding:16px 24px;border-top:1px solid var(--line);font-size:15px}}
.facts div:first-child{{border-top:0}}
.facts dt{{color:var(--mut)}}
.facts dd{{font-weight:700;word-break:break-word}}
.team{{display:flex;gap:10px;flex-wrap:wrap;margin-top:26px}}
.team span{{background:#fff;border:1px solid var(--line);border-radius:999px;padding:9px 16px;font-weight:700;font-size:14px}}
.team small{{color:var(--o);font-weight:800;margin-left:6px;letter-spacing:.08em;font-size:11px}}

/* visit */
.visit{{display:grid;grid-template-columns:.9fr 1.1fr;gap:48px;align-items:stretch}}
.hours{{margin:26px 0;background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:6px 22px}}
.hours div{{display:grid;grid-template-columns:28px 90px 1fr;gap:10px;align-items:start;padding:14px 0;border-top:1px solid var(--line);font-size:15px}}
.hours div:first-child{{border-top:0}}
.hours svg{{color:var(--o);margin-top:2px}}
.hours dt{{color:var(--mut)}}
.hours dd{{font-weight:700}}
.open-now{{display:inline-flex;align-items:center;gap:8px;font-size:13px;font-weight:700;padding:6px 12px;border-radius:999px;background:#E8F7EE;color:#167A3E}}
.open-now::before{{content:"";width:8px;height:8px;border-radius:50%;background:currentColor;box-shadow:0 0 0 4px rgba(22,122,62,.15)}}
.open-now.closed{{background:#F4F4F5;color:#5B6270}}
.actions-row{{display:flex;gap:12px;flex-wrap:wrap}}
.map{{border-radius:24px;overflow:hidden;border:1px solid var(--line);min-height:440px;background:var(--alt);box-shadow:0 30px 60px -30px rgba(35,39,46,.35)}}
.map iframe{{display:block;width:100%;height:100%;min-height:440px;border:0}}

/* contact */
.contact{{display:grid;grid-template-columns:.85fr 1.15fr;gap:48px}}
.info{{display:grid;gap:14px;margin-top:28px}}
.info a,.info div{{display:flex;gap:16px;align-items:center;text-decoration:none;background:#fff;border:1px solid var(--line);border-radius:16px;padding:18px;transition:border-color .2s}}
.info a:hover{{border-color:#F3CFA4}}
.ico{{width:46px;height:46px;border-radius:12px;background:var(--os);color:var(--o);display:grid;place-items:center;flex:none}}
.info b{{display:block;font-size:13px;color:var(--mut);font-weight:600}}
.info span span{{font-weight:700}}
form.qf{{background:#fff;border:1px solid var(--line);border-radius:24px;padding:34px;display:grid;grid-template-columns:1fr 1fr;gap:16px;box-shadow:0 30px 60px -40px rgba(35,39,46,.4)}}
form.qf h3{{grid-column:1/-1;font-size:22px;font-weight:800}}
form.qf .full{{grid-column:1/-1}}
textarea{{min-height:120px;resize:vertical}}
.form-actions{{grid-column:1/-1;display:flex;gap:12px;flex-wrap:wrap}}
.form-actions .btn{{flex:1}}
.form-note{{grid-column:1/-1;font-size:13px;color:var(--mut)}}

/* cta band */
.cta{{padding:0 0 110px}}
.cta-box{{position:relative;overflow:hidden;border-radius:28px;background:var(--o);color:#fff;padding:56px;display:flex;justify-content:space-between;align-items:center;gap:32px;flex-wrap:wrap}}
.cta-box::after{{content:"";position:absolute;right:-80px;top:-120px;width:380px;height:380px;border-radius:50%;border:70px solid rgba(255,255,255,.12)}}
.cta-box h2{{color:#fff;margin:0;max-width:640px;font-size:clamp(28px,3.6vw,42px)}}
.cta-box .btns{{display:flex;gap:12px;flex-wrap:wrap;position:relative;z-index:1}}
.btn-white{{background:#fff;color:var(--ink)}}
.btn-outline-w{{border-color:rgba(255,255,255,.6);color:#fff}}
.btn-outline-w:hover{{border-color:#fff;background:rgba(255,255,255,.1)}}

/* footer */
footer{{background:var(--c2);color:#AEB4BD;font-size:14.5px}}
.strip{{height:6px;background:linear-gradient(90deg,var(--o) 0 60%,var(--br) 60% 62%,var(--c) 62%)}}
.foot{{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:40px;padding-top:64px;padding-bottom:44px}}
.foot .tile{{display:inline-block;background:#fff;border-radius:14px;padding:10px 14px;margin-bottom:18px}}
.foot .tile img{{height:64px;width:auto}}
.foot h4{{color:#fff;font-size:12px;letter-spacing:.22em;text-transform:uppercase;margin-bottom:16px}}
.foot ul{{list-style:none;display:grid;gap:9px}}
.foot a{{text-decoration:none;transition:color .2s}}
.foot a:hover{{color:var(--o2)}}
.legal{{border-top:1px solid rgba(255,255,255,.08)}}
.legal .wrap{{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;padding-top:20px;padding-bottom:20px;font-size:12.5px;color:#8A919C}}

/* floating + mobile bar */
.wa{{position:fixed;right:22px;bottom:22px;z-index:60;width:60px;height:60px;border-radius:50%;background:#25D366;color:#fff;display:grid;place-items:center;box-shadow:0 14px 30px -8px rgba(0,0,0,.35)}}
.wa svg{{width:30px;height:30px}}
.wa::before{{content:"";position:absolute;inset:0;border-radius:50%;background:#25D366;animation:pulse 2.4s ease-out infinite;z-index:-1}}
@keyframes pulse{{0%{{transform:scale(1);opacity:.6}}100%{{transform:scale(1.7);opacity:0}}}}
.totop{{position:fixed;right:30px;bottom:96px;z-index:60;width:44px;height:44px;border-radius:50%;border:1px solid var(--line);background:#fff;cursor:pointer;display:grid;place-items:center;opacity:0;pointer-events:none;transition:opacity .3s,transform .3s;transform:translateY(10px);box-shadow:0 10px 20px -10px rgba(0,0,0,.3)}}
.totop.show{{opacity:1;pointer-events:auto;transform:none}}
.totop svg{{transform:rotate(-90deg)}}
.mbar{{display:none}}

/* responsive */
@media (max-width:1080px){{
  nav ul{{gap:0}} nav a{{padding:10px 8px;font-size:14px}}
  .pgrid{{grid-template-columns:repeat(2,1fr)}}
  .why{{grid-template-columns:repeat(2,1fr)}}
  .steps{{grid-template-columns:repeat(2,1fr);row-gap:40px}}
  .step:nth-child(2)::after{{display:none}}
  .qb .wrap,.company,.contact,.visit,.faq-wrap{{grid-template-columns:1fr}}
  .export::before,.export::after{{display:none}}
  .export .wrap{{grid-template-columns:1fr}}
  .ex-card{{justify-self:start}}
  .foot{{grid-template-columns:1fr 1fr}}
  .ratings,.buyers{{grid-template-columns:1fr}}
}}
@media (max-width:900px){{
  nav ul{{position:absolute;top:78px;left:0;right:0;background:#fff;flex-direction:column;align-items:stretch;padding:8px 24px 24px;border-bottom:1px solid var(--line);box-shadow:0 30px 40px -30px rgba(0,0,0,.3);display:none}}
  nav ul.open{{display:flex}}
  nav li a{{display:block;padding:14px 4px;font-size:16px;border-bottom:1px solid var(--line);border-radius:0}}
  nav li .btn{{margin:14px 0 0;border:0;border-radius:12px}}
  .menu-btn{{display:block}}
  .hero .wrap{{grid-template-columns:1fr;padding-top:56px;padding-bottom:72px;gap:40px}}
  .collage{{height:420px}}
  .collage .p1{{height:300px}} .collage .p2{{height:190px}} .collage .p3{{height:200px}}
  .badge.b2{{top:200px}}
  .stats .wrap{{grid-template-columns:1fr 1fr}}
  .stat{{padding:28px 20px}}
  .stat:nth-child(3){{border-left:0;padding-left:0}}
  .stat:nth-child(n+3){{border-top:1px solid var(--line)}}
  .gal{{grid-template-columns:1fr 1fr;grid-auto-rows:180px}}
  .gitem:nth-child(4){{grid-column:span 1}}
  .topbar .hide-md,.topbar .tb-r .hide-md{{display:none}}
  .topbar{{font-size:12.5px}} .topbar .wrap>span{{white-space:nowrap}}
}}
@media (max-width:640px){{
  .wrap{{padding:0 18px}}
  section{{padding:76px 0}}
  .brand img{{height:44px}} .brand .name{{font-size:18px}} .brand .sub{{letter-spacing:.32em}}
  .hero h1{{font-size:clamp(38px,11vw,48px)}}
  .hero p.sub{{font-size:17px}}
  .hero .actions .btn{{flex:1}}
  .trust{{gap:18px 26px}}
  .collage{{height:340px}}
  .collage .p1{{width:70%;height:250px}} .collage .p2{{width:44%;height:150px}} .collage .p3{{width:52%;height:160px}}
  .badge{{padding:10px 12px}} .badge.b1{{left:0;bottom:40px}} .badge.b2{{right:0;top:170px}}
  .logo-chip img{{height:44px}}
  .stat b{{font-size:36px}}
  .pgrid,.why,.steps{{grid-template-columns:1fr}}
  .step::after{{display:none}}
  .qcard{{padding:22px}}
  .qrow{{grid-template-columns:1fr}}
  .qtotal b{{font-size:28px}}
  .sku{{flex-wrap:wrap;align-items:flex-start;padding:14px}}
  .sku-img{{width:64px;height:64px}}
  .sku-main{{flex:1 1 calc(100% - 90px)}}
  .sku-side{{flex:1 1 100%;justify-content:space-between;text-align:left;padding-top:10px;border-top:1px solid var(--line)}}
  .searchbox{{flex:1 1 100%}}
  form.qf{{grid-template-columns:1fr;padding:22px}}
  .facts div{{grid-template-columns:1fr;gap:2px}}
  .hours div{{grid-template-columns:28px 1fr}} .hours dd{{grid-column:2}}
  .map,.map iframe{{min-height:320px}}
  .cta-box{{padding:34px 24px}}
  .cta-box .btns .btn{{flex:1}}
  .foot{{grid-template-columns:1fr}}
  .wa,.totop{{display:none}}
  .mbar{{display:grid;grid-template-columns:1fr 1fr 1.3fr;gap:8px;position:fixed;left:0;right:0;bottom:0;z-index:70;background:rgba(255,255,255,.96);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-top:1px solid var(--line);padding:10px 12px calc(10px + env(safe-area-inset-bottom))}}
  .mbar a{{display:flex;align-items:center;justify-content:center;gap:8px;min-height:48px;border-radius:12px;font-weight:700;font-size:14.5px;text-decoration:none}}
  .mbar .m1{{background:var(--alt)}}
  .mbar .m2{{background:#1FA855;color:#fff}}
  .mbar .m3{{background:var(--o);color:#fff}}
  .mbar svg{{width:18px;height:18px}}
  body{{padding-bottom:78px}}
}}
@media (prefers-reduced-motion:reduce){{
  *,*::before,*::after{{animation:none!important;transition:none!important}}
  html{{scroll-behavior:auto}}
  .js .rv{{opacity:1;transform:none}}
}}
</style>
</head>
<body id="top">

<div class="topbar">
  <div class="wrap">
    <span><b>Export enquiries welcome</b><span class="hide-md"> · Written quotes within one working day</span></span>
    <span class="tb-r"><span class="hide-md">{ICON["clock"]} Open daily 8 AM – 5 PM</span><a href="tel:+{PHONE}">{PHONE_DISPLAY}</a></span>
  </div>
</div>

<header id="hdr">
  <div class="wrap nav">
    <a class="brand" href="#top" aria-label="Parkash Industries home">
      <img src="logo.png" alt="Parkash logo" width="282" height="402">
      <i class="bar" aria-hidden="true"></i>
      <span><span class="name">PARKASH</span><span class="sub">INDUSTRIES</span></span>
    </a>
    <button class="menu-btn" id="menuBtn" aria-label="Open menu" aria-expanded="false" aria-controls="menu"><span></span><span></span><span></span></button>
    <nav aria-label="Main">
      <ul id="menu">
        <li><a href="#products">Products</a></li>
        <li><a href="#quote-builder">Price calculator</a></li>
        <li><a href="#catalog">Catalogue</a></li>
        <li><a href="#gallery">Gallery</a></li>
        <li><a href="#export">Export</a></li>
        <li><a href="#faq">FAQ</a></li>
        <li><a href="#visit">Visit us</a></li>
        <li><a class="btn btn-primary" href="#contact">Get a quote</a></li>
      </ul>
    </nav>
  </div>
  <div class="progress" id="progress"></div>
</header>

<main>
<section class="hero">
  <div class="wrap">
    <div>
      <span class="pill"><b>SINCE 2018</b> Poultry equipment manufacturer · Safidon, Haryana</span>
      <h1>Factory-made poultry <span class="rot" aria-hidden="true"><span class="on">cages</span><span>fencing</span><span>cooling</span><span>ventilation</span></span><span class="sr-only" style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)">equipment</span> for India&rsquo;s farms.</h1>
      <p class="sub">Layer, brooder and grower cages, chain link fencing, cooling pads, exhaust fans and feeders. One manufacturer for the whole shed, at factory prices, for farms across India and abroad.</p>
      <div class="actions">
        <a class="btn btn-primary" href="#quote-builder">Calculate your price {ICON["arrow"]}</a>
        <a class="btn btn-ghost" href="#catalog">View {NSKU} products</a>
      </div>
      <div class="trust">
        <div><b><i>4.4</i>★ Google</b>16 buyer reviews</div>
        <div><b>100%</b>on-time delivery rating</div>
        <div><b>Saudi Arabia</b>export experience</div>
      </div>
    </div>
    <div class="collage" aria-hidden="true">
      <div class="ph p1" data-par="0.06"><img src="{HERO[0]}" alt="" width="500" height="500"></div>
      <div class="ph p2" data-par="-0.05"><img src="{HERO[1]}" alt="" width="500" height="500"></div>
      <div class="ph p3" data-par="0.04"><img src="{HERO[2]}" alt="" width="500" height="500"></div>
      <div class="logo-chip"><img src="logo.png" alt="" width="282" height="402"></div>
      <div class="badge b1"><span class="bi">★</span><span><b>4.4 on Google</b><small>Rated by farm buyers</small></span></div>
      <div class="badge b2"><span class="bi">₹</span><span><b>From ₹80 / cage</b><small>Factory price, ex-works</small></span></div>
    </div>
  </div>
</section>

<div class="marquee" aria-hidden="true"><div class="track">{marquee}{marquee}</div></div>

<section class="stats" aria-label="Key facts">
  <div class="wrap">
    <div class="stat rv"><b><span class="count" data-to="2018">2018</span></b><span>Making poultry equipment since</span></div>
    <div class="stat rv" style="--d:80ms"><b><span class="count" data-to="{NSKU}">{NSKU}</span><i>+</i></b><span>Products across 9 categories</span></div>
    <div class="stat rv" style="--d:160ms"><b><span class="count" data-to="4.4" data-dec="1">4.4</span><i>★</i></b><span>Google rating, 16 reviews</span></div>
    <div class="stat rv" style="--d:240ms"><b><span class="count" data-to="7">7</span><i>/7</i></b><span>Days a week factory open</span></div>
  </div>
</section>

<section id="products">
  <div class="wrap">
    <div class="head split">
      <div><span class="eyebrow">Product range</span><h2>Everything a <em>poultry shed</em> needs</h2></div>
      <p class="lead">Pick a category to see every model with specifications and indicative factory prices.</p>
    </div>
    <div class="pgrid">
{product_cards()}
    </div>
  </div>
</section>

<section id="quote-builder" class="qb">
  <div class="wrap">
    <div class="rv">
      <span class="eyebrow">Instant price calculator</span>
      <h2>Know your budget in <em>10 seconds</em></h2>
      <p class="lead">Choose a product and quantity to see an indicative factory price, then send it to us on WhatsApp for a written quote.</p>
      <ul class="pts">
        <li>{ICON["check"]} All {NSKU} products with current listed rates</li>
        <li>{ICON["check"]} Minimum order check built in</li>
        <li>{ICON["check"]} One tap to WhatsApp with your details filled in</li>
      </ul>
    </div>
    <div class="qcard rv" style="--d:120ms">
      <h3>Estimate your order</h3>
      <div class="qrow">
        <label>Product<select id="qProd">{quote_options()}</select></label>
        <label>Quantity <span id="qUnitLbl" style="font-weight:500"></span><input id="qQty" type="number" inputmode="numeric" min="1" step="1" value="5000"></label>
      </div>
      <div class="qout" aria-live="polite">
        <div class="qline"><span>Rate</span><b id="qRate">–</b></div>
        <div class="qline"><span>Quantity</span><b id="qQ">–</b></div>
        <div class="qtotal"><span>Estimated total</span><b id="qTotal">–</b></div>
        <p class="qnote">Ex-works estimate. GST, freight and custom sizes are added on your written quote.</p>
        <p class="qwarn" id="qWarn" hidden></p>
      </div>
      <div class="qbtns">
        <a class="btn btn-wa" id="qWa" href="#" target="_blank" rel="noopener">{ICON["wa"]} Send on WhatsApp</a>
        <a class="btn btn-line" href="#contact" id="qForm">Fill enquiry form</a>
      </div>
    </div>
  </div>
</section>

<section id="catalog" class="alt">
  <div class="wrap">
    <div class="head split">
      <div><span class="eyebrow">Specifications &amp; prices</span><h2>Product catalogue</h2></div>
      <p class="lead">Indicative ex-works prices. The final price depends on size, quantity and steel rates.</p>
    </div>
    <div class="cat-tools">
      <div class="searchbox">{ICON["search"]}<input id="catSearch" type="search" placeholder="Search e.g. layer cage, 3 tier, GI…" aria-label="Search products"></div>
      <span class="fine" id="catCount" style="margin:0">{NSKU} products</span>
    </div>
    <div class="tabs" role="tablist" aria-label="Product categories">{TABS}</div>
    <div class="skus" id="skus">
{SKUS}
    </div>
    <p class="empty" id="catEmpty" hidden>No product matches your search. Send us your requirement and we will quote.</p>
    <p class="fine">Prices exclude GST and freight. MOQ = minimum order quantity.</p>
  </div>
</section>

<section id="gallery">
  <div class="wrap">
    <div class="head split">
      <div><span class="eyebrow">Gallery</span><h2>Our equipment <em>on the farm</em></h2></div>
      <p class="lead">Cage systems, cooling and ventilation set up for layer and broiler sheds. Tap a photo to enlarge.</p>
    </div>
    <div class="gal">{gallery()}</div>
  </div>
</section>

<section id="why" class="alt">
  <div class="wrap">
    <div class="head"><span class="eyebrow">Why Parkash</span><h2>A manufacturer, <em>not a middleman</em></h2>
      <p class="lead">You deal directly with the people who make the product, which keeps quotes clear and lead times short.</p></div>
    <div class="why">
      <div class="wcard rv"><span class="wico">{ICON["factory"]}</span><h3>Direct from the factory</h3><p>Made at our own unit in Safidon, Jind, so you talk to the maker and pay factory prices.</p></div>
      <div class="wcard rv" style="--d:80ms"><span class="wico">{ICON["layers"]}</span><h3>The whole shed</h3><p>Cages, fencing, cooling, ventilation and feeding from one supplier and one invoice.</p></div>
      <div class="wcard rv" style="--d:160ms"><span class="wico">{ICON["shield"]}</span><h3>Checked every batch</h3><p>Hot-dip galvanized and zinc-plated steel, with quality checks before dispatch.</p></div>
      <div class="wcard rv" style="--d:240ms"><span class="wico">{ICON["doc"]}</span><h3>Registered company</h3><p>Backed by ASN Poultech Private Limited with proper GST invoicing.</p></div>
    </div>
  </div>
</section>

<section id="how">
  <div class="wrap">
    <div class="head"><span class="eyebrow">How to order</span><h2>From enquiry to <em>delivery</em></h2>
      <p class="lead">The same simple process for farms in India and buyers overseas.</p></div>
    <div class="steps">
      <div class="step rv"><h3>Send your enquiry</h3><p>Share the product, quantity and your location by WhatsApp, call or the form.</p></div>
      <div class="step rv" style="--d:100ms"><h3>Get a written quote</h3><p>We reply within one working day with price, specifications and lead time.</p></div>
      <div class="step rv" style="--d:200ms"><h3>Confirm the order</h3><p>Approve the quote and agree on payment terms.</p></div>
      <div class="step rv" style="--d:300ms"><h3>Production &amp; dispatch</h3><p>We manufacture, check, pack and ship to your farm or port.</p></div>
    </div>
  </div>
</section>

<section id="export" class="export">
  <div class="wrap">
    <div class="rv">
      <span class="eyebrow">Export</span>
      <h2>Supplying buyers <em>beyond India</em></h2>
      <p>Parkash equipment has already reached buyers in Saudi Arabia. We welcome enquiries from distributors, integrators and farm projects worldwide.</p>
      <ul class="checks">
        <li><i>{ICON["check"]}</i><div><b>Container and project quantities</b><span>Clear pricing for bulk and repeat orders.</span></div></li>
        <li><i>{ICON["check"]}</i><div><b>Export packing</b><span>Packed for sea freight and long transit.</span></div></li>
        <li><i>{ICON["check"]}</i><div><b>Documentation support</b><span>Commercial invoice and packing list prepared on order.</span></div></li>
      </ul>
      <a class="btn btn-primary" href="#contact">Send an export enquiry {ICON["arrow"]}</a>
    </div>
    <div class="ex-card rv" style="--d:140ms">
      <span class="flag">{ICON["globe"]} Export desk</span>
      <h3>Tell us three things</h3>
      <dl>
        <div><dt>1. Product &amp; model</dt><dd>e.g. A-type layer cage</dd></div>
        <div><dt>2. Quantity</dt><dd>pieces, kg or containers</dd></div>
        <div><dt>3. Destination</dt><dd>country &amp; port</dd></div>
      </dl>
      <a class="btn btn-wa" style="width:100%;margin-top:18px" href="{WA_BASE}Hello%20Parkash%20Industries%2C%20I%20have%20an%20export%20enquiry." target="_blank" rel="noopener">{ICON["wa"]} WhatsApp export desk</a>
    </div>
  </div>
</section>

<section id="reviews">
  <div class="wrap">
    <div class="head"><span class="eyebrow">Trusted by farm buyers</span><h2>What our <em>buyers say</em></h2></div>
    <div class="ratings">
      <a class="rating rv" href="{PLACE}" target="_blank" rel="noopener"><b>4.4<span>★</span></b><div><strong>Google</strong><small>16 reviews · see on Google Maps</small></div></a>
      <a class="rating rv" style="--d:80ms" href="https://www.parkashindustry.com/profile.html" target="_blank" rel="noopener"><b>4.0<span>★</span></b><div><strong>IndiaMART</strong><small>13 buyer ratings · 100% on delivery</small></div></a>
      <div class="rating rv" style="--d:160ms"><b>SA</b><div><strong>Exported</strong><small>Buyers in Saudi Arabia</small></div></div>
    </div>
    <div class="buyers">
      <div class="buyer rv"><span class="stars">★★★★★</span><p>Poultry cage order</p><div class="who"><span class="av">B</span><span>Bablu K.<small>Orai, Uttar Pradesh</small></span></div></div>
      <div class="buyer rv" style="--d:80ms"><span class="stars">★★★★★</span><p>Chain link fencing order</p><div class="who"><span class="av">A</span><span>Arun M.<small>Panipat, Haryana</small></span></div></div>
      <div class="buyer rv" style="--d:160ms"><span class="stars">★★★★★</span><p>Rated for response, quality and delivery</p><div class="who"><span class="av">J</span><span>Jyoti Ranjan B.<small>Cuttack, Odisha</small></span></div></div>
    </div>
  </div>
</section>

<section id="faq" class="alt">
  <div class="wrap faq-wrap">
    <div class="rv">
      <span class="eyebrow">FAQ</span>
      <h2>Questions buyers <em>ask us</em></h2>
      <p class="lead">Still unsure? Call or WhatsApp us and talk to the factory directly.</p>
      <div class="actions-row" style="margin-top:26px">
        <a class="btn btn-wa" href="{WA_BASE}Hello%20Parkash%20Industries%2C%20I%20have%20a%20question." target="_blank" rel="noopener">{ICON["wa"]} Ask on WhatsApp</a>
        <a class="btn btn-line" href="tel:+{PHONE}">{ICON["phone"]} Call us</a>
      </div>
    </div>
    <div class="faq-list">{faq()}</div>
  </div>
</section>

<section id="company">
  <div class="wrap company">
    <div class="rv">
      <span class="eyebrow">The company</span>
      <h2>A brand of <em>ASN Poultech</em> Private Limited</h2>
      <p class="lead">Parkash Industries has made poultry cages and farm equipment in Safidon since 2018, built on the experience of the Kharb family. Today the brand is run by ASN Poultech Private Limited, a poultry equipment and farming company registered in Haryana.</p>
      <div class="team">
        <span>Surender Kharb <small>DIRECTOR</small></span>
        <span>Narinder Kharb <small>DIRECTOR</small></span>
        <span>Aman <small>DIRECTOR</small></span>
      </div>
    </div>
    <dl class="facts rv" style="--d:120ms">
      <div><dt>Legal name</dt><dd>ASN Poultech Private Limited</dd></div>
      <div><dt>Brand</dt><dd>Parkash Industries</dd></div>
      <div><dt>CIN</dt><dd>U46203HR2026PTC151614</dd></div>
      <div><dt>GSTIN</dt><dd>06ABGCA9618L1Z9</dd></div>
      <div><dt>Registered office</dt><dd>Plot No. 55, Tito Kheri Road, Village Tito Kheri, Safidon, Distt. Jind, Haryana 126112</dd></div>
    </dl>
  </div>
</section>

<section id="visit" class="alt">
  <div class="wrap visit">
    <div class="rv">
      <span class="eyebrow">Visit the factory</span>
      <h2>Find us in <em>Tito Kheri</em>, Safidon</h2>
      <p class="lead">Buyers are welcome to visit the unit and see cages being made before ordering.</p>
      <p style="margin-top:16px"><span class="open-now" id="openNow">Open today 8 AM – 5 PM</span></p>
      <dl class="hours">
        <div>{ICON["clock"]}<dt>Open</dt><dd>Every day, Monday to Sunday</dd></div>
        <div>{ICON["clock"]}<dt>Timings</dt><dd>8:00 AM – 5:00 PM</dd></div>
        <div>{ICON["pin"]}<dt>Address</dt><dd>Plot No. 55, Tito Kheri Road, near Govt. School, Village Tito Kheri, Safidon, Distt. Jind, Haryana 126112</dd></div>
      </dl>
      <div class="actions-row">
        <a class="btn btn-primary" href="{DIRECTIONS}" target="_blank" rel="noopener">{ICON["pin"]} Get directions</a>
        <a class="btn btn-dark" href="{PLACE}" target="_blank" rel="noopener">Open in Google Maps</a>
      </div>
    </div>
    <div class="map rv" style="--d:120ms"><iframe title="Parkash Industries on Google Maps" src="https://maps.google.com/maps?q=29.3936889,76.716061&amp;z=15&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe></div>
  </div>
</section>

<section id="contact">
  <div class="wrap contact">
    <div class="rv">
      <span class="eyebrow">Contact</span>
      <h2>Request a <em>quote</em></h2>
      <p class="lead">Tell us what you need. We reply within one working day.</p>
      <div class="info">
        <a href="tel:+{PHONE}"><span class="ico">{ICON["phone"]}</span><span><b>Phone &amp; WhatsApp</b><span>{PHONE_DISPLAY}</span></span></a>
        <a href="mailto:{EMAIL}"><span class="ico">{ICON["mail"]}</span><span><b>Email</b><span>{EMAIL}</span></span></a>
        <a href="{PLACE}" target="_blank" rel="noopener"><span class="ico">{ICON["pin"]}</span><span><b>Factory · open daily 8 AM – 5 PM</b><span>Village Tito Kheri, Safidon, Distt. Jind, Haryana 126112</span></span></a>
      </div>
    </div>
    <form class="qf rv" id="quote" style="--d:120ms" novalidate>
      <h3>Enquiry form</h3>
      <label>Your name<input name="name" required autocomplete="name"></label>
      <label>Phone or email<input name="contact" required autocomplete="tel"></label>
      <label>Product
        <select name="product">{"".join(f"<option>{esc(t)}</option>" for _,t,_,_,_ in CATS)}<option>Other</option></select>
      </label>
      <label>Quantity<input name="qty" placeholder="e.g. 5,000 pieces"></label>
      <label class="full">Country and city<input name="place" placeholder="e.g. Hisar, India or Riyadh, Saudi Arabia"></label>
      <label class="full">Details<textarea name="details" placeholder="Model, sizes, tiers, delivery timeline…"></textarea></label>
      <div class="form-actions">
        <button class="btn btn-wa" type="submit" data-via="wa">{ICON["wa"]} Send on WhatsApp</button>
        <button class="btn btn-dark" type="button" data-via="mail">{ICON["mail"]} Send by email</button>
      </div>
      <p class="form-note">Your enquiry opens in WhatsApp or your email app, ready to send.</p>
    </form>
  </div>
</section>

<section class="cta">
  <div class="wrap">
    <div class="cta-box rv">
      <h2>Planning a new shed or expanding one? Get factory prices today.</h2>
      <div class="btns">
        <a class="btn btn-white" href="#quote-builder">Calculate price</a>
        <a class="btn btn-outline-w" href="{WA_BASE}Hello%20Parkash%20Industries%2C%20I%20would%20like%20a%20quote." target="_blank" rel="noopener">{ICON["wa"]} WhatsApp us</a>
      </div>
    </div>
  </div>
</section>
</main>

<footer>
  <div class="strip"></div>
  <div class="wrap foot">
    <div>
      <span class="tile"><img src="logo.png" alt="Parkash logo" width="282" height="402" loading="lazy"></span>
      <p>Manufacturer of poultry cages and poultry farm equipment. Quality poultry equipment, made in India.</p>
    </div>
    <div><h4>Products</h4><ul>{"".join(f'<li><a href="#catalog" data-cat="{s}">{esc(t)}</a></li>' for s,t,_,_,_ in CATS[:5])}</ul></div>
    <div><h4>Company</h4><ul><li><a href="#why">Why Parkash</a></li><li><a href="#export">Export</a></li><li><a href="#reviews">Reviews</a></li><li><a href="#faq">FAQ</a></li><li><a href="#company">ASN Poultech</a></li></ul></div>
    <div><h4>Contact</h4><ul><li><a href="tel:+{PHONE}">{PHONE_DISPLAY}</a></li><li><a href="mailto:{EMAIL}">{EMAIL}</a></li><li><a href="{DIRECTIONS}" target="_blank" rel="noopener">Get directions</a></li><li><a href="https://www.parkashindustry.com/" target="_blank" rel="noopener">IndiaMART catalogue</a></li><li><a href="https://bizwithaman.com/">Biz With Aman</a></li></ul></div>
  </div>
  <div class="legal"><div class="wrap"><span>© 2026 Parkash Industries · A brand of ASN Poultech Private Limited</span><span>CIN U46203HR2026PTC151614 · GSTIN 06ABGCA9618L1Z9</span></div></div>
</footer>

<div class="lb" id="lb" hidden role="dialog" aria-modal="true" aria-label="Photo viewer">
  <button class="lb-close" id="lbClose" type="button" aria-label="Close photo">{ICON["x"]}</button>
  <figure><img id="lbImg" src="" alt=""><figcaption id="lbCap"></figcaption></figure>
</div>

<button class="totop" id="toTop" type="button" aria-label="Back to top">{ICON["arrow"]}</button>
<a class="wa" href="{WA_BASE}Hello%2C%20I%20would%20like%20a%20quote%20from%20Parkash%20Industries" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{ICON["wa"]}</a>
<div class="mbar">
  <a class="m1" href="tel:+{PHONE}">{ICON["phone"]} Call</a>
  <a class="m2" href="{WA_BASE}Hello%2C%20I%20would%20like%20a%20quote%20from%20Parkash%20Industries" target="_blank" rel="noopener">{ICON["wa"]} WhatsApp</a>
  <a class="m3" href="#quote-builder">Get price</a>
</div>

<script>
(function(){{
  var PHONE='{PHONE}', EMAIL='{EMAIL}';
  var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
  function $(s,c){{return (c||document).querySelector(s)}}
  function $$(s,c){{return Array.prototype.slice.call((c||document).querySelectorAll(s))}}
  function inr(n){{return '₹'+Math.round(n).toLocaleString('en-IN')}}

  /* menu */
  var mb=$('#menuBtn'),menu=$('#menu');
  mb.addEventListener('click',function(){{var o=menu.classList.toggle('open');mb.setAttribute('aria-expanded',o)}});
  menu.addEventListener('click',function(e){{if(e.target.closest('a')){{menu.classList.remove('open');mb.setAttribute('aria-expanded','false')}}}});

  /* scroll: header, progress, to-top, parallax */
  var hdr=$('#hdr'),pr=$('#progress'),tt=$('#toTop'),par=$$('[data-par]'),tick=false;
  function onScroll(){{
    var y=window.scrollY,h=document.documentElement.scrollHeight-innerHeight;
    hdr.classList.toggle('scrolled',y>10);
    pr.style.transform='scaleX('+(h>0?y/h:0)+')';
    tt.classList.toggle('show',y>900);
    if(!reduce&&y<900)par.forEach(function(el){{el.style.transform='translateY('+(y*parseFloat(el.dataset.par))+'px)'}});
    tick=false;
  }}
  addEventListener('scroll',function(){{if(!tick){{requestAnimationFrame(onScroll);tick=true}}}},{{passive:true}});
  onScroll();
  tt.addEventListener('click',function(){{scrollTo({{top:0,behavior:reduce?'auto':'smooth'}})}});

  /* active nav link */
  var links=$$('nav a[href^="#"]'),secs=links.map(function(a){{return $(a.getAttribute('href'))}}).filter(Boolean);
  if('IntersectionObserver' in window){{
    var nio=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{links.forEach(function(a){{a.classList.toggle('active',a.getAttribute('href')==='#'+e.target.id)}})}}}})}},{{rootMargin:'-45% 0px -50% 0px'}});
    secs.forEach(function(s){{nio.observe(s)}});
  }}

  /* reveal + counters */
  function count(el){{
    var to=parseFloat(el.dataset.to),dec=+(el.dataset.dec||0),from=to>1000?to-8:0,t0=null,dur=1400;
    if(reduce){{el.textContent=to.toFixed(dec);return}}
    function f(t){{if(!t0)t0=t;var p=Math.min(1,(t-t0)/dur),e=1-Math.pow(1-p,3);el.textContent=(from+(to-from)*e).toFixed(dec);if(p<1)requestAnimationFrame(f)}}
    requestAnimationFrame(f);
  }}
  if('IntersectionObserver' in window){{
    var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');$$('.count',e.target).forEach(count);io.unobserve(e.target)}}}})}},{{threshold:.12,rootMargin:'0px 0px -40px 0px'}});
    $$('.rv').forEach(function(el){{io.observe(el)}});
  }}else{{$$('.rv').forEach(function(el){{el.classList.add('in')}})}}

  /* rotating word */
  var words=$$('.rot span'),wi=0;
  if(words.length&&!reduce)setInterval(function(){{var a=words[wi];a.classList.remove('on');a.classList.add('off');wi=(wi+1)%words.length;var b=words[wi];b.classList.remove('off');void b.offsetWidth;b.classList.add('on');setTimeout(function(){{a.classList.remove('off')}},500)}},2200);

  /* catalogue: tabs + search */
  var tabs=$$('.tab'),skus=$$('.sku'),search=$('#catSearch'),cnt=$('#catCount'),empty=$('#catEmpty'),cur='all';
  function render(){{
    var q=(search.value||'').trim().toLowerCase(),n=0;
    skus.forEach(function(s){{var ok=(cur==='all'||s.dataset.cat===cur)&&(!q||q.split(/\\s+/).every(function(w){{return s.dataset.q.indexOf(w)>-1}}));s.hidden=!ok;if(ok)n++}});
    cnt.textContent=n+(n===1?' product':' products');empty.hidden=n>0;
  }}
  function setCat(c){{cur=c;tabs.forEach(function(t){{t.setAttribute('aria-selected',t.dataset.cat===c)}});render()}}
  tabs.forEach(function(t){{t.addEventListener('click',function(){{setCat(t.dataset.cat)}})}});
  search.addEventListener('input',render);
  $$('[data-cat]').forEach(function(a){{if(a.tagName==='A')a.addEventListener('click',function(){{search.value='';setCat(a.dataset.cat)}})}});

  /* price calculator */
  var qp=$('#qProd'),qq=$('#qQty'),qwa=$('#qWa'),qwarn=$('#qWarn');
  function calc(){{
    var o=qp.options[qp.selectedIndex],p=+o.dataset.price,u=o.dataset.unit,moq=+o.dataset.moq,q=Math.max(0,Math.floor(+qq.value||0));
    $('#qUnitLbl').textContent='('+u+')';
    $('#qRate').textContent=inr(p)+' / '+u;
    $('#qQ').textContent=q.toLocaleString('en-IN')+' '+u;
    $('#qTotal').textContent=q?inr(p*q):'–';
    if(moq&&q&&q<moq){{qwarn.hidden=false;qwarn.textContent='Minimum order for this model is '+moq.toLocaleString('en-IN')+' '+u+'. Smaller quantities may be possible on request.'}}else qwarn.hidden=true;
    var msg='Hello Parkash Industries, I would like a quote.\\n\\nProduct: '+o.value+' ('+o.dataset.cat+')\\nQuantity: '+q.toLocaleString('en-IN')+' '+u+'\\nWebsite estimate: '+(q?inr(p*q):'-')+' (ex-works, excl. GST & freight)\\n\\nMy location: ';
    qwa.href='https://wa.me/'+PHONE+'?text='+encodeURIComponent(msg);
  }}
  qp.addEventListener('change',function(){{var m=+qp.options[qp.selectedIndex].dataset.moq;if(m)qq.value=m;calc()}});
  qq.addEventListener('input',calc);calc();
  function pick(name){{for(var i=0;i<qp.options.length;i++)if(qp.options[i].value===name){{qp.selectedIndex=i;var m=+qp.options[i].dataset.moq;qq.value=m||100;calc();break}}}}
  $$('[data-pick]').forEach(function(b){{b.addEventListener('click',function(){{pick(b.dataset.pick);$('#quote-builder').scrollIntoView({{behavior:reduce?'auto':'smooth'}})}})}});
  $('#qForm').addEventListener('click',function(){{
    var o=qp.options[qp.selectedIndex],f=$('#quote');
    for(var i=0;i<f.product.options.length;i++)if(f.product.options[i].text===o.dataset.cat)f.product.selectedIndex=i;
    f.qty.value=(+qq.value||0).toLocaleString('en-IN')+' '+o.dataset.unit;
    if(!f.details.value)f.details.value='Model: '+o.value+'\\n';
  }});

  /* enquiry form */
  var f=$('#quote');
  function send(via){{
    if(!f.name.value.trim()||!f.contact.value.trim()){{(f.name.value.trim()?f.contact:f.name).focus();f.reportValidity&&f.reportValidity();return}}
    var msg='Hello Parkash Industries, I would like a quote.\\n\\nName: '+f.name.value+'\\nContact: '+f.contact.value+'\\nProduct: '+f.product.value+'\\nQuantity: '+(f.qty.value||'-')+'\\nLocation: '+(f.place.value||'-')+'\\nDetails: '+(f.details.value||'-');
    if(via==='mail')location.href='mailto:'+EMAIL+'?subject='+encodeURIComponent('Quote request: '+f.product.value)+'&body='+encodeURIComponent(msg);
    else window.open('https://wa.me/'+PHONE+'?text='+encodeURIComponent(msg),'_blank','noopener');
  }}
  f.addEventListener('submit',function(e){{e.preventDefault();send('wa')}});
  $('[data-via="mail"]',f).addEventListener('click',function(){{send('mail')}});

  /* lightbox */
  var lb=$('#lb'),li=$('#lbImg'),lc=$('#lbCap'),last=null;
  function close(){{lb.hidden=true;document.body.style.overflow='';if(last)last.focus()}}
  $$('.gitem').forEach(function(g){{g.addEventListener('click',function(){{last=g;li.src=g.dataset.full;li.alt=g.dataset.cap;lc.textContent=g.dataset.cap;lb.hidden=false;document.body.style.overflow='hidden';$('#lbClose').focus()}})}});
  $('#lbClose').addEventListener('click',close);
  lb.addEventListener('click',function(e){{if(e.target===lb)close()}});
  addEventListener('keydown',function(e){{if(e.key==='Escape'&&!lb.hidden)close()}});

  /* open now (IST) */
  var on=$('#openNow');
  try{{var h=+new Intl.DateTimeFormat('en-GB',{{hour:'numeric',hour12:false,timeZone:'Asia/Kolkata'}}).format(new Date());
    if(h>=8&&h<17)on.textContent='Open now · closes 5 PM';else{{on.textContent='Closed now · opens 8 AM';on.classList.add('closed')}}}}catch(e){{}}

  /* subtle tilt on product cards (desktop) */
  if(!reduce&&matchMedia('(hover:hover) and (pointer:fine)').matches)$$('.pcard').forEach(function(c){{
    c.addEventListener('mousemove',function(e){{var r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;c.style.transform='perspective(900px) rotateX('+(-y*4)+'deg) rotateY('+(x*4)+'deg) translateY(-4px)'}});
    c.addEventListener('mouseleave',function(){{c.style.transform=''}});
  }});
}})();
</script>
</body>
</html>
'''
open(OUT, "w", encoding="utf-8").write(page)
print("wrote", OUT, len(page), "bytes,", NSKU, "SKUs")
