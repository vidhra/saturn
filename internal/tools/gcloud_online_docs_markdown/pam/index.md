# gcloud pam  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pam](https://cloud.google.com/sdk/gcloud/reference/pam)*

**NAME**

: **gcloud pam - manage Privileged Access Manager entitlements and grants**

**SYNOPSIS**

: **`gcloud pam` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/pam#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/pam#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pam#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The `gcloud pam` command group lets you manage Privileged Access
Manager (PAM) entitlements and grants.

**EXAMPLES**

: To check the PAM onboarding status for a project named
`sample-project` and in location `global`, run:

```
gcloud pam check-onboarding-status --project=sample-project --location=global
```

To check the PAM onboarding status for a folder with ID
``FOLDER_ID`` and in location
`global`, run:

```
gcloud pam check-onboarding-status --folder=FOLDER_ID --location=global
```

To check the PAM onboarding status for an organization with ID
``ORGANIZATION_ID`` and in location
`global`, run:

```
gcloud pam check-onboarding-status --organization=ORGANIZATION_ID --location=global
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[entitlements](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements)`**:
Manage Privileged Access Manager (PAM) entitlements.

**`[grants](https://cloud.google.com/sdk/gcloud/reference/pam/grants)`**:
Manage Privileged Access Manager (PAM) grants.

**`[operations](https://cloud.google.com/sdk/gcloud/reference/pam/operations)`**:
Manage Privileged Access Manager (PAM) Long Running Operations.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[check-onboarding-status](https://cloud.google.com/sdk/gcloud/reference/pam/check-onboarding-status)`**:
Check Privileged Access Manager (PAM) onboarding status for a resource.

**NOTES**

: These variants are also available:

```
gcloud alpha pam
```

```
gcloud beta pam
```