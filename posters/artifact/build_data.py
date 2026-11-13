"""Zabalí ikony + screenshoty z assets/ do data.json (data URI) pro artefakt."""
import json, base64, io, pathlib
from PIL import Image
R=pathlib.Path(__file__).parent.parent
H=json.load(open(R/"harvest.json")); P=json.load(open(R/"poster.json"))
def uri(im,fmt,**kw):
    b=io.BytesIO(); im.save(b,fmt,**kw); return f"data:image/{'jpeg' if fmt=='JPEG' else 'png'};base64,"+base64.b64encode(b.getvalue()).decode()
cat_of={}
for s in P["sheets"]:
    if s["kind"]=="apps" and s["id"]!="obchody":
        for sl in s["slugs"]: cat_of[sl]=s["id"]
cats={s["id"]:s["title"] for s in P["sheets"] if s["kind"]=="apps" and s["id"]!="obchody"}
# appky na Google Play bez odkazu na olin.now (ověřeno na play.google.com/store/apps/developer?id=Ol1n, 2026-11-13)
EXTRA_ANDROID={"behanek":"https://play.google.com/store/apps/details?id=com.ol1n.behanek",
 "kaceny":"https://play.google.com/store/apps/details?id=com.ol1n.kaceny",
 "webtoon":"https://play.google.com/store/apps/details?id=com.ol1n.webtoon"}
for a in H:
    if not a["android"] and a["slug"] in EXTRA_ANDROID: a["android"]=EXTRA_ANDROID[a["slug"]]
apps=[]
for a in H:
    d=R/"assets"/a["slug"]; icon=None; shots=[]
    if (d/"icon.png").exists():
        im=Image.open(d/"icon.png").convert("RGBA"); im.thumbnail((128,128)); icon=uri(im,"PNG",optimize=True)
    for f in a["shots"][:10]:
        im=Image.open(d/f).convert("RGB"); w,h=im.size; th=int(w*19.5/9)
        if h>=th: im=im.crop((0,0,w,th))
        else:
            nw=int(h*9/19.5); x=(w-nw)//2; im=im.crop((x,0,x+nw,h))
        im=im.resize((360,780),Image.LANCZOS); shots.append(uri(im,"JPEG",quality=68,optimize=True))
    apps.append(dict(slug=a["slug"],name=a["name"],tagline=a["tagline"],cat=cat_of.get(a["slug"],"ai"),ios=a["ios"],android=a["android"],page=a["page"],icon=icon,shots=shots))
lg=Image.open(R/"assets/logo.png").convert("RGBA"); lg.thumbnail((400,400))
out=dict(apps=apps,cats=cats,logo=uri(lg,"PNG",optimize=True),store=[a["slug"] for a in H if a["ios"] or a["android"]],
  devIos="https://apps.apple.com/cz/developer/olin-vorechovsky/id1896437133",
  devPlay="https://play.google.com/store/apps/developer?id=Ol1n", pt="128849798")
json.dump(out,open(pathlib.Path(__file__).parent/"data.json","w"),ensure_ascii=False,separators=(",",":"))
print(len(apps),sum(len(a["shots"]) for a in apps),pathlib.Path(__file__).parent.joinpath("data.json").stat().st_size//1024,"KB")
