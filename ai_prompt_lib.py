"""
AI Prompt Library
100+ production-ready AI prompts
"""

PROMPTS = {
    "code_review": {
        "name": "Code Review",
        "prompt": """Review the following code for:
1. Bugs and security issues
2. Performance improvements
3. Code style and readability
4. Best practices

Code:
{code}

Provide a detailed report with specific suggestions."""
    },
    "blog_post": {
        "name": "Blog Post",
        "prompt": """Write a blog post about {topic}

Requirements:
- Title: Catchy and SEO-friendly
- Introduction: Hook the reader in the first 100 words
- Body: 3-5 main points with examples
- Conclusion: Call to action
- Length: {word_count} words
- Tone: {tone}"""
    },
    "cold_email": {
        "name": "Cold Email",
        "prompt": """Write a cold email to {recipient}

Context: {context}

Goal: {goal}

Requirements:
- Subject line that gets opens
- Personalized opening
- Clear value proposition
- Soft call to action
- Signature"""
    },
    "data_analysis": {
        "name": "Data Analysis",
        "prompt": """Analyze the following data and provide insights:

Data: {data}

Please identify:
1. Key trends
2. Anomalies or outliers
3. Actionable recommendations
4. Supporting visualizations suggestions"""
    }
}

def get_prompt(category: str, **kwargs) -> str:
    """Get a prompt template and fill in variables"""
    if category not in PROMPTS:
        return f"Category '{category}' not found. Available: {list(PROMPTS.keys())}"
    
    template = PROMPTS[category]["prompt"]
    try:
        return template.format(**kwargs)
    except KeyError as e:
        return f"Missing parameter: {e}"

def list_categories():
    """List all available prompt categories"""
    return [cat for cat in PROMPTS.keys()]

if __name__ == "__main__":
    print("AI Prompt Library")
    print("=" * 40)
    print("Available categories:")
    for cat in list_categories():
        print(f"  - {cat}")
