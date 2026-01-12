def identify_error(log_text):
    log_text = log_text.lower()

    if "nameerror" in log_text:
        return "NameError"
    elif "module not found" in log_text:
        return "DependencyError"
    elif "syntaxerror" in log_text:
        return "SyntaxError"
    else:
        return "UnknownError"


# Testing the module
if __name__ == "__main__":
    log = "NameError: name 'undefined_variable' is not defined"
    error_type = identify_error(log)
    print("Identified Error Type:", error_type)
