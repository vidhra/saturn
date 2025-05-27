# gcloud database-migration connection-profiles create sqlserver  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver)*

**NAME**

: **gcloud database-migration connection-profiles create sqlserver - create a Database Migration Service connection profile for SQL Server**

**SYNOPSIS**

: **`gcloud database-migration connection-profiles create sqlserver` (`[CONNECTION_PROFILE](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver#CONNECTION_PROFILE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver#--region)`=`REGION`) [`[--no-async](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver#--async)`] [`[--database](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver#--database)`=`DATABASE`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver#--display-name)`=`DISPLAY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver#--labels)`=[`KEY`=`VALUE`,…]] [`[--role](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver#--role)`=`ROLE`] [`[--ca-certificate](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver#--ca-certificate)`=`CA_CERTIFICATE` `[--ssl-type](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver#--ssl-type)`=`SSL_TYPE`] [[`[--gcs-bucket](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver#--gcs-bucket)`=`GCS_BUCKET` : `[--gcs-prefix](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver#--gcs-prefix)`=`GCS_PREFIX` `[--provider](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver#--provider)`=`PROVIDER`]     | `[--host](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver#--host)`=`HOST` `[--port](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver#--port)`=`PORT`] [`[--private-connection](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver#--private-connection)`=`PRIVATE_CONNECTION`     | `[--static-ip-connectivity](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver#--static-ip-connectivity)`     | [`[--forward-ssh-hostname](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver#--forward-ssh-hostname)`=`FORWARD_SSH_HOSTNAME` `[--forward-ssh-username](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver#--forward-ssh-username)`=`FORWARD_SSH_USERNAME` (`[--forward-ssh-password](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver#--forward-ssh-password)`=`FORWARD_SSH_PASSWORD` | `[--forward-ssh-private-key](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver#--forward-ssh-private-key)`=`FORWARD_SSH_PRIVATE_KEY`) : `[--forward-ssh-port](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver#--forward-ssh-port)`=`FORWARD_SSH_PORT`; default=22]] [`[--username](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver#--username)`=`USERNAME` (`[--password](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver#--password)`=`PASSWORD` | `[--prompt-for-password](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver#--prompt-for-password)`) : `[--cloudsql-instance](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver#--cloudsql-instance)`=`CLOUDSQL_INSTANCE` `[--cloudsql-project-id](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver#--cloudsql-project-id)`=`CLOUDSQL_PROJECT_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Database Migration Service connection profile for SQL Server.

**EXAMPLES**

: To create a source connection profile my-source-profile for SQL Server:

```
gcloud database-migration connection-profiles create sqlserver my-source-profile --region=us-central1 --gcs-bucket=bucket-name --gcs-prefix=prefix/path
```

To create a destination connection profile my-dest-profile for SQL Server:

```
gcloud database-migration connection-profiles create sqlserver my-dest-profile --region=us-central1 --cloudsql-instance=cloudsql-id
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

**FLAGS**

: **--no-async**:
Waits for the operation in progress to complete before returning.

**--database**:
The specific database within the host.

**--display-name**:
A user-friendly name for the connection profile. The display name can include
letters, numbers, spaces, and hyphens, and must start with a letter.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--role**:
The role of the connection profile. `ROLE` must be one of:
`SOURCE`, `DESTINATION`.

**--ca-certificate**:
x509 PEM-encoded certificate of the CA that signed the database server's
certificate. The value for this flag needs to be the content of the certificate
file, not the path to the file. For example, on a Linux machine you can use
command substitution:
<code>--ca-certificate=$(</path/to/certificate_file.pem)</code>.
Database Migration Service will use this certificate to verify it's connecting
to the correct host. Database Migration Service encrypts the value when storing
it.

**--ssl-type**:
The type of SSL configuration. `SSL_TYPE` must be one of:
`SERVER_ONLY`, `REQUIRED`, `NONE`.

**--gcs-bucket**

**At most one of these can be specified:

**Private connection resource - Resource ID of the private connection. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--private-connection` on the command line with
a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `region` attribute:

- provide the argument `--private-connection` on the command line with
a fully specified name;
- provide the argument `--region` on the command line.

**--private-connection**:
ID of the private_connection or fully qualified identifier for the
private_connection.
To set the `private_connection` attribute:

- provide the argument `--private-connection` on the command line.**

**--static-ip-connectivity**:
use static ip connectivity

**--forward-ssh-hostname**:
Hostname for the SSH tunnel.
This flag argument must be specified if any of the other arguments in this group
are specified.

**--forward-ssh-username**:
Username for the SSH tunnel.
This flag argument must be specified if any of the other arguments in this group
are specified.

**--forward-ssh-port**:
Port for the SSH tunnel, default value is 22.

**--forward-ssh-password****

**--username**:
Username that Database Migration Service uses to connect to the database for
metrics and observability. We highly recommend that you use the sqlserver user
for this. Database Migration Service encrypts the value when storing it.

**--cloudsql-instance**:
If the source or destination is a Cloud SQL database, then use this field to
provide the respective Cloud SQL instance ID.

**--cloudsql-project-id**:
The project id of the Cloud SQL instance. Only needed if the Cloud SQL instance
is in a different project than the connection profile. This is only supported
for source connection profiles for SQL Server.

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