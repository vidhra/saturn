# gcloud run domain-mappings create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/run/domain-mappings/create](https://cloud.google.com/sdk/gcloud/reference/run/domain-mappings/create)*

**NAME**

: **gcloud run domain-mappings create - create domain mappings for Cloud Run for Anthos**

**SYNOPSIS**

: **`gcloud run domain-mappings create` `[--service](https://cloud.google.com/sdk/gcloud/reference/run/domain-mappings/create#--service)`=`SERVICE` (`[--domain](https://cloud.google.com/sdk/gcloud/reference/run/domain-mappings/create#--domain)`=`DOMAIN` : `[--namespace](https://cloud.google.com/sdk/gcloud/reference/run/domain-mappings/create#--namespace)`=`NAMESPACE`) [`[--force-override](https://cloud.google.com/sdk/gcloud/reference/run/domain-mappings/create#--force-override)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/run/domain-mappings/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create domain mappings for Cloud Run for Anthos.
For domain mapping support with fully managed Cloud Run, use `[gcloud beta run
domain-mappings create](https://cloud.google.com/sdk/gcloud/reference/beta/run/domain-mappings/create)`.

**EXAMPLES**

: To create a Cloud Run domain mapping, run:

```
gcloud run domain-mappings create --service=myapp --domain=www.example.com
```

**REQUIRED FLAGS**

: **--service**:
Create domain mapping for the given service.

**--domain**

**OPTIONAL FLAGS**

: **--force-override**:
Map this domain even if it is already mapped to another service.

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
gcloud alpha run domain-mappings create
```

```
gcloud beta run domain-mappings create
```