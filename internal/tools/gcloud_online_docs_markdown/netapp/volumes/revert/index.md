# gcloud netapp volumes revert  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/revert](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/revert)*

**NAME**

: **gcloud netapp volumes revert - revert a Cloud NetApp Volume back to a specified Snapshot**

**SYNOPSIS**

: **`gcloud netapp volumes revert` (`[VOLUME](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/revert#VOLUME)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/revert#--location)`=`LOCATION`) `[--snapshot](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/revert#--snapshot)`=`SNAPSHOT` [`[--async](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/revert#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/revert#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Revert a Cloud NetApp Volume back to a specified source Snapshot

**EXAMPLES**

: The following command reverts a Volume named NAME in the given location and
snapshot

```
gcloud netapp volumes revert NAME --location=us-central1 --snapshot="snapshot1"
```

**POSITIONAL ARGUMENTS**

: **Volume resource - The Volume to revert. The arguments in this group can be used
to specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `volume` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`VOLUME`**:
ID of the volume or fully qualified identifier for the volume.
To set the `volume` attribute:

- provide the argument `volume` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the volume.
To set the `location` attribute:

- provide the argument `volume` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `netapp/location`.**

**REQUIRED FLAGS**

: **Snapshot resource - The Snapshot to revert the Volume back to. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `--snapshot` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--snapshot` on the command line with a fully
specified name;
- set the property `netapp/location`.

To set the `volume` attribute:

- provide the argument `--snapshot` on the command line with a fully
specified name.

This must be specified.

**--snapshot**:
ID of the snapshot or fully qualified identifier for the snapshot.
To set the `snapshot` attribute:

- provide the argument `--snapshot` on the command line.**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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
gcloud alpha netapp volumes revert
```

```
gcloud beta netapp volumes revert
```