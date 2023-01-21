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
    """Don't get wrecked."""
    repo = Repository(github_repo_link)
    auditor = Auditor(repo)
    auditor.audit()


if __name__ == "__main__":
    cli()
