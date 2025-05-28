# gcloud spanner instance-partitions describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/instance-partitions/describe](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-partitions/describe)*

**NAME**

: **gcloud spanner instance-partitions describe - describe a Spanner instance partition**

**SYNOPSIS**

: **`gcloud spanner instance-partitions describe` (`[INSTANCE_PARTITION](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-partitions/describe#INSTANCE_PARTITION)` : `[--instance](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-partitions/describe#--instance)`=`INSTANCE`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/instance-partitions/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a Spanner instance partition.

**EXAMPLES**

: To describe a Spanner instance partition, run:

```
gcloud spanner instance-partitions describe my-instance-partition-id --instance=my-instance-id
```

**POSITIONAL ARGUMENTS**

: **Instance partition resource - The Spanner instance partition to describe. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `instance_partition` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INSTANCE_PARTITION`**:
ID of the instance partition or fully qualified identifier for the instance
partition.
To set the `instance partition` attribute:

- provide the argument `instance_partition` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--instance**:
The Cloud Spanner instance for the instance partition.
To set the `instance` attribute:

- provide the argument `instance_partition` on the command line with a
fully specified name;
- provide the argument `--instance` on the command line;
- set the property `spanner/instance`.**

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
gcloud alpha spanner instance-partitions describe
```

```
gcloud beta spanner instance-partitions describe
```