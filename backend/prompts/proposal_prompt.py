def build_prompt(budget, event, audience):

    return f"""
Return ONLY JSON.

Create a sustainable gifting proposal.

Budget: {budget}

Event: {event}

Audience: {audience}

Return JSON format:

{{
"products":[{{"name":"","quantity":0,"cost":0}}],
"total_cost":0,
"impact_summary":""
}}
"""