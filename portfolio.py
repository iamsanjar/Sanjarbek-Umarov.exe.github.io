#!/usr/bin/env python3
"""
SANJARBEK.EXE — interactive terminal portfolio
Run:  python3 portfolio.py
No external dependencies required (standard library only).
"""

import sys
import time
import shutil
import random

# ---------------------------------------------------------------- colors ---
class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"
    ITALIC  = "\033[3m"
    GREEN   = "\033[38;5;121m"
    GREEN2  = "\033[38;5;42m"
    AMBER   = "\033[38;5;215m"
    FAINT   = "\033[38;5;65m"
    WHITE   = "\033[38;5;253m"
    RED     = "\033[38;5;203m"

def supports_color():
    return sys.stdout.isatty()

USE_COLOR = supports_color()

def c(text, color):
    if not USE_COLOR:
        return text
    return f"{color}{text}{C.RESET}"

# ------------------------------------------------------------- effects ---
def typewriter(text, delay=0.014, color=None, end="\n"):
    for ch in text:
        out = c(ch, color) if color else ch
        sys.stdout.write(out)
        sys.stdout.flush()
        time.sleep(delay if ch != " " else delay / 3)
    sys.stdout.write(end)
    sys.stdout.flush()

def slow_print_block(lines, delay=0.008, color=None):
    for line in lines:
        typewriter(line, delay=delay, color=color)

def loading_bar(label, width=28, duration=0.55):
    steps = 24
    for i in range(steps + 1):
        filled = int(width * i / steps)
        bar = "█" * filled + "░" * (width - filled)
        pct = int(100 * i / steps)
        sys.stdout.write(f"\r{c(label, C.FAINT)} [{c(bar, C.GREEN2)}] {pct:3d}%")
        sys.stdout.flush()
        time.sleep(duration / steps)
    print("  " + c("[ OK ]", C.GREEN))

def rule(char="─", color=C.FAINT):
    width = shutil.get_terminal_size((80, 20)).columns
    print(c(char * min(width, 78), color))

def ascii_bar(pct, width=20):
    filled = round(width * pct / 100)
    return "█" * filled + "░" * (width - filled)

def header(title):
    print()
    rule()
    print(c(f"# {title}", C.GREEN) + c("  ", C.FAINT))
    rule()

# ------------------------------------------------------------------ data ---
BANNER = r"""
 ███████╗██╗   ██╗███╗   ███╗ █████╗ ██████╗  ██████╗ ██╗   ██╗
 ██╔════╝██║   ██║████╗ ████║██╔══██╗██╔══██╗██╔═══██╗██║   ██║
 ███████╗██║   ██║██╔████╔██║███████║██████╔╝██║   ██║██║   ██║
 ╚════██║██║   ██║██║╚██╔╝██║██╔══██║██╔══██╗██║   ██║╚██╗ ██╔╝
 ███████║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║  ██║╚██████╔╝ ╚████╔╝
 ╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝   ╚═══╝
"""

ABOUT = (
    "Motivated Economics & Data Science student with hands-on experience in "
    "Python and data analysis. Curious about solving real-world problems "
    "through data, with a growing focus on fiscal policy and taxation."
)

EXPERIENCE = [
    {
        "role": "AI Content & Data Entry Specialist",
        "org": "Ibrat Farzandlari, Tashkent, Uzbekistan",
        "date": "04/2025 - 05/2026",
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
        "date": "10/2024 - 12/2024",
        "bullets": [
            "Researched application processes for South Asian universities to guide students effectively.",
            "Delivered 2 presentations that improved student understanding of the application process.",
            "Assisted 50+ students with applications and documentation.",
            "Helped increase student acceptance rate by +20%.",
        ],
    },
]

