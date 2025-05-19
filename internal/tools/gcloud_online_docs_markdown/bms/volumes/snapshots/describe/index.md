# gcloud bms volumes snapshots describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/bms/volumes/snapshots/describe](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/snapshots/describe)*

**NAME**

: **gcloud bms volumes snapshots describe - describe a Bare Metal Solution boot volume snapshot**

**SYNOPSIS**

: **`gcloud bms volumes snapshots describe` (`[SNAPSHOT](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/snapshots/describe#SNAPSHOT)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/snapshots/describe#--region)`=`REGION` `[--volume](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/snapshots/describe#--volume)`=`VOLUME`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/snapshots/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a Bare Metal Solution boot volume snapshot.

**EXAMPLES**

: To get a description of a snapshot called
``my-snapshot`` on boot volume
``my-boot-volume`` in region
``us-central1``, run:

```
gcloud bms volumes snapshots describe my-snapshot --region=us-central1 --volume=my-boot-volume
```

**POSITIONAL ARGUMENTS**

: **Snapshot resource - snapshot. The arguments in this group can be used to specify
the attributes of this resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `snapshot` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SNAPSHOT`**:
ID of the snapshot or fully qualified identifier for the snapshot.
To set the `snapshot` attribute:

- provide the argument `snapshot` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
Region of the resource.
To set the `region` attribute:

- provide the argument `snapshot` on the command line with a fully
specified name;
- provide the argument `--region` on the command line.

**--volume**:
Bare Metal Solution volume.
To set the `volume` attribute:

- provide the argument `snapshot` on the command line with a fully
specified name;
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

: This variant is also available:

```
gcloud alpha bms volumes snapshots describe
```