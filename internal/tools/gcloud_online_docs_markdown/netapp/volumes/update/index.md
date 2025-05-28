# gcloud netapp volumes update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update)*

**NAME**

: **gcloud netapp volumes update - update a Cloud NetApp Volume**

**SYNOPSIS**

: **`gcloud netapp volumes update` (`[VOLUME](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#VOLUME)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#--async)`] [`[--backup-config](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#--backup-config)`=[`backup-policies`=`BACKUP-POLICIES`],[`backup-vault`=`BACKUP-VAULT`],[`enable-scheduled-backups`=`ENABLE-SCHEDULED-BACKUPS`]] [`[--capacity](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#--capacity)`=`CAPACITY`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#--description)`=`DESCRIPTION`] [`[--enable-kerberos](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#--enable-kerberos)`=`ENABLE_KERBEROS`] [`[--export-policy](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#--export-policy)`=[`access-type`=`ACCESS-TYPE`],[`allowed-clients`=`ALLOWED-CLIENTS`],[`has-root-access`=`HAS-ROOT-ACCESS`],[`kerberos-5-read-only`=`KERBEROS-5-READ-ONLY`],[`kerberos-5-read-write`=`KERBEROS-5-READ-WRITE`],[`kerberos-5i-read-only`=`KERBEROS-5I-READ-ONLY`],[`kerberos-5i-read-write`=`KERBEROS-5I-READ-WRITE`],[`kerberos-5p-read-only`=`KERBEROS-5P-READ-ONLY`],[`kerberos-5p-read-write`=`KERBEROS-5P-READ-WRITE`],[`nfsv3`=`NFSV3`],[`nfsv4`=`NFSV4`]] [`[--protocols](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#--protocols)`=`PROTOCOL`,[`[PROTOCOL](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#PROTOCOL)`,…]] [`[--restricted-actions](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#--restricted-actions)`=`RESTRICTED_ACTION`,[…]] [`[--security-style](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#--security-style)`=`SECURITY_STYLE`; default=`"SECURITY_STYLE_UNSPECIFIED"`] [`[--share-name](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#--share-name)`=`SHARE_NAME`] [`[--smb-settings](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#--smb-settings)`=`SMB_SETTING`,[`[SMB_SETTING](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#SMB_SETTING)`,…]] [`[--snap-reserve](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#--snap-reserve)`=`SNAP_RESERVE`] [`[--snapshot-daily](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#--snapshot-daily)`=[`hour`=`HOUR`],[`minute`=`MINUTE`],[`snapshots-to-keep`=`SNAPSHOTS-TO-KEEP`]] [`[--snapshot-directory](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#--snapshot-directory)`=`SNAPSHOT_DIRECTORY`; default="true"] [`[--snapshot-hourly](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#--snapshot-hourly)`=[`minute`=`MINUTE`],[`snapshots-to-keep`=`SNAPSHOTS-TO-KEEP`]] [`[--snapshot-monthly](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#--snapshot-monthly)`=[`day`=`DAY`],[`hour`=`HOUR`],[`minute`=`MINUTE`],[`snapshots-to-keep`=`SNAPSHOTS-TO-KEEP`]] [`[--snapshot-weekly](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#--snapshot-weekly)`=[`day`=`DAY`],[`hour`=`HOUR`],[`minute`=`MINUTE`],[`snapshots-to-keep`=`SNAPSHOTS-TO-KEEP`]] [`[--source-snapshot](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#--source-snapshot)`=`SOURCE_SNAPSHOT`] [`[--storage-pool](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#--storage-pool)`=`STORAGE_POOL`] [`[--tiering-policy](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#--tiering-policy)`=[`tier-action`=`ENABLED`|`[PAUSED](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#PAUSED)`,…]] [`[--unix-permissions](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#--unix-permissions)`=`UNIX_PERMISSIONS`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#--remove-labels)`=[`KEY`,…]] [`[--source-backup](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#--source-backup)`=`SOURCE_BACKUP` : `--backup_vault`=`BACKUP_VAULT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Cloud NetApp Volume and its specified parameters

**EXAMPLES**

: The following command updates a Volume named NAME and its specified parameters

```
gcloud netapp volumes update NAME --location=us-central1 --capacity=4096 --description="new description" --enable-kerberos=false --storage-pool=sp3 --unix-permissions=0777
```

**POSITIONAL ARGUMENTS**

: **Volume resource - The Volume to update. The arguments in this group can be used
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

**FLAGS**

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

**--capacity**:
The desired capacity of the Volume in GiB or TiB units.If no capacity unit is
specified, GiB is assumed.

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

**--protocols**:
Type of File System protocols for the Cloud NetApp Files Volume. Valid component
values are: `NFSV3`, `NFSV4`, `SMB`.

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

**--share-name**:
Share name of the Mount path clients will use.

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

**--storage-pool**:
ID of the storage_pool or fully qualified identifier for the storage_pool.
To set the `storage_pool` attribute:

- provide the argument `--storage-pool` on the command line.**

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

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

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
gcloud alpha netapp volumes update
```

```
gcloud beta netapp volumes update
```