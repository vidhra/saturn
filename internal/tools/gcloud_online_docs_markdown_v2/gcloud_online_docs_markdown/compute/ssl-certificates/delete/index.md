# gcloud compute ssl-certificates delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/delete](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/delete)*

**NAME**

: **gcloud compute ssl-certificates delete - delete Compute Engine SSL certificates**

**SYNOPSIS**

: **`gcloud compute ssl-certificates delete` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/delete#NAME)` [`[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/delete#NAME)` …] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/delete#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/delete#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/ssl-certificates/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute ssl-certificates delete` deletes one or more Compute
Engine SSL certificate resources. SSL certificates can only be deleted when no
other resources (for example, target HTTPS proxies) refer to them.

**EXAMPLES**

: To delete a certificate resource 'my-cert', run:

```
gcloud compute ssl-certificates delete my-cert
```

To delete certificate resources 'my-cert1', 'my-cert2' and 'my-cert3', run:

```
gcloud compute ssl-certificates delete my-cert1 my-cert2 my-cert3
```

**POSITIONAL ARGUMENTS**

: **`NAME` [`NAME` …]**:
Names of the SSL certificates to delete.

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
gcloud alpha compute ssl-certificates delete
```

```
gcloud beta compute ssl-certificates delete
```