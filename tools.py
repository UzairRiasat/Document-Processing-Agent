from openai import OpenAI
from config import OPENAI_API_KEY
import json

client = OpenAI(api_key=OPENAI_API_KEY)

EXPECTED_FIELDS = [
    "full_name", "email", "phone", "location", "professional_summary",
    "technical_skills", "work_experience", "education", "certifications",
    "projects", "languages", "interests"
]

def extractor(raw_text):
    prompt = f"""
Extract the following fields from the document as JSON: {EXPECTED_FIELDS}.
If a field is missing, use null.
Return ONLY valid JSON, no extra text.

Document:
{raw_text[:6000]}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        response_format={"type": "json_object"}
    )
    result = json.loads(response.choices[0].message.content)
    for f in EXPECTED_FIELDS:
        if f not in result:
            result[f] = None
    return result

def validator(extracted):
    missing = []
    for field, value in extracted.items():
        if value is None or value == "" or value == "null":
            missing.append(field)
    return missing

def clarifier(raw_text, missing_fields):
    if not missing_fields:
        return {}
    prompt = f"""
The following fields were missing: {missing_fields}.
Look again at the document and provide ONLY those fields in JSON.
Document:
{raw_text[:6000]}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        response_format={"type": "json_object"}
    )
    return json.loads(response.choices[0].message.content)