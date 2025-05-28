# gcloud bms volumes restore  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/bms/volumes/restore](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/restore)*

**NAME**

: **gcloud bms volumes restore - restore a Bare Metal Solution boot volume from an existing snapshot**

**SYNOPSIS**

: **`gcloud bms volumes restore` (`[VOLUME](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/restore#VOLUME)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/restore#--region)`=`REGION`) `[--snapshot](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/restore#--snapshot)`=`SNAPSHOT` [`[--async](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/restore#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/restore#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Restore a Bare Metal Solution boot volume from an existing snapshot.

**EXAMPLES**

: To restore a boot volume named
``my-boot-volume`` in region
``us-central1`` from snapshot named
``my-snapshot``, run:

```
gcloud bms volumes restore my-boot-volume --region=us-central1 --snapshot=my-snapshot
```

**POSITIONAL ARGUMENTS**

: **Volume resource - volume. The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
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

**--region**:
Region of the resource.
To set the `region` attribute:

- provide the argument `volume` on the command line with a fully
specified name;
- provide the argument `--region` on the command line.**

**REQUIRED FLAGS**

: **--snapshot**:
Name of the snapshot to restore.

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

: This variant is also available:

```
gcloud alpha bms volumes restore
```