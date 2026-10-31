#!/usr/bin/env python3
"""Generates index.html (Biz With Aman homepage)."""
import html, json, sys
OUT = sys.argv[1] if len(sys.argv) > 1 else "index.html"
PHONE="919817475759"; PHONE_D="+91 98174 75759"; EMAIL="admin.advaman@gmail.com"
WA=f"https://wa.me/{PHONE}?text="
def esc(s): return html.escape(s, quote=True)

I = {
 "arrow":'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "check":'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7"/></svg>',
 "phone":'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 3h4l2 5-3 2a12 12 0 006 6l2-3 5 2v4a2 2 0 01-2 2A17 17 0 013 5a2 2 0 012-2"/></svg>',
 "mail":'<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg>',
 "target":'<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1"/></svg>',
 "chart":'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 20h18M6 16l4-5 3 3 6-8"/><path d="M15 6h4v4"/></svg>',
 "star":'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/></svg>',
 "globe":'<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c3 3.5 3 14.5 0 18M12 3c-3 3.5-3 14.5 0 18"/></svg>',
 "wa":'<svg viewBox="0 0 32 32" aria-hidden="true" class="fill"><path d="M16 3a13 13 0 00-11.2 19.6L3 29l6.6-1.7A13 13 0 1016 3zm0 23.6a10.6 10.6 0 01-5.4-1.5l-.4-.2-3.9 1 1-3.8-.2-.4A10.6 10.6 0 1116 26.6zm5.8-7.9c-.3-.2-1.9-.9-2.2-1s-.5-.2-.7.2-.8 1-1 1.2-.4.2-.7.1a8.7 8.7 0 01-2.6-1.6 9.7 9.7 0 01-1.8-2.2c-.2-.3 0-.5.1-.7l.5-.6.3-.5a.6.6 0 000-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6a1.2 1.2 0 00-.9.4 3.7 3.7 0 00-1.1 2.7 6.5 6.5 0 001.3 3.4 14.6 14.6 0 005.7 5c2.1.9 2.9 1 4 .8a3.3 3.3 0 002.2-1.5 2.7 2.7 0 00.2-1.5c-.1-.1-.3-.2-.6-.4z"/></svg>',
}

SERVICES = [
 ("target","Strategy sessions","One focused session to review your business, set priorities for the next 90 days and leave with a written plan you can start on the same day.",
  ["Business review and the one or two real blockers","Written 90-day plan with weekly actions","Clear numbers to track"],"Best for owners who feel stuck","Book a session"),
 ("chart","Growth consulting","Ongoing monthly work on sales, marketing and operations. We set targets, track the numbers and adjust every week.",
  ["Monthly targets and weekly check-ins","Sales follow-up and enquiry systems","Monthly progress report"],"Best for businesses ready to scale","Start growing"),
 ("globe","Website & digital setup","A professional website that brings enquiries, plus the digital basics done properly so buyers can find and trust you.",
  ["Fast, mobile-first business website","Domain, company email and Google Business Profile","WhatsApp enquiry and quote systems"],"Best for manufacturers and local businesses","Get my website"),
 ("star","Personal brand building","Positioning, profile makeover and a simple content routine so the right clients find you and trust you before the first call.",
  ["Positioning and a one-line pitch","LinkedIn and Instagram profile makeover","A content routine you can keep"],"Best for founders, freelancers and professionals","Build my brand"),
]

QUIZ = [
 "I have a written plan for the next 90 days.",
 "I track my enquiries and sales numbers every week.",
 "My website brings me enquiries, not just a visiting card online.",
 "My Google Business Profile is complete and correct.",
 "Every new lead gets a follow-up within 24 hours.",
 "I share useful content about my business at least once a week.",
]

FAQ = [
 ("Who do you work with?","Founders, small business owners, manufacturers, freelancers and professionals who want clear priorities and steady growth without a large consulting budget."),
 ("How long does it take to see results?","You leave the first strategy session with a written 90-day plan. Most clients see their first changes in sales or enquiries within the first one to two months, depending on the business."),
 ("What does it cost?","It depends on the service and how much support you need. After the free call I send a clear proposal with the scope, timeline and price before you commit."),
 ("Can you build my website too?","Yes. I design and set up business websites with product catalogues, price calculators and WhatsApp enquiries, along with domain, company email and Google Business Profile. Parkash Industries is a live example."),
 ("Do you work with clients outside India?","Yes. Sessions run on video call, so location is not a limit."),
]

MARQ = ["Business strategy","90-day plans","Sales systems","Marketing","Business websites","Google Business Profile","WhatsApp lead systems","Personal branding","Export growth"]
marq = "".join(f"<span>{esc(x)}</span><i aria-hidden=\"true\">✦</i>" for x in MARQ)

def services():
    o=[]
    for i,(ic,t,d,pts,best,cta) in enumerate(SERVICES):
        lis="".join(f"<li>{I['check']}{esc(p)}</li>" for p in pts)
        o.append(f'''<article class="svc rv" style="--d:{i*80}ms"><span class="sico">{I[ic]}</span><span class="snum">0{i+1}</span>
<h3>{esc(t)}</h3><p>{esc(d)}</p><ul>{lis}</ul><span class="best">{esc(best)}</span>
<a class="slink" href="#contact" data-svc="{esc(t)}">{esc(cta)} {I["arrow"]}</a></article>''')
    return "\n".join(o)

def quiz():
    return "".join(f'''<li class="qz"><span class="qn">{i+1}</span><span class="qt">{esc(q)}</span>
<span class="seg" role="group" aria-label="Answer for statement {i+1}"><button type="button" data-v="1" aria-pressed="false">Yes</button><button type="button" data-v="0" aria-pressed="false">No</button></span></li>''' for i,q in enumerate(QUIZ))

def faq():
    return "".join(f'<details class="rv"{" open" if i==0 else ""}><summary>{esc(q)}<i aria-hidden="true"></i></summary><p>{esc(a)}</p></details>' for i,(q,a) in enumerate(FAQ))

LD={"@context":"https://schema.org","@type":"ProfessionalService","name":"Biz With Aman","url":"https://bizwithaman.com/","logo":"https://bizwithaman.com/logo.png","image":"https://bizwithaman.com/aman.jpg","slogan":"Business, Growth, Success","telephone":"+91-9817475759","email":EMAIL,"areaServed":"Worldwide","founder":{"@type":"Person","name":"Aman"},
 "description":"Business strategy, growth consulting, websites and personal brand building for founders and small businesses."}
FAQLD={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in FAQ]}

