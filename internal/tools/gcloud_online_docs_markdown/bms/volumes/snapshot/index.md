# gcloud bms volumes snapshot  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/bms/volumes/snapshot](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/snapshot)*

**NAME**

: **gcloud bms volumes snapshot - create a snapshot of a Bare Metal Solution boot volume**

**SYNOPSIS**

: **`gcloud bms volumes snapshot` (`[VOLUME](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/snapshot#VOLUME)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/snapshot#--region)`=`REGION`) `[--description](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/snapshot#--description)`=`DESCRIPTION` `[--snapshot-name](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/snapshot#--snapshot-name)`=`SNAPSHOT_NAME` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/snapshot#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a snapshot of a Bare Metal Solution boot volume.

**EXAMPLES**

: To create a snapshot of a boot volume named
``my-boot-volume`` in region
``us-central1`` with the name
``my-snapshot`` and description
``my-description``, run:

```
gcloud bms volumes snapshot my-boot-volume --region=us-central1 --snapshot-name=my-snapshot --description=my-description
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

: **--description**:
Textual description of the created snapshot.

**--snapshot-name**:
Name to assign to the created snapshot.

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
gcloud alpha bms volumes snapshot
```