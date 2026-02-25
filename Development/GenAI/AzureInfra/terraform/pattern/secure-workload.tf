// Secure Workload Pattern
// This pattern deploys a storage account, key vault, and assigns RBAC for a secure workload.

variable "location" { default = "eastus" }
variable "workload_name" { default = "secure-workload" }

resource "azurerm_resource_group" "workload_rg" {
  name     = "${var.workload_name}-rg"
  location = var.location
}

resource "azurerm_storage_account" "storage" {
  name                     = "${var.workload_name}stor"
  location                 = var.location
  resource_group_name      = azurerm_resource_group.workload_rg.name
  account_tier             = "Standard"
  account_replication_type = "LRS"
  account_kind             = "StorageV2"
}

resource "azurerm_key_vault" "kv" {
  name                        = "${var.workload_name}-kv"
  location                    = var.location
  resource_group_name         = azurerm_resource_group.workload_rg.name
  tenant_id                   = "00000000-0000-0000-0000-000000000000" // Replace with real tenant
  sku_name                    = "standard"
  soft_delete_enabled         = true
  purge_protection_enabled    = true
}

resource "azurerm_role_assignment" "storage_blob_data_contributor" {
  scope                = azurerm_storage_account.storage.id
  role_definition_name = "Storage Blob Data Contributor"
  principal_id         = "<PRINCIPAL_ID>" // Replace with actual principal
}
