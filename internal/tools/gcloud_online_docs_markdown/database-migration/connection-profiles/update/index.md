# gcloud database-migration connection-profiles update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/update](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/update)*

**NAME**

: **gcloud database-migration connection-profiles update - update a Database Migration Service connection profile**

**SYNOPSIS**

: **`gcloud database-migration connection-profiles update` (`[CONNECTION_PROFILE](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/update#CONNECTION_PROFILE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/update#--region)`=`REGION`) [`[--alloydb-cluster](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/update#--alloydb-cluster)`=`ALLOYDB_CLUSTER`] [`[--ca-certificate](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/update#--ca-certificate)`=`CA_CERTIFICATE`] [`[--client-certificate](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/update#--client-certificate)`=`CLIENT_CERTIFICATE`] [`[--cloudsql-instance](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/update#--cloudsql-instance)`=`CLOUDSQL_INSTANCE`] [`[--cloudsql-project-id](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/update#--cloudsql-project-id)`=`CLOUDSQL_PROJECT_ID`] [`[--database](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/update#--database)`=`DATABASE`] [`[--database-service](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/update#--database-service)`=`DATABASE_SERVICE`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/update#--display-name)`=`DISPLAY_NAME`] [`[--host](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/update#--host)`=`HOST`] [`[--port](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/update#--port)`=`PORT`] [`[--private-key](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/update#--private-key)`=`PRIVATE_KEY`] [`[--ssl-type](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/update#--ssl-type)`=`SSL_TYPE`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--username](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/update#--username)`=`USERNAME`] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/update#--remove-labels)`=[`KEY`,…]] [`[--gcs-bucket](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/update#--gcs-bucket)`=`GCS_BUCKET` : `[--gcs-prefix](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/update#--gcs-prefix)`=`GCS_PREFIX`] [`[--password](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/update#--password)`=`PASSWORD`     | `[--prompt-for-password](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/update#--prompt-for-password)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Database Migration Service connection profile.

- Draft connection profile: the user can update all flags available in
`connection-profiles create` command.
- Existing connection profile: the user can update a limited list of flags, see
`connection-profiles update` Synopsis.
- If a migration job is using the connection profile, then updates to fields
`host`, `port`, `username`, and
`password` will propagate to the destination instance.

**EXAMPLES**

: To update the username of a connection profile:

```
gcloud database-migration connection-profiles update my-profile --region=us-central1 --username=new-user
```

**POSITIONAL ARGUMENTS**

: **Connection profile resource - The connection profile to update. The arguments in
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

**FLAGS**

: **--alloydb-cluster**:
If the destination is an AlloyDB cluster, use this field to provide the AlloyDB
cluster ID.

**--ca-certificate**:
x509 PEM-encoded certificate of the CA that signed the database server's
certificate. The value for this flag needs to be the content of the certificate
file, not the path to the file. For example, on a Linux machine you can use
command substitution:
<code>--ca-certificate=$(</path/to/certificate_file.pem)</code>.
Database Migration Service will use this certificate to verify it's connecting
to the correct host. Database Migration Service encrypts the value when storing
it.

**--client-certificate**:
x509 PEM-encoded certificate that will be used by the replica to authenticate
against the database server. The value for this flag needs to be the content of
the certificate file, not the path to the file. For example, on a Linux machine
you can use command substitution:
<code>--ca-certificate=$(</path/to/certificate_file.pem)</code>.
Database Migration Service encrypts the value when storing it.

**--cloudsql-instance**:
If the source or destination is a Cloud SQL database, then use this field to
provide the respective Cloud SQL instance ID.

**--cloudsql-project-id**:
The project id of the Cloud SQL instance. Only needed if the Cloud SQL instance
is in a different project than the connection profile. This is only supported
for source connection profiles for SQL Server.

**--database**:
The specific database within the host.

**--database-service**:
database service for the oracle connection profile.

**--display-name**:
A user-friendly name for the connection profile. The display name can include
letters, numbers, spaces, and hyphens, and must start with a letter.

**--host**:
IP or hostname of the database. When `--psc-service-attachment` is
also specified, this field value should be: 1. For Cloud SQL PSC enabled
instance - the dns_name field (e.g <uid>.<region>.sql.goog.). 2. For
Cloud SQL PSA instance (vpc peering) - the private ip of the instance.

**--port**:
Network port of the database.

**--private-key**:
Unencrypted PKCS#1 or PKCS#8 PEM-encoded private key associated with the Client
Certificate. The value for this flag needs to be the content of the certificate
file, not the path to the file. For example, on a Linux machine you can use
command substitution:
<code>--ca-certificate=$(</path/to/certificate_file.pem)</code>.
Database Migration Service encrypts the value when storing it.

**--ssl-type**:
The type of SSL configuration. `SSL_TYPE` must be one of:
`SERVER_ONLY`, `SERVER_CLIENT`, `REQUIRED`,
`NONE`.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--username**:
Username that Database Migration Service uses to connect to the database.
Database Migration Service encrypts the value when storing it.

**--clear-labels**

**--gcs-bucket**:
Cloud Storage bucket for the source SQL Server connection profile where the
backups are stored. This flag is used only for SQL Server to Cloud SQL
migrations.

**--gcs-prefix**:
Cloud Storage prefix path within the bucket for the source SQL Server connection
profile where the backups are stored. This flag is used only for SQL Server to
Cloud SQL migrations.

**--password**

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
gcloud alpha database-migration connection-profiles update
```