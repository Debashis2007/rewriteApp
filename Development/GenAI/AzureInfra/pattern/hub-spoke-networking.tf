// Hub-and-Spoke Networking Pattern
// This pattern creates a hub virtual network and two spoke virtual networks, with peering between them.

variable "location" { default = "eastus" }

resource "azurerm_virtual_network" "hub" {
  name                = "hub-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = var.location
  resource_group_name = "<RESOURCE_GROUP_NAME>"
}

resource "azurerm_virtual_network" "spoke1" {
  name                = "spoke1-vnet"
  address_space       = ["10.1.0.0/16"]
  location            = var.location
  resource_group_name = "<RESOURCE_GROUP_NAME>"
}

resource "azurerm_virtual_network" "spoke2" {
  name                = "spoke2-vnet"
  address_space       = ["10.2.0.0/16"]
  location            = var.location
  resource_group_name = "<RESOURCE_GROUP_NAME>"
}

resource "azurerm_virtual_network_peering" "hub_to_spoke1" {
  name                      = "hub-to-spoke1"
  resource_group_name       = "<RESOURCE_GROUP_NAME>"
  virtual_network_name      = azurerm_virtual_network.hub.name
  remote_virtual_network_id = azurerm_virtual_network.spoke1.id
  allow_forwarded_traffic   = true
  allow_gateway_transit     = false
}

resource "azurerm_virtual_network_peering" "hub_to_spoke2" {
  name                      = "hub-to-spoke2"
  resource_group_name       = "<RESOURCE_GROUP_NAME>"
  virtual_network_name      = azurerm_virtual_network.hub.name
  remote_virtual_network_id = azurerm_virtual_network.spoke2.id
  allow_forwarded_traffic   = true
  allow_gateway_transit     = false
}
