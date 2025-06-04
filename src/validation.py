def is_valid_format(code: str) -> bool:
    return code.isdigit() and len(code) in {2, 4, 6, 8}

def exists_in_data(code: str, df) -> bool:
    return code in set(df['HSNCode'])

def validate_hierarchy(code: str, df):
    hierarchy = [code[:i] for i in [2, 4, 6, 8] if i <= len(code)]
    valid_codes = set(df['HSNCode'])
    return {h: h in valid_codes for h in hierarchy}

def get_description(code: str, df):
    return df[df['HSNCode'] == code]['Description'].values[0]
