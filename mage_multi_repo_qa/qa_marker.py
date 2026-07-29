"""Small fixture for Mage Pro multi-repository QA."""

QA_REPOSITORY = "Richardmageai/Test-repo"
QA_BRANCH = "codex/multi-repo-ui-qa-20260729"


def marker() -> str:
    return f"{QA_REPOSITORY}@{QA_BRANCH}"