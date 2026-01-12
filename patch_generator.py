import re

def generate_patch(log_text):
    # Extract variable name from NameError
    match = re.search(r"name '(.+?)' is not defined", log_text)

    if match:
        variable_name = match.group(1)
        patch = f"{variable_name} = 0  # Auto-generated patch"
        return patch

    return "No patch generated"


# Test
if __name__ == "__main__":
    log = "NameError: name 'undefined_variable' is not defined"
    patch = generate_patch(log)
    print("Generated Patch:")
    print(patch)
