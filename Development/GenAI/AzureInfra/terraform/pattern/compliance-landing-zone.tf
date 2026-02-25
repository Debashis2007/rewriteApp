// Compliance Landing Zone Pattern
// This pattern combines policy assignment, audit logging, and evidence storage for a compliant Azure landing zone.

variable "location" { default = "eastus" }
variable "policy_definition_id" {}
variable "assignment_name" { default = "compliance-policy" }

resource "azurerm_resource_group" "compliance_rg" {
  name     = "compliance-rg"
  location = var.location
}

resource "azurerm_policy_assignment" "compliance_policy" {
  name                 = var.assignment_name
  policy_definition_id = var.policy_definition_id
  scope                = azurerm_resource_group.compliance_rg.id
}

// Placeholder for audit logs and evidence storage resources
// Add azurerm_storage_account or other resources as needed
