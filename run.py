#this code was all written with AI
import json
import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://openai.rc.asu.edu/v1",
    api_key=os.getenv("API_KEY")
)


def load_products(filename):
    with open(filename, "r") as file:
        return json.load(file)


def load_request(filename):
    with open(filename, "r") as file:
        return file.read().strip()


def build_prompt(user_request, products):
    product_text = json.dumps(products, indent=2)

    return f"""
You are a shopping recommendation system.

Your task is to recommend clothing products based ONLY on the information
provided below. Do not assume information that is not included.

Evaluate products using three categories:

1. PRICE
- The product should satisfy the user's stated budget.
- Do not recommend products above the maximum budget.

2. QUALITY
- Consider the provided material composition.
- Consider the product rating and number of reviews.
- Missing information should be treated as uncertainty.
- Do not assume that a specific material automatically guarantees quality.

3. LEGITIMACY
- Consider the provided information about the seller.
- Do not claim that a seller is definitely legitimate or a scam.
- Limited seller information should be treated as uncertainty.

Give each product a score from 1 to 5 for:
- Price
- Quality
- Legitimacy

Then recommend the three products that best match the user's request.

For each recommendation, provide:
- Product name
- Price
- Price score
- Quality score
- Legitimacy score
- Overall score
- A short explanation

Also identify products that were rejected and explain why.

USER REQUEST:
{user_request}

PRODUCTS:
{product_text}
"""


def main():
    products = load_products("products.json")
    user_request = load_request("input.txt")

    prompt = build_prompt(user_request, products)

    response = client.chat.completions.create(
        model="gpt-oss-120b",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    result = response.choices[0].message.content

    with open("output.txt", "w") as file:
        file.write(result)
    
    print("result written in output.txt")


if __name__ == "__main__":
    main()