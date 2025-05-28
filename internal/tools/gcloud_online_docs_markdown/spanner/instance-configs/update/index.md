# gcloud spanner instance-configs update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/update](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/update)*

**NAME**

: **gcloud spanner instance-configs update - update a Cloud Spanner instance configuration**

**SYNOPSIS**

: **`gcloud spanner instance-configs update` `[INSTANCE_CONFIG](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/update#INSTANCE_CONFIG)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/update#--async)`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/update#--display-name)`=`DISPLAY_NAME`] [`[--etag](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/update#--etag)`=`ETAG`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/update#--validate-only)`] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Cloud Spanner instance configuration.

**EXAMPLES**

: To update display name of a custom Cloud Spanner instance configuration
'custom-instance-config', run:

```
gcloud spanner instance-configs update custom-instance-config --display-name=nam3-RO-us-central1
```

To modify the instance config 'custom-instance-config' by adding label 'k0',
with value 'value1' and label 'k1' with value 'value2' and removing labels with
key 'k3', run:

```
gcloud spanner instance-configs update custom-instance-config --update-labels=k0=value1,k1=value2 --remove-labels=k3
```

To clear all labels of a custom Cloud Spanner instance configuration
'custom-instance-config', run:

```
gcloud spanner instance-configs update custom-instance-config --clear-labels
```

To remove an existing label of a custom Cloud Spanner instance configuration
'custom-instance-config', run:

```
gcloud spanner instance-configs update custom-instance-config --remove-labels=KEY1,KEY2
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_CONFIG`**:
Cloud Spanner instance config. The 'custom-' prefix is required to avoid name
conflicts with Google-managed configurations.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--display-name**:
The name of this instance configuration as it appears in UIs.

**--etag**:
Used for optimistic concurrency control.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--validate-only**:
Use this flag to validate that the request will succeed before executing it.

**--clear-labels**

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
gcloud alpha spanner instance-configs update
```

```
gcloud beta spanner instance-configs update
```