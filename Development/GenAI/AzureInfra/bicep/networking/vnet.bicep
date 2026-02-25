// Virtual Network with subnets
param location string = 'eastus'
param vnetName string = 'lz-vnet'
param addressPrefix string = '10.10.0.0/16'
param subnetPrefixes array = [
  '10.10.1.0/24'
  '10.10.2.0/24'
]

resource vnet 'Microsoft.Network/virtualNetworks@2021-05-01' = {
  name: vnetName
  location: location
  properties: {
    addressSpace: {
      addressPrefixes: [addressPrefix]
    }
    subnets: [for (prefix, i) in subnetPrefixes: {
      name: 'subnet${i+1}'
      properties: {
        addressPrefix: prefix
      }
    }]
  }
}

output vnetName string = vnet.name
