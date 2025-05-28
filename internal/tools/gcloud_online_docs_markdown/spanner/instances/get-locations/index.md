# gcloud spanner instances get-locations  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/instances/get-locations](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/get-locations)*

**NAME**

: **gcloud spanner instances get-locations - get the location of every replica in a Cloud Spanner instance**

**SYNOPSIS**

: **`gcloud spanner instances get-locations` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/get-locations#INSTANCE)` [`[--verbose](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/get-locations#--verbose)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/instances/get-locations#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get the location of every replica in a Cloud Spanner instance.

**EXAMPLES**

: To get the location of every replica in a Cloud Spanner instance in this
project, run:

```
gcloud spanner instances get-locations my-instance-id
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE`**:
Cloud Spanner instance ID.

**FLAGS**

: **--verbose**:
Indicates that both regions and types of replicas be returned.

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
gcloud alpha spanner instances get-locations
```

```
gcloud beta spanner instances get-locations
```