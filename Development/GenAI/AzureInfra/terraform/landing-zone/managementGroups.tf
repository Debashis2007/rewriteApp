// Mock management group module
variable "mg_name" { default = "lz-mgmt-group" }
// Management group resources are not directly deployable via Terraform without permissions, so this is a placeholder
output "management_group_name" {
  value = var.mg_name
}
