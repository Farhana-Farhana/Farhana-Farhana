import os
from urllib.parse import quote
from PIL import Image, ImageOps   # pip install pillow

W, H = 1200, 900
OUT = "cert_cards"
os.makedirs(OUT, exist_ok=True)

# (image file, title, subtitle)
certs = [
    ("ISRO.png", "Bharatiya Antariksh Hackathon 2026", "ISRO & Hack2Skill"),
    ("FOSSEE.png", "FOSSEE Summer Fellowship 2026", "FOSSEE, IIT Bombay"),
    ("antenna.png", "METIX RF Antenna Design Contest 2026", "METIX RF"),
    ("be10x.jpg", "AI Tools & ChatGPT Workshop", "be10x · June 2026"),
    ("NIELIT.png", "Online Internship in Embedded C", "NIELIT Virtual Academy · 6 Weeks"),
    ("THIRANEX.png", "C++ Programming Internship", "Thiranex · May–June 2026"),
    ("START.jpg", "START Programme", "ISRO"),
    ("Certificates/esim-FOSSEE.jpg", "eSim Research Migration Project", "FOSSEE, IIT Bombay"),
    ("Certificates/nptel-semiconductor.jpg", "Semiconductor Devices", "NPTEL Elite"),
    ("Certificates/stm32-workshop.jpeg", "STM32 for DSP", "Workshop"),
    ("Certificates/python-infosys.jpg", "Python Programming", "Infosys Springboard"),
    ("Certificates/Matlab.jpg", "MATLAB Workshop", "IEEE EdSoc SBC NITC"),
    ("Certificates/python_bootcamp.jpg", "Python Bootcamp", "ELDII"),
    ("Certificates/java_certificate.jpg", "Java Complete Course", "Udemy"),
    ("Certificates/Data Science & Analytics.jpg", "Data Science & Analytics", "HP LIFE Foundation"),
    ("Certificates/N-S-Farhana_qnayds/N S Farhana_qnayds_page-0001.jpg", "Web Development Internship", "Qnayds LLP · 1 Week"),
    ("Certificates/N-S-Farhana_qnayds/N S Farhana_qnayds_page-0002.jpg", "Web Development Workshop", "Qnayds LLP · 2 Days"),
    ("Certificates/N-S-Farhana_qnayds/N S Farhana_qnayds_page-0003.jpg", "Web Development Quiz", "Qnayds LLP · 1 Day"),
    ("Certificates/Encamp.jpg", "ENCAMP 4.0", "Web Development"),
]

cells = []
for path, title, sub in certs:
    if not os.path.exists(path):
        print("MISSING:", path); continue
    img = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    img.thumbnail((W - 60, H - 60))                 # keep aspect ratio
    card = Image.new("RGB", (W, H), "white")
    card.paste(img, ((W - img.width) // 2, (H - img.height) // 2))
    card = ImageOps.expand(card, border=4, fill=(210, 214, 220))
    card = card.resize((W, H))
    name = os.path.splitext(os.path.basename(path))[0].replace(" ", "_") + ".jpg"
    card.save(f"{OUT}/{name}", quality=90)
    cells.append(f'''    <td align="center" valign="top" width="33%">
      <img src="{OUT}/{quote(name)}" width="360" alt="{title}"/><br/>
      <b>{title.replace("&", "&amp;")}</b><br/>
      <sub>{sub.replace("&", "&amp;")}</sub>
    </td>''')

while len(cells) % 3:
    cells.append('    <td width="33%"></td>')

rows = ["  <tr>\n" + "\n".join(cells[i:i+3]) + "\n  </tr>" for i in range(0, len(cells), 3)]
html = '<div align="center">\n<table>\n' + "\n".join(rows) + "\n</table>\n</div>\n"
open("certifications_section.md", "w", encoding="utf-8").write(html)
print("Done -> certifications_section.md")
