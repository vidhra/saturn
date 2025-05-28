# gcloud alpha bms nfs-shares create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/bms/nfs-shares/create](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/nfs-shares/create)*

**NAME**

: **gcloud alpha bms nfs-shares create - create a Bare Metal Solution NFS share**

**SYNOPSIS**

: **`gcloud alpha bms nfs-shares create` (`[NFS_SHARE](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/nfs-shares/create#NFS_SHARE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/nfs-shares/create#--region)`=`REGION`) `[--allowed-client](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/nfs-shares/create#--allowed-client)`=[`PROPERTY`=`VALUE`,…] `[--size-gib](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/nfs-shares/create#--size-gib)`=`SIZE_GIB` `[--storage-type](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/nfs-shares/create#--storage-type)`=`STORAGE_TYPE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/nfs-shares/create#--async)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/nfs-shares/create#--labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/bms/nfs-shares/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a Bare Metal Solution NFS share.

**EXAMPLES**

: To create an NFS share called ``my-share`` in
region ``us-central1``, with requested size of
256 Gib, SSD storage and 2 allowed clients, run:

```
gcloud alpha bms nfs-shares create my-share --region=us-central1 --size-gib=256 --storage-type=SSD --allowed-client=network=my-network,network-project-id=some-other-project,cidr=10.130.240.24/29,mount-permissions=READ_ONLY,allow-dev=yes,allow-suid=no,enable-root-squash=yes --allowed-client=network=my-network2,cidr=10.130.240.26/28,mount-permissions=READ_WRITE,allow-dev=yes,allow-suid=yes,enable-root-squash=no
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

: **--allowed-client**:
Adds an allowed client to the NFS share. This flag can be repeated to specify
multiple allowed clients.

**`network`**:
The name of the network to allow.

**`network-project-id`**:
The project ID of the allowed client network. If not present, the project ID of
the NFS share will be used.

**`cidr`**:
The subnet of IP addresses permitted to access the NFS share.

**`mount-permissions`**:
The mount permissions for the allowed client.
``MOUNT_PERMISSIONS`` must be one of:
`READ_ONLY`, `READ_WRITE`.

**`allow-dev`**:
If ``yes``, allows creation of devices.

**`allow-suid`**:
If ``yes``, allows SUID.

**`enable-root-squash`**:
If ``yes``, enables root squashing which is a
special mapping of the remote superuser (root) identity when using identity
authentication .

**--size-gib**:
The requested size of the NFS share in GiB

**--storage-type**:
Specifies the storage type of the underlying volume which will be created for
the NFS share. `STORAGE_TYPE` must be one of:

**`HDD`**:
The storage type of the underlying volume will be HDD

**`SSD`**:
The storage type of the underlying volume will be SSD

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

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
gcloud bms nfs-shares create
```