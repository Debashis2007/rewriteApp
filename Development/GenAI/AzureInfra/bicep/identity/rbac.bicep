// RBAC assignment module (reuse from landing-zone/rbac.bicep)
// This file can import or reference the core RBAC module
module coreRbac '../landing-zone/rbac.bicep' = {
  name: 'coreRbac'
  params: {
    principalId: '00000000-0000-0000-0000-000000000000'
    scope: '/subscriptions/00000000-0000-0000-0000-000000000000'
  }
}
