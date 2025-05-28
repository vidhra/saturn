# gcloud spanner instance-configs delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/delete](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/delete)*

**NAME**

: **gcloud spanner instance-configs delete - delete a Cloud Spanner instance configuration**

**SYNOPSIS**

: **`gcloud spanner instance-configs delete` `[INSTANCE_CONFIG](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/delete#INSTANCE_CONFIG)` [`[--etag](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/delete#--etag)`=`ETAG`] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/delete#--validate-only)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a Cloud Spanner instance configuration.

**EXAMPLES**

: To delete a custom Cloud Spanner instance configuration, run:

```
gcloud spanner instance-configs delete custom-instance-config
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_CONFIG`**:
Cloud Spanner instance config.

**FLAGS**

: **--etag**:
Used for optimistic concurrency control as a way to help prevent simultaneous
deletes of an instance config from overwriting each other.

**--validate-only**:
If specified, validate that the deletion will succeed without deleting the
instance config.

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
gcloud alpha spanner instance-configs delete
```

```
gcloud beta spanner instance-configs delete
```