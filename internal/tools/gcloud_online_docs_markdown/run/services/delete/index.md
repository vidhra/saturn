# gcloud run services delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/run/services/delete](https://cloud.google.com/sdk/gcloud/reference/run/services/delete)*

**NAME**

: **gcloud run services delete - delete a service**

**SYNOPSIS**

: **`gcloud run services delete` (`[SERVICE](https://cloud.google.com/sdk/gcloud/reference/run/services/delete#SERVICE)` : `[--namespace](https://cloud.google.com/sdk/gcloud/reference/run/services/delete#--namespace)`=`NAMESPACE`) [`[--[no-]async](https://cloud.google.com/sdk/gcloud/reference/run/services/delete#--[no-]async)`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/run/services/delete#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/run/services/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a service.

**EXAMPLES**

: To delete a service:

```
gcloud run services delete <service-name>
```

**POSITIONAL ARGUMENTS**

: **Service resource - Service to delete. The arguments in this group can be used to
specify the attributes of this resource.
This must be specified.

**`SERVICE`**:
ID of the service or fully qualified identifier for the service.
To set the `service` attribute:

- provide the argument `SERVICE` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--namespace**:
Specific to Cloud Run for Anthos: Kubernetes namespace for the service.
To set the `namespace` attribute:

- provide the argument `SERVICE` on the command line with a fully
specified name;
- provide the argument `--namespace` on the command line;
- set the property `run/namespace`;
- For Cloud Run on Kubernetes Engine, defaults to "default". Otherwise, defaults
to project ID.;
- provide the argument `project` on the command line;
- set the property `core/project`.**

**FLAGS**

: **--[no-]async**:
Return immediately, without waiting for the operation in progress to complete.
Defaults to --no-async. Use `--async` to enable and
`--no-async` to disable.

**--region**:
Region in which the resource can be found. Alternatively, set the property
[run/region].

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

: These variants are also available:

```
gcloud alpha run services delete
```

```
gcloud beta run services delete
```