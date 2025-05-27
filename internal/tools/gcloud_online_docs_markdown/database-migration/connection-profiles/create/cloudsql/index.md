# gcloud database-migration connection-profiles create cloudsql  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql)*

**NAME**

: **gcloud database-migration connection-profiles create cloudsql - create a Database Migration Service connection profile for Cloud SQL**

**SYNOPSIS**

: **`gcloud database-migration connection-profiles create cloudsql` (`[CONNECTION_PROFILE](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#CONNECTION_PROFILE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--region)`=`REGION`) `[--source-id](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--source-id)`=`SOURCE_ID` `[--tier](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--tier)`=`TIER` (`[--database-version](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--database-version)`=`DATABASE_VERSION`     | `[--database-version-name](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--database-version-name)`=`DATABASE_VERSION_NAME`) [`[--activation-policy](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--activation-policy)`=`ACTIVATION_POLICY`] [`[--allocated-ip-range](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--allocated-ip-range)`=`ALLOCATED_IP_RANGE`] [`[--no-async](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--async)`] [`[--authorized-networks](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--authorized-networks)`=`NETWORK`,[`[NETWORK](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#NETWORK)`,…]] [`[--no-auto-storage-increase](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--auto-storage-increase)`] [`[--availability-type](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--availability-type)`=`AVAILABILITY_TYPE`] [`[--data-disk-size](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--data-disk-size)`=`DATA_DISK_SIZE`] [`[--data-disk-type](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--data-disk-type)`=`DATA_DISK_TYPE`] [`[--database-flags](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--database-flags)`=[`FLAG`=`VALUE`,…]] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--display-name)`=`DISPLAY_NAME`] [`[--edition](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--edition)`=`EDITION`] [`[--no-enable-ip-v4](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--enable-ip-v4)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--labels)`=[`KEY`=`VALUE`,…]] [`[--private-network](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--private-network)`=`PRIVATE_NETWORK`] [`[--provider](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--provider)`=`PROVIDER`] [`[--require-ssl](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--require-ssl)`] [`[--role](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--role)`=`ROLE`] [`[--root-password](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--root-password)`=`ROOT_PASSWORD`] [`[--secondary-zone](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--secondary-zone)`=`SECONDARY_ZONE`] [`[--storage-auto-resize-limit](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--storage-auto-resize-limit)`=`STORAGE_AUTO_RESIZE_LIMIT`] [`[--user-labels](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--user-labels)`=[`KEY`=`VALUE`,…]] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--zone)`=`ZONE`] [`[--cmek-key](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--cmek-key)`=`CMEK_KEY` : `[--cmek-keyring](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--cmek-keyring)`=`CMEK_KEYRING` `[--cmek-project](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#--cmek-project)`=`CMEK_PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Database Migration Service destination connection profile for Cloud
SQL. This will create a Cloud SQL replica. Used for PostgreSQL and MySQL
migrations.

**EXAMPLES**

: To create a connection profile for Cloud SQL with database version MySQL 5.6:

```
gcloud database-migration connection-profiles create cloudsql my-profile --region=us-central1 --database-version=MYSQL_5_6 --source-id=cp1 --tier=db-n1-standard-1
```

To create a connection profile for Cloud SQL and a Cloud SQL replica with
database version PostgreSQL 10:

```
gcloud database-migration connection-profiles create cloudsql my-profile --region=us-central1 --database-version=POSTGRES_10 --source-id=cp1 --tier=db-custom-1-3840 --zone=us-central1-a
```

**POSITIONAL ARGUMENTS**

: **Connection profile resource - The connection profile to create. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `connection_profile` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CONNECTION_PROFILE`**:
ID of the connection_profile or fully qualified identifier for the
connection_profile.
To set the `connection_profile` attribute:

- provide the argument `connection_profile` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The Cloud region for the connection_profile.
To set the `region` attribute:

- provide the argument `connection_profile` on the command line with a
fully specified name;
- provide the argument `--region` on the command line.**

**REQUIRED FLAGS**

: **Connection profile resource - Database Migration Service source connection
profile ID. This represents a Cloud resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--source-id` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `region` attribute:

- provide the argument `--source-id` on the command line with a fully
specified name;
- provide the argument `--region` on the command line.

This must be specified.

**--source-id**:
ID of the connection_profile or fully qualified identifier for the
connection_profile.
To set the `connection_profile` attribute:

- provide the argument `--source-id` on the command line.**

**--tier**:
Tier (or machine type) for this instance, for example:
``db-n1-standard-1`` (MySQL instances) or
``db-custom-1-3840`` (PostgreSQL instances).
For more information, see [Cloud SQL
Instance Settings](https://cloud.google.com/sql/docs/mysql/instance-settings).

**--database-version**

**OPTIONAL FLAGS**

: **--activation-policy**:
Activation policy specifies when the instance is activated; it is applicable
only when the instance state is 'RUNNABLE'. Valid values:
ALWAYS: The instance is on, and remains so even in the absence of connection
requests.
NEVER: The instance is off; it is not activated, even if a connection request
arrives.
`ACTIVATION_POLICY` must be one of: `ALWAYS`,
`NEVER`.

**--allocated-ip-range**:
The name of the allocated IP range for the private IP Cloud SQL instance. This
name refers to an already allocated IP range. If set, the instance IP will be
created in the allocated range.

**--no-async**:
Waits for the operation in progress to complete before returning.

**--authorized-networks**:
List of external networks that are allowed to connect to the instance. Specify
values in CIDR notation, also known as 'slash' notation (e.g.192.168.100.0/24).

**--auto-storage-increase**:
If you enable this setting, Cloud SQL checks your available storage every 30
seconds. If the available storage falls below a threshold size, Cloud SQL
automatically adds additional storage capacity. If the available storage
repeatedly falls below the threshold size, Cloud SQL continues to add storage
until it reaches the maximum of 64 TB. Default: ON. Enabled by default, use
`--no-auto-storage-increase` to disable.

**--availability-type**:
Cloud SQL availability type. `AVAILABILITY_TYPE` must be
one of: `REGIONAL`, `ZONAL`.

**--data-disk-size**:
Storage capacity available to the database, in GB. The minimum (and default)
size is 10GB.

**--data-disk-type**:
Type of storage. `DATA_DISK_TYPE` must be one of:
`PD_SSD`, `PD_HDD`.

**--database-flags**:
Comma-separated list of database flags to set on the instance. Use an equals
sign to separate the flag name and value. Flags without values, like
skip_grant_tables, can be written out without a value, e.g.,
`skip_grant_tables=`. Use on/off values for booleans. View the
Instance Resource API for allowed flags. (e.g., `--database-flags
max_allowed_packet=55555 skip_grant_tables=,log_output=1`).

**--display-name**:
A user-friendly name for the connection profile. The display name can include
letters, numbers, spaces, and hyphens, and must start with a letter.

**--edition**:
Specifies edition. `EDITION` must be one of:

**`enterprise`**:
Enterprise is the standard option for smaller instances.

**`enterprise-plus`**:
Enterprise plus option recommended for cpu-intensive workloads. Offers access to
premium features and capabilities.

**--enable-ip-v4**:
Whether the instance should be assigned an IPv4 address or not. Enabled by
default, use `--no-enable-ip-v4` to disable.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--private-network**:
Resource link for the VPC network from which the Cloud SQL instance is
accessible for private IP. For example,
/projects/myProject/global/networks/default. This setting can be updated, but it
cannot be removed after it is set.

**--provider**:
Database provider, for managed databases. `PROVIDER` must
be one of: `RDS`, `CLOUDSQL`.

**--require-ssl**:
Whether SSL connections over IP should be enforced or not.

**--role**:
The role of the connection profile. `ROLE` must be one of:
`SOURCE`, `DESTINATION`.

**--root-password**:
Root Cloud SQL user's password.

**--secondary-zone**:
Google Cloud Platform zone where the failover Cloud SQL database instance is
located. Used when the Cloud SQL database availability type is REGIONAL (i.e.
multiple zones / highly available).

**--storage-auto-resize-limit**:
Maximum size to which storage capacity can be automatically increased. The
default value is 0, which specifies that there is no limit.

**--user-labels**:
The resource labels for a Cloud SQL instance to use to annotate any related
underlying resources such as Compute Engine VMs. An object containing a list of
"key": "value" pairs.

**--zone**:
Google Cloud Platform zone where your Cloud SQL database instance is located.

**Cmek key resource - Name of the CMEK (customer-managed encryption key) used for
the connection profile. For example,
projects/myProject/locations/us-central1/keyRings/myKeyRing/cryptoKeys/myKey.
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `region` attribute:

- provide the argument `--cmek-key` on the command line with a fully
specified name.

**--cmek-key**:
ID of the cmek-key or fully qualified identifier for the cmek-key.
To set the `cmek-key` attribute:

- provide the argument `--cmek-key` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--cmek-keyring**:
The CMEK keyring id of the cmek-key.
To set the `cmek-keyring` attribute:

- provide the argument `--cmek-key` on the command line with a fully
specified name;
- provide the argument `--cmek-keyring` on the command line.

**--cmek-project**:
The Cloud project id for the cmek-key.
To set the `cmek-project` attribute:

- provide the argument `--cmek-key` on the command line with a fully
specified name;
- provide the argument `--cmek-project` on the command line.**

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
gcloud alpha database-migration connection-profiles create cloudsql
```