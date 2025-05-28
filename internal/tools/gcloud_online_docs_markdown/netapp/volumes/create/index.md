# gcloud netapp volumes create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create)*

**NAME**

: **gcloud netapp volumes create - create a Cloud NetApp Volume**

**SYNOPSIS**

: **`gcloud netapp volumes create` (`[VOLUME](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#VOLUME)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#--location)`=`LOCATION`) `[--capacity](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#--capacity)`=`CAPACITY` `[--protocols](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#--protocols)`=`PROTOCOL`,[`[PROTOCOL](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#PROTOCOL)`,…] `[--share-name](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#--share-name)`=`SHARE_NAME` `[--storage-pool](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#--storage-pool)`=`STORAGE_POOL` [`[--async](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#--async)`] [`[--backup-config](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#--backup-config)`=[`backup-policies`=`BACKUP-POLICIES`],[`backup-vault`=`BACKUP-VAULT`],[`enable-scheduled-backups`=`ENABLE-SCHEDULED-BACKUPS`]] [`[--description](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#--description)`=`DESCRIPTION`] [`[--enable-kerberos](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#--enable-kerberos)`=`ENABLE_KERBEROS`] [`[--export-policy](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#--export-policy)`=[`access-type`=`ACCESS-TYPE`],[`allowed-clients`=`ALLOWED-CLIENTS`],[`has-root-access`=`HAS-ROOT-ACCESS`],[`kerberos-5-read-only`=`KERBEROS-5-READ-ONLY`],[`kerberos-5-read-write`=`KERBEROS-5-READ-WRITE`],[`kerberos-5i-read-only`=`KERBEROS-5I-READ-ONLY`],[`kerberos-5i-read-write`=`KERBEROS-5I-READ-WRITE`],[`kerberos-5p-read-only`=`KERBEROS-5P-READ-ONLY`],[`kerberos-5p-read-write`=`KERBEROS-5P-READ-WRITE`],[`nfsv3`=`NFSV3`],[`nfsv4`=`NFSV4`]] [`[--hybrid-replication-parameters](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#--hybrid-replication-parameters)`=[`cluster-location`=`CLUSTER-LOCATION`],[`description`=`DESCRIPTION`],[`hybrid-replication-type`=`HYBRID-REPLICATION-TYPE`],[`labels`=`LABELS`],[`large-volume-constituent-count`=`LARGE-VOLUME-CONSTITUENT-COUNT`],[`peer-cluster-name`=`PEER-CLUSTER-NAME`],[`peer-ip-addresses`=`PEER-IP-ADDRESSES`],[`peer-svm-name`=`PEER-SVM-NAME`],[`peer-volume-name`=`PEER-VOLUME-NAME`],[`replication`=`REPLICATION`],[`replication-schedule`=`REPLICATION-SCHEDULE`]] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--large-capacity](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#--large-capacity)`=`LARGE_CAPACITY`] [`[--multiple-endpoints](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#--multiple-endpoints)`=`MULTIPLE_ENDPOINTS`] [`[--restricted-actions](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#--restricted-actions)`=`RESTRICTED_ACTION`,[…]] [`[--security-style](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#--security-style)`=`SECURITY_STYLE`; default=`"SECURITY_STYLE_UNSPECIFIED"`] [`[--smb-settings](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#--smb-settings)`=`SMB_SETTING`,[`[SMB_SETTING](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#SMB_SETTING)`,…]] [`[--snap-reserve](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#--snap-reserve)`=`SNAP_RESERVE`] [`[--snapshot-daily](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#--snapshot-daily)`=[`hour`=`HOUR`],[`minute`=`MINUTE`],[`snapshots-to-keep`=`SNAPSHOTS-TO-KEEP`]] [`[--snapshot-directory](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#--snapshot-directory)`=`SNAPSHOT_DIRECTORY`; default="true"] [`[--snapshot-hourly](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#--snapshot-hourly)`=[`minute`=`MINUTE`],[`snapshots-to-keep`=`SNAPSHOTS-TO-KEEP`]] [`[--snapshot-monthly](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#--snapshot-monthly)`=[`day`=`DAY`],[`hour`=`HOUR`],[`minute`=`MINUTE`],[`snapshots-to-keep`=`SNAPSHOTS-TO-KEEP`]] [`[--snapshot-weekly](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#--snapshot-weekly)`=[`day`=`DAY`],[`hour`=`HOUR`],[`minute`=`MINUTE`],[`snapshots-to-keep`=`SNAPSHOTS-TO-KEEP`]] [`[--source-snapshot](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#--source-snapshot)`=`SOURCE_SNAPSHOT`] [`[--tiering-policy](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#--tiering-policy)`=[`tier-action`=`ENABLED`|`[PAUSED](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#PAUSED)`,…]] [`[--unix-permissions](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#--unix-permissions)`=`UNIX_PERMISSIONS`] [`[--source-backup](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#--source-backup)`=`SOURCE_BACKUP` : `--backup_vault`=`BACKUP_VAULT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Cloud NetApp Volume

**EXAMPLES**

: The following command creates a NFS Volume named NAME asynchronously using the
specified arguments

```
gcloud netapp volumes create NAME --capacity=1024 --protocols=nfsv3,nfsv4 --share-name=share1 --storage-pool=sp1 --description="test description" --enable-kerberos=true --unix-permissions=0755 --async
```

The following command creates a SMB Volume named NAME asynchronously using the
specified arguments

```
gcloud netapp volumes create NAME --capacity=1024 --protocols=smb --share-name=share2 --storage-pool=sp2 --description="test smb" --security-style=ntfs --smb-settings=SHOW_SNAPSHOT,SHOW_PREVIOUS_VERSIONS,ACCESS_BASED_ENUMERATION --snap-reserve=0.1 --async
```

**POSITIONAL ARGUMENTS**

: **Volume resource - The Volume to create. The arguments in this group can be used
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

: **--capacity**:
The desired capacity of the Volume in GiB or TiB units.If no capacity unit is
specified, GiB is assumed.

**--protocols**:
Type of File System protocols for the Cloud NetApp Files Volume. Valid component
values are: `NFSV3`, `NFSV4`, `SMB`.

**--share-name**:
Share name of the Mount path clients will use.

**Storage pool resource - The Storage Pool to associate with Volume. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--storage-pool` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--storage-pool` on the command line with a
fully specified name;
- provide the argument `--location` on the command line;
- set the property `netapp/location`.

This must be specified.

**--storage-pool**:
ID of the storage_pool or fully qualified identifier for the storage_pool.
To set the `storage_pool` attribute:

- provide the argument `--storage-pool` on the command line.**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--backup-config**:
Backup Config contains backup related config on a volume.

```
Backup Config will have the following format
`--backup-config=backup-policies=BACKUP_POLICIES,
backup-vault=BACKUP_VAULT_NAME,
enable-scheduled-backups=ENABLE_SCHEDULED_BACKUPS
```

backup-policies is a pound-separated (#) list of backup policy names,
backup-vault can include a single backup-vault resource name, and
enable-scheduled-backups is a Boolean value indicating whether or not scheduled
backups are enabled on the volume.

**--description**:
A description of the Cloud NetApp Volume

**--enable-kerberos**:
Boolean flag indicating whether Volume is a kerberos Volume or not

**--export-policy**:
Export Policy of a Cloud NetApp Files Volume. This will be a field similar to
network in which export policy fields can be specified as such:
`--export-policy=allowed-clients=ALLOWED_CLIENTS_IP_ADDRESSES,
has-root-access=HAS_ROOT_ACCESS_BOOL,access=ACCESS_TYPE,nfsv3=NFSV3,
nfsv4=NFSV4,kerberos-5-read-only=KERBEROS_5_READ_ONLY,
kerberos-5-read-write=KERBEROS_5_READ_WRITE,
kerberos-5i-read-only=KERBEROS_5I_READ_ONLY,
kerberos-5i-read-write=KERBEROS_5I_READ_WRITE,
kerberos-5p-read-only=KERBEROS_5P_READ_ONLY,
kerberos-5p-read-write=KERBEROS_5P_READ_WRITE`

**--hybrid-replication-parameters**:
Hybrid Replication Parameters contains hybrid replication parameters on a
volume.

```
Hybrid Replication Parameters will have the following format
--hybrid-replication-parameters=replication=REPLICATION,
peer-volume-name=PEER_VOLUME_NAME,
peer-cluster-name=PEER_CLUSTER_NAME,
peer-svm-name=PEER_SVM_NAME,
peer-ip-addresses=[PEER-IP-ADDRESS1#PEER-IP-ADDRESS2#…],
cluster-location=CLUSTER_LOCATION,
description=DESCRIPTION,
replication-schedule=REPLICATION_SCHEDULE,
hybrid-replication-type=HYBRID_REPLICATION_TYPE,
large-volume-constituent-count=LARGE_VOLUME_CONSTITUENT_COUNT,
labels=[KEY1:VALUE1#KEY2:VALUE2#…],
```

replication is the desired name for the replication of the volume,
peer-volume-name is the name of the user's local source volume,
peer-cluster-name is the name of the user's local source cluster, peer-svm-name
is the name of the user's local source vserver svm, peer-ip-addresses is a
ampersand-separated(#) list of ip addresses, cluster-location is the name of the
source cluster location, description is the description of the replication,
replication-schedule is the schedule of corresponding hybrid replication
created, hybrid-replication-type is the hybrid replication type of the
corresponding hybrid replication created, large-volume-constituent-count is the
number of constituent volumes in the large volume, and labels is an
hashtag-separated(#) key value pair of labels with key and value separated by
colon(:) for the replication.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--large-capacity**:
Boolean flag indicating whether Volume is a large capacity Volume or not

**--multiple-endpoints**:
Boolean flag indicating whether Volume is a multiple endpoints Volume or not

**--restricted-actions**:
Actions to be restricted for a volume. Valid restricted action options are:
'DELETE'.

**--security-style**:
The security style of the Volume. This can either be UNIX or NTFS.
`SECURITY_STYLE` must be one of:

**`ntfs`**:
NTFS security style for Volume.

**`unix`**:
UNIX security style for Volume

**--smb-settings**:
List of settings specific to SMB protocol for a Cloud NetApp Files Volume. Valid
component values are: `ENCRYPT_DATA`, `BROWSABLE`,
`CHANGE_NOTIFY`, `NON_BROWSABLE`, `OPLOCKS`,
`SHOW_SNAPSHOT`, `SHOW_PREVIOUS_VERSIONS`,
`ACCESS_BASED_ENUMERATION`, `CONTINUOUSLY_AVAILABLE`.

**--snap-reserve**:
(DEPRECATED) The percentage of volume storage reserved for snapshot storage. The
default value for this is 0 percent
The snap-reserve option is deprecated

**--snapshot-daily**:
Make a snapshot every day e.g. at 06:00, 05:20, 23:50

**--snapshot-directory**:
Snapshot Directory if enabled (true) makes the Volume contain a read-only
.snapshot directory which provides access to each of the volume's snapshots

**--snapshot-hourly**:
Make a snapshot every hour e.g. at 04:00, 05:20, 06:00

**--snapshot-monthly**:
Make a snapshot once a month e.g. at 2nd 04:00, 7th 05:20, 24th 23:50

**--snapshot-weekly**:
Make a snapshot every week e.g. at Monday 04:00, Wednesday 05:20, Sunday 23:50

**Snapshot resource - The source Snapshot to create the Volume from. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--source-snapshot` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--source-snapshot` on the command line with a
fully specified name;
- set the property `netapp/location`.

To set the `volume` attribute:

- provide the argument `--source-snapshot` on the command line with a
fully specified name.

**--source-snapshot**:
ID of the snapshot or fully qualified identifier for the snapshot.
To set the `snapshot` attribute:

- provide the argument `--source-snapshot` on the command line.**

**--tiering-policy**:
Tiering Policy contains auto tiering policy on a volume.

```
Tiering Policy will have the following format
--tiering-policy=tier-action=TIER_ACTION,
cooling-threshold-days=COOLING_THRESHOLD_DAYS
```

```
tier-action is an enum, supported values are ENABLED or PAUSED,

 cooling-threshold-days is an integer represents time in days to mark the
volume's data block as cold and make it eligible for tiering, can be range from
7-183. Default is 31.
```

**--unix-permissions**:
Unix permissions the mount point will be created with. Unix permissions are only
applicable with NFS protocol only

**Backup resource - The source Backup to create the Volume from. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--source-backup` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--source-backup` on the command line with a
fully specified name;
- set the property `netapp/location`.

**--source-backup**:
ID of the backup or fully qualified identifier for the backup.
To set the `backup` attribute:

- provide the argument `--source-backup` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--backup_vault**:
The Backup Vault of the backup.
To set the `backup_vault` attribute:

- provide the argument `--source-backup` on the command line with a
fully specified name;
- provide the argument `--backup_vault` on the command line;
- provide the argument `--backup-vault` on the command line.**

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
gcloud alpha netapp volumes create
```

```
gcloud beta netapp volumes create
```