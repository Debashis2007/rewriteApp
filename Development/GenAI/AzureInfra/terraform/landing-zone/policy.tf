// Policy assignment module
variable "policy_definition_id" {}
variable "assignment_name" {}
variable "scope" {}

resource "azurerm_policy_assignment" "policy_assignment" {
  name                 = var.assignment_name
  policy_definition_id = var.policy_definition_id
  scope                = var.scope
}
