# gcloud alpha bms volumes update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes/update](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes/update)*

**NAME**

: **gcloud alpha bms volumes update - update a Bare Metal Solution volume**

**SYNOPSIS**

: **`gcloud alpha bms volumes update` (`[VOLUME](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes/update#VOLUME)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes/update#--region)`=`REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes/update#--async)`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/volumes/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Update a Bare Metal Solution volume.
This call returns immediately, but the update operation may take several minutes
to complete. To check if the operation is complete, use the
`describe` command for the volume.

**EXAMPLES**

: To add the label 'key1=value1' to a policy, run:

```
gcloud alpha bms volumes update my-volume --update-labels=key1=value1
```

To clear all labels, run:

```
gcloud alpha bms volumes update my-volume --clear-labels
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

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--update-labels**:
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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud bms volumes update
```