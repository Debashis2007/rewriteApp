# Azure Mock Cloud & Security Architecture (Bicep)

This repository provides a modular, best-practice Azure architecture using Bicep templates for demonstration, documentation, and as a starting point for real deployments. All modules are parameterized and mock-only (no real Azure connection required).

## Structure
- **landing-zone/**: Core setup (resource groups, management, RBAC, policy)
- **networking/**: vNet, subnets, NSGs, VPN, ExpressRoute (mock), private endpoints
- **identity/**: Entra ID (AAD), Conditional Access (mock), PIM, RBAC
- **workloads/**: IaaS (VM), PaaS (App Service, SQL), Storage, Key Vault
- **security/**: Defender, Sentinel, security policies, alerting
- **compliance/**: HITRUST/SOC 2 policy assignments, audit logs, evidence storage

## Governance, Risk, and Operations
- MSP oversight, SLAs, vendor management, and risk processes are documented here for reference.

## Usage
- All Bicep files are mock modules and can be composed for architecture demos, compliance mapping, or as a template for real deployments.
- See each module for parameters and outputs.

## Compliance & Security
- Policy and security modules are placeholders for HITRUST, SOC 2, and Zero Trust.
- Audit, evidence, and alerting modules are for demonstration only.

---

**Note:** This repo is for architecture, compliance, and security demonstration. No real Azure resources will be deployed without valid credentials and parameterization.
