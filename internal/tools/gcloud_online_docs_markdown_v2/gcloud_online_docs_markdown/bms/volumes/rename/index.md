# gcloud bms volumes rename  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/bms/volumes/rename](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/rename)*

**NAME**

: **gcloud bms volumes rename - rename a Bare Metal Solution volume**

**SYNOPSIS**

: **`gcloud bms volumes rename` (`[VOLUME](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/rename#VOLUME)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/rename#--region)`=`REGION`) `[--new-name](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/rename#--new-name)`=`NEW_NAME` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/bms/volumes/rename#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Rename a Bare Metal Solution volume.

**EXAMPLES**

: To rename a volume ``my-volume`` to
``my-new-volume-name`` in region
``us-central1``, run:

```
gcloud bms volumes rename my-volume --new-name=my-new-volume-name --region=us-central1 --project=bms-example-project
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

: **--new-name**:
New volume name for renaming an already existing volume.

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
gcloud alpha bms volumes rename
```