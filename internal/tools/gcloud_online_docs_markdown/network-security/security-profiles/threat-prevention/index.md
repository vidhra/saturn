# gcloud network-security security-profiles threat-prevention  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention)*

**NAME**

: **gcloud network-security security-profiles threat-prevention - manage Security Profiles - Threat Prevention Profile**

**SYNOPSIS**

: **`gcloud network-security security-profiles threat-prevention` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Manage Security Profiles - Threat Prevention Profile.

**EXAMPLES**

: To create a Security Profile with the name `my-security-profile`
which includes location as global or region specified and organization ID,
optional description as `New Security Profile`, run:

```
gcloud network-security security-profiles threat-prevention create my-security-profile --description="New Security Profile"
```

To add an override, run:

```
gcloud network-security security-profiles threat-prevention add-override my-security-profile --severities=MEDIUM --action=ALLOW
```

```
`my-security-profile` is the name of the Security Profile in the
format organizations/{organizationID}/locations/{location}/securityProfiles/
{security_profile_id} where organizationID is the organization ID to which
the changes should apply, location either global or region specified and
security_profile_id the Security Profile Identifier.
```

To update an override, run:

```
gcloud network-security security-profiles threat-prevention update-override my-security-profile --severities=MEDIUM --action=ALLOW
```

```
`my-security-profile` is the name of the Security Profile in the
format organizations/{organizationID}/locations/{location}/securityProfiles/
{security_profile_id} where organizationID is the organization ID to which
the changes should apply, location either global or region specified and
security_profile_id the Security Profile Identifier.
```

To list overrides, run:

```
gcloud network-security security-profiles threat-prevention list-overrides my-security-profile
```

```
`my-security-profile` is the name of the Security Profile in the
format organizations/{organizationID}/locations/{location}/securityProfiles/
{security_profile_id} where organizationID is the organization ID to which
the changes should apply, location either global or region specified and
security_profile_id the Security Profile Identifier.
```

To delete an override, run:

```
gcloud network-security security-profiles threat-prevention delete-override my-security-profile --severities=MEDIUM
```

```
`my-security-profile` is the name of the Security Profile in the
format organizations/{organizationID}/locations/{location}/securityProfiles/
{security_profile_id} where organizationID is the organization ID to which
the changes should apply, location either global or region specified and
security_profile_id the Security Profile Identifier.
```

To list Security Profiles in specified location and organization, run:

```
gcloud network-security security-profiles threat-prevention list --location=global
```

To delete a Security Profile called `my-security-profile` which
includes location as global or region specified and organization ID, run:

```
gcloud network-security security-profiles threat-prevention delete my-security-profile
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[add-override](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/add-override)`**:
Add overrides to Threat Prevention Profile.

**`[create](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/create)`**:
Create a new Threat Prevention Profile.

**`[delete](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/delete)`**:
Delete a Security Profile.

**`[delete-override](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/delete-override)`**:
Delete overrides of Threat Prevention Profile.

**`[list](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/list)`**:
List Threat Prevention Security Profiles.

**`[list-overrides](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/list-overrides)`**:
List overrides of Threat Prevention Profile.

**`[update-override](https://cloud.google.com/sdk/gcloud/reference/network-security/security-profiles/threat-prevention/update-override)`**:
Update Overrides of Threat Prevention Profile.

**NOTES**

: These variants are also available:

```
gcloud alpha network-security security-profiles threat-prevention
```

```
gcloud beta network-security security-profiles threat-prevention
```