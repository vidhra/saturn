# gcloud netapp active-directories update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/update](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/update)*

**NAME**

: **gcloud netapp active-directories update - update a Cloud NetApp Active Directory**

**SYNOPSIS**

: **`gcloud netapp active-directories update` (`[ACTIVE_DIRECTORY](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/update#ACTIVE_DIRECTORY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/update#--location)`=`LOCATION`) `[--dns](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/update#--dns)`=`DNS` `[--domain](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/update#--domain)`=`DOMAIN` `[--net-bios-prefix](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/update#--net-bios-prefix)`=`NET_BIOS_PREFIX` `[--password](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/update#--password)`=`PASSWORD` `[--username](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/update#--username)`=`USERNAME` [`[--administrators](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/update#--administrators)`=[`ADMINISTRATOR`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/update#--async)`] [`[--backup-operators](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/update#--backup-operators)`=[`BACKUP_OPERATOR`,…]] [`[--description](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/update#--description)`=`DESCRIPTION`] [`[--enable-aes](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/update#--enable-aes)`=`ENABLE_AES`] [`[--enable-ldap-signing](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/update#--enable-ldap-signing)`=`ENABLE_LDAP_SIGNING`] [`[--encrypt-dc-connections](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/update#--encrypt-dc-connections)`=`ENCRYPT_DC_CONNECTIONS`] [`[--kdc-hostname](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/update#--kdc-hostname)`=`KDC_HOSTNAME`] [`[--kdc-ip](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/update#--kdc-ip)`=`KDC_IP`] [`[--nfs-users-with-ldap](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/update#--nfs-users-with-ldap)`=`NFS_USERS_WITH_LDAP`] [`[--organizational-unit](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/update#--organizational-unit)`=`ORGANIZATIONAL_UNIT`] [`[--security-operators](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/update#--security-operators)`=[`SECURITY_OPERATOR`,…]] [`[--site](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/update#--site)`=`SITE`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/netapp/active-directories/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates AD (Active Directory) configs for Cloud NetApp Volumes.

**EXAMPLES**

: The following command updates an AD config in the given project and location
with specified arguments:

```
gcloud netapp active-directories update AD_NAME --location=us-central1 --domain=new-domain.com --dns=1.1.1.1 --site=new_site --net-bios-prefix=new_prefix --organizational-unit=ou2 --enable-aes=true --username=user2 --password="secure2" --backup-operators=backup_op1,backup_op2 --security-operators=secure_op1,secure_op2 --administrators=admin_op1,admin_op2 --enable-ldap-signing=true --encrypt-dc-connections=yes --kdc-hostname=kdc-host1
```

**POSITIONAL ARGUMENTS**

: **Active directory resource - The Active Directory to update. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `active_directory` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ACTIVE_DIRECTORY`**:
ID of the active_directory or fully qualified identifier for the
active_directory.
To set the `active_directory` attribute:

- provide the argument `active_directory` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the active_directory.
To set the `location` attribute:

- provide the argument `active_directory` on the command line with a
fully specified name;
- provide the argument `--location` on the command line;
- set the property `netapp/location`.**

**REQUIRED FLAGS**

: **--dns**:
A comma separated list of DNS server IP addresses for the Active Directory
domain.

**--domain**:
The Active Directory domain.

**--net-bios-prefix**:
NetBIOS prefix name of the server.

**--password**:
Password of the Active Directory domain administrator.

**--username**:
Username of the Active Directory domain administrator.

**OPTIONAL FLAGS**

: **--administrators**:
Members of the Active Directory built-in Administrators group.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--backup-operators**:
Users to be added to the Built-in Backup Operator Active Directory group.

**--description**:
A description of the Cloud NetApp Active Directory

**--enable-aes**:
The Boolean value indiciating whether AES encryption will be enabled for SMB
communication.

**--enable-ldap-signing**:
Boolean flag that specifies whether or not LDAP traffic needs to be signed.

**--encrypt-dc-connections**:
Boolean flag that specifies whether traffic between SMB server to Domain
Controller (DC) will be encrypted.

**--kdc-hostname**:
Name of the Active Directory machine.

**--kdc-ip**:
KDC server IP address for the Active Directory machine.

**--nfs-users-with-ldap**:
Boolean flag that allows access to local users and LDAP users. If access is
needed only for LDAP users, it has to be disabled.

**--organizational-unit**:
The Organizational Unit (OU) within the Windows Active Directory the user
belongs to.

**--security-operators**:
Domain users to be given the Security privilege.

**--site**:
The Active Directory site the service will limit Domain Controller discovery to.

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

: These variants are also available:

```
gcloud alpha netapp active-directories update
```

```
gcloud beta netapp active-directories update
```