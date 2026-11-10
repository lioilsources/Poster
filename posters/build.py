"""Konfigurovatelný build plakátů. Edituj poster.json, spusť: .venv/bin/python build.py [sada1 sada2 ...] [--theme neon] [--place kavarna]"""
import json, sys, pathlib, re
from urllib.parse import quote
from jinja2 import Environment, FileSystemLoader
from playwright.sync_api import sync_playwright
from pypdf import PdfWriter, PdfReader
from qr import qr_data_uri
R=pathlib.Path(__file__).parent
cfg=json.load(open(R/"poster.json")); H={a["slug"]:a for a in json.load(open(R/"harvest.json"))}
argv=sys.argv[1:]
def opt(n):
    return argv[argv.index(n)+1] if n in argv else None
theme_name=opt("--theme") or cfg["theme"]; place=opt("--place") or cfg["place"]
skip={i for n in ("--theme","--place") if n in argv for i in (argv.index(n),argv.index(n)+1)}
build=[a for i,a in enumerate(argv) if i not in skip] or cfg["build"]
def web(path=""): return f"https://olin.now/{path}{'&' if '?' in path else '?'}src={place}"
def play(u): return u+("&" if "?" in u else "?")+"referrer="+quote(f"utm_source={place}&utm_medium=poster")
def card(slug,per):
    a=H[slug]; d=R/"assets"/slug; shots=a["shots"]
    ov=cfg["shots"].get(slug); f=ov if ov else (shots[min(cfg["shot_index"],len(shots)-1)] if shots else None)
    qrs=[]
    if a["ios"] and a["android"]:
        qrs=[dict(uri=qr_data_uri(a["ios"]),label="App Store"),dict(uri=qr_data_uri(play(a["android"])),label="Google Play")]
    else: qrs=[dict(uri=qr_data_uri(web(slug+".html")),label="Podívej se · olin.now")]
    return dict(name=a["name"],tagline=a["tagline"],shot=(d/f).as_uri() if f and (d/f).exists() else None,
        icon=(d/"icon.png").as_uri() if (d/"icon.png").exists() else None,qrs=qrs)
env=Environment(loader=FileSystemLoader(R/"templates")); tpl=env.get_template("page.html")
theme=(R/"theme.css").read_text(); logo=(R/"assets/logo.png").as_uri()
sheets={s["id"]:s for s in cfg["sheets"]}
out=R/"out"/f"{theme_name}-{place}"; out.mkdir(parents=True,exist_ok=True)
pages=[]
for sid in build:
    s=sheets[sid]; k=s["kind"]
    base=dict(theme=theme,theme_name=theme_name,logo=logo,title=s["title"],sub=s["sub"],cat=s.get("cat","default"),kind=k,text=s.get("text",""),webqr=qr_data_uri(web()))
    if k=="apps":
        n=s.get("per_page",cfg["per_page"]); sl=s["slugs"]
        chunks=[sl[i:i+n] for i in range(0,len(sl),n)]
        if len(chunks)>1 and len(chunks[-1])==1 and n>2: chunks=[sl[i:i+(len(sl)+1)//2] for i in range(0,len(sl),(len(sl)+1)//2)] if len(sl)<=2*n else chunks
        for i,ch in enumerate(chunks):
            m=len(ch)
            dims=dict(icon=9,h2=15,ptxt=9.5,qr=22) if n>4 else dict(icon=11,h2=17,ptxt=10.5,qr=21)
            pages.append((f"{sid}{i+1}",dict(base,title=s["title"]+(f" ({i+1}/{len(chunks)})" if len(chunks)>1 else ""),apps=[card(x,n) for x in ch],**dims)))
    else:
        pages.append((sid,dict(base,fqrs=[dict(uri=qr_data_uri(web()),label="olin.now")] if k=="free" else
          [dict(uri=qr_data_uri(web()),label="olin.now")]+[],icon=0,h2=0,ptxt=0,qr=0)))
files=[]
with sync_playwright() as pw:
    b=pw.chromium.launch(); pg=b.new_page()
    for i,(sid,ctx) in enumerate(pages,1):
        h=out/f"{i:02d}-{sid}.html"; h.write_text(tpl.render(**ctx)); pg.goto(h.as_uri()); pg.wait_for_load_state("networkidle")
        f=out/f"{i:02d}-{sid}.pdf"; pg.pdf(path=str(f),width="210mm",height="297mm",print_background=True); files.append(f)
    b.close()
w=PdfWriter()
for f in files: w.append(PdfReader(str(f)))
w.write(out/"_all.pdf"); print("OK",len(files),"listů ->",out/"_all.pdf")
