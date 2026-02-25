// Compliance Policy Assignments (mock)
variable "assignment_name" { default = "lz-compliance-policy" }

// Placeholder for azurerm_policy_assignment resource.
output "compliance_policy_assignment" {
  value = var.assignment_name
}
