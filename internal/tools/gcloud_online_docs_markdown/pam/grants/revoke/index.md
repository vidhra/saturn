# gcloud pam grants revoke  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pam/grants/revoke](https://cloud.google.com/sdk/gcloud/reference/pam/grants/revoke)*

**NAME**

: **gcloud pam grants revoke - revoke a Privileged Access Manager grant**

**SYNOPSIS**

: **`gcloud pam grants revoke` (`[GRANT](https://cloud.google.com/sdk/gcloud/reference/pam/grants/revoke#GRANT)` : `[--entitlement](https://cloud.google.com/sdk/gcloud/reference/pam/grants/revoke#--entitlement)`=`ENTITLEMENT` `[--folder](https://cloud.google.com/sdk/gcloud/reference/pam/grants/revoke#--folder)`=`FOLDER` `[--location](https://cloud.google.com/sdk/gcloud/reference/pam/grants/revoke#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/pam/grants/revoke#--organization)`=`ORGANIZATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/pam/grants/revoke#--async)`] [`[--reason](https://cloud.google.com/sdk/gcloud/reference/pam/grants/revoke#--reason)`=`REASON`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pam/grants/revoke#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Revoke a Privileged Access Manager (PAM) grant with a reason.

**EXAMPLES**

: The following command revokes a grant with the full name
``GRANT_NAME`` and a reason of `revoke
reason`:

```
gcloud pam grants revoke GRANT_NAME --reason="revoke reason"
```

**POSITIONAL ARGUMENTS**

: **Grant resource - Name of the grant to revoke. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `grant` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`. This resource can be one of the
following types:
[privilegedaccessmanager.projects.locations.entitlements.grants,
privilegedaccessmanager.folders.locations.entitlements.grants,
privilegedaccessmanager.organizations.locations.entitlements.grants].

This must be specified.

**`GRANT`**:
ID of the grant or fully qualified identifier for the grant.
To set the `grant` attribute:

- provide the argument `grant` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--entitlement**:
The entitlement id
To set the `entitlement` attribute:

- provide the argument `grant` on the command line with a fully
specified name;
- provide the argument `--entitlement` on the command line.

**--folder**:
The name of the folder
To set the `folder` attribute:

- provide the argument `grant` on the command line with a fully
specified name;
- provide the argument `--folder` on the command line. Must be
specified for resource of type
[privilegedaccessmanager.folders.locations.entitlements.grants].

**--location**:
The resource location
To set the `location` attribute:

- provide the argument `grant` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--organization**:
The name of the organization
To set the `organization` attribute:

- provide the argument `grant` on the command line with a fully
specified name;
- provide the argument `--organization` on the command line. Must be
specified for resource of type
[privilegedaccessmanager.organizations.locations.entitlements.grants].**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--reason**:
Reason for revoking the grant.

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
gcloud alpha pam grants revoke
```

```
gcloud beta pam grants revoke
```