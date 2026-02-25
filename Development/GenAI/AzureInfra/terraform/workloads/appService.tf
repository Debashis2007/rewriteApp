// App Service (mocked)
variable "location" { default = "eastus" }
variable "app_service_name" { default = "lz-appservice" }

// Placeholder for App Service resource. Add azurerm_app_service and azurerm_app_service_plan as needed.
output "app_service_name" {
  value = var.app_service_name
}
