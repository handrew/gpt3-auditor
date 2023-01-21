import click
from utils.auditor import Auditor
from utils.repository import Repository


@click.group()
def cli():
    """Command scripts."""
    pass


@cli.command()
@click.argument("github_repo_link")
def audit(github_repo_link):
    """Audit a GitHub repo."""
    repo = Repository(github_repo_link)
    auditor = Auditor(repo)
    auditor.audit()

@cli.command()
@click.argument("single_file")
def audit_file(single_file):
    """Audit a single file."""
    auditor = Auditor()
    # Load the single file in text and analyze it.
    with open(single_file, "r") as f:
        content = f.read()
    analysis = auditor.analyze_code(content)
    analyses = {single_file: analysis}
    audit_report = auditor.create_audit_report(analyses)
    # Write audit_report to file.
    with open("audit_report.md", "w") as f:
        f.write(audit_report)
    print(audit_report)

if __name__ == "__main__":
    cli()
