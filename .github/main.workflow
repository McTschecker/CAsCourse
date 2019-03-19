workflow "Run Test on push" {
  on = "push"
}

action "Filters for GitHub Actions" {
  uses = "actions/bin/filter@d820d56839906464fb7a57d1b4e1741cf5183efa"
  args = "branch solutions"
}

action "Python Syntax Checker" {
  uses = "cclauss/Find-Python-syntax-errors-action@master"
}
