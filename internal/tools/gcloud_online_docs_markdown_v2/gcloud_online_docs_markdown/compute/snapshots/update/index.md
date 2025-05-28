# gcloud compute snapshots update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/update](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/update)*

**NAME**

: **gcloud compute snapshots update - update a Compute Engine snapshot**

**SYNOPSIS**

: **`gcloud compute snapshots update` `[SNAPSHOT_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/update#SNAPSHOT_NAME)` [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/snapshots/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute snapshots update` updates labels for a Compute Engine
snapshot.

**EXAMPLES**

: To update labels ``k0`` and
``k1`` and remove labels with key
``k3``, run:

```
gcloud compute snapshots update example-snapshot --update-labels=k0=value1,k1=value2 --remove-labels=k3
```

```
`_k0_` and `_k1_` will be added as new labels if not already present.
```

Labels can be used to identify the snapshot and to filter them like:

```
gcloud compute snapshots list --filter='labels.k1:value2'
```

To list only the labels when describing a resource, use --format:

```
gcloud compute snapshots describe example-snapshot --format="default(labels)"
```

**POSITIONAL ARGUMENTS**

: **`SNAPSHOT_NAME`**:
Name of the snapshot to update.

**FLAGS**

: **--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

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
gcloud alpha compute snapshots update
```

```
gcloud beta compute snapshots update
```