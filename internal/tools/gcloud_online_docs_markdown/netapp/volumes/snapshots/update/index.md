# gcloud netapp volumes snapshots update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/snapshots/update](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/snapshots/update)*

**NAME**

: **gcloud netapp volumes snapshots update - update a Cloud NetApp Volume Snapshot**

**SYNOPSIS**

: **`gcloud netapp volumes snapshots update` (`[SNAPSHOT](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/snapshots/update#SNAPSHOT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/snapshots/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/snapshots/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/snapshots/update#--description)`=`DESCRIPTION`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/snapshots/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--volume](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/snapshots/update#--volume)`=`VOLUME`] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/snapshots/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/snapshots/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/snapshots/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Cloud NetApp Volume Snapshot and its specified parameters.

**EXAMPLES**

: The following command updates a Snapshot named NAME and its specified
parameters:

```
gcloud netapp volumes snapshots update NAME --location=us-central1 --description="new" --update-labels=key2=val2 --volume=vol1
```

**POSITIONAL ARGUMENTS**

: **Snapshot resource - The Snapshot to update. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `snapshot` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `volume` attribute:

- provide the argument `snapshot` on the command line with a fully
specified name;
- provide the argument `--volume` on the command line.

This must be specified.

**`SNAPSHOT`**:
ID of the snapshot or fully qualified identifier for the snapshot.
To set the `snapshot` attribute:

- provide the argument `snapshot` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the snapshot.
To set the `location` attribute:

- provide the argument `snapshot` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `netapp/location`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
A description of the Cloud NetApp Snapshot

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**Volume resource - The Volume to take a Snapshot of. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `--volume` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--volume` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `netapp/location`.

**--volume**:
ID of the volume or fully qualified identifier for the volume.
To set the `volume` attribute:

- provide the argument `--volume` on the command line.**

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
gcloud alpha netapp volumes snapshots update
```

```
gcloud beta netapp volumes snapshots update
```