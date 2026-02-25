// Microsoft Defender for Cloud (mock)
param enableDefender bool = true
// Defender plans are not directly deployable in Bicep for all resources, so this is a placeholder
output defenderEnabled bool = enableDefender
