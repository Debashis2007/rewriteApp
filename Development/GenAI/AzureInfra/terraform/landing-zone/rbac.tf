// RBAC assignment module
variable "principal_id" {}
variable "role_definition_id" { default = "b24988ac-6180-42a0-ab88-20f7382dd24c" } // Contributor
variable "scope" {}

resource "azurerm_role_assignment" "role_assignment" {
  name               = uuid()
  scope              = var.scope
  role_definition_id = var.role_definition_id
  principal_id       = var.principal_id
}
