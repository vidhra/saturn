# gcloud database-migration connection-profiles create postgresql  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/postgresql](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/postgresql)*

**NAME**

: **gcloud database-migration connection-profiles create postgresql - create a Database Migration Service connection profile for PostgreSQL**

**SYNOPSIS**

: **`gcloud database-migration connection-profiles create postgresql` (`[CONNECTION_PROFILE](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/postgresql#CONNECTION_PROFILE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/postgresql#--region)`=`REGION`) [`[--alloydb-cluster](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/postgresql#--alloydb-cluster)`=`ALLOYDB_CLUSTER`] [`[--no-async](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/postgresql#--async)`] [`[--cloudsql-instance](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/postgresql#--cloudsql-instance)`=`CLOUDSQL_INSTANCE`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/postgresql#--display-name)`=`DISPLAY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/postgresql#--labels)`=[`KEY`=`VALUE`,…]] [`[--role](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/postgresql#--role)`=`ROLE`] [`[--ca-certificate](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/postgresql#--ca-certificate)`=`CA_CERTIFICATE` : `[--ssl-type](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/postgresql#--ssl-type)`=`SSL_TYPE` `[--client-certificate](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/postgresql#--client-certificate)`=`CLIENT_CERTIFICATE` `[--private-key](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/postgresql#--private-key)`=`PRIVATE_KEY`] [`[--host](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/postgresql#--host)`=`HOST` `[--port](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/postgresql#--port)`=`PORT` `[--username](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/postgresql#--username)`=`USERNAME` (`[--password](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/postgresql#--password)`=`PASSWORD` | `[--prompt-for-password](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/postgresql#--prompt-for-password)`)] [`[--psc-service-attachment](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/postgresql#--psc-service-attachment)`=`PSC_SERVICE_ATTACHMENT`     | `[--static-ip-connectivity](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/postgresql#--static-ip-connectivity)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/postgresql#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Database Migration Service connection profile for PostgreSQL.

**EXAMPLES**

: To create a connection profile my-profile for PostgreSQL:

```
gcloud database-migration connection-profiles create postgresql my-profile --region=us-central1 --password=123456 --username=my-user --host=1.2.3.4 --port=5432
```

If the source is a Cloud SQL database, run:

```
gcloud database-migration connection-profiles create postgresql my-profile --region=us-central1 --password=123456 --username=my-user --host=1.2.3.4 --port=5432 --cloudsql-instance=my-instance
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

: **--alloydb-cluster**:
If the destination is an AlloyDB cluster, use this field to provide the AlloyDB
cluster ID.

**--no-async**:
Waits for the operation in progress to complete before returning.

**--cloudsql-instance**:
If the source or destination is a Cloud SQL database, then use this field to
provide the respective Cloud SQL instance ID.

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
`SERVER_ONLY`, `SERVER_CLIENT`, `REQUIRED`,
`NONE`.

**--client-certificate**:
x509 PEM-encoded certificate that will be used by the replica to authenticate
against the database server. The value for this flag needs to be the content of
the certificate file, not the path to the file. For example, on a Linux machine
you can use command substitution:
<code>--ca-certificate=$(</path/to/certificate_file.pem)</code>.
Database Migration Service encrypts the value when storing it.

**--private-key**:
Unencrypted PKCS#1 or PKCS#8 PEM-encoded private key associated with the Client
Certificate. The value for this flag needs to be the content of the certificate
file, not the path to the file. For example, on a Linux machine you can use
command substitution:
<code>--ca-certificate=$(</path/to/certificate_file.pem)</code>.
Database Migration Service encrypts the value when storing it.

**--host**:
IP or hostname of the database. When `--psc-service-attachment` is
also specified, this field value should be: 1. For Cloud SQL PSC enabled
instance - the dns_name field (e.g <uid>.<region>.sql.goog.). 2. For
Cloud SQL PSA instance (vpc peering) - the private ip of the instance.

**--port**:
Network port of the database.

**--username**:
Username that Database Migration Service uses to connect to the database.
Database Migration Service encrypts the value when storing it.

**--password**

**At most one of these can be specified:

**Service attachment resource - Resource ID of the service attachment. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--psc-service-attachment` on the command line
with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `region` attribute:

- provide the argument `--psc-service-attachment` on the command line
with a fully specified name;
- provide the argument `--region` on the command line.

**--psc-service-attachment**:
ID of the service_attachment or fully qualified identifier for the
service_attachment.
To set the `service_attachment` attribute:

- provide the argument `--psc-service-attachment` on the command line.**

**--static-ip-connectivity**:
use static ip connectivity**

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