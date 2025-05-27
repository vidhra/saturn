# gcloud database-migration connection-profiles create alloydb  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/alloydb](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/alloydb)*

**NAME**

: **gcloud database-migration connection-profiles create alloydb - create a Database Migration Service connection profile for AlloyDB**

**SYNOPSIS**

: **`gcloud database-migration connection-profiles create alloydb` (`[CONNECTION_PROFILE](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/alloydb#CONNECTION_PROFILE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/alloydb#--region)`=`REGION`) `[--cpu-count](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/alloydb#--cpu-count)`=`CPU_COUNT` `[--password](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/alloydb#--password)`=`PASSWORD` `[--primary-id](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/alloydb#--primary-id)`=`PRIMARY_ID` [`[--no-async](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/alloydb#--async)`] [`[--authorized-network-cidr-ranges](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/alloydb#--authorized-network-cidr-ranges)`=[`NETWORK`,…]] [`[--cluster-labels](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/alloydb#--cluster-labels)`=[`KEY`=`VALUE`,…]] [`[--database-flags](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/alloydb#--database-flags)`=[`FLAG`=`VALUE`,…]] [`[--database-version](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/alloydb#--database-version)`=`DATABASE_VERSION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/alloydb#--display-name)`=`DISPLAY_NAME`] [`[--enable-outbound-public-ip](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/alloydb#--enable-outbound-public-ip)`] [`[--enable-public-ip](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/alloydb#--enable-public-ip)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/alloydb#--labels)`=[`KEY`=`VALUE`,…]] [`[--network](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/alloydb#--network)`=`NETWORK`] [`[--primary-labels](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/alloydb#--primary-labels)`=[`KEY`=`VALUE`,…]] [`[--role](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/alloydb#--role)`=`ROLE`] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/alloydb#--kms-key)`=`KMS_KEY` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/alloydb#--kms-keyring)`=`KMS_KEYRING` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/alloydb#--kms-project)`=`KMS_PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/alloydb#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Database Migration Service destination connection profile for AlloyDB.
This will create an AlloyDB cluster and primary instance.

**EXAMPLES**

: To create a connection profile for AlloyDB:

```
gcloud database-migration connection-profiles create alloydb my-profile --region=us-central1 --password=my_password --primary-id=my-primary --cpu-count=2
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

: **--cpu-count**:
Whole number value indicating how many vCPUs the machine should contain. Each
vCPU count corresponds to a N2 high-mem machine:
(https://cloud.google.com/compute/docs/general-purpose-machines#n2_machines).
`CPU_COUNT` must be one of: `2`,
`4`, `8`, `16`, `32`,
`64`.

**--password**:
Initial password for the 'postgres' user.

**--primary-id**:
The ID of the primary instance for this AlloyDB cluster.

**OPTIONAL FLAGS**

: **--no-async**:
Waits for the operation in progress to complete before returning.

**--authorized-network-cidr-ranges**:
Comma-separated list of CIDR ranges that can connect to the AlloyDB instance.

**--cluster-labels**:
The resource labels for an AlloyDB cluster. An object containing a list of
"key": "value" pairs.

**--database-flags**:
Comma-separated list of database flags to set on the AlloyDB primary instance.
Use an equals sign to separate the flag name and value. Flags without values,
like skip_grant_tables, can be written out without a value, e.g.,
`skip_grant_tables=`. Use on/off values for booleans. View AlloyDB's
documentation for allowed flags (e.g., `--database-flags
max_allowed_packet=55555,skip_grant_tables=,log_output=1`).

**--database-version**:
Database engine major version. `DATABASE_VERSION` must be
one of: `POSTGRES_14`, `POSTGRES_15`,
`POSTGRES_16`.

**--display-name**:
A user-friendly name for the connection profile. The display name can include
letters, numbers, spaces, and hyphens, and must start with a letter.

**--enable-outbound-public-ip**:
If true, Enables an outbound public IP address to support a database server
sending requests out into the internet.

**--enable-public-ip**:
If true, the AlloyDB instance will be accessible via public IP.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--network**:
The VPC network from which the AlloyDB instance is accessible via private IP.
For example, projects/myProject/global/networks/default. This setting cannot be
updated after it is set.

**--primary-labels**:
The resource labels for an AlloyDB primary instance. An object containing a list
of "key": "value" pairs.

**--role**:
The role of the connection profile. `ROLE` must be one of:
`SOURCE`, `DESTINATION`.

**Kms key resource - Name of the CMEK (customer-managed encryption key) used for
this AlloyDB cluster. For example,
projects/myProject/locations/us-central1/keyRings/myKeyRing/cryptoKeys/myKey.
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `region` attribute:

- provide the argument `--kms-key` on the command line with a fully
specified name;
- provide the argument `--region` on the command line.

**--kms-key**:
ID of the kms-key or fully qualified identifier for the kms-key.
To set the `kms-key` attribute:

- provide the argument `--kms-key` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--kms-keyring**:
The CMEK keyring id of the kms-key.
To set the `kms-keyring` attribute:

- provide the argument `--kms-key` on the command line with a fully
specified name;
- provide the argument `--kms-keyring` on the command line.

**--kms-project**:
The Cloud project id for the kms-key.
To set the `kms-project` attribute:

- provide the argument `--kms-key` on the command line with a fully
specified name;
- provide the argument `--kms-project` on the command line.**

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