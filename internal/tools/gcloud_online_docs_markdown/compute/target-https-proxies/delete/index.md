# gcloud compute target-https-proxies delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/delete](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/delete)*

**NAME**

: **gcloud compute target-https-proxies delete - delete target HTTPS proxies**

**SYNOPSIS**

: **`gcloud compute target-https-proxies delete` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/delete#NAME)` [`[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/delete#NAME)` …] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/delete#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/delete#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/target-https-proxies/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute target-https-proxies delete` deletes one or more
target HTTPS proxies.

**EXAMPLES**

: Delete a global target HTTPS proxy by running:

```
gcloud compute target-https-proxies delete PROXY_NAME
```

Delete a regional target HTTPS proxy by running:

```
gcloud compute target-https-proxies delete PROXY_NAME --region=REGION_NAME
```

**POSITIONAL ARGUMENTS**

: **`NAME` [`NAME` …]**:
Names of the target HTTPS proxies to delete.

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
gcloud alpha compute target-https-proxies delete
```

```
gcloud beta compute target-https-proxies delete
```