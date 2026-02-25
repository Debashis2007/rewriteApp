// Mock management group module
param mgName string = 'lz-mgmt-group'
// Management group resources are not directly deployable via Bicep without permissions, so this is a placeholder
output managementGroupName string = mgName
