import os
import pandas as pd
from google.adk.agents import Agent
from src.data_utils import load_hsn_data
from src.validation import is_valid_format, exists_in_data, validate_hierarchy, get_description

# Load HSN master data once
df = load_hsn_data("/home/vamsi/Desktop/settyl_assignment/data/HSN_Master_Data.csv")

# Tool 1: Validate HSN code format and hierarchy
def validate_hsn_code(input_data: str) -> dict:
    if not input_data.isdigit():
        return {
            "status": "error",
            "error_message": "Input is not a numeric HSN code.",
        }

    code = input_data.strip()
    format_ok = is_valid_format(code)
    exists = exists_in_data(code, df)
    hierarchy = validate_hierarchy(code, df)

    response = {
        "status": "success",
        "input_type": "HSN_CODE",
        "code": code,
        "format_valid": format_ok,
        "exists": exists,
        "hierarchy_validation": hierarchy,
    }

    if exists:
        response["description"] = get_description(code, df)
    else:
        response["error"] = "Code does not exist in master data"

    return response

# Tool 2: Suggest HSN codes from product description (rule-based placeholder)
def suggest_codes_from_description(description: str) -> dict:
    if description.isdigit():
        return {
            "status": "error",
            "error_message": "Input appears to be a code, not a description.",
        }

    # Simple keyword match suggestion (can be replaced by an LLM later)
    suggestions = []
    desc_lower = description.lower()
    for _, row in df.iterrows():
        if desc_lower in row["Description"].lower():
            suggestions.append({"HSNCode": row["HSNCode"], "Description": row["Description"]})
        if len(suggestions) >= 5:
            break

    return {
        "status": "success",
        "input_type": "PRODUCT_DESCRIPTION",
        "query": description,
        "suggestions": suggestions or "No matching HSN codes found.",
    }

# Construct agent
root_agent = Agent(
    name="hsn_code_agent",
    model="gemini-2.0-flash",  # or another model supported in your ADK setup
    description="Agent to validate and suggest HSN codes based on code or product description.",
    instruction="You are an HSN code expert. Use tools to validate an HSN code or suggest codes based on a product description.",
    tools=[validate_hsn_code, suggest_codes_from_description],
)
