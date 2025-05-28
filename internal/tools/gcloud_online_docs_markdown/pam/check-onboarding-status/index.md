# gcloud pam check-onboarding-status  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pam/check-onboarding-status](https://cloud.google.com/sdk/gcloud/reference/pam/check-onboarding-status)*

**NAME**

: **gcloud pam check-onboarding-status - check Privileged Access Manager onboarding status for a resource**

**SYNOPSIS**

: **`gcloud pam check-onboarding-status` (`[--location](https://cloud.google.com/sdk/gcloud/reference/pam/check-onboarding-status#--location)`=`LOCATION` : `[--folder](https://cloud.google.com/sdk/gcloud/reference/pam/check-onboarding-status#--folder)`=`FOLDER` `[--organization](https://cloud.google.com/sdk/gcloud/reference/pam/check-onboarding-status#--organization)`=`ORGANIZATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pam/check-onboarding-status#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Check Privileged Access Manager (PAM) onboarding status for a
project/organization/folder location.

**EXAMPLES**

: The following command checks the PAM onboarding status for a project named
`sample-project` and in location `global`:

```
gcloud pam check-onboarding-status --project=sample-project --location=global
```

The following command checks the PAM onboarding status for a folder with ID
``FOLDER_ID`` and in location
`global`:

```
gcloud pam check-onboarding-status --folder=FOLDER_ID --location=global
```

The following command checks the PAM onboarding status for an organization with
ID ``ORGANIZATION_ID`` and in location
`global`:

```
gcloud pam check-onboarding-status --organization=ORGANIZATION_ID --location=global
```

**REQUIRED FLAGS**

: **Location resource - The project/organization/folder location for which the
onboarding status is to be checked. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`. This resource can be one of the
following types: [privilegedaccessmanager.projects.locations,
privilegedaccessmanager.folders.locations,
privilegedaccessmanager.organizations.locations].

This must be specified.

**--location**:
ID of the location or fully qualified identifier for the location.
To set the `location` attribute:

- provide the argument `--location` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--folder**:
The name of the folder
To set the `folder` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- provide the argument `--folder` on the command line. Must be
specified for resource of type [privilegedaccessmanager.folders.locations].

**--organization**:
The name of the organization
To set the `organization` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- provide the argument `--organization` on the command line. Must be
specified for resource of type
[privilegedaccessmanager.organizations.locations].**

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--access-token-file](https://cloud.google.com/sdk/gcloud/reference#--access-token-file)`,
`[--account](https://cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://cloud.google.com/sdk/gcloud/reference#--billing-project)`,
`[--configuration](https://cloud.google.com/sdk/gcloud/reference#--configuration)`,
`[--flags-file](https://cloud.google.com/sdk/gcloud/reference#--flags-file)`,
`[--flatten](https://cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`,
`[--log-http](https://cloud.google.com/sdk/gcloud/reference#--log-http)`,
`[--project](https://cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`,
`[--verbosity](https://cloud.google.com/sdk/gcloud/reference#--verbosity)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**API REFERENCE**

: This command uses the `privilegedaccessmanager/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/iam/docs/pam-overview](https://cloud.google.com/iam/docs/pam-overview)

**NOTES**

: These variants are also available:

```
gcloud alpha pam check-onboarding-status
```

```
gcloud beta pam check-onboarding-status
```