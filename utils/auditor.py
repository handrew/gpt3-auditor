import pdb
import requests

SCALE_ENDPOINTS = {
    "analyze": "https://dashboard.scale.com/spellbook/api/app/az2v3925",
    "extract_functions": "https://dashboard.scale.com/spellbook/api/app/ow3439dg",
}


class Auditor:
    def __init__(self, repo_object=None):
        if repo_object is not None:
            self.repo = repo_object
            self.repo.clone()

    def _get_spellbook(self, endpoint, authorization, input_str):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Basic {}".format(authorization)
        }
        data = {"input": input_str}

        response = requests.post(endpoint, headers=headers, json=data)
        return response

    def _extract_functions(self, code_string):
        """Hit the Spellbook endpoint to get the functions from the code."""
        endpoint = SCALE_ENDPOINTS["extract_functions"]
        return self._get_spellbook(endpoint, "cld6dojw3003vsq1a60tk2uqx", code_string)
    
    def analyze_code(self, code_string):
        """Hit Spellbook endpoint to get the auditor's analysis."""
        endpoint = SCALE_ENDPOINTS["analyze"]
        resp = self._get_spellbook(endpoint, "cld6f77o0019cv91a5bahbpig", code_string)
        return resp.json()["text"].strip()

    def create_audit_report(self, analyses_dict):
        """Create a report of the audit given a dict of analyses."""
        # Create Markdown string and add to it.
        audit_report = "# Audit Report\n"
        for file_name, analysis in analyses_dict.items():
            audit_report += "## {}\n".format(file_name)
            audit_report += analysis
            audit_report += "\n\n"
        return audit_report

    def audit(self):
        """DO IT!"""
        analyses = {}
        for file_path, content_string in self.repo.files():
            print("Analyzing: ", file_path)
            try:
                analysis = self.analyze_code(content_string).strip()
            except requests.exceptions.JSONDecodeError:
                analysis = "Error: Could not analyze this file. Was probably too long lol."
            if "SAFE!" in analysis:
                analysis = "SAFE!"
            analyses[file_path] = analysis

        audit_report = self.create_audit_report(analyses)
        print(audit_report)
        # Write audit_report to file.
        with open("audit_report.md", "w") as f:
            f.write(audit_report)
        return audit_report
