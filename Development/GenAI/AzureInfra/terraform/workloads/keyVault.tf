// Key Vault
variable "location" { default = "eastus" }
variable "key_vault_name" { default = "lz-keyvault" }

resource "azurerm_key_vault" "kv" {
  name                        = var.key_vault_name
  location                    = var.location
  resource_group_name         = "<RESOURCE_GROUP_NAME>" // Replace with actual RG
  tenant_id                   = "00000000-0000-0000-0000-000000000000" // mock
  sku_name                    = "standard"
  soft_delete_enabled         = true
  purge_protection_enabled    = true
  access_policy               = []
}

output "key_vault_name" {
  value = azurerm_key_vault.kv.name
}
