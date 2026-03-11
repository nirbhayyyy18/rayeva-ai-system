CATEGORIES = [
"Personal Care",
"Home",
"Kitchen",
"Office",
"Stationery",
"Packaging"
]

def build_prompt(name, description):

    return f"""
You are an AI product catalog assistant for a sustainable commerce platform.

Your task is to classify the product and generate useful metadata.

Allowed primary categories:
{CATEGORIES}

Product Name: {name}

Product Description:
{description}

Tasks:
1. Select ONE primary category from the allowed list
2. Suggest the most appropriate sub-category
3. Generate 5–10 SEO tags
4. Suggest sustainability filters from the following list:

plastic-free  
compostable  
vegan  
recycled  
biodegradable  
zero-waste  
eco-friendly  

Return ONLY valid JSON.

Output format:

{{
"category": "",
"sub_category": "",
"tags": [],
"sustainability": []
}}
"""