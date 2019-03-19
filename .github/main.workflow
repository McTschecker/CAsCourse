workflow "Run Test on push" {
  on = "push"
  resolves = ["HTTP client"]
}

action "Filters for GitHub Actions" {
  uses = "actions/bin/filter@d820d56839906464fb7a57d1b4e1741cf5183efa"
  args = "branch solutions"
}

action "HTTP client" {
  uses = "swinton/httpie.action@8ab0a0e926d091e0444fcacd5eb679d2e2d4ab3d"
  needs = ["Filters for GitHub Actions"]
}

workflow "New workflow" {
  on = "push"
}
