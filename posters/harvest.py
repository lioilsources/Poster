"""Sklidí olin.now: názvy, taglines, ikony, logo, mobilní screenshoty, store odkazy -> apps.json + assets/<slug>/"""
import re, json, urllib.request, urllib.parse, pathlib, io, html
from PIL import Image
B="https://olin.now/"; R=pathlib.Path(__file__).parent
def get(u):
    return urllib.request.urlopen(urllib.request.Request(B+urllib.parse.quote(u,safe="/:?=&%"),headers={"User-Agent":"poster-harvest"}),timeout=30).read()
idx=get("index.html").decode()
cards=re.findall(r'<a class="app-card" href="([^"]+)\.html">\s*<div class="icon"><img src="([^"]+)" alt="([^"]*)">.*?<p class="tagline">(.*?)</p>',idx,re.S)
(R/"assets").mkdir(exist_ok=True); (R/"badges").mkdir(exist_ok=True)
open(R/"assets/logo.png","wb").write(get("assets/img/ananas-bananas-logo.png"))
apps=[]
for slug,icon,name,tag in cards:
    d=R/"assets"/slug; d.mkdir(exist_ok=True)
    try: open(d/"icon.png","wb").write(get(icon))
    except Exception as e: print("icon",slug,e)
    page=get(slug+".html").decode()
    shots=re.findall(r'src="(screenshots/[^"]+/mobile/[^"]+\.(?:webp|png|jpg))"',page)
    shots=list(dict.fromkeys(shots))
    saved=[]
    for i,s in enumerate(shots[:10]):
        try:
            im=Image.open(io.BytesIO(get(s))).convert("RGB"); fn=f"shot{i+1}-"+pathlib.Path(s).stem+".png"; im.save(d/fn); saved.append(fn)
        except Exception as e: print("shot",s,e)
    ios=re.findall(r'href="(https://apps\.apple\.com[^"]+)"',page); gp=re.findall(r'href="(https://play\.google\.com[^"]+)"',page)
    mark=re.findall(r'class="badge[^"]*">([^<]+)<',page)
    apps.append(dict(slug=slug,name=html.unescape(name),tagline=html.unescape(tag.strip()),shots=saved,
        ios=ios[0] if ios else None,android=gp[0] if gp else None,page=B+slug+".html"))
    print(slug,len(saved),bool(ios),bool(gp))
json.dump(apps,open(R/"harvest.json","w"),ensure_ascii=False,indent=1)
