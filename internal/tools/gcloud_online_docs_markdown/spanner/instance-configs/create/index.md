# gcloud spanner instance-configs create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/create](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/create)*

**NAME**

: **gcloud spanner instance-configs create - create a Cloud Spanner instance configuration**

**SYNOPSIS**

: **`gcloud spanner instance-configs create` `[INSTANCE_CONFIG](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/create#INSTANCE_CONFIG)` (`[--base-config](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/create#--base-config)`=`BASE_CONFIG` `[--replicas](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/create#--replicas)`=`location`=`LOCATION`,`type`=`TYPE`:[…]     | [`[--clone-config](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/create#--clone-config)`=`INSTANCE_CONFIG` : `[--add-replicas](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/create#--add-replicas)`=`location`=`LOCATION`,`type`=`TYPE`:[…] `[--skip-replicas](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/create#--skip-replicas)`=`location`=`LOCATION`,`type`=`TYPE`:[…]]) [`[--async](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/create#--async)`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/create#--display-name)`=`DISPLAY_NAME`] [`[--etag](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/create#--etag)`=`ETAG`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/create#--validate-only)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-configs/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Cloud Spanner instance configuration.

**EXAMPLES**

: To create a custom Cloud Spanner instance configuration based on an existing
Google-managed configuration (`nam3`) by adding a
`READ_ONLY` type replica in location `us-east4`, run:

```
gcloud spanner instance-configs create custom-instance-config --clone-config=nam3 --add-replicas=location=us-east4,type=READ_ONLY
```

To create a custom Cloud Spanner instance configuration based on another custom
configuration (`custom-instance-config`) by adding a
`READ_ONLY` type replica in location `us-east1` and
removing a `READ_ONLY` type replica in location
`us-east4`, run:

```
gcloud spanner instance-configs create custom-instance-config1 --clone-config=custom-instance-config --add-replicas=location=us-east1,type=READ_ONLY --skip-replicas=location=us-east4,type=READ_ONLY
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE_CONFIG`**:
Cloud Spanner instance configuration. The 'custom-' prefix is required to avoid
name conflicts with Google-managed configurations.

**REQUIRED FLAGS**

: **--base-config**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--display-name**:
The name of this instance configuration as it appears in UIs. Must specify this
option if creating an instance-config with --replicas.

**--etag**:
Used for optimistic concurrency control.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--validate-only**:
If specified, validate that the creation will succeed without creating the
instance configuration.

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
gcloud alpha spanner instance-configs create
```

```
gcloud beta spanner instance-configs create
```