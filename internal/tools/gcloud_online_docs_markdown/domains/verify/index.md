# gcloud domains verify  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/domains/verify](https://cloud.google.com/sdk/gcloud/reference/domains/verify)*

**NAME**

: **gcloud domains verify - verifies a domain via an in-browser workflow**

**SYNOPSIS**

: **`gcloud domains verify` `[DOMAIN](https://cloud.google.com/sdk/gcloud/reference/domains/verify#DOMAIN)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/domains/verify#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Verifies a domain via an in-browser workflow.

**EXAMPLES**

: To verify a domain for the current user, run:

```
gcloud domains verify example.com
```

This will allow the domain to be used with App Engine through gcloud domains app
domain-mappings and across Google Cloud products.

**POSITIONAL ARGUMENTS**

: **`DOMAIN`**:
The domain to be verified.

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
gcloud beta domains verify
```