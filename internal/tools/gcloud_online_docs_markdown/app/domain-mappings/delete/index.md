# gcloud app domain-mappings delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/domain-mappings/delete](https://cloud.google.com/sdk/gcloud/reference/app/domain-mappings/delete)*

**NAME**

: **gcloud app domain-mappings delete - deletes a specified domain mapping**

**SYNOPSIS**

: **`gcloud app domain-mappings delete` `[DOMAIN](https://cloud.google.com/sdk/gcloud/reference/app/domain-mappings/delete#DOMAIN)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/domain-mappings/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Deletes a specified domain mapping.

**EXAMPLES**

: To delete an App Engine domain mapping, run:

```
gcloud app domain-mappings delete '*.example.com'
```

**POSITIONAL ARGUMENTS**

: **`DOMAIN`**:
A valid domain which may begin with a wildcard, such as:
`example.com` or `*.example.com`

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
gcloud alpha app domain-mappings delete
```

```
gcloud beta app domain-mappings delete
```