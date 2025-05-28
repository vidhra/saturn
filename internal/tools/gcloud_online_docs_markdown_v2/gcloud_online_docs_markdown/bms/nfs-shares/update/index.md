# gcloud bms nfs-shares update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/bms/nfs-shares/update](https://cloud.google.com/sdk/gcloud/reference/bms/nfs-shares/update)*

**NAME**

: **gcloud bms nfs-shares update - update a Bare Metal Solution NFS share**

**SYNOPSIS**

: **`gcloud bms nfs-shares update` (`[NFS_SHARE](https://cloud.google.com/sdk/gcloud/reference/bms/nfs-shares/update#NFS_SHARE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/bms/nfs-shares/update#--region)`=`REGION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/bms/nfs-shares/update#--async)`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/bms/nfs-shares/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--add-allowed-client](https://cloud.google.com/sdk/gcloud/reference/bms/nfs-shares/update#--add-allowed-client)`=[`PROPERTY`=`VALUE`,…]     | `[--clear-allowed-clients](https://cloud.google.com/sdk/gcloud/reference/bms/nfs-shares/update#--clear-allowed-clients)`     | `[--remove-allowed-client](https://cloud.google.com/sdk/gcloud/reference/bms/nfs-shares/update#--remove-allowed-client)`=[`PROPERTY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/bms/nfs-shares/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/bms/nfs-shares/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/bms/nfs-shares/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Bare Metal Solution NFS share.
This call returns immediately, but the update operation may take several minutes
to complete. To check if the operation is complete, use the
`describe` command for the NFS share.

**EXAMPLES**

: To update an NFS share called ``my-share`` in
region ``us-central1`` with a new label
``key1=value1``, run:

```
gcloud bms nfs-shares update my-share --region=us-central1 --update-labels=key1=value1
```

To clear all labels, run:

```
gcloud bms nfs-shares update my-share --region=us-central1 --clear-labels
```

To remove label ``key1``, run:

```
gcloud bms nfs-shares update my-share --region=us-central1 --remove-labels=key1
```

**POSITIONAL ARGUMENTS**

: **Nfs share resource - nfs_share. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `nfs_share` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`NFS_SHARE`**:
ID of the nfs_share or fully qualified identifier for the nfs_share.
To set the `nfs_share` attribute:

- provide the argument `nfs_share` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
Region of the resource.
To set the `region` attribute:

- provide the argument `nfs_share` on the command line with a fully
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

**--add-allowed-client**

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

: This variant is also available:

```
gcloud alpha bms nfs-shares update
```