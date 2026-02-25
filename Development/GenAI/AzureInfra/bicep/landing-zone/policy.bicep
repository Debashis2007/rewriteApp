// Policy assignment module
param policyDefinitionId string
param assignmentName string
param scope string

resource policyAssignment 'Microsoft.Authorization/policyAssignments@2021-06-01' = {
  name: assignmentName
  properties: {
    policyDefinitionId: policyDefinitionId
    scope: scope
  }
}
