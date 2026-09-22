#!/usr/bin/env python3
"""Merge 2026 table assignments into orgs.json."""
import json
import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ORGS_PATH = ROOT / "views" / "_data" / "orgs.json"
DATA_DIR = ROOT / "data"

with ORGS_PATH.open() as f:
    existing = {o["id"]: o for o in json.load(f)}


def has_logo(org_id):
    return (DATA_DIR / org_id / "logo.png").is_file() or (DATA_DIR / org_id / "logo.jpg").is_file()


def base_org(**kwargs):
    defaults = {
        "short_name": "",
        "description": "",
        "location": "Court of Sciences",
        "website": "",
        "mailing_list": "",
        "linktree": "",
        "linkedin": "",
        "slack": "",
        "instagram": "",
        "discord": "",
        "facebook": "",
    }
    defaults.update(kwargs)
    defaults["has_logo"] = has_logo(defaults["id"])
    return defaults


# id -> (display_table, tables[], department, department_name)
ASSIGNMENTS = [
    ("esuc", "1", [1], "general", "General (All Departments)"),
    ("ea", "2", [2], "general", "General (All Departments)"),
    ("tbp", "3", [3], "general", "General (All Departments)"),
    ("swe", "4", [4], "general", "General (All Departments)"),
    ("nsbe", "5", [5], "general", "General (All Departments)"),
    ("pies", "6", [6], "general", "General (All Departments)"),
    ("soles", "7", [7], "general", "General (All Departments)"),
    ("ksea", "8", [8], "general", "General (All Departments)"),
    ("makerspace", "9", [9], "general", "General (All Departments)"),
    ("uip", "10", [10], "general", "General (All Departments)"),
    ("career_center", "11", [11], "general", "General (All Departments)"),
    ("bmes", "12", [12], "bioe", "Bioengineering"),
    ("crux", "13", [13], "bioe", "Bioengineering"),
    ("aiche", "14", [14], "chembe", "Chemical and Biomolecular Engineering"),
    ("aises", "15", [15], "mse", "Materials Science and Engineering"),
    ("mrs", "16", [16], "mse", "Materials Science and Engineering"),
    ("asce", "17", [17], "cee", "Civil and Environmental Engineering"),
    ("xe", "18", [18], "cee", "Civil and Environmental Engineering"),
    ("eeri_seaosc", "19", [19], "cee", "Civil and Environmental Engineering"),
    ("ite", "20", [20], "cee", "Civil and Environmental Engineering"),
    ("ewb", "21", [21], "cee", "Civil and Environmental Engineering"),
    ("mentorseas", "22", [22], "general", "General (All Departments)"),
    ("lug", "23", [23], "cs", "Computer Science"),
    ("exploretech", "24", [24], "cs", "Computer Science"),
    ("lahacks", "25", [25], "cs", "Computer Science"),
    ("nova", "26", [26], "cs", "Computer Science"),
    ("acm", "27–28", [27, 28], "cs", "Computer Science"),
    ("upe", "29", [29], "cs", "Computer Science"),
    ("hkn", "30", [30], "ece", "Electrical and Computer Engineering"),
    ("ieee", "31", [31], "ece", "Electrical and Computer Engineering"),
    ("ieee_watt", "32", [32], "ece", "Electrical and Computer Engineering"),
    ("barc", "33", [33], "ece", "Electrical and Computer Engineering"),
    ("qcsa", "34", [34], "ece", "Electrical and Computer Engineering"),
    ("3d4e", "35", [35], "ece", "Electrical and Computer Engineering"),
    ("bes", "36", [36], "mae", "Mechanical and Aerospace Engineering"),
    ("beam", "37", [37], "mae", "Mechanical and Aerospace Engineering"),
    ("asme", "38", [38], "mae", "Mechanical and Aerospace Engineering"),
    ("bruinspace", "39", [39], "mae", "Mechanical and Aerospace Engineering"),
    ("bfr", "40", [40], "mae", "Mechanical and Aerospace Engineering"),
    ("smv", "41", [41], "mae", "Mechanical and Aerospace Engineering"),
    ("baja_sae", "42", [42], "mae", "Mechanical and Aerospace Engineering"),
    ("uas", "43", [43], "mae", "Mechanical and Aerospace Engineering"),
    ("dbf", "44", [44], "mae", "Mechanical and Aerospace Engineering"),
    ("rocket_project", "45", [45], "mae", "Mechanical and Aerospace Engineering"),
    ("aiaa", "46", [46], "mae", "Mechanical and Aerospace Engineering"),
]

