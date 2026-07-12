import time
import streamlit as st

# ------------------------------------------------------------------ config ---
st.set_page_config(
    page_title="sanjarbek@tashkent:~$",
    page_icon="🖥️",
    layout="centered",
)

# ------------------------------------------------------------------- data ---
ABOUT = (
    "Motivated Economics &amp; Data Science student with hands-on experience in "
    "<span class='hl'>Python</span> and data analysis. Curious about solving real-world "
    "problems through data, with a growing focus on <span class='hl'>fiscal policy and taxation</span>."
)

EXPERIENCE = [
    {
        "role": "AI Content & Data Entry Specialist",
        "org": "Ibrat Farzandlari, Tashkent, Uzbekistan",
        "date": "04/2025 – 05/2026",
        "bullets": [
            "Used generative AI tools to produce audio, image, and video assets for Ibrat Academy courses.",
            "Contributed to Super Start A2/Intermediate/B2, Tezkor Koreys tili A1/A2, and English for Start-ups course lines.",
            "Worked inside the Ibrat Academy app dashboard, identifying and fixing flaws and errors.",
            "Collaborated closely with a cross-functional content team.",
        ],
    },
    {
        "role": "University Admissions Counselor",
        "org": "TOP 100 UNI, Tashkent, Uzbekistan",
        "date": "10/2024 – 12/2024",
        "bullets": [
            "Researched application processes for South Asian universities to guide students effectively.",
            "Delivered 2 presentations that improved student understanding of the application process.",
            "Assisted 50+ students with applications and documentation.",
            "Helped increase student acceptance rate by <span class='stat'>+20%</span>.",
        ],
    },
]

EDUCATION = {
    "degree": "BSc Economics with Data Science",
    "org": "Westminster International University in Tashkent",
    "date": "09/2024 – exp. 05/2028",
    "bullets": [
        "Relevant courses: Quantitative Methods, Mathematics for Economics, Exploring Economics, "
        "Understanding Finance, Contemporary Issues on Global Economy, Introduction to Artificial "
        "Intelligence, Foundations of Programming, Academic English.",
        "Certificate of Foundation Studies — Upper Second-Class Honours (<span class='stat'>67%</span>).",
        "Level 4 Economics with its pathways — <span class='stat'>83%</span>.",
    ],
}

SKILLS = [
    ("Python", 78), ("Power BI", 70), ("Statistics & Probability", 75),
    ("Linear Algebra", 68), ("Google Colab/Cloud", 65), ("Excel", 80), ("GitHub", 60),
]

LANGUAGES = [
    ("Uzbek", "Native"),
    ("English", "Advanced (IELTS 6.5)"),
    ("Russian", "Elementary"),
]

SOFT_SKILLS = ["Storytelling", "Problem-solving", "Teamwork", "Curiosity", "Communication"]

PROJECTS = [
    {"name": "01. project_name_here", "desc": "Swap in a real title + 1–2 lines on what it does.", "tags": ["Python", "Pandas"], "link": "github.com/your-username/repo"},
    {"name": "02. project_name_here", "desc": "Swap in a real title + 1–2 lines on what it does.", "tags": ["Power BI", "Excel"], "link": "link-to-dashboard"},
    {"name": "03. project_name_here", "desc": "Swap in a real title + 1–2 lines on what it does.", "tags": ["Statistics", "Colab"], "link": "link-to-notebook"},
    {"name": "04. project_name_here", "desc": "Swap in a real title + 1–2 lines on what it does.", "tags": ["Data Viz"], "link": "link-to-project"},
]

CERTS = [
    ("Data Science and AI — Mohirdev", "IN PROGRESS · since 07/2025", False),
    ("What is Data Science? — Coursera", "DONE · 06/2025", True),
    ("Business Analytics with Excel: Elementary to Advanced — Coursera", "DONE · 01/2025", True),
    ("IELTS — Overall Band 6.5", "DONE · 10/2023", True),
    ("Financial Markets — Coursera", "DONE · 11/2023", True),
]

CONTACT = {
    "Email": ("sanjarbekumarovvv@gmail.com", "mailto:sanjarbekumarovvv@gmail.com"),
    "Phone": ("+998 93 613 77 11", "tel:+998936137711"),
    "LinkedIn": ("/in/sanjarbek-umarovv", "https://www.linkedin.com/in/sanjarbek-umarovv/"),
    "GitHub": ("add-your-username", "#"),
}

# --------------------------------------------------------------------- css ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;700;800&display=swap');

