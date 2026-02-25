// Core resource group module
variable "location" { default = "eastus" }
variable "rg_name" { default = "lz-core-rg" }

resource "azurerm_resource_group" "core_rg" {
  name     = var.rg_name
  location = var.location
}

output "resource_group_name" {
  value = azurerm_resource_group.core_rg.name
}