NEW_ORGS = {
    "ea": base_org(
        id="ea",
        full_name="Engineering Ambassadors",
        short_name="EA",
        description="Engineering Ambassadors represent the UCLA Samueli School of Engineering at campus events, give tours, and help prospective and incoming students learn about life as a Bruin Engineer.",
        website="https://www.seasoasa.ucla.edu/",
        instagram="",
    ),
    "tbp": base_org(
        id="tbp",
        full_name="Tau Beta Pi",
        short_name="TBP",
        description="Tau Beta Pi is the engineering honor society at UCLA. We recognize academic excellence and host professional development, service, and community events for engineers across all majors.",
        website="https://tbp.seas.ucla.edu/",
        instagram="tbp.ucla",
    ),
    "swe": base_org(
        id="swe",
        full_name="Society of Women Engineers",
        short_name="SWE",
        description="Join SWE-UCLA for professional development in STEM, scholarship opportunities, networking, and community outreach. We welcome undergraduate students of all years, backgrounds, and genders!",
        website="https://uclaswe.com/",
        instagram="sweucla",
    ),
    "nsbe": base_org(
        id="nsbe",
        full_name="National Society of Black Engineers",
        short_name="NSBE",
        description="The mission of the National Society of Black Engineers is to increase the number of culturally responsible Black Engineers who excel academically, succeed professionally, and positively impact the community. We welcome undergrad and grad students of any major.",
        website="https://nsbebruins.wixsite.com/nsbe",
        instagram="uclansbe",
        facebook="https://www.facebook.com/ucla.nsbe",
    ),
    "ksea": base_org(
        id="ksea",
        full_name="Korean-American Scientists and Engineers Association",
        short_name="KSEA",
        description="KSEA at UCLA connects Korean-American students in science and engineering through professional development, community, and outreach. Students of all backgrounds interested in STEM are welcome.",
        website="",
        instagram="",
    ),
    "makerspace": base_org(
        id="makerspace",
        full_name="UCLA Engineering Makerspace",
        short_name="Makerspace",
        description="The UCLA Engineering Makerspace is a hands-on workspace with tools, equipment, and support for student projects, prototyping, and building. Stop by to learn how to get trained and start making.",
        website="https://makerspace.seas.ucla.edu/",
    ),
    "career_center": base_org(
        id="career_center",
        full_name="UCLA Career Center",
        short_name="Career Center",
        description="The UCLA Career Center helps engineering students explore internships, jobs, and graduate school. Learn about advising, career fairs, and resources to start your path as a Bruin Engineer.",
        website="https://career.ucla.edu/",
    ),
    "mentorseas": base_org(
        id="mentorseas",
        full_name="MentorSEAS",
        short_name="",
        description="MentorSEAS pairs incoming engineering students with peer mentors who can help you navigate UCLA, your major, and student life. Meet your mentor family and learn how to stay involved throughout the year.",
        website="https://mentorseas.seas.ucla.edu/",
        instagram="mentorseas",
    ),
    "aises": base_org(
        id="aises",
        full_name="American Indian Science and Engineering Society & Bearospace",
        short_name="AISES",
        description="AISES at UCLA is an outreach, professional development, and technical organization that supports Native and Indigenous students in STEM. Our rocketry team, Bearospace, competes in NASA Student Launch and First Nations Launch. Students of any major and background are welcome.",
        website="https://aisesatucla.wixsite.com/aisesucla",
        instagram="ucla_aises",
        facebook="https://www.facebook.com/uclaaises/",
    ),
    "eeri_seaosc": base_org(
        id="eeri_seaosc",
        full_name="Earthquake Engineering Research Institute and Structural Engineers Association of Southern California",
        short_name="EERI-SEAOSC",
        description="EERI-SEAOSC at UCLA inspires the next generation of earthquake and structural engineering professionals through research events, industry mentorship, office visits, and a community of students across Southern California. Open to CEE students and related fields.",
        website="",
        instagram="",
    ),
    "lug": base_org(
        id="lug",
        full_name="Linux User Group",
        short_name="LUG",
        description="The UCLA Linux User Group is a community for students interested in Linux, open source, and systems. Beginners and experienced users are welcome to workshops, installfests, and projects.",
        website="https://linux.ucla.edu/",
        instagram="",
    ),
    "lahacks": base_org(
        id="lahacks",
        full_name="LA Hacks",
        short_name="",
        description="LA Hacks is UCLA's premier hackathon, bringing students together to build projects, learn new skills, and meet others in tech. Come learn how to get involved as an organizer or hacker.",
        website="https://lahacks.com/",
        instagram="lahacks",
    ),
    "barc": base_org(
        id="barc",
        full_name="Bruin Amateur Radio Club",
        short_name="BARC",
        description="The Bruin Amateur Radio Club is UCLA's amateur radio organization. Learn about radio and communications, get licensed, and get involved in technical projects and emergency communications.",
        website="",
        instagram="",
    ),
    "qcsa": base_org(
        id="qcsa",
        full_name="Quantum Computing Student Association",
        short_name="QCSA",
        description="The Quantum Computing Student Association introduces students to quantum computing through workshops, talks, and community. No prior experience required.",
        website="",
        instagram="",
    ),
    "bes": base_org(
        id="bes",
        full_name="Bruin Earth Solutions",
        short_name="BES",
        description="Bruin Earth Solutions is a student organization focused on sustainability and environmental solutions through projects, outreach, and engineering. Open to students who want to work on climate and earth-centered work.",
        website="",
        instagram="",
    ),
}

