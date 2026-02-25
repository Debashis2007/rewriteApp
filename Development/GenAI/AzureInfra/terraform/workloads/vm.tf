// Virtual Machine (mocked)
variable "location" { default = "eastus" }
variable "vm_name" { default = "lz-vm" }

// Placeholder for VM resource. Add azurerm_linux_virtual_machine or azurerm_windows_virtual_machine as needed.
output "vm_name" {
  value = var.vm_name
}
