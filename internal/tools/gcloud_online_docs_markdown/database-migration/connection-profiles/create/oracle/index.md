# gcloud database-migration connection-profiles create oracle  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/oracle](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/oracle)*

**NAME**

: **gcloud database-migration connection-profiles create oracle - create a Database Migration Service connection profile for Oracle**

**SYNOPSIS**

: **`gcloud database-migration connection-profiles create oracle` (`[CONNECTION_PROFILE](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/oracle#CONNECTION_PROFILE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/oracle#--region)`=`REGION`) `[--database-service](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/oracle#--database-service)`=`DATABASE_SERVICE` `[--host](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/oracle#--host)`=`HOST` `[--port](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/oracle#--port)`=`PORT` `[--username](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/oracle#--username)`=`USERNAME` (`[--password](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/oracle#--password)`=`PASSWORD`     | `[--prompt-for-password](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/oracle#--prompt-for-password)`) [`[--no-async](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/oracle#--async)`] [`[--ca-certificate](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/oracle#--ca-certificate)`=`CA_CERTIFICATE`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/oracle#--display-name)`=`DISPLAY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/oracle#--labels)`=[`KEY`=`VALUE`,…]] [`[--role](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/oracle#--role)`=`ROLE`] [`[--private-connection](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/oracle#--private-connection)`=`PRIVATE_CONNECTION`     | `[--static-ip-connectivity](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/oracle#--static-ip-connectivity)`     | [`[--forward-ssh-hostname](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/oracle#--forward-ssh-hostname)`=`FORWARD_SSH_HOSTNAME` `[--forward-ssh-username](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/oracle#--forward-ssh-username)`=`FORWARD_SSH_USERNAME` (`[--forward-ssh-password](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/oracle#--forward-ssh-password)`=`FORWARD_SSH_PASSWORD` | `[--forward-ssh-private-key](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/oracle#--forward-ssh-private-key)`=`FORWARD_SSH_PRIVATE_KEY`) : `[--forward-ssh-port](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/oracle#--forward-ssh-port)`=`FORWARD_SSH_PORT`; default=22]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/oracle#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Database Migration Service connection profile for Oracle.

**EXAMPLES**

: To create a connection profile my-profile for Oracle:

```
gcloud database-migration connection-profiles create oracle my-profile --region=us-central1 --password=123456 --username=my-user --host=1.2.3.4 --port=5432
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

: **--database-service**:
database service for the oracle connection profile.

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

**OPTIONAL FLAGS**

: **--no-async**:
Waits for the operation in progress to complete before returning.

**--ca-certificate**:
x509 PEM-encoded certificate of the CA that signed the database server's
certificate. The value for this flag needs to be the content of the certificate
file, not the path to the file. For example, on a Linux machine you can use
command substitution:
<code>--ca-certificate=$(</path/to/certificate_file.pem)</code>.
Database Migration Service will use this certificate to verify it's connecting
to the correct host. Database Migration Service encrypts the value when storing
it.

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