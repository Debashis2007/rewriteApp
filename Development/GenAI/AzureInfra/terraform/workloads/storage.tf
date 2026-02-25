// Storage Account
variable "location" { default = "eastus" }
variable "storage_account_name" { default = "lzstorageacct" }

resource "azurerm_storage_account" "storage" {
  name                     = var.storage_account_name
  location                 = var.location
  resource_group_name      = "<RESOURCE_GROUP_NAME>" // Replace with actual RG
  account_tier             = "Standard"
  account_replication_type = "LRS"
  account_kind             = "StorageV2"
}

output "storage_account_name" {
  value = azurerm_storage_account.storage.name
}
