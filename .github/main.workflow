workflow "lint && test" {
  on = "push"
  resolves = [
    "Filters for GitHub Actions",
    "py3.7 linting black",
    "py3.7 testing",
  
  ]
}
action "Filters for GitHub Actions" {
  uses = "actions/bin/filter@d820d56839906464fb7a57d1b4e1741cf5183efa"
  args = "branch solutions"
}
action "py3.7 linting black" {
  uses = "docker://gr1n/the-python-action:master"
  args = "tox -e py37-black"
  env = {
    PYTHON_VERSION = "3.7.2"
  }
}

action "py3.7 testing" {
  uses = "docker://gr1n/the-python-action:master"
  args = "poetry install && poetry run pytest"
  env = {
    PYTHON_VERSION = "3.7.2"
  }
}
