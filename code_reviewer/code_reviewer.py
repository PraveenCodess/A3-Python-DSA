import ast
import os


class CodeAnalyzer(ast.NodeVisitor):
    def __init__(self):
        self.stats = {
            "function_count": 0,
            "function_complexity": {},
            "imports": set(),
            "unused_imports": set(),
            "issues": [],
        }

    def visit_FunctionDef(self, node):
        self.stats["function_count"] += 1
        complexity = self.calculate_complexity(node)
        self.stats["function_complexity"][node.name] = complexity
        if complexity > 5:
            self.stats["issues"].append(
                f"Function '{node.name}' has high complexity: {complexity}"
            )
        self.generic_visit(node)

    def visit_Import(self, node):
        for alias in node.names:
            self.stats["imports"].add(alias.name)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        if node.module:
            self.stats["imports"].add(node.module)
        self.generic_visit(node)

    def calculate_complexity(self, node):
        complexity = sum(
            isinstance(n, (ast.If, ast.For, ast.While, ast.Try)) for n in ast.walk(node)
        )
        return complexity

    def find_unused_imports(self, code):
        code_tree = ast.parse(code)
        all_names = {
            node.id for node in ast.walk(code_tree) if isinstance(node, ast.Name)
        }
        self.stats["unused_imports"] = self.stats["imports"] - all_names
        for imp in self.stats["unused_imports"]:
            self.stats["issues"].append(f"Unused import detected: '{imp}'")

    def report(self):
        return {
            "function_count": self.stats["function_count"],
            "function_complexity": self.stats["function_complexity"],
            "imports": self.stats["imports"],
            "unused_imports": self.stats["unused_imports"],
            "issues": self.stats["issues"],
        }


def analyze_code(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' not found.")
        return None

    with open(file_path, "r") as f:
        code = f.read()

    analyzer = CodeAnalyzer()
    analyzer.visit(ast.parse(code))
    analyzer.find_unused_imports(code)
    return analyzer.report()


# Optional test run when executing this file directly
if __name__ == "__main__":
    # Specify the path to the sample code file
    file_path = "c:/Users/praveen/Desktop/A3-Python+DSA/code_reviewer/sample_code.py"
    report = analyze_code(file_path)
    print(report)  # Print report to test directly
