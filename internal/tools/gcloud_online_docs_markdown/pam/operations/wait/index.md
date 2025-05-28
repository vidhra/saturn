# gcloud pam operations wait  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pam/operations/wait](https://cloud.google.com/sdk/gcloud/reference/pam/operations/wait)*

**NAME**

: **gcloud pam operations wait - poll a Privileged Access Manager long running operation**

**SYNOPSIS**

: **`gcloud pam operations wait` (`[OPERATION](https://cloud.google.com/sdk/gcloud/reference/pam/operations/wait#OPERATION)` : `[--folder](https://cloud.google.com/sdk/gcloud/reference/pam/operations/wait#--folder)`=`FOLDER` `[--location](https://cloud.google.com/sdk/gcloud/reference/pam/operations/wait#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/pam/operations/wait#--organization)`=`ORGANIZATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pam/operations/wait#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Poll a Privileged Access Manager (PAM) long running operation until it completes
and then display its result.

**EXAMPLES**

: The following command polls an operation with the full name
``OPERATION_NAME``:

```
gcloud pam operations wait OPERATION_NAME
```

**POSITIONAL ARGUMENTS**

: **Operation resource - Name of the operation to poll. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `operation` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`. This resource can be one of the
following types: [privilegedaccessmanager.projects.locations.operations,
privilegedaccessmanager.folders.locations.operations,
privilegedaccessmanager.organizations.locations.operations].

This must be specified.

**`OPERATION`**:
ID of the operation or fully qualified identifier for the operation.
To set the `operation` attribute:

- provide the argument `operation` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--folder**:
The name of the folder
To set the `folder` attribute:

- provide the argument `operation` on the command line with a fully
specified name;
- provide the argument `--folder` on the command line. Must be
specified for resource of type
[privilegedaccessmanager.folders.locations.operations].

**--location**:
The resource location
To set the `location` attribute:

- provide the argument `operation` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--organization**:
The name of the organization
To set the `organization` attribute:

- provide the argument `operation` on the command line with a fully
specified name;
- provide the argument `--organization` on the command line. Must be
specified for resource of type
[privilegedaccessmanager.organizations.locations.operations].**

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
gcloud alpha pam operations wait
```

```
gcloud beta pam operations wait
```