html, body, [class*="css"]  { font-family: 'JetBrains Mono', monospace !important; }
.stApp {
    background:
      repeating-linear-gradient(0deg, rgba(61,255,160,0.015) 0px, rgba(61,255,160,0.015) 1px, transparent 1px, transparent 3px),
      radial-gradient(ellipse at top, #0c130d 0%, #080b08 55%);
    color: #c9f2d1;
}
#MainMenu, footer, header { visibility: hidden; }

.termbox{
    background:#0d130e; border:1px solid #1c3323; border-radius:8px;
    padding:18px 22px; margin-bottom:16px;
    box-shadow:0 20px 60px -20px rgba(0,0,0,.8), 0 0 40px -12px rgba(61,255,160,.06);
}
.banner{ color:#3dffa0; font-size:9px; line-height:1.15; white-space:pre; overflow-x:auto;
         text-shadow:0 0 12px rgba(61,255,160,.25); }
.hl{ color:#ffb454; }
.stat{ color:#ffb454; font-weight:700; }
.sec-title{ color:#3dffa0; font-weight:700; font-size:13px; letter-spacing:.04em;
            border-bottom:1px solid #1c3323; padding-bottom:6px; margin-bottom:10px; text-transform:uppercase; }
.role{ color:#e8fff0; font-weight:700; font-size:14px; }
.org{ color:#25d488; font-size:13px; }
.date{ color:#5f8a6d; font-size:11.5px; float:right; }
ul.bul{ margin:6px 0 14px 18px; color:#a9d1b3; font-size:13px; }
ul.bul li{ margin-bottom:4px; }
.skillname{ display:inline-block; width:190px; color:#c9f2d1; font-size:12.5px; }
.skillbar{ color:#3dffa0; letter-spacing:-1px; font-size:13px; }
.skillpct{ color:#5f8a6d; font-size:11.5px; }
.lang-row, .cert-row{ display:flex; justify-content:space-between; font-size:12.5px;
                       padding:5px 0; border-bottom:1px dashed #1c3323; }
.proj{ border:1px solid #1c3323; border-radius:6px; padding:12px 14px; margin-bottom:10px; }
.proj-name{ color:#3dffa0; font-weight:700; font-size:13px; }
.proj-desc{ color:#a9d1b3; font-size:12px; margin:6px 0; }
.tag{ font-size:10px; color:#a97c3f; border:1px solid #2a5237; padding:2px 6px; border-radius:3px; margin-right:6px; }
.chip{ border:1px solid #2a5237; color:#a9d1b3; padding:3px 9px; border-radius:3px; font-size:11px; margin-right:6px; }
.contact-row{ font-size:13px; padding:6px 0; }
.contact-row b{ color:#5f8a6d; font-weight:400; display:inline-block; width:90px; }
a { color:#3dffa0 !important; }
.prompt-line{ color:#5f8a6d; font-size:12.5px; margin-bottom:6px; }
.prompt-line .path{ color:#25d488; }
</style>
""", unsafe_allow_html=True)

BANNER = r"""
 ███████╗██╗   ██╗███╗   ███╗ █████╗ ██████╗  ██████╗ ██╗   ██╗
 ██╔════╝██║   ██║████╗ ████║██╔══██╗██╔══██╗██╔═══██╗██║   ██║
 ███████╗██║   ██║██╔████╔██║███████║██████╔╝██║   ██║██║   ██║
 ╚════██║██║   ██║██║╚██╔╝██║██╔══██║██╔══██╗██║   ██║╚██╗ ██╔╝
 ███████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║  ██║╚██████╔╝ ╚████╔╝
 ╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝   ╚═══╝
"""

# --------------------------------------------------------------- boot fx ---
def boot_sequence():
    box = st.empty()
    lines = [
        "booting profile.sys ...",
        "loading resume.json ......... [ OK ]",
        "mounting /skills /experience /education ... [ OK ]",
        "auth: guest — read-only session",
    ]
    shown = ""
    for line in lines:
        shown += line + "\n"
        box.markdown(f"<div class='termbox'><pre class='date' style='float:none;color:#5f8a6d;font-size:12px;'>{shown}</pre></div>", unsafe_allow_html=True)
        time.sleep(0.35)
    time.sleep(0.2)
    box.empty()

# ---------------------------------------------------------------- render ---
def render_hero():
    st.markdown(f"""
    <div class="termbox">
      <pre class="banner">{BANNER}</pre>
      <div class="role">DATA_SCIENTIST.exe — Umarov, Sanjarbek</div>
      <div style="color:#5f8a6d;font-size:13px;margin-top:6px;">
        Economics × Data Science, Westminster International University in Tashkent — turning numbers into decisions.
      </div>
      <div style="margin-top:12px;">
        <span class="chip">📍 Tashkent, UZ</span>
        <span class="chip">🎓 Class of 2028</span>
        <span class="chip">🐍 Python</span>
        <span class="chip">📊 Power BI</span>
        <span class="chip">🗣 UZ · EN · RU</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

def render_about():
    st.markdown(f"""
    <div class="termbox">
      <div class="prompt-line"><span class="path">~$</span> whoami</div>
      <div class="sec-title"># about</div>
      <div style="font-size:13.5px;">{ABOUT}</div>
    </div>
    """, unsafe_allow_html=True)

def render_experience():
    rows = ""
    for job in EXPERIENCE:
        bullets = "".join(f"<li>{b}</li>" for b in job["bullets"])
        rows += f"""
        <div style="margin-bottom:16px;">
          <span class="role">{job['role']}</span><span class="date">{job['date']}</span>
          <div class="org">{job['org']}</div>
          <ul class="bul">{bullets}</ul>
        </div>"""
    st.markdown(f"""
    <div class="termbox">
      <div class="prompt-line"><span class="path">~$</span> cat experience.log</div>
      <div class="sec-title"># experience</div>
      {rows}
    </div>
    """, unsafe_allow_html=True)

def render_education():
    bullets = "".join(f"<li>{b}</li>" for b in EDUCATION["bullets"])
    st.markdown(f"""
    <div class="termbox">
      <div class="prompt-line"><span class="path">~$</span> ls -la education/</div>
      <div class="sec-title"># education</div>
      <span class="role">{EDUCATION['degree']}</span><span class="date">{EDUCATION['date']}</span>
      <div class="org">{EDUCATION['org']}</div>
      <ul class="bul">{bullets}</ul>
    </div>
    """, unsafe_allow_html=True)

def render_skills():
    bar_width = 20
    rows = ""
    for name, pct in SKILLS:
        filled = round(bar_width * pct / 100)
        bar = "█" * filled + "░" * (bar_width - filled)
        rows += f"<div><span class='skillname'>{name}</span><span class='skillbar'>{bar}</span> <span class='skillpct'>{pct}%</span></div>"
    langs = "".join(f"<div class='lang-row'><span>{l}</span><span style='color:#a97c3f;'>{v}</span></div>" for l, v in LANGUAGES)
    chips = "".join(f"<span class='chip'>{s}</span>" for s in SOFT_SKILLS)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="termbox">
          <div class="prompt-line"><span class="path">~$</span> cat skills.json</div>
          <div class="sec-title"># technical</div>
          {rows}
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="termbox">
          <div class="sec-title"># languages</div>
          {langs}
          <div class="sec-title" style="margin-top:14px;"># soft skills</div>
          {chips}
        </div>
        """, unsafe_allow_html=True)

def render_projects():
    cards = ""
    for p in PROJECTS:
        tags = "".join(f"<span class='tag'>{t}</span>" for t in p["tags"])
        cards += f"""
        <div class="proj">
          <div class="proj-name">{p['name']}</div>
          <div class="proj-desc">{p['desc']}</div>
          <div>{tags}</div>
          <div style="margin-top:8px;font-size:12px;">→ {p['link']}</div>
        </div>"""
    st.markdown(f"""
    <div class="termbox">
      <div class="prompt-line"><span class="path">~$</span> ls -la projects/</div>
      <div class="sec-title"># projects</div>
      <div style="color:#5f8a6d;font-size:11.5px;font-style:italic;margin-bottom:10px;">
        placeholder slots — edit the PROJECTS list in app.py to add your own
      </div>
      {cards}
    </div>
    """, unsafe_allow_html=True)

def render_certs():
    rows = ""
    for name, status, done in CERTS:
        color = "#25d488" if done else "#ffb454"
        rows += f"<div class='cert-row'><span>{name}</span><span style='color:{color};'>[{status}]</span></div>"
    st.markdown(f"""
    <div class="termbox">
      <div class="prompt-line"><span class="path">~$</span> cat certifications.log</div>
      <div class="sec-title"># certifications &amp; courses</div>
      {rows}
    </div>
    """, unsafe_allow_html=True)

def render_contact():
    rows = ""
    for label, (value, href) in CONTACT.items():
        rows += f"<div class='contact-row'><b>{label}</b> <a href='{href}' target='_blank'>{value}</a></div>"
    st.markdown(f"""
    <div class="termbox">
      <div class="prompt-line"><span class="path">~$</span> ./contact.sh --now</div>
      <div class="sec-title"># connect</div>
      {rows}
    </div>
    """, unsafe_allow_html=True)

# ----------------------------------------------------------------- main ---
if "booted" not in st.session_state:
    boot_sequence()
    st.session_state.booted = True

render_hero()
render_about()
render_experience()
render_education()
render_skills()
render_projects()
render_certs()
render_contact()

st.markdown(
    "<div style='text-align:center;color:#3a5943;font-size:11px;margin-top:10px;'>"
    "● process exited with code 0 — thanks for scrolling.</div>",
    unsafe_allow_html=True,
)
