# gcloud run domain-mappings describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/run/domain-mappings/describe](https://cloud.google.com/sdk/gcloud/reference/run/domain-mappings/describe)*

**NAME**

: **gcloud run domain-mappings describe - describe domain mappings for Cloud Run for Anthos**

**SYNOPSIS**

: **`gcloud run domain-mappings describe` (`[--domain](https://cloud.google.com/sdk/gcloud/reference/run/domain-mappings/describe#--domain)`=`DOMAIN` : `[--namespace](https://cloud.google.com/sdk/gcloud/reference/run/domain-mappings/describe#--namespace)`=`NAMESPACE`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/run/domain-mappings/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe domain mappings for Cloud Run for Anthos.
For domain mapping support with fully managed Cloud Run, use `[gcloud beta run
domain-mappings describe](https://cloud.google.com/sdk/gcloud/reference/beta/run/domain-mappings/describe)`.

**EXAMPLES**

: To describe a Cloud Run domain mapping, run:

```
gcloud run domain-mappings describe --domain=www.example.com
```

**REQUIRED FLAGS**

: **--domain**

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
gcloud alpha run domain-mappings describe
```

```
gcloud beta run domain-mappings describe
```