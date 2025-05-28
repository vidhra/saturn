# gcloud run domain-mappings delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/run/domain-mappings/delete](https://cloud.google.com/sdk/gcloud/reference/run/domain-mappings/delete)*

**NAME**

: **gcloud run domain-mappings delete - delete domain mappings for Cloud Run for Anthos**

**SYNOPSIS**

: **`gcloud run domain-mappings delete` (`[--domain](https://cloud.google.com/sdk/gcloud/reference/run/domain-mappings/delete#--domain)`=`DOMAIN` : `[--namespace](https://cloud.google.com/sdk/gcloud/reference/run/domain-mappings/delete#--namespace)`=`NAMESPACE`) [`[--[no-]async](https://cloud.google.com/sdk/gcloud/reference/run/domain-mappings/delete#--[no-]async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/run/domain-mappings/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete domain mappings for Cloud Run for Anthos.
For domain mapping support with fully managed Cloud Run, use `[gcloud beta run
domain-mappings delete](https://cloud.google.com/sdk/gcloud/reference/beta/run/domain-mappings/delete)`.

**EXAMPLES**

: To delete a Cloud Run domain mapping, run:

```
gcloud run domain-mappings delete --domain=www.example.com
```

**REQUIRED FLAGS**

: **--domain**

**OPTIONAL FLAGS**

: **--[no-]async**:
Return immediately, without waiting for the operation in progress to complete.
Defaults to --no-async. Use `--async` to enable and
`--no-async` to disable.

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
gcloud alpha run domain-mappings delete
```

```
gcloud beta run domain-mappings delete
```