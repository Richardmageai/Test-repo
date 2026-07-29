# Mage QA Overwrite Protection Test Repo

This repository is disposable test data for Mage QA.

Use branch:

```text
codex/qa-overwrite-protection-20260729
```

## Ticket 1 Test File

Use this file for stale deployment tests:

```text
qa_deploy_file.py
```

Start state:

```python
VERSION = "v1 - initial file before Mage deployment test"
```

During stale-page testing, edit it in GitHub to:

```python
VERSION = "v2 - GitHub changed after Mage page loaded"
```

## Ticket 2 Test File

Use this file for Mage editor versus external editor conflict tests:

```text
shared_conflict_file.py
```

Start state:

```python
VALUE = "original value before conflict"
```

Mage-side conflicting edit:

```python
VALUE = "Mage edit - preserve this version"
```

GitHub-side conflicting edit:

```python
VALUE = "GitHub external edit - preserve this version"
```

## Safe Test Rules

- Do not use this repo for customer data.
- Do not put secrets or real credentials in this repo.
- Use only disposable branches and files.
