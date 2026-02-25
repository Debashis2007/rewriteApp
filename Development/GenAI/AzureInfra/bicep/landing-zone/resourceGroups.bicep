// Core resource group module
param location string = 'eastus'
param rgName string = 'lz-core-rg'

resource coreRg 'Microsoft.Resources/resourceGroups@2021-04-01' = {
  name: rgName
  location: location
}

output resourceGroupName string = coreRg.name
