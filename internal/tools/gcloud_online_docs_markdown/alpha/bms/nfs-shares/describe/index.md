# gcloud alpha bms nfs-shares describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/bms/nfs-shares/describe](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/nfs-shares/describe)*

**NAME**

: **gcloud alpha bms nfs-shares describe - describe a Bare Metal solution NFS share**

**SYNOPSIS**

: **`gcloud alpha bms nfs-shares describe` (`[NFS_SHARE](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/nfs-shares/describe#NFS_SHARE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/nfs-shares/describe#--region)`=`REGION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/nfs-shares/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Describe a Bare Metal Solution NFS share.

**EXAMPLES**

: To get a description of an NFS share called
``my-nfs-share`` in project
``my-project`` and region
``us-central1``, run:

```
gcloud alpha bms nfs-shares describe my-nfs-share --project=my-project --region=us-central1
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
gcloud bms nfs-shares describe
```