# Split Career Center out of the old combined UIP/Career Center entry.
UIP_OVERRIDES = {
    "full_name": "Undergraduate Research & Internship Programs",
    "short_name": "URP/UIP",
    "description": "The Undergraduate Research Program and Undergraduate Internship Program help engineering students find research labs, internships, and advising so you can start building experience in your first year.",
    "website": "https://www.seasoasa.ucla.edu/uip/",
}

NOVA_OVERRIDES = {
    "full_name": "Nova for Good",
    "short_name": "Nova",
}

IEEE_WATT_OVERRIDES = {
    "full_name": "Women Advancing Technology through Teamwork",
    "short_name": "IEEE WATT",
}

ACM_OVERRIDES = {
    "full_name": "Association for Computing Machinery",
    "short_name": "ACM",
}

BEAM_OVERRIDES = {
    "full_name": "Bruins Encouraging Active Minds",
    "short_name": "BEAM",
}

BFR_OVERRIDES = {
    "full_name": "Bruin Racing - Formula",
    "short_name": "BFR",
}

SMV_OVERRIDES = {
    "full_name": "Bruin Racing - Supermileage",
    "short_name": "SMV",
}

BAJA_OVERRIDES = {
    "full_name": "Bruin Racing - Baja",
    "short_name": "Baja SAE",
}

UAS_OVERRIDES = {
    "full_name": "American Institute of Aeronautics and Astronautics - Uncrewed Aerial Systems",
    "short_name": "UAS@UCLA",
}

DBF_OVERRIDES = {
    "full_name": "American Institute of Aeronautics and Astronautics – Design Build Fly",
    "short_name": "DBF",
}

ROCKET_OVERRIDES = {
    "full_name": "American Institute of Aeronautics and Astronautics – Rocket Project",
    "short_name": "",
}

AIAA_OVERRIDES = {
    "full_name": "American Institute of Aeronautics and Astronautics",
    "short_name": "",
}

result = []
for org_id, table, tables, dept, dept_name in ASSIGNMENTS:
    if org_id in existing:
        org = dict(existing[org_id])
    elif org_id in NEW_ORGS:
        org = dict(NEW_ORGS[org_id])
    else:
        raise SystemExit(f"Missing org definition: {org_id}")

    if org_id == "uip":
        org.update(UIP_OVERRIDES)
    elif org_id == "nova":
        org.update(NOVA_OVERRIDES)
    elif org_id == "ieee_watt":
        org.update(IEEE_WATT_OVERRIDES)
    elif org_id == "acm":
        org.update(ACM_OVERRIDES)
    elif org_id == "beam":
        org.update(BEAM_OVERRIDES)
    elif org_id == "bfr":
        org.update(BFR_OVERRIDES)
    elif org_id == "smv":
        org.update(SMV_OVERRIDES)
    elif org_id == "baja_sae":
        org.update(BAJA_OVERRIDES)
    elif org_id == "uas":
        org.update(UAS_OVERRIDES)
    elif org_id == "dbf":
        org.update(DBF_OVERRIDES)
    elif org_id == "rocket_project":
        org.update(ROCKET_OVERRIDES)
    elif org_id == "aiaa":
        org.update(AIAA_OVERRIDES)

    org["table"] = table
    org["tables"] = tables
    org["department"] = dept
    org["department_name"] = dept_name
    org["has_logo"] = has_logo(org_id)
    org["location"] = "Court of Sciences"
    result.append(org)

ORGS_PATH.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
print(f"Wrote {len(result)} orgs to {ORGS_PATH}")
for org in result:
    print(f"  {org['table']:>6}  {org['id']:16}  {org['department']:8}  {org['full_name']}")
