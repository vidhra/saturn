# gcloud spanner instance-configs describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/describe](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/describe)*

**NAME**

: **gcloud spanner instance-configs describe - describe a Cloud Spanner instance configuration**

**SYNOPSIS**

: **`gcloud spanner instance-configs describe` `[INSTANCE_CONFIG](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/describe#INSTANCE_CONFIG)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a Cloud Spanner instance configuration.

**EXAMPLES**

: To describe an instance config named regional-us-central1, run:

```
gcloud spanner instance-configs describe regional-us-central1
```

To describe an instance config named nam-eur-asia1, run:

```
gcloud spanner instance-configs describe nam-eur-asia1
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_CONFIG`**:
Cloud Spanner instance config.

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
gcloud alpha spanner instance-configs describe
```

```
gcloud beta spanner instance-configs describe
```