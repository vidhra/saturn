# gcloud datastream connection-profiles update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update)*

**NAME**

: **gcloud datastream connection-profiles update - update a Datastream connection profile**

**SYNOPSIS**

: **`gcloud datastream connection-profiles update` (`[CONNECTION_PROFILE](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#CONNECTION_PROFILE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--location)`=`LOCATION`) `[--type](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--type)`=`TYPE` [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--display-name)`=`DISPLAY_NAME`] [`[--force](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--force)`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--bucket](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--bucket)`=`BUCKET` `[--root-path](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--root-path)`=`ROOT_PATH`     | `[--database-service](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--database-service)`=`DATABASE_SERVICE` `[--oracle-hostname](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--oracle-hostname)`=`ORACLE_HOSTNAME` `[--oracle-port](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--oracle-port)`=`ORACLE_PORT` `[--oracle-username](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--oracle-username)`=`ORACLE_USERNAME` `[--oracle-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--oracle-password)`=`ORACLE_PASSWORD`     | `[--oracle-prompt-for-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--oracle-prompt-for-password)`     | `[--oracle-secret-manager-stored-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--oracle-secret-manager-stored-password)`=`ORACLE_SECRET_MANAGER_STORED_PASSWORD`     | `[--mongodb-direct-connection](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--mongodb-direct-connection)` `[--mongodb-host-addresses](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--mongodb-host-addresses)`=`IPv4_ADDRESS_OR_HOSTNAME`:`[PORT](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#PORT)`,[…] `[--mongodb-replica-set](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--mongodb-replica-set)`=`MONGODB_REPLICA_SET` `[--mongodb-username](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--mongodb-username)`=`MONGODB_USERNAME` `[--mongodb-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--mongodb-password)`=`MONGODB_PASSWORD`     | `[--mongodb-prompt-for-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--mongodb-prompt-for-password)`     | `[--mongodb-secret-manager-stored-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--mongodb-secret-manager-stored-password)`=`MONGODB_SECRET_MANAGER_STORED_PASSWORD` `[--mongodb-srv-connection-format](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--mongodb-srv-connection-format)`     | `[--mongodb-standard-connection-format](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--mongodb-standard-connection-format)`     | `[--mysql-hostname](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--mysql-hostname)`=`MYSQL_HOSTNAME` `[--mysql-port](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--mysql-port)`=`MYSQL_PORT` `[--mysql-username](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--mysql-username)`=`MYSQL_USERNAME` `[--ca-certificate](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--ca-certificate)`=`CA_CERTIFICATE` `[--client-certificate](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--client-certificate)`=`CLIENT_CERTIFICATE` `[--client-key](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--client-key)`=`CLIENT_KEY` `[--mysql-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--mysql-password)`=`MYSQL_PASSWORD`     | `[--mysql-prompt-for-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--mysql-prompt-for-password)`     | `[--mysql-secret-manager-stored-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--mysql-secret-manager-stored-password)`=`MYSQL_SECRET_MANAGER_STORED_PASSWORD`     | `[--postgresql-database](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--postgresql-database)`=`POSTGRESQL_DATABASE` `[--postgresql-hostname](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--postgresql-hostname)`=`POSTGRESQL_HOSTNAME` `[--postgresql-port](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--postgresql-port)`=`POSTGRESQL_PORT` `[--postgresql-username](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--postgresql-username)`=`POSTGRESQL_USERNAME` `[--postgresql-ca-certificate](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--postgresql-ca-certificate)`=`POSTGRESQL_CA_CERTIFICATE` `[--postgresql-client-certificate](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--postgresql-client-certificate)`=`POSTGRESQL_CLIENT_CERTIFICATE` `[--postgresql-client-key](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--postgresql-client-key)`=`POSTGRESQL_CLIENT_KEY` `[--postgresql-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--postgresql-password)`=`POSTGRESQL_PASSWORD`     | `[--postgresql-prompt-for-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--postgresql-prompt-for-password)`     | `[--postgresql-secret-manager-stored-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--postgresql-secret-manager-stored-password)`=`POSTGRESQL_SECRET_MANAGER_STORED_PASSWORD`     | `[--salesforce-domain](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--salesforce-domain)`=`SALESFORCE_DOMAIN` `[--salesforce-oauth2-client-id](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--salesforce-oauth2-client-id)`=`SALESFORCE_OAUTH2_CLIENT_ID` `[--salesforce-oauth2-client-secret](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--salesforce-oauth2-client-secret)`=`SALESFORCE_OAUTH2_CLIENT_SECRET`     | `[--salesforce-prompt-for-oauth2-client-secret](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--salesforce-prompt-for-oauth2-client-secret)`     | `[--salesforce-secret-manager-stored-oauth2-client-secret](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--salesforce-secret-manager-stored-oauth2-client-secret)`=`SALESFORCE_SECRET_MANAGER_STORED_OAUTH2_CLIENT_SECRET`     | `[--salesforce-username](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--salesforce-username)`=`SALESFORCE_USERNAME` `[--salesforce-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--salesforce-password)`=`SALESFORCE_PASSWORD`     | `[--salesforce-prompt-for-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--salesforce-prompt-for-password)`     | `[--salesforce-secret-manager-stored-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--salesforce-secret-manager-stored-password)`=`SALESFORCE_SECRET_MANAGER_STORED_PASSWORD` `[--salesforce-prompt-for-security-token](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--salesforce-prompt-for-security-token)`     | `[--salesforce-secret-manager-stored-security-token](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--salesforce-secret-manager-stored-security-token)`=`SALESFORCE_SECRET_MANAGER_STORED_SECURITY_TOKEN`     | `[--salesforce-security-token](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--salesforce-security-token)`=`SALESFORCE_SECURITY_TOKEN`     | `[--sqlserver-database](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--sqlserver-database)`=`SQLSERVER_DATABASE` `[--sqlserver-hostname](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--sqlserver-hostname)`=`SQLSERVER_HOSTNAME` `[--sqlserver-port](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--sqlserver-port)`=`SQLSERVER_PORT` `[--sqlserver-username](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--sqlserver-username)`=`SQLSERVER_USERNAME` `[--sqlserver-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--sqlserver-password)`=`SQLSERVER_PASSWORD`     | `[--sqlserver-prompt-for-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--sqlserver-prompt-for-password)`     | `[--sqlserver-secret-manager-stored-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--sqlserver-secret-manager-stored-password)`=`SQLSERVER_SECRET_MANAGER_STORED_PASSWORD`] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--remove-labels)`=[`KEY`,…]] [`[--private-connection](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--private-connection)`=`PRIVATE_CONNECTION`     | `[--static-ip-connectivity](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--static-ip-connectivity)`     | `[--forward-ssh-hostname](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--forward-ssh-hostname)`=`FORWARD_SSH_HOSTNAME` `[--forward-ssh-port](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--forward-ssh-port)`=`FORWARD_SSH_PORT`; default=22 `[--forward-ssh-username](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--forward-ssh-username)`=`FORWARD_SSH_USERNAME` `[--forward-ssh-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--forward-ssh-password)`=`FORWARD_SSH_PASSWORD`     | `[--forward-ssh-private-key](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#--forward-ssh-private-key)`=`FORWARD_SSH_PRIVATE_KEY`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates a Datastream connection profile

**EXAMPLES**

: To update a connection profile for Oracle:

```
gcloud datastream connection-profiles update CONNECTION_PROFILE --location=us-central1 --type=oracle --oracle-password=fakepassword --oracle-username=fakeuser --display-name=my-profile --oracle-hostname=35.188.150.50 --oracle-port=1521 --database-service=ORCL --static-ip-connectivity
```

To update a connection profile for MySQL:

```
gcloud datastream connection-profiles update CONNECTION_PROFILE --location=us-central1 --type=mysql --mysql-password=fakepassword --mysql-username=fakeuser --display-name=my-profile --mysql-hostname=35.188.150.50 --mysql-port=3306 --static-ip-connectivity
```

To update a connection profile for PostgreSQL:

```
gcloud datastream connection-profiles update CONNECTION_PROFILE --location=us-central1 --type=postgresql --postgresql-password=fakepassword --postgresql-username=fakeuser --display-name=my-profile --postgresql-hostname=35.188.150.50 --postgresql-port=5432 --postgresql-database=db --static-ip-connectivity
```

To update a connection profile for SQL Server:

```
gcloud datastream connection-profiles update CONNECTION_PROFILE --location=us-central1 --type=sqlserver --sqlserver-password=fakepassword --sqlserver-username=fakeuser --display-name=my-profile --sqlserver-hostname=35.188.150.50 --sqlserver-port=1433 --sqlserver-database=db --static-ip-connectivity
```

To update a connection profile for Salesforce:

```
gcloud datastream connection-profiles update CONNECTION_PROFILE --location=us-central1 --type=salesforce --salesforce-password=fakepassword --salesforce-username=fakeuser --display-name=my-profile --salesforce-domain=fakecompany.my.salesforce.com --static-ip-connectivity
```

To update a connection profile for Google Cloud Storage:

```
gcloud datastream connection-profiles update CONNECTION_PROFILE --location=us-central1 --type=google-cloud-storage --bucket=fake-bucket --root-path=/root/path --display-name=my-profile
```

To update a connection profile for BigQuery:

```
gcloud datastream connection-profiles update CONNECTION_PROFILE --location=us-central1 --type=bigquery --display-name=my-profile
```

To update a connection profile for MongoDB:

```
gcloud datastream connection-profiles update CONNECTION_PROFILE --location=us-central1 --type=mongodb --mongodb-password=fakepassword --mongodb-username=fakeuser --display-name=my-profile --mongodb-host-addresses=35.188.150.50:27017 --static-ip-connectivity
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

**--location**:
The Cloud location for the connection_profile.
To set the `location` attribute:

- provide the argument `connection_profile` on the command line with a
fully specified name;
- provide the argument `--location` on the command line.**

**REQUIRED FLAGS**

: **--type**:
Type can be MYSQL, ORACLE, POSTGRESQL, GOOGLE-CLOUD-STORAGE or BIGQUERY

**OPTIONAL FLAGS**

: **--display-name**:
Friendly name for the connection profile.

**--force**:
Update the connection profile without validating it.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--bucket**

**--clear-labels**

**At most one of these can be specified:

**Private connection resource - Resource ID of the private connection. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--private-connection` on the command line with
a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--private-connection` on the command line with
a fully specified name;
- provide the argument `--location` on the command line.

**--private-connection**:
ID of the private_connection or fully qualified identifier for the
private_connection.
To set the `private_connection` attribute:

- provide the argument `--private-connection` on the command line.**

**--static-ip-connectivity**:
use static ip connectivity

**--forward-ssh-hostname**:
Hostname for the SSH tunnel.

**--forward-ssh-port**:
Port for the SSH tunnel, default value is 22.

**--forward-ssh-username**:
Username for the SSH tunnel.

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

**NOTES**

: This variant is also available:

```
gcloud beta datastream connection-profiles update
```