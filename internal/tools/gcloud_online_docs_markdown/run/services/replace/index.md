# gcloud run services replace  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/run/services/replace](https://cloud.google.com/sdk/gcloud/reference/run/services/replace)*

**NAME**

: **gcloud run services replace - create or replace a service from a YAML service specification**

**SYNOPSIS**

: **`gcloud run services replace` `[FILE](https://cloud.google.com/sdk/gcloud/reference/run/services/replace#FILE)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/run/services/replace#--async)`] [`[--dry-run](https://cloud.google.com/sdk/gcloud/reference/run/services/replace#--dry-run)`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/run/services/replace#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/run/services/replace#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates or replaces a service from a YAML service specification.

**EXAMPLES**

: To replace the specification for a service defined in myservice.yaml

```
gcloud run services replace myservice.yaml
```

**POSITIONAL ARGUMENTS**

: **`FILE`**:
The absolute path to the YAML file with a Knative service definition for the
service to update or deploy.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--dry-run**:
If set to true, only validates the configuration. The configuration will not be
applied.

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
gcloud alpha run services replace
```

```
gcloud beta run services replace
```