page=f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Biz With Aman | Business Strategy, Growth &amp; Websites</title>
<meta name="description" content="Biz With Aman helps founders, manufacturers and small businesses grow with a clear 90-day plan, a steady enquiry pipeline, a website that sells and a brand people trust. Book a free 30-minute call.">
<link rel="canonical" href="https://bizwithaman.com/">
<meta name="theme-color" content="#08112b">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Biz With Aman">
<meta property="og:title" content="Biz With Aman | Business. Growth. Success.">
<meta property="og:description" content="A clear plan, a steady pipeline and a brand people trust. Book a free 30-minute call.">
<meta property="og:url" content="https://bizwithaman.com/">
<meta property="og:image" content="https://bizwithaman.com/logo.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="favicon.png">
<link rel="apple-touch-icon" href="favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,400;0,500;0,600;0,700;0,800;1,500&display=swap" rel="stylesheet">
<script type="application/ld+json">{json.dumps(LD,ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(FAQLD,ensure_ascii=False)}</script>
<script>document.documentElement.classList.add('js')</script>
<style>
:root{{
  --navy:#14295f;--deep:#0d1c45;--night:#08112b;--gold:#d9a93f;--gl:#f0cd74;--gd:#b8861b;
  --cream:#fbf6ea;--paper:#fffdf8;--ink:#14295f;--mut:#56638a;--line:#e9e1cc;--soft:#aebbe0;
  --grad:linear-gradient(100deg,#f0cd74 0%,#d9a93f 45%,#b8861b 100%);
  --r:20px;--max:1200px;--ease:cubic-bezier(.2,.7,.2,1);
}}
*{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth;scroll-padding-top:88px;-webkit-text-size-adjust:100%}}
body{{font-family:Poppins,system-ui,Arial,sans-serif;color:var(--ink);background:var(--paper);line-height:1.65;font-size:16.5px;-webkit-font-smoothing:antialiased;overflow-x:hidden}}
img{{max-width:100%;display:block}}
a{{color:inherit}}
button{{font:inherit;color:inherit}}
svg{{width:20px;height:20px;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round;flex:none}}
svg.fill{{fill:currentColor;stroke:none}}
.wrap{{max-width:var(--max);margin:0 auto;padding:0 24px}}
.kick{{display:inline-flex;align-items:center;gap:10px;font-weight:600;font-size:14px;color:var(--gd)}}
.kick::before{{content:"";width:30px;height:2px;background:currentColor}}
.dark .kick{{color:var(--gl)}}
h1,h2,h3{{line-height:1.1;letter-spacing:-.025em}}
h2{{font-size:clamp(32px,4.4vw,52px);font-weight:800;margin:14px 0 16px}}
h2 em,h1 em{{font-style:normal;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent}}
.lead{{color:var(--mut);font-size:18px;max-width:620px}}
.dark{{background:var(--night);color:#fff}}
.dark .lead{{color:var(--soft)}}
section{{padding:110px 0;position:relative}}
.cream{{background:var(--cream)}}
.head{{margin-bottom:52px}}
.head.split{{display:flex;justify-content:space-between;align-items:flex-end;gap:32px;flex-wrap:wrap}}
.btn{{display:inline-flex;align-items:center;justify-content:center;gap:10px;font-weight:600;font-size:15.5px;text-decoration:none;padding:15px 28px;border-radius:999px;border:2px solid transparent;cursor:pointer;min-height:50px;white-space:nowrap;transition:transform .25s var(--ease),box-shadow .25s,background .25s,border-color .25s}}
.btn:hover{{transform:translateY(-2px)}}
.btn-gold{{background:var(--grad);color:var(--night);box-shadow:0 14px 30px -12px rgba(217,169,63,.75)}}
.btn-gold:hover{{box-shadow:0 18px 36px -12px rgba(217,169,63,.95)}}
.btn-navy{{background:var(--navy);color:#fff}}
.btn-line{{border-color:rgba(255,255,255,.3);color:#fff}}
.btn-line:hover{{border-color:#fff;background:rgba(255,255,255,.06)}}
.btn-out{{border-color:var(--line);background:#fff}}
.btn-out:hover{{border-color:var(--navy)}}
.btn-wa{{background:#1FA855;color:#fff}}
.btn-wa:hover{{background:#178A45}}
.js .rv{{opacity:0;transform:translateY(28px);transition:opacity .8s var(--ease),transform .8s var(--ease);transition-delay:var(--d,0ms)}}
.js .rv.in{{opacity:1;transform:none}}
.js .svc.rv.in{{transition:transform .35s var(--ease),box-shadow .35s,border-color .35s,opacity .8s;transition-delay:0s}}

/* header */
header{{position:sticky;top:0;z-index:50;background:rgba(255,253,248,.9);backdrop-filter:saturate(1.5) blur(14px);-webkit-backdrop-filter:saturate(1.5) blur(14px);border-bottom:1px solid transparent;transition:border-color .3s,box-shadow .3s}}
header.scrolled{{border-color:var(--line);box-shadow:0 10px 30px -22px rgba(8,17,43,.4)}}
.nav{{display:flex;align-items:center;justify-content:space-between;height:80px;gap:20px}}
.brand img{{height:52px;width:auto}}
nav ul{{display:flex;gap:4px;list-style:none;align-items:center}}
nav a{{text-decoration:none;font-weight:500;font-size:15px;padding:10px 13px;border-radius:999px;transition:color .2s,background .2s}}
nav a:hover,nav a.active{{color:var(--gd)}}
nav .btn{{margin-left:10px;padding:11px 22px;min-height:44px;font-size:14.5px}}
nav .btn:hover{{color:var(--night)}}
.menu-btn{{display:none;background:none;border:0;width:46px;height:46px;cursor:pointer;border-radius:12px}}
.menu-btn span{{display:block;width:22px;height:2px;background:var(--navy);margin:5px auto;transition:.3s var(--ease)}}
.menu-btn[aria-expanded="true"] span:nth-child(1){{transform:translateY(7px) rotate(45deg)}}
.menu-btn[aria-expanded="true"] span:nth-child(2){{opacity:0}}
.menu-btn[aria-expanded="true"] span:nth-child(3){{transform:translateY(-7px) rotate(-45deg)}}
.progress{{position:absolute;left:0;bottom:-1px;height:3px;width:100%;transform-origin:0 50%;transform:scaleX(0);background:var(--grad)}}

/* hero */
.hero{{background:radial-gradient(1100px 640px at 82% 38%,#1e3a82 0%,transparent 62%),linear-gradient(160deg,var(--deep),var(--night));color:#fff;overflow:hidden;padding:0}}
.hero::before{{content:"";position:absolute;inset:0;background-image:radial-gradient(rgba(255,255,255,.08) 1px,transparent 1px);background-size:26px 26px;mask-image:radial-gradient(ellipse at 30% 50%,#000 10%,transparent 70%);-webkit-mask-image:radial-gradient(ellipse at 30% 50%,#000 10%,transparent 70%)}}
.hero .wrap{{position:relative;z-index:1;display:grid;grid-template-columns:1.1fr .9fr;gap:56px;align-items:center;padding-top:92px;padding-bottom:112px}}
.pill{{display:inline-flex;align-items:center;gap:10px;font-size:13.5px;font-weight:500;color:#E5EAF7;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.14);padding:7px 16px 7px 8px;border-radius:999px}}
.pill b{{background:var(--grad);color:var(--night);font-size:11.5px;font-weight:700;padding:3px 10px;border-radius:999px;letter-spacing:.04em}}
.hero h1{{font-size:clamp(40px,5.4vw,70px);font-weight:800;margin:26px 0 22px;letter-spacing:-.035em}}
.rot{{display:grid}}
.rot span{{grid-area:1/1;opacity:0;transform:translateY(40%);transition:opacity .5s var(--ease),transform .5s var(--ease);background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent;padding-bottom:.08em}}
.rot span.on{{opacity:1;transform:none}}
.rot span.off{{opacity:0;transform:translateY(-40%)}}
.hero p.sub{{color:#C4CDE8;font-size:19px;max-width:560px}}
.hero .actions{{display:flex;gap:14px;flex-wrap:wrap;margin-top:34px}}
.pillars{{display:grid;grid-template-columns:repeat(4,auto);justify-content:start;gap:16px 30px;margin-top:44px;padding-top:28px;border-top:1px solid rgba(255,255,255,.12)}}
.pillars b{{display:block;font-size:16px;font-weight:700}}
.pillars span{{font-size:13.5px;color:var(--soft)}}
.portrait{{position:relative;width:min(100%,440px);aspect-ratio:1;justify-self:center}}
.ring{{position:absolute;border-radius:50%}}
.ring.r1{{inset:-26px;border:18px solid var(--gold);border-top-color:transparent;border-left-color:transparent;transform:rotate(-12deg);animation:spin1 1.6s .2s var(--ease) both}}
.ring.r2{{inset:-48px;border:12px solid rgba(255,255,255,.14);border-bottom-color:transparent;border-right-color:transparent;transform:rotate(-20deg);animation:spin2 1.6s .3s var(--ease) both}}
@keyframes spin1{{from{{transform:rotate(-140deg);opacity:0}}}}
@keyframes spin2{{from{{transform:rotate(120deg);opacity:0}}}}
.portrait .face{{position:absolute;inset:0;border-radius:50%;overflow:hidden;border:8px solid #fff;background:linear-gradient(180deg,#f6e3b0,#e9c67a);box-shadow:0 40px 80px -30px rgba(0,0,0,.7)}}
.portrait .face img{{width:100%;height:100%;object-fit:cover}}
.spark{{position:absolute;right:-6px;top:-30px;width:70px;height:70px;color:var(--gold);animation:tw 3.4s ease-in-out infinite}}
.spark svg{{width:100%;height:100%}}
@keyframes tw{{0%,100%{{transform:scale(1) rotate(0)}}50%{{transform:scale(.82) rotate(18deg)}}}}
.badge{{position:absolute;z-index:2;display:flex;align-items:center;gap:12px;background:#fff;color:var(--ink);border-radius:16px;padding:12px 16px;box-shadow:0 22px 44px -18px rgba(0,0,0,.6);font-size:13px;animation:float 6s ease-in-out infinite}}
.badge b{{display:block;font-size:14.5px}}
.badge small{{color:var(--mut)}}
.badge .bi{{width:38px;height:38px;border-radius:12px;background:var(--cream);color:var(--gd);display:grid;place-items:center}}
.badge.b1{{left:-40px;bottom:46px}}
.badge.b2{{right:-46px;top:40%;animation-delay:-3s}}
.live{{width:9px;height:9px;border-radius:50%;background:#22C55E;box-shadow:0 0 0 4px rgba(34,197,94,.2);display:inline-block;margin-right:6px}}
@keyframes float{{0%,100%{{transform:translateY(0)}}50%{{transform:translateY(-10px)}}}}

.marquee{{background:var(--grad);color:var(--night);overflow:hidden;white-space:nowrap;padding:17px 0;font-weight:700;font-size:16.5px}}
.marquee .track{{display:inline-flex;gap:28px;align-items:center;animation:mq 38s linear infinite;padding-right:28px}}
.marquee i{{font-style:normal;opacity:.6}}
@keyframes mq{{to{{transform:translateX(-50%)}}}}

/* promise stats */
.stats{{padding:0;background:#fff;border-bottom:1px solid var(--line)}}
.stats .wrap{{display:grid;grid-template-columns:repeat(4,1fr)}}
.stat{{padding:40px 28px;border-left:1px solid var(--line)}}
.stat:first-child{{border-left:0;padding-left:0}}
.stat b{{display:block;font-size:44px;font-weight:800;letter-spacing:-.04em;line-height:1}}
.stat b i{{font-style:normal;color:var(--gd);font-size:.55em;margin-left:4px;letter-spacing:0}}
.stat>span{{display:block;margin-top:10px;color:var(--mut);font-size:15px}}

/* about */
.about .wrap{{display:grid;grid-template-columns:.9fr 1.1fr;gap:64px;align-items:center}}
.quote{{position:relative;background:var(--night);color:#fff;border-radius:28px;padding:48px 44px;overflow:hidden}}
.quote::before{{content:"\\201C";position:absolute;right:26px;top:-24px;font-size:200px;font-weight:800;color:rgba(217,169,63,.22);line-height:1}}
.quote p{{font-size:clamp(24px,2.6vw,32px);font-weight:700;line-height:1.3;letter-spacing:-.02em;position:relative}}
.quote .by{{display:flex;align-items:center;gap:14px;margin-top:28px}}
.quote .by img{{width:52px;height:52px;border-radius:50%;object-fit:cover;border:2px solid var(--gold)}}
.quote .by small{{display:block;color:var(--soft)}}
.creds{{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px}}
.creds span{{background:#fff;border:1px solid var(--line);border-radius:999px;padding:8px 16px;font-size:14px}}
.creds b{{color:var(--gd);font-weight:700;margin-right:6px}}
.creds a{{font-weight:600}}
.beliefs{{list-style:none;display:grid;gap:14px;margin-top:28px}}
.beliefs li{{display:flex;gap:14px;align-items:flex-start;background:#fff;border:1px solid var(--line);border-radius:16px;padding:16px 18px}}
.beliefs i{{flex:none;width:30px;height:30px;border-radius:50%;background:var(--grad);display:grid;place-items:center;color:var(--night)}}
.beliefs i svg{{width:16px;height:16px;stroke-width:3}}
.beliefs b{{display:block}}
.beliefs span{{color:var(--mut);font-size:15px}}

/* services */
.sgrid{{display:grid;grid-template-columns:repeat(2,1fr);gap:24px}}
.svc{{position:relative;background:#fff;border:1px solid var(--line);border-radius:24px;padding:36px 34px;display:flex;flex-direction:column;transition:transform .35s var(--ease),box-shadow .35s,border-color .35s;overflow:hidden}}
.svc::after{{content:"";position:absolute;left:0;top:0;height:4px;width:0;background:var(--grad);transition:width .4s var(--ease)}}
.svc:hover{{transform:translateY(-6px);box-shadow:0 34px 60px -34px rgba(8,17,43,.45);border-color:#e3cf9c}}
.svc:hover::after{{width:100%}}
.sico{{width:58px;height:58px;border-radius:16px;background:var(--navy);color:var(--gl);display:grid;place-items:center;margin-bottom:22px}}
.sico svg{{width:26px;height:26px}}
.snum{{position:absolute;right:30px;top:26px;font-size:54px;font-weight:800;color:var(--cream);letter-spacing:-.04em;line-height:1}}
.svc h3{{font-size:24px;font-weight:700;margin-bottom:10px}}
.svc p{{color:var(--mut);margin-bottom:18px}}
.svc ul{{list-style:none;display:grid;gap:8px;margin-bottom:22px}}
.svc li{{display:flex;gap:10px;align-items:flex-start;font-size:15px}}
.svc li svg{{color:var(--gd);margin-top:3px;width:18px;height:18px;stroke-width:2.6}}
.best{{display:inline-block;align-self:flex-start;font-size:13px;font-weight:600;color:var(--gd);background:var(--cream);border-radius:999px;padding:6px 14px;margin-bottom:22px}}
.slink{{margin-top:auto;display:inline-flex;align-items:center;gap:8px;font-weight:600;text-decoration:none;color:var(--navy)}}
.slink svg{{transition:transform .3s var(--ease)}}
.svc:hover .slink svg{{transform:translateX(5px)}}

/* growth check */
.check{{overflow:hidden}}
.check .wrap{{display:grid;grid-template-columns:.85fr 1.15fr;gap:56px;align-items:start}}
.check::before{{content:"";position:absolute;right:-200px;top:-200px;width:640px;height:640px;border-radius:50%;background:radial-gradient(circle,rgba(30,58,130,.7),transparent 65%);pointer-events:none}}
.check .wrap>*{{position:relative}}
.qcard{{background:#fff;color:var(--ink);border-radius:28px;padding:30px;box-shadow:0 40px 80px -30px rgba(0,0,0,.6)}}
.qlist{{list-style:none;display:grid;gap:10px}}
.qz{{display:grid;grid-template-columns:32px 1fr auto;gap:14px;align-items:center;padding:12px 14px;border:1px solid var(--line);border-radius:14px;transition:border-color .2s,background .2s}}
.qz.done{{background:#FFFCF4;border-color:#ead9ad}}
.qn{{width:32px;height:32px;border-radius:50%;background:var(--cream);color:var(--gd);display:grid;place-items:center;font-weight:700;font-size:14px}}
.qt{{font-size:15px;font-weight:500}}
.seg{{display:inline-flex;background:var(--cream);border-radius:999px;padding:4px}}
.seg button{{border:0;background:none;cursor:pointer;font-weight:600;font-size:14px;padding:8px 16px;border-radius:999px;min-height:40px;min-width:56px;transition:background .2s,color .2s}}
.seg button[aria-pressed="true"][data-v="1"]{{background:var(--navy);color:#fff}}
.seg button[aria-pressed="true"][data-v="0"]{{background:#fff;color:var(--ink);box-shadow:0 2px 8px rgba(8,17,43,.15)}}
.result{{margin-top:20px;display:grid;grid-template-columns:120px 1fr;gap:22px;align-items:center;background:var(--cream);border-radius:20px;padding:20px 22px}}
.gauge{{position:relative;width:120px;height:120px}}
.gauge svg{{width:120px;height:120px;transform:rotate(-90deg)}}
.gauge circle{{fill:none;stroke-width:11}}
.gauge .bg{{stroke:#ecdfbd}}
.gauge .fg{{stroke:url(#gg);stroke-linecap:round;transition:stroke-dashoffset .8s var(--ease)}}
.gauge b{{position:absolute;inset:0;display:grid;place-items:center;font-size:28px;font-weight:800}}
.result h4{{font-size:18px;font-weight:700;margin-bottom:4px}}
.result p{{color:var(--mut);font-size:14.5px}}
.result .btn{{margin-top:12px;padding:11px 20px;min-height:44px;font-size:14.5px}}

/* case study */
.case{{display:grid;grid-template-columns:1.15fr .85fr;gap:56px;align-items:center}}
.shot{{position:relative}}
.browser{{border-radius:18px;overflow:hidden;background:#fff;box-shadow:0 50px 90px -40px rgba(8,17,43,.6);border:1px solid var(--line)}}
.browser .bar{{display:flex;align-items:center;gap:7px;padding:12px 16px;background:#F1EEE6;border-bottom:1px solid var(--line)}}
.browser .bar i{{width:11px;height:11px;border-radius:50%;background:#E0D8C4}}
.browser .bar span{{margin-left:12px;flex:1;background:#fff;border-radius:999px;font-size:12.5px;color:var(--mut);padding:5px 14px}}
.browser img{{width:100%;height:auto}}
.shot .calc{{position:absolute;right:-28px;bottom:-40px;width:46%;height:auto;border-radius:16px;overflow:hidden;box-shadow:0 30px 60px -24px rgba(8,17,43,.55);border:4px solid #fff}}
.tag{{display:inline-block;font-size:12.5px;font-weight:600;padding:5px 12px;border-radius:999px;background:var(--cream);color:var(--gd);margin-bottom:14px}}
.case h3{{font-size:clamp(28px,3vw,38px);font-weight:800;margin-bottom:12px}}
.ba{{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:24px 0 28px}}
.ba div{{border-radius:16px;padding:18px}}
.ba .bf{{background:#F3F1EC}}
.ba .af{{background:var(--night);color:#fff}}
.ba h4{{font-size:12px;letter-spacing:.16em;text-transform:uppercase;margin-bottom:10px}}
.ba .bf h4{{color:var(--mut)}}
.ba .af h4{{color:var(--gl)}}
.ba ul{{list-style:none;display:grid;gap:7px;font-size:14px}}
.ba .bf li::before{{content:"– ";color:var(--mut)}}
.ba .af li::before{{content:"✓ ";color:var(--gl);font-weight:700}}
.actions-row{{display:flex;gap:12px;flex-wrap:wrap}}

/* process */
.steps{{display:grid;grid-template-columns:repeat(3,1fr);gap:0;counter-reset:s}}
.step{{padding:0 28px 0 0;position:relative}}
.step::before{{counter-increment:s;content:counter(s);display:block;font-size:84px;font-weight:800;line-height:1;background:var(--grad);-webkit-background-clip:text;background-clip:text;color:transparent;margin-bottom:14px}}
.step::after{{content:"";position:absolute;top:42px;left:72px;right:24px;height:2px;background:repeating-linear-gradient(90deg,#e3cf9c 0 8px,transparent 8px 15px)}}
.step:last-child::after{{display:none}}
.step h3{{font-size:22px;font-weight:700;margin-bottom:8px}}
.step p{{color:var(--mut)}}

/* faq */
.faq-wrap{{display:grid;grid-template-columns:.8fr 1.2fr;gap:56px;align-items:start}}
.faq-list{{display:grid;gap:12px}}
details{{background:#fff;border:1px solid var(--line);border-radius:16px;transition:border-color .2s,box-shadow .2s}}
details[open]{{border-color:#e3cf9c;box-shadow:0 18px 36px -28px rgba(8,17,43,.4)}}
summary{{list-style:none;cursor:pointer;padding:20px 22px;font-weight:600;font-size:16.5px;display:flex;justify-content:space-between;gap:16px;align-items:center}}
summary::-webkit-details-marker{{display:none}}
summary i{{flex:none;width:30px;height:30px;border-radius:50%;background:var(--cream);position:relative}}
summary i::before,summary i::after{{content:"";position:absolute;left:50%;top:50%;width:12px;height:2px;background:var(--gd);transform:translate(-50%,-50%);transition:transform .3s var(--ease)}}
summary i::after{{transform:translate(-50%,-50%) rotate(90deg)}}
details[open] summary i::after{{transform:translate(-50%,-50%) rotate(0)}}
details p{{padding:0 22px 22px;color:var(--mut)}}

/* contact */
.contact{{background:radial-gradient(900px 520px at 12% 0%,#1e3a82 0%,transparent 60%),var(--night);color:#fff}}
.contact .wrap{{display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:start}}
.contact h2{{color:#fff}}
.info{{display:grid;gap:12px;margin-top:30px}}
.info a{{display:flex;align-items:center;gap:16px;text-decoration:none;background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.12);border-radius:16px;padding:16px 18px;transition:border-color .2s,background .2s}}
.info a:hover{{border-color:var(--gold);background:rgba(255,255,255,.08)}}
.ico{{width:46px;height:46px;border-radius:14px;background:var(--grad);color:var(--night);display:grid;place-items:center;flex:none}}
.info small{{display:block;color:var(--soft);font-size:13px}}
.info b{{font-weight:600;word-break:break-all}}
form.cf{{background:rgba(255,255,255,.05);border:1px solid rgba(255,255,255,.14);border-radius:26px;padding:34px;display:grid;gap:16px}}
label{{display:grid;gap:7px;font-weight:600;font-size:14px;color:#E6ECFF}}
input,select,textarea{{font:inherit;font-size:15px;padding:13px 16px;border:1.5px solid rgba(255,255,255,.2);border-radius:14px;background:rgba(255,255,255,.07);color:#fff;width:100%;min-width:0;min-height:50px;transition:border-color .2s,box-shadow .2s}}
select option{{color:var(--ink)}}
input::placeholder,textarea::placeholder{{color:#8D99C2}}
input:focus,select:focus,textarea:focus{{outline:none;border-color:var(--gold);box-shadow:0 0 0 4px rgba(217,169,63,.25)}}
textarea{{min-height:120px;resize:vertical}}
.frow{{display:grid;grid-template-columns:1fr 1fr;gap:16px}}
.fbtns{{display:flex;gap:12px;flex-wrap:wrap}}
.fbtns .btn{{flex:1}}
.note{{font-size:13px;color:var(--soft)}}

footer{{background:#050b1f;color:var(--soft);font-size:14.5px}}
.foot{{display:flex;justify-content:space-between;align-items:center;gap:20px;flex-wrap:wrap;padding-top:34px;padding-bottom:34px}}
.foot img{{height:44px;width:auto;background:#fff;border-radius:10px;padding:4px 8px}}
.foot nav ul{{gap:0}}
.foot nav a{{color:var(--soft);font-size:14px}}
.foot nav a:hover{{color:var(--gl)}}
.legal{{border-top:1px solid rgba(255,255,255,.07)}}
.legal .wrap{{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;padding-top:18px;padding-bottom:18px;font-size:12.5px;color:#7884AA}}

.wa{{position:fixed;right:22px;bottom:22px;z-index:60;width:60px;height:60px;border-radius:50%;background:#25D366;color:#fff;display:grid;place-items:center;box-shadow:0 14px 30px -8px rgba(0,0,0,.35)}}
.wa svg{{width:30px;height:30px}}
.wa::before{{content:"";position:absolute;inset:0;border-radius:50%;background:#25D366;animation:pulse 2.4s ease-out infinite;z-index:-1}}
@keyframes pulse{{0%{{transform:scale(1);opacity:.6}}100%{{transform:scale(1.7);opacity:0}}}}
.totop{{position:fixed;right:30px;bottom:96px;z-index:60;width:44px;height:44px;border-radius:50%;border:1px solid var(--line);background:#fff;cursor:pointer;display:grid;place-items:center;opacity:0;pointer-events:none;transition:opacity .3s,transform .3s;transform:translateY(10px)}}
.totop.show{{opacity:1;pointer-events:auto;transform:none}}
.totop svg{{transform:rotate(-90deg)}}
.mbar{{display:none}}

@media (max-width:1080px){{
  nav ul{{gap:0}} nav a{{padding:10px 9px;font-size:14.5px}}
  .about .wrap,.check .wrap,.case,.faq-wrap,.contact .wrap{{grid-template-columns:1fr}}
  .shot .calc{{right:8px}}
  .case{{gap:80px}}
}}
@media (max-width:900px){{
  header nav ul{{position:absolute;top:80px;left:0;right:0;background:var(--paper);flex-direction:column;align-items:stretch;padding:8px 24px 24px;border-bottom:1px solid var(--line);box-shadow:0 30px 40px -30px rgba(0,0,0,.3);display:none}}
  header nav ul.open{{display:flex}}
  header nav li a{{display:block;padding:14px 4px;font-size:16px;border-bottom:1px solid var(--line);border-radius:0}}
  header nav li .btn{{margin:14px 0 0;border:0;border-radius:999px}}
  .menu-btn{{display:block}}
  .hero .wrap{{grid-template-columns:1fr;padding-top:60px;padding-bottom:90px;gap:80px}}
  .portrait{{width:min(78%,360px)}}
  .badge.b1{{left:-24px}} .badge.b2{{right:-30px}}
  .stats .wrap{{grid-template-columns:1fr 1fr}}
  .stat{{padding:28px 20px}}
  .stat:nth-child(3){{border-left:0;padding-left:0}}
  .stat:nth-child(n+3){{border-top:1px solid var(--line)}}
  .sgrid,.steps{{grid-template-columns:1fr}}
  .step{{padding:0 0 36px}}
  .step::after{{display:none}}
}}
@media (max-width:640px){{
  .wrap{{padding:0 18px}}
  section{{padding:78px 0}}
  .brand img{{height:44px}}
  .hero h1{{font-size:clamp(36px,10.5vw,46px)}}
  .hero p.sub{{font-size:17px}}
  .hero .actions .btn{{flex:1}}
  .pillars{{grid-template-columns:1fr 1fr}}
  .badge{{padding:9px 12px;font-size:12px}} .badge b{{font-size:13px}} .badge .bi{{width:32px;height:32px}}
  .badge.b1{{left:-14px;bottom:10px}} .badge.b2{{right:-14px}}
  .stat b{{font-size:34px}}
  .quote{{padding:34px 26px}}
  .svc{{padding:28px 24px}}
  .snum{{font-size:42px;right:22px}}
  .qcard{{padding:18px}}
  .qz{{grid-template-columns:28px 1fr;gap:10px 12px}}
  .qn{{width:28px;height:28px;font-size:13px}}
  .seg{{grid-column:2;justify-self:start}}
  .result{{grid-template-columns:1fr;justify-items:start}}
  .ba{{grid-template-columns:1fr}}
  .shot .calc{{width:52%;bottom:-36px;right:-6px}}
  form.cf{{padding:22px}}
  .frow{{grid-template-columns:1fr}}
  .wa,.totop{{display:none}}
  .mbar{{display:grid;grid-template-columns:1fr 1fr 1.3fr;gap:8px;position:fixed;left:0;right:0;bottom:0;z-index:70;background:rgba(255,253,248,.96);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border-top:1px solid var(--line);padding:10px 12px calc(10px + env(safe-area-inset-bottom))}}
  .mbar a{{display:flex;align-items:center;justify-content:center;gap:8px;min-height:48px;border-radius:999px;font-weight:600;font-size:14.5px;text-decoration:none}}
  .mbar .m1{{background:var(--cream)}} .mbar .m2{{background:#1FA855;color:#fff}} .mbar .m3{{background:var(--grad);color:var(--night)}}
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
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs><linearGradient id="gg" x1="0" x2="1"><stop offset="0" stop-color="#f0cd74"/><stop offset="1" stop-color="#b8861b"/></linearGradient></defs></svg>

<header id="hdr">
  <div class="wrap nav">
    <a class="brand" href="#top" aria-label="Biz With Aman home"><img src="logo-sm.png" alt="Biz With Aman" width="440" height="201"></a>
    <button class="menu-btn" id="menuBtn" aria-label="Open menu" aria-expanded="false" aria-controls="menu"><span></span><span></span><span></span></button>
    <nav aria-label="Main">
      <ul id="menu">
        <li><a href="#about">About</a></li>
        <li><a href="#services">Services</a></li>
        <li><a href="#growth-check">Growth check</a></li>
        <li><a href="#work">Work</a></li>
        <li><a href="#process">Process</a></li>
        <li><a href="#faq">FAQ</a></li>
        <li><a class="btn btn-gold" href="#contact">Book a free call</a></li>
      </ul>
    </nav>
  </div>
  <div class="progress" id="progress"></div>
</header>

<main>
<section class="hero">
  <div class="wrap">
    <div>
      <span class="pill"><b>FREE</b> 30-minute strategy call · India &amp; worldwide</span>
      <h1>Grow your business with a <span class="rot" aria-hidden="true"><span class="on">clear plan</span><span>steady pipeline</span><span>website that sells</span><span>trusted brand</span></span><span style="position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)">clear plan</span> that actually works.</h1>
      <p class="sub">I&rsquo;m Aman. I help founders, manufacturers and small businesses find the one or two things holding growth back, fix them first, and build a routine that keeps results coming.</p>
      <div class="actions">
        <a class="btn btn-gold" href="#contact">Book a free call {I["arrow"]}</a>
        <a class="btn btn-line" href="#growth-check">Take the 1-minute growth check</a>
      </div>
      <div class="pillars">
        <div><b>Strategy</b><span>Clear 90-day plans</span></div>
        <div><b>Growth</b><span>Sales and marketing</span></div>
        <div><b>Digital</b><span>Websites that bring enquiries</span></div>
        <div><b>Brand</b><span>Be known for your work</span></div>
      </div>
    </div>
    <div class="portrait">
      <span class="ring r2" aria-hidden="true"></span><span class="ring r1" aria-hidden="true"></span>
      <div class="face"><img src="aman.jpg" alt="Portrait of Aman" width="560" height="560"></div>
      <span class="spark" aria-hidden="true"><svg viewBox="0 0 24 24" class="fill"><path d="M12 0c.6 6.2 5.8 11.4 12 12-6.2.6-11.4 5.8-12 12-.6-6.2-5.8-11.4-12-12C6.2 11.4 11.4 6.2 12 0z"/></svg></span>
      <div class="badge b1"><span class="bi">{I["target"]}</span><span><b>Aman</b><small>Business &amp; growth consultant</small></span></div>
      <a class="badge b2" href="#work" style="text-decoration:none"><span class="bi">{I["globe"]}</span><span><b><span class="live"></span>Live project</b><small>Parkash Industries</small></span></a>
    </div>
  </div>
</section>

<div class="marquee" aria-hidden="true"><div class="track">{marq}{marq}</div></div>

<section class="stats" aria-label="How I work">
  <div class="wrap">
    <div class="stat rv"><b><span class="count" data-to="30">30</span><i>min</i></b><span>Free first call, no obligation</span></div>
    <div class="stat rv" style="--d:80ms"><b><span class="count" data-to="90">90</span><i>days</i></b><span>Written plan you can start on</span></div>
    <div class="stat rv" style="--d:160ms"><b><span class="count" data-to="1">1</span><i>day</i></b><span>Reply within one working day</span></div>
    <div class="stat rv" style="--d:240ms"><b><span class="count" data-to="4">4</span><i>ways</i></b><span>To work together</span></div>
  </div>
</section>

<section id="about" class="about">
  <div class="wrap">
    <figure class="quote rv">
      <p>Growth is not about doing more. It is about doing the right few things, every week.</p>
      <figcaption class="by"><img src="aman.jpg" alt="" width="52" height="52"><span><b>Aman</b><small>Founder, Biz With Aman</small></span></figcaption>
    </figure>
    <div class="rv" style="--d:120ms">
      <span class="kick">About me</span>
      <h2>Practical advice from someone who <em>does the work</em></h2>
      <p class="lead">I work with owners who are busy running the business and don&rsquo;t have time to work out why growth has stalled. No jargon, no 80-page decks.</p>
      <div class="creds"><span><b>Founder</b>Biz With Aman</span><span><b>Director</b>ASN Poultech Pvt. Ltd.</span><span><b>Live client</b><a href="/parkash/">Parkash Industries</a></span></div>
      <ul class="beliefs">
        <li><i>{I["check"]}</i><div><b>Fix the bottleneck first</b><span>Find the one or two things holding you back before adding anything new.</span></div></li>
        <li><i>{I["check"]}</i><div><b>Numbers over opinions</b><span>Weekly targets and a simple scorecard, so you always know what is working.</span></div></li>
        <li><i>{I["check"]}</i><div><b>Done, not just advised</b><span>From the plan to the website and the WhatsApp system, I build it with you.</span></div></li>
      </ul>
    </div>
  </div>
</section>

<section id="services" class="cream">
  <div class="wrap">
    <div class="head split">
      <div><span class="kick">Services</span><h2>Four ways to <em>work together</em></h2></div>
      <p class="lead">Start with one session or bring me in for ongoing growth. Every engagement starts with a free call.</p>
    </div>
    <div class="sgrid">
{services()}
    </div>
  </div>
</section>

<section id="growth-check" class="check dark">
  <div class="wrap">
    <div class="rv">
      <span class="kick">Free growth check</span>
      <h2>How ready is your business to <em>grow?</em></h2>
      <p class="lead">Answer six quick questions. You get a score and the first area to fix, and you can send the result to me for a free review.</p>
    </div>
    <div class="qcard rv" style="--d:120ms">
      <ol class="qlist" id="quiz">{quiz()}</ol>
      <div class="result" aria-live="polite">
        <div class="gauge"><svg viewBox="0 0 120 120" aria-hidden="true"><circle class="bg" cx="60" cy="60" r="50"/><circle class="fg" id="gFg" cx="60" cy="60" r="50" stroke-dasharray="314.16" stroke-dashoffset="314.16"/></svg><b id="gNum">0</b></div>
        <div><h4 id="rTitle">Answer the questions to see your score</h4><p id="rText">Your score out of 100 appears here as you answer.</p>
        <a class="btn btn-wa" id="rWa" href="{WA}Hi%20Aman%2C%20I%20want%20a%20free%20growth%20review." target="_blank" rel="noopener">{I["wa"]} Send my result to Aman</a></div>
      </div>
    </div>
  </div>
</section>

<section id="work">
  <div class="wrap case">
    <div class="shot rv">
      <div class="browser"><div class="bar"><i></i><i></i><i></i><span>bizwithaman.com/parkash</span></div>
        <img src="work-parkash.jpg" alt="Parkash Industries website home page" width="1200" height="532" loading="lazy"></div>
      <img class="calc" src="work-parkash-calc.jpg" alt="Instant price calculator on the Parkash website" width="630" height="479" loading="lazy">
    </div>
    <div class="rv" style="--d:120ms">
      <span class="kick">Featured work</span>
      <h3>Parkash Industries</h3>
      <span class="tag">Poultry equipment manufacturer · Jind, Haryana</span>
      <p class="lead">A brand of ASN Poultech Pvt. Ltd. I built a full brand website that works as a 24-hour sales desk for farms in India and export buyers.</p>
      <div class="ba">
        <div class="bf"><h4>Before</h4><ul><li>Only a marketplace catalogue</li><li>No price or spec details for buyers</li><li>Enquiries scattered across calls</li></ul></div>
        <div class="af"><h4>After</h4><ul><li>Brand site with 24-product catalogue</li><li>Instant price calculator</li><li>One-tap WhatsApp quotes, map &amp; FAQ</li></ul></div>
      </div>
      <div class="actions-row">
        <a class="btn btn-navy" href="/parkash/">Visit the live site {I["arrow"]}</a>
        <a class="btn btn-out" href="#contact" data-svc="Website &amp; digital setup">I want one like this</a>
      </div>
    </div>
  </div>
</section>

<section id="process" class="cream">
  <div class="wrap">
    <div class="head"><span class="kick">How it works</span><h2>From first call to <em>real results</em></h2></div>
    <div class="steps">
      <div class="step rv"><h3>Talk</h3><p>A free 30-minute call to understand your goals and where you are today.</p></div>
      <div class="step rv" style="--d:100ms"><h3>Plan</h3><p>I send a clear proposal with what we&rsquo;ll do, how long it takes and what it costs.</p></div>
      <div class="step rv" style="--d:200ms"><h3>Deliver</h3><p>We work through the plan together, with regular check-ins and honest progress reports.</p></div>
    </div>
  </div>
</section>

<section id="faq">
  <div class="wrap faq-wrap">
    <div class="rv">
      <span class="kick">FAQ</span>
      <h2>Common <em>questions</em></h2>
      <p class="lead">Something else on your mind? Message me on WhatsApp and I&rsquo;ll answer personally.</p>
      <div class="actions-row" style="margin-top:26px"><a class="btn btn-wa" href="{WA}Hi%20Aman%2C%20I%20have%20a%20question." target="_blank" rel="noopener">{I["wa"]} Ask on WhatsApp</a></div>
    </div>
    <div class="faq-list">{faq()}</div>
  </div>
</section>

<section id="contact" class="contact">
  <div class="wrap">
    <div class="rv">
      <span class="kick" style="color:var(--gl)">Contact</span>
      <h2>Let&rsquo;s talk about <em>your business</em></h2>
      <p class="lead">Tell me what you&rsquo;re working on and where you want to be in a year. I reply within one working day.</p>
      <div class="info">
        <a href="{WA}Hi%20Aman%2C%20I%20found%20you%20on%20bizwithaman.com" target="_blank" rel="noopener"><span class="ico">{I["wa"]}</span><span><small>WhatsApp</small><b>Message me directly</b></span></a>
        <a href="tel:+{PHONE}"><span class="ico">{I["phone"]}</span><span><small>Call</small><b>{PHONE_D}</b></span></a>
        <a href="mailto:{EMAIL}"><span class="ico">{I["mail"]}</span><span><small>Email</small><b>{EMAIL}</b></span></a>
      </div>
    </div>
    <form class="cf rv" id="cf" style="--d:120ms" novalidate>
      <div class="frow">
        <label>Your name<input name="n" required autocomplete="name"></label>
        <label>Phone or email<input name="c" required autocomplete="tel"></label>
      </div>
      <label>I&rsquo;m interested in
        <select name="s">{"".join(f"<option>{esc(s[1])}</option>" for s in SERVICES)}<option>Not sure yet</option></select>
      </label>
      <label>What do you need help with?<textarea name="m" placeholder="Your business, your goal for the next year, and what is holding you back…"></textarea></label>
      <div class="fbtns">
        <button class="btn btn-gold" type="submit">{I["wa"]} Send on WhatsApp</button>
        <button class="btn btn-line" type="button" id="cfMail">{I["mail"]} Send by email</button>
      </div>
      <p class="note">Your message opens in WhatsApp or your email app, ready to send.</p>
    </form>
  </div>
</section>
</main>

<footer>
  <div class="wrap foot">
    <img src="logo-sm.png" alt="Biz With Aman" width="440" height="201" loading="lazy">
    <nav aria-label="Footer"><ul style="display:flex;flex-wrap:wrap;list-style:none"><li><a href="#services">Services</a></li><li><a href="#growth-check">Growth check</a></li><li><a href="#work">Work</a></li><li><a href="/parkash/">Parkash Industries</a></li><li><a href="#contact">Contact</a></li></ul></nav>
  </div>
  <div class="legal"><div class="wrap"><span>© <span id="yr">2026</span> Biz With Aman. All rights reserved.</span><span>Business · Growth · Success</span></div></div>
</footer>

<button class="totop" id="toTop" type="button" aria-label="Back to top">{I["arrow"]}</button>
<a class="wa" href="{WA}Hi%20Aman%2C%20I%20found%20you%20on%20bizwithaman.com" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{I["wa"]}</a>
<div class="mbar">
  <a class="m1" href="tel:+{PHONE}">{I["phone"]} Call</a>
  <a class="m2" href="{WA}Hi%20Aman%2C%20I%20found%20you%20on%20bizwithaman.com" target="_blank" rel="noopener">{I["wa"]} WhatsApp</a>
  <a class="m3" href="#contact">Free call</a>
</div>

<script>
(function(){{
  var PHONE='{PHONE}',EMAIL='{EMAIL}';
  var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
  function $(s,c){{return (c||document).querySelector(s)}}
  function $$(s,c){{return Array.prototype.slice.call((c||document).querySelectorAll(s))}}
  $('#yr').textContent=new Date().getFullYear();

  var mb=$('#menuBtn'),menu=$('#menu');
  mb.addEventListener('click',function(){{var o=menu.classList.toggle('open');mb.setAttribute('aria-expanded',o)}});
  menu.addEventListener('click',function(e){{if(e.target.closest('a')){{menu.classList.remove('open');mb.setAttribute('aria-expanded','false')}}}});

  var hdr=$('#hdr'),pr=$('#progress'),tt=$('#toTop'),tick=false;
  function onScroll(){{var y=scrollY,h=document.documentElement.scrollHeight-innerHeight;hdr.classList.toggle('scrolled',y>10);pr.style.transform='scaleX('+(h>0?y/h:0)+')';tt.classList.toggle('show',y>900);tick=false}}
  addEventListener('scroll',function(){{if(!tick){{requestAnimationFrame(onScroll);tick=true}}}},{{passive:true}});onScroll();
  tt.addEventListener('click',function(){{scrollTo({{top:0,behavior:reduce?'auto':'smooth'}})}});

  var links=$$('header nav a[href^="#"]'),secs=links.map(function(a){{return $(a.getAttribute('href'))}}).filter(Boolean);
  function count(el){{var to=+el.dataset.to,t0=null;if(reduce){{el.textContent=to;return}}function f(t){{if(!t0)t0=t;var p=Math.min(1,(t-t0)/1200),e=1-Math.pow(1-p,3);el.textContent=Math.round(to*e);if(p<1)requestAnimationFrame(f)}}requestAnimationFrame(f)}}
  if('IntersectionObserver' in window){{
    var nio=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting)links.forEach(function(a){{a.classList.toggle('active',a.getAttribute('href')==='#'+e.target.id)}})}})}},{{rootMargin:'-45% 0px -50% 0px'}});
    secs.forEach(function(s){{nio.observe(s)}});
    var io=new IntersectionObserver(function(es){{es.forEach(function(e){{if(e.isIntersecting){{e.target.classList.add('in');$$('.count',e.target).forEach(count);io.unobserve(e.target)}}}})}},{{threshold:.12,rootMargin:'0px 0px -40px 0px'}});
    $$('.rv').forEach(function(el){{io.observe(el)}});
  }}else $$('.rv').forEach(function(el){{el.classList.add('in')}});

  var words=$$('.rot span'),wi=0;
  if(words.length&&!reduce)setInterval(function(){{var a=words[wi];a.classList.remove('on');a.classList.add('off');wi=(wi+1)%words.length;var b=words[wi];b.classList.remove('off');void b.offsetWidth;b.classList.add('on');setTimeout(function(){{a.classList.remove('off')}},500)}},2400);

  /* growth check */
  var items=$$('.qz'),ans={{}},C=314.16;
  var AREAS=['a written 90-day plan','tracking your numbers weekly','a website that brings enquiries','your Google Business Profile','fast lead follow-up','a regular content routine'];
  function score(){{
    var n=Object.keys(ans).length,yes=0,firstNo=-1;
    items.forEach(function(it,i){{if(ans[i]===1)yes++;else if(ans[i]===0&&firstNo<0)firstNo=i}});
    var pct=Math.round(yes/items.length*100);
    $('#gNum').textContent=n?pct:0;$('#gFg').style.strokeDashoffset=C*(1-(n?pct:0)/100);
    var t,x;
    if(!n){{t='Answer the questions to see your score';x='Your score out of 100 appears here as you answer.'}}
    else if(n<items.length){{t='Keep going: '+n+' of '+items.length+' answered';x='Answer all six to get your first area to fix.'}}
    else if(pct>=84){{t='Strong foundations';x='You have the basics in place. The next step is scaling what already works.'}}
    else if(pct>=50){{t='Good base, clear gaps';x='Start with '+AREAS[firstNo]+'. Fixing that first usually gives the quickest result.'}}
    else{{t='Big room to grow';x='Start with '+AREAS[firstNo]+'. A 90-day plan will put the rest in order.'}}
    $('#rTitle').textContent=t;$('#rText').textContent=x;
    var msg='Hi Aman, I took the growth check on bizwithaman.com.\\nScore: '+(n?pct:'-')+'/100 ('+n+'/'+items.length+' answered)';
    items.forEach(function(it,i){{if(i in ans)msg+='\\n'+(ans[i]?'Yes':'No')+': '+it.querySelector('.qt').textContent}});
    msg+='\\n\\nI would like a free review.';
    $('#rWa').href='https://wa.me/'+PHONE+'?text='+encodeURIComponent(msg);
  }}
  items.forEach(function(it,i){{$$('button',it).forEach(function(b){{b.addEventListener('click',function(){{ans[i]=+b.dataset.v;$$('button',it).forEach(function(x){{x.setAttribute('aria-pressed',x===b)}});it.classList.add('done');score()}})}})}});

  /* service links preselect */
  var cf=$('#cf');
  $$('[data-svc]').forEach(function(a){{a.addEventListener('click',function(){{var v=a.dataset.svc;for(var i=0;i<cf.s.options.length;i++)if(cf.s.options[i].text===v)cf.s.selectedIndex=i}})}});
  function send(via){{
    if(!cf.n.value.trim()||!cf.c.value.trim()){{(cf.n.value.trim()?cf.c:cf.n).focus();return}}
    var msg='Hi Aman,\\n\\nName: '+cf.n.value+'\\nContact: '+cf.c.value+'\\nInterested in: '+cf.s.value+'\\n\\n'+(cf.m.value||'');
    if(via==='mail')location.href='mailto:'+EMAIL+'?subject='+encodeURIComponent('Enquiry from bizwithaman.com: '+cf.s.value)+'&body='+encodeURIComponent(msg);
    else window.open('https://wa.me/'+PHONE+'?text='+encodeURIComponent(msg),'_blank','noopener');
  }}
  cf.addEventListener('submit',function(e){{e.preventDefault();send('wa')}});
  $('#cfMail').addEventListener('click',function(){{send('mail')}});
}})();
</script>
</body>
</html>
'''
open(OUT,"w",encoding="utf-8").write(page)
print("wrote",OUT,len(page))
