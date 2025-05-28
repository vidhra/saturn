# gcloud pam grants create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pam/grants/create](https://cloud.google.com/sdk/gcloud/reference/pam/grants/create)*

**NAME**

: **gcloud pam grants create - create a new Privileged Access Manager grant**

**SYNOPSIS**

: **`gcloud pam grants create` `[--requested-duration](https://cloud.google.com/sdk/gcloud/reference/pam/grants/create#--requested-duration)`=`REQUESTED_DURATION` (`[--entitlement](https://cloud.google.com/sdk/gcloud/reference/pam/grants/create#--entitlement)`=`ENTITLEMENT` : `[--folder](https://cloud.google.com/sdk/gcloud/reference/pam/grants/create#--folder)`=`FOLDER` `[--location](https://cloud.google.com/sdk/gcloud/reference/pam/grants/create#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/pam/grants/create#--organization)`=`ORGANIZATION`) [`[--additional-email-recipients](https://cloud.google.com/sdk/gcloud/reference/pam/grants/create#--additional-email-recipients)`=[`ADDITIONAL_EMAIL_RECIPIENTS`,…]] [`[--justification](https://cloud.google.com/sdk/gcloud/reference/pam/grants/create#--justification)`=`JUSTIFICATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pam/grants/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Privileged Access Manager (PAM) grant under an entitlement.

**EXAMPLES**

: The following command creates a new grant against the entitlement with the full
name ``ENTITLEMENT_NAME``, a requested duration
of 1 hour 30 minutes, a justification of `some justification` and two
additional email recipients `abc@example.com` and
`xyz@example.com`:

```
gcloud pam grants create --entitlement=ENTITLEMENT_NAME --requested-duration=5400s --justification="some justification" --additional-email-recipients=abc@example.com,xyz@example.com
```

**REQUIRED FLAGS**

: **--requested-duration**:
Duration of the grant being created.

**Entitlement resource - Entitlement the grant is to be created against. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `--entitlement` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`. This resource can be one of the
following types: [privilegedaccessmanager.projects.locations.entitlements,
privilegedaccessmanager.folders.locations.entitlements,
privilegedaccessmanager.organizations.locations.entitlements].

This must be specified.

**--entitlement**:
ID of the entitlement or fully qualified identifier for the entitlement.
To set the `entitlement` attribute:

- provide the argument `--entitlement` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--folder**:
The name of the folder
To set the `folder` attribute:

- provide the argument `--entitlement` on the command line with a fully
specified name;
- provide the argument `--folder` on the command line. Must be
specified for resource of type
[privilegedaccessmanager.folders.locations.entitlements].

**--location**:
The resource location
To set the `location` attribute:

- provide the argument `--entitlement` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--organization**:
The name of the organization
To set the `organization` attribute:

- provide the argument `--entitlement` on the command line with a fully
specified name;
- provide the argument `--organization` on the command line. Must be
specified for resource of type
[privilegedaccessmanager.organizations.locations.entitlements].**

**OPTIONAL FLAGS**

: **--additional-email-recipients**:
Additional email addresses that are notified for all actions performed on the
grant.

**--justification**:
Justification for the grant.

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
gcloud alpha pam grants create
```

```
gcloud beta pam grants create
```