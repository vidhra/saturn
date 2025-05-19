# gcloud alpha apphub applications services delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/apphub/applications/services/delete](https://cloud.google.com/sdk/gcloud/reference/alpha/apphub/applications/services/delete)*

**NAME**

: **gcloud alpha apphub applications services delete - delete an Apphub application service**

**SYNOPSIS**

: **`gcloud alpha apphub applications services delete` (`[SERVICE](https://cloud.google.com/sdk/gcloud/reference/alpha/apphub/applications/services/delete#SERVICE)` : `[--application](https://cloud.google.com/sdk/gcloud/reference/alpha/apphub/applications/services/delete#--application)`=`APPLICATION` `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/apphub/applications/services/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/apphub/applications/services/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/apphub/applications/services/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Delete an Apphub application service.

**EXAMPLES**

: To delete the Service `my-service` from the Application
`my-app` in location `us-east1`, run:

```
gcloud alpha apphub applications services delete my-service --application=my-app --location=us-east1
```

**POSITIONAL ARGUMENTS**

: **Service resource - The Service ID. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `service` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SERVICE`**:
ID of the service or fully qualified identifier for the service.
To set the `service` attribute:

- provide the argument `service` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--application**:
Name for the application
To set the `application` attribute:

- provide the argument `service` on the command line with a fully
specified name;
- provide the argument `--application` on the command line.

**--location**:
The Cloud location for the service.
To set the `location` attribute:

- provide the argument `service` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud apphub applications services delete
```