EDUCATION = {
    "degree": "BSc Economics with Data Science",
    "org": "Westminster International University in Tashkent",
    "date": "09/2024 - exp. 05/2028",
    "bullets": [
        "Relevant courses: Quantitative Methods, Mathematics for Economics, Exploring Economics, "
        "Understanding Finance, Contemporary Issues on Global Economy, Introduction to Artificial "
        "Intelligence, Foundations of Programming, Academic English.",
        "Certificate of Foundation Studies - Upper Second-Class Honours (67%).",
        "Level 4 Economics with its pathways - 83%.",
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
    {"name": "01. project_name_here", "desc": "Swap in a real title + 1-2 lines on what it does.", "tags": ["Python", "Pandas"], "link": "github.com/your-username/repo"},
    {"name": "02. project_name_here", "desc": "Swap in a real title + 1-2 lines on what it does.", "tags": ["Power BI", "Excel"], "link": "link-to-dashboard"},
    {"name": "03. project_name_here", "desc": "Swap in a real title + 1-2 lines on what it does.", "tags": ["Statistics", "Colab"], "link": "link-to-notebook"},
    {"name": "04. project_name_here", "desc": "Swap in a real title + 1-2 lines on what it does.", "tags": ["Data Viz"], "link": "link-to-project"},
]

CERTS = [
    ("Data Science and AI - Mohirdev", "IN PROGRESS since 07/2025", False),
    ("What is Data Science? - Coursera", "DONE 06/2025", True),
    ("Business Analytics with Excel: Elementary to Advanced - Coursera", "DONE 01/2025", True),
    ("IELTS - Overall Band 6.5", "DONE 10/2023", True),
    ("Financial Markets - Coursera", "DONE 11/2023", True),
]

CONTACT = {
    "Email": "sanjarbekumarovvv@gmail.com",
    "Phone": "+998 93 613 77 11",
    "LinkedIn": "https://www.linkedin.com/in/sanjarbek-umarovv/",
    "GitHub": "add-your-username",
}

# --------------------------------------------------------------- sections ---
def boot_sequence():
    print()
    typewriter("booting profile.sys ...", delay=0.01, color=C.FAINT)
    loading_bar("loading resume.json")
    loading_bar("mounting /skills /experience /education")
    typewriter("auth: guest -- read-only session", delay=0.008, color=C.FAINT)
    time.sleep(0.2)
    print(c(BANNER, C.GREEN))
    typewriter("DATA_SCIENTIST.exe -- Umarov, Sanjarbek", delay=0.012, color=C.BOLD + C.WHITE)
    typewriter("Economics x Data Science, Westminster International University in Tashkent.",
               delay=0.006, color=C.FAINT)
    print()
    chips = ["Tashkent, UZ", "Class of 2028", "Python", "Power BI", "UZ . EN . RU"]
    print(c("  [ " + " ]  [ ".join(chips) + " ]", C.AMBER))

def cmd_about():
    header("about")
    slow_print_block([ABOUT], delay=0.006, color=C.WHITE)

def cmd_experience():
    header("experience")
    for job in EXPERIENCE:
        print(c(job["role"], C.BOLD + C.WHITE) + c(f"   [{job['date']}]", C.FAINT))
        print(c(job["org"], C.GREEN2))
        for b in job["bullets"]:
            print(c("  > ", C.FAINT) + b)
        print()

def cmd_education():
    header("education")
    print(c(EDUCATION["degree"], C.BOLD + C.WHITE) + c(f"   [{EDUCATION['date']}]", C.FAINT))
    print(c(EDUCATION["org"], C.GREEN2))
    for b in EDUCATION["bullets"]:
        print(c("  > ", C.FAINT) + b)

def cmd_skills():
    header("skills")
    print(c("Technical", C.FAINT))
    for name, pct in SKILLS:
        bar = ascii_bar(pct)
        print(f"  {name:<26}{c(bar, C.GREEN)} {c(str(pct)+'%', C.FAINT)}")
    print()
    print(c("Languages", C.FAINT))
    for lang, level in LANGUAGES:
        print(f"  {lang:<12}{c(level, C.AMBER)}")
    print()
    print(c("Soft skills", C.FAINT))
    print("  " + c(" | ".join(SOFT_SKILLS), C.WHITE))

def cmd_projects():
    header("projects")
    print(c("(placeholder slots -- edit the PROJECTS list in this script to add your own)", C.ITALIC + C.FAINT))
    print()
    for p in PROJECTS:
        print(c(p["name"], C.GREEN))
        print("  " + p["desc"])
        print("  " + c("[" + "] [".join(p["tags"]) + "]", C.AMBER))
        print("  -> " + c(p["link"], C.GREEN2))
        print()

def cmd_certifications():
    header("certifications & courses")
    for name, status, done in CERTS:
        tag = c(f"[{status}]", C.GREEN2 if done else C.AMBER)
        print(f"  {name:<62}{tag}")

def cmd_contact():
    header("connect")
    for label, value in CONTACT.items():
        print(f"  {c(label + ':', C.FAINT):<20}{c(value, C.WHITE)}")

def cmd_resume():
    cmd_about()
    cmd_experience()
    cmd_education()
    cmd_skills()
    cmd_projects()
    cmd_certifications()
    cmd_contact()
    print()
    rule()

HELP_TEXT = """
Available commands:
  whoami              about me
  cat experience.log  work experience
  ls education/       education
  cat skills.json     skills & languages
  ls projects/        projects
  cat certs.log       certifications & courses
  ./contact.sh        contact info
  resume               show everything, top to bottom
  clear                clear the screen
  help                 show this message
  exit                 quit
"""

COMMANDS = {
    "whoami": cmd_about,
    "cat experience.log": cmd_experience,
    "ls education/": cmd_education,
    "cat skills.json": cmd_skills,
    "ls projects/": cmd_projects,
    "cat certs.log": cmd_certifications,
    "./contact.sh": cmd_contact,
    "resume": cmd_resume,
}

def main():
    try:
        boot_sequence()
        print()
        typewriter("type 'help' to see available commands.", delay=0.008, color=C.FAINT)
        while True:
            try:
                raw = input(c("\nsanjarbek@tashkent", C.GREEN2) + c(":~$ ", C.FAINT))
            except EOFError:
                break
            cmd = raw.strip()
            if not cmd:
                continue
            if cmd in ("exit", "quit"):
                typewriter("connection closed.", delay=0.01, color=C.FAINT)
                break
            elif cmd == "help":
                print(c(HELP_TEXT, C.WHITE))
            elif cmd == "clear":
                print("\033c", end="")
            elif cmd in COMMANDS:
                COMMANDS[cmd]()
            else:
                print(c(f"command not found: {cmd}", C.RED) + c("  (type 'help')", C.FAINT))
    except KeyboardInterrupt:
        print()
        typewriter("interrupted. connection closed.", delay=0.01, color=C.FAINT)

if __name__ == "__main__":
    main()
