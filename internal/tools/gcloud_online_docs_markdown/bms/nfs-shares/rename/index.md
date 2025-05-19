# gcloud bms nfs-shares rename  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/bms/nfs-shares/rename](https://cloud.google.com/sdk/gcloud/reference/bms/nfs-shares/rename)*

**NAME**

: **gcloud bms nfs-shares rename - rename a Bare Metal Solution nfs-share**

**SYNOPSIS**

: **`gcloud bms nfs-shares rename` (`[NFS_SHARE](https://cloud.google.com/sdk/gcloud/reference/bms/nfs-shares/rename#NFS_SHARE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/bms/nfs-shares/rename#--region)`=`REGION`) `[--new-name](https://cloud.google.com/sdk/gcloud/reference/bms/nfs-shares/rename#--new-name)`=`NEW_NAME` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/bms/nfs-shares/rename#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Rename a Bare Metal Solution nfs-share.

**EXAMPLES**

: To rename a nfs-share ``my-nfs-share`` to
``my-new-nfs-share-name`` in region
``us-central1``, run:

```
gcloud bms nfs-shares rename my-nfs-share --new-name=my-new-nfs-share-name --region=us-central1 --project=bms-example-project
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

**REQUIRED FLAGS**

: **--new-name**:
New nfs-share name for renaming an already existing nfs-share.

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
gcloud alpha bms nfs-shares rename
```