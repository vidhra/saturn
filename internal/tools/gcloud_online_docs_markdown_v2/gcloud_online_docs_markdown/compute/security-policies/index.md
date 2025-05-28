# gcloud compute security-policies  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/security-policies](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies)*

**NAME**

: **gcloud compute security-policies - read and manipulate Cloud Armor security policies**

**SYNOPSIS**

: **`gcloud compute security-policies` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Read and manipulate Cloud Armor security policies.
Security policies are used to control access to Google Cloud HTTP/HTTPS load
balancers.
For more information about security policies, see [Security
policies for HTTPS load balancing](https://cloud.google.com/armor/docs/security-policy-concepts#security_policies_for_https_load_balancing).
See also: [Security
policies API](https://cloud.google.com/compute/docs/reference/rest/v1/securityPolicies).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[rules](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules)`**:
Read and manipulate Compute Engine security policies rules.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[add-layer7-ddos-defense-threshold-config](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/add-layer7-ddos-defense-threshold-config)`**:
Add a layer7 ddos defense threshold config to a Compute Engine security policy.

**`[add-user-defined-field](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/add-user-defined-field)`**:
Add a user defined field to a Compute Engine security policy.

**`[create](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/create)`**:
Create a Compute Engine security policy.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/delete)`**:
Delete security policies.

**`[describe](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/describe)`**:
Describe a Compute Engine security policy.

**`[export](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/export)`**:
Export security policy configs into YAML or JSON files.

**`[import](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/import)`**:
Import security policy configs into your project.

**`[list](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/list)`**:
List Google Compute Engine security policies.

**`[list-preconfigured-expression-sets](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/list-preconfigured-expression-sets)`**:
List all available preconfigured expression sets.

**`[remove-layer7-ddos-defense-threshold-config](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/remove-layer7-ddos-defense-threshold-config)`**:
Remove a layer7 ddos defense threshold config from a Compute Engine security
policy.

**`[remove-user-defined-field](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/remove-user-defined-field)`**:
Remove a user defined field from a Compute Engine security policy.

**`[update](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/update)`**:
Update a Compute Engine security policy.

**NOTES**

: These variants are also available:

```
gcloud alpha compute security-policies
```

```
gcloud beta compute security-policies
```