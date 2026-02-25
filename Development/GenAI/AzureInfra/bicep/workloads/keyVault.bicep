// Key Vault
param location string = 'eastus'
param keyVaultName string = 'lz-keyvault'

resource kv 'Microsoft.KeyVault/vaults@2022-07-01' = {
  name: keyVaultName
  location: location
  properties: {
    sku: {
      family: 'A'
      name: 'standard'
    }
    tenantId: '00000000-0000-0000-0000-000000000000' // mock
    accessPolicies: []
    enableSoftDelete: true
    enablePurgeProtection: true
  }
}

output keyVaultName string = kv.name
