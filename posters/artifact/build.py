import pathlib
H=pathlib.Path(__file__).parent
t=(H/"template.html").read_text(); d=(H/"data.json").read_text()
(H/"plakatovna.html").write_text(t.replace("__DATA__",d))
print((H/"plakatovna.html").stat().st_size//1024,"KB")
