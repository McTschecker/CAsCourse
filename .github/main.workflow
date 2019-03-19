workflow "lint && test" {
  on = "push"
  resolves = [
    "py3.7 linting black",
    "py3.7 testing",
  ]
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
