# gcloud compute ssl-certificates describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/describe](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/describe)*

**NAME**

: **gcloud compute ssl-certificates describe - describe a Compute Engine SSL certificate**

**SYNOPSIS**

: **`gcloud compute ssl-certificates describe` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/describe#NAME)` [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/describe#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/describe#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute ssl-certificates describe` displays all data (except
private keys) associated with Compute Engine SSL certificate resources in a
project.

**EXAMPLES**

: To display a description of a certificate 'my-cert', run:

```
gcloud compute ssl-certificates describe my-cert
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the SSL certificate to describe.

**FLAGS**

: **--global**

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
gcloud alpha compute ssl-certificates describe
```

```
gcloud beta compute ssl-certificates describe
```