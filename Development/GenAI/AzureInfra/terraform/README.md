# Terraform Azure Infrastructure Modules

This directory contains Terraform modules that mirror the structure and intent of the original Bicep modules. Each subdirectory represents a logical area of Azure infrastructure, with `.tf` files providing either real or placeholder Terraform resources.

## Directory Structure

- **compliance/**: Modules for compliance-related resources (policy assignments, evidence storage, audit logs).
- **identity/**: Modules for identity and access management (RBAC, PIM, Entra ID, Conditional Access).
- **landing-zone/**: Core landing zone setup (resource groups, management groups, RBAC, policy assignments).
- **networking/**: Networking resources (VNet, NSG, ExpressRoute, VPN Gateway, Private Endpoint).
- **security/**: Security resources (Defender, Sentinel, Security Policy, Alerting).
- **workloads/**: Workload resources (App Service, Key Vault, SQL, Storage, VM).

## Module Overview

### compliance/
- **policyAssignments.tf**: Placeholder for compliance policy assignment (e.g., HITRUST/SOC 2).
- **evidenceStorage.tf**: Placeholder for evidence storage resource.
- **auditLogs.tf**: Placeholder for audit logs resource.

### identity/
- **rbac.tf**: Placeholder for RBAC resource.
- **pim.tf**: Placeholder for Privileged Identity Management.
- **entraId.tf**: Placeholder for Entra ID resource.
- **conditionalAccess.tf**: Placeholder for Conditional Access resource.

### landing-zone/
- **resourceGroups.tf**: Deploys a core resource group.
- **managementGroups.tf**: Placeholder for management group (not directly deployable in Terraform without permissions).
- **rbac.tf**: Assigns RBAC roles to principals.
- **policy.tf**: Assigns policies to scopes.

### networking/
- **vnet.tf**: Placeholder for Virtual Network.
- **nsg.tf**: Placeholder for Network Security Group.
- **expressRoute.tf**: Placeholder for ExpressRoute circuit.
- **vpnGateway.tf**: Placeholder for VPN Gateway.
- **privateEndpoint.tf**: Placeholder for Private Endpoint.

### security/
- **defender.tf**: Placeholder for Defender resource.
- **sentinel.tf**: Placeholder for Sentinel resource.
- **securityPolicy.tf**: Placeholder for Security Policy.
- **alerting.tf**: Placeholder for Alerting resource.

### workloads/
- **appService.tf**: Placeholder for App Service (add App Service Plan as needed).
- **keyVault.tf**: Deploys a Key Vault with basic configuration.
- **sql.tf**: Placeholder for SQL Server and Database.
- **storage.tf**: Deploys a Storage Account with basic configuration.
- **vm.tf**: Placeholder for Virtual Machine (add details as needed).

## Notes
- Placeholders indicate where you should add real Terraform resources and configuration for your use case.
- Replace `<RESOURCE_GROUP_NAME>` and other placeholders with actual values as needed.
- For production, expand each module with full resource definitions, variables, and outputs.

## Getting Started
1. Review each module and update placeholders with your actual infrastructure requirements.
2. Initialize Terraform in this directory:
   ```sh
   terraform init
   ```
3. Plan and apply your changes:
   ```sh
   terraform plan
   terraform apply
   ```

## References
- [Terraform Azure Provider Documentation](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs)
- [Azure Resource Manager Documentation](https://docs.microsoft.com/en-us/azure/azure-resource-manager/)

---

## Simple Service Descriptions

Below is a simple explanation of each service/module represented in this Terraform structure:

### compliance/
- **policyAssignments**: Assigns compliance policies (like security or audit requirements) to Azure resources.
- **evidenceStorage**: Stores files or data that prove compliance with regulations.
- **auditLogs**: Keeps records of actions and changes for security and compliance reviews.

### identity/
- **rbac**: Controls who can do what in your Azure environment (Role-Based Access Control).
- **pim**: Manages and limits privileged (high-level) access to resources.
- **entraId**: Manages user identities and access (formerly Azure Active Directory).
- **conditionalAccess**: Sets rules for when and how users can access resources (e.g., require MFA).

### landing-zone/
- **resourceGroups**: Groups related resources together for easier management.
- **managementGroups**: Organizes subscriptions into a hierarchy for governance.
- **rbac**: Assigns permissions to users or groups for specific resources.
- **policy**: Applies rules to resources to enforce standards (like naming or security).

### networking/
- **vnet**: Creates a private network in Azure for your resources.
- **nsg**: Controls network traffic to and from resources (like a firewall).
- **expressRoute**: Provides a private, dedicated connection from your on-premises network to Azure.
- **vpnGateway**: Connects your on-premises network to Azure over an encrypted VPN.
- **privateEndpoint**: Lets you securely connect to Azure services over a private network.

### security/
- **defender**: Adds advanced security protection for your Azure resources.
- **sentinel**: Provides security monitoring and threat detection (SIEM).
- **securityPolicy**: Sets security rules and standards for your environment.
- **alerting**: Notifies you about important security or operational events.

### workloads/
- **appService**: Runs web apps or APIs without managing servers.
- **keyVault**: Safely stores secrets, passwords, and encryption keys.
- **sql**: Provides managed SQL databases in Azure.
- **storage**: Stores files, blobs, and other data in the cloud.
- **vm**: Creates virtual machines (servers) in Azure.

---

This structure is designed to help you migrate from Bicep to Terraform and understand the mapping between the two IaC languages. Expand and customize as needed for your environment.
