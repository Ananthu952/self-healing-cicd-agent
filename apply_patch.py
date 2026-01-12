from patch_generator import generate_patch

LOG_FILE = "error.log"
APP_FILE = "app.py"

def apply_patch():
    # Read error log
    with open(LOG_FILE, "r") as log:
        log_text = log.read()

    patch = generate_patch(log_text)

    if "No patch" in patch:
        print("No fix applied")
        return

    # Read app.py
    with open(APP_FILE, "r") as file:
        code = file.read()

    # Add patch at the top
    updated_code = patch + "\n\n" + code

    # Write back to app.py
    with open(APP_FILE, "w") as file:
        file.write(updated_code)

    print("Patch applied successfully!")

if __name__ == "__main__":
    apply_patch()
