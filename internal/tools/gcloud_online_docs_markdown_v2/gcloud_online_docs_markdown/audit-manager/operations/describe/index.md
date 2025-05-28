# gcloud audit-manager operations describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/audit-manager/operations/describe](https://cloud.google.com/sdk/gcloud/reference/audit-manager/operations/describe)*

**NAME**

: **gcloud audit-manager operations describe - describe Audit operation**

**SYNOPSIS**

: **`gcloud audit-manager operations describe` (`[OPERATION](https://cloud.google.com/sdk/gcloud/reference/audit-manager/operations/describe#OPERATION)` : `[--folder](https://cloud.google.com/sdk/gcloud/reference/audit-manager/operations/describe#--folder)`=`FOLDER` `[--location](https://cloud.google.com/sdk/gcloud/reference/audit-manager/operations/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/audit-manager/operations/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Obtain details about an audit operation.

**EXAMPLES**

: To describe an Audit operation in the `us-central1` region, belonging
to a project with ID `123`, with operation ID
`operation-456`, run:

```
gcloud audit-manager operations describe operation-456 --project=123 --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Operation resource - The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `operation` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`. This resource can be one of the
following types: [auditmanager.folders.locations.operationDetails,
auditmanager.projects.locations.operationDetails].

This must be specified.

**`OPERATION`**:
ID of the operation or fully qualified identifier for the operation.
To set the `operation` attribute:

- provide the argument `operation` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--folder**:
The folder for the operation.
To set the `folder` attribute:

- provide the argument `operation` on the command line with a fully
specified name;
- provide the argument `--folder` on the command line. Must be
specified for resource of type
[auditmanager.folders.locations.operationDetails].

**--location**:
The location for the operation.
To set the `location` attribute:

- provide the argument `operation` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

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

**NOTES**

: This variant is also available:

```
gcloud alpha audit-manager operations describe
```