# gcloud netapp volumes snapshots create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/snapshots/create](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/snapshots/create)*

**NAME**

: **gcloud netapp volumes snapshots create - create a Cloud NetApp Volume Snapshot**

**SYNOPSIS**

: **`gcloud netapp volumes snapshots create` (`[SNAPSHOT](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/snapshots/create#SNAPSHOT)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/snapshots/create#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/snapshots/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/snapshots/create#--description)`=`DESCRIPTION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/snapshots/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--volume](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/snapshots/create#--volume)`=`VOLUME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/snapshots/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Cloud NetApp Volume Snapshot.

**EXAMPLES**

: The following command creates a Snapshot named NAME using the required
arguments:

```
gcloud netapp volumes snapshots create NAME --location=us-central1 --volume=vol1
```

**POSITIONAL ARGUMENTS**

: **Snapshot resource - The Snapshot to create. The arguments in this group can be
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

**--labels**:
List of label KEY=VALUE pairs to add.
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
gcloud alpha netapp volumes snapshots create
```

```
gcloud beta netapp volumes snapshots create
```