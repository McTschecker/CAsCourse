workflow "Run Test on push" {
  on = "push"
  resolves = ["new-action"]
  resolves = [
    "py3.7 testing",
  ]
}

action "Filters for GitHub Actions" {
  uses = "actions/bin/filter@d820d56839906464fb7a57d1b4e1741cf5183efa"
  args = "branch solutions"
}

action "Python Syntax Checker" {
  uses = "cclauss/Find-Python-syntax-errors-action@master"
}

action "action" {
  uses = "andymckay/pycodestyle-action@master"
}
action "py3.7 testing" {
  uses = "docker://gr1n/the-python-action:master"
  args = "poetry install && poetry run pytest"
  env = {
    PYTHON_VERSION = "3.7.2"
  }
}
