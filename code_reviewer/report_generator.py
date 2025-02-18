from code_reviewer import analyze_code


def display_report(file_path):
    report = analyze_code(file_path)
    if not report:
        return

    print("\nCode Review Report")
    print("=" * 50)
    print(f"Total Functions: {report['function_count']}")
    print("Function Complexity:")
    for func, complexity in report["function_complexity"].items():
        print(f"  - {func}: Complexity {complexity}")

    print("\nImports Detected:")
    print(f"  {', '.join(report['imports'])}")

    if report["unused_imports"]:
        print("\nUnused Imports:")
        for imp in report["unused_imports"]:
            print(f"  - {imp}")

    print("\nIssues Found:")
    if report["issues"]:
        for issue in report["issues"]:
            print(f"  - {issue}")
    else:
        print("  No issues detected")


# Specify the path to the sample code file
file_path = "c:/Users/praveen/Desktop/A3-Python+DSA/code_reviewer/sample_code.py"
display_report(file_path)
