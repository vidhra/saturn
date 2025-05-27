# gcloud datastream connection-profiles create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create)*

**NAME**

: **gcloud datastream connection-profiles create - create a Datastream connection profile**

**SYNOPSIS**

: **`gcloud datastream connection-profiles create` (`[CONNECTION_PROFILE](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#CONNECTION_PROFILE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--location)`=`LOCATION`) `[--display-name](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--display-name)`=`DISPLAY_NAME` `[--type](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--type)`=`TYPE` [`[--force](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--force)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--labels)`=[`KEY`=`VALUE`,…]] [[`[--bucket](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--bucket)`=`BUCKET` : `[--root-path](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--root-path)`=`ROOT_PATH`]     | `[--database-service](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--database-service)`=`DATABASE_SERVICE` `[--oracle-hostname](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--oracle-hostname)`=`ORACLE_HOSTNAME` `[--oracle-port](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--oracle-port)`=`ORACLE_PORT` `[--oracle-username](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--oracle-username)`=`ORACLE_USERNAME` (`[--oracle-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--oracle-password)`=`ORACLE_PASSWORD` | `[--oracle-prompt-for-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--oracle-prompt-for-password)` | `[--oracle-secret-manager-stored-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--oracle-secret-manager-stored-password)`=`ORACLE_SECRET_MANAGER_STORED_PASSWORD`)     | [`[--mongodb-host-addresses](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--mongodb-host-addresses)`=`IPv4_ADDRESS_OR_HOSTNAME`:`[PORT](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#PORT)`,[…] `[--mongodb-username](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--mongodb-username)`=`MONGODB_USERNAME` (`[--mongodb-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--mongodb-password)`=`MONGODB_PASSWORD` | `[--mongodb-prompt-for-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--mongodb-prompt-for-password)` | `[--mongodb-secret-manager-stored-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--mongodb-secret-manager-stored-password)`=`MONGODB_SECRET_MANAGER_STORED_PASSWORD`) (`[--mongodb-srv-connection-format](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--mongodb-srv-connection-format)` | `[--mongodb-standard-connection-format](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--mongodb-standard-connection-format)`) : `[--mongodb-direct-connection](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--mongodb-direct-connection)` `[--mongodb-replica-set](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--mongodb-replica-set)`=`MONGODB_REPLICA_SET`]     | [`[--mysql-hostname](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--mysql-hostname)`=`MYSQL_HOSTNAME` `[--mysql-port](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--mysql-port)`=`MYSQL_PORT` `[--mysql-username](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--mysql-username)`=`MYSQL_USERNAME` (`[--mysql-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--mysql-password)`=`MYSQL_PASSWORD` | `[--mysql-prompt-for-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--mysql-prompt-for-password)` | `[--mysql-secret-manager-stored-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--mysql-secret-manager-stored-password)`=`MYSQL_SECRET_MANAGER_STORED_PASSWORD`) : `[--ca-certificate](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--ca-certificate)`=`CA_CERTIFICATE` `[--client-certificate](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--client-certificate)`=`CLIENT_CERTIFICATE` `[--client-key](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--client-key)`=`CLIENT_KEY`]     | [`[--postgresql-database](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--postgresql-database)`=`POSTGRESQL_DATABASE` `[--postgresql-hostname](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--postgresql-hostname)`=`POSTGRESQL_HOSTNAME` `[--postgresql-port](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--postgresql-port)`=`POSTGRESQL_PORT` `[--postgresql-username](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--postgresql-username)`=`POSTGRESQL_USERNAME` (`[--postgresql-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--postgresql-password)`=`POSTGRESQL_PASSWORD` | `[--postgresql-prompt-for-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--postgresql-prompt-for-password)` | `[--postgresql-secret-manager-stored-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--postgresql-secret-manager-stored-password)`=`POSTGRESQL_SECRET_MANAGER_STORED_PASSWORD`) : [`[--postgresql-ca-certificate](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--postgresql-ca-certificate)`=`POSTGRESQL_CA_CERTIFICATE` : `[--postgresql-client-certificate](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--postgresql-client-certificate)`=`POSTGRESQL_CLIENT_CERTIFICATE` `[--postgresql-client-key](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--postgresql-client-key)`=`POSTGRESQL_CLIENT_KEY`]]     | `[--salesforce-domain](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--salesforce-domain)`=`SALESFORCE_DOMAIN` (`[--salesforce-oauth2-client-id](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--salesforce-oauth2-client-id)`=`SALESFORCE_OAUTH2_CLIENT_ID` (`[--salesforce-oauth2-client-secret](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--salesforce-oauth2-client-secret)`=`SALESFORCE_OAUTH2_CLIENT_SECRET` | `[--salesforce-prompt-for-oauth2-client-secret](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--salesforce-prompt-for-oauth2-client-secret)` | `[--salesforce-secret-manager-stored-oauth2-client-secret](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--salesforce-secret-manager-stored-oauth2-client-secret)`=`SALESFORCE_SECRET_MANAGER_STORED_OAUTH2_CLIENT_SECRET`) | `[--salesforce-username](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--salesforce-username)`=`SALESFORCE_USERNAME` (`[--salesforce-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--salesforce-password)`=`SALESFORCE_PASSWORD` | `[--salesforce-prompt-for-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--salesforce-prompt-for-password)` | `[--salesforce-secret-manager-stored-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--salesforce-secret-manager-stored-password)`=`SALESFORCE_SECRET_MANAGER_STORED_PASSWORD`) (`[--salesforce-prompt-for-security-token](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--salesforce-prompt-for-security-token)` | `[--salesforce-secret-manager-stored-security-token](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--salesforce-secret-manager-stored-security-token)`=`SALESFORCE_SECRET_MANAGER_STORED_SECURITY_TOKEN` | `[--salesforce-security-token](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--salesforce-security-token)`=`SALESFORCE_SECURITY_TOKEN`))     | `[--sqlserver-database](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--sqlserver-database)`=`SQLSERVER_DATABASE` `[--sqlserver-hostname](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--sqlserver-hostname)`=`SQLSERVER_HOSTNAME` `[--sqlserver-port](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--sqlserver-port)`=`SQLSERVER_PORT` `[--sqlserver-username](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--sqlserver-username)`=`SQLSERVER_USERNAME` (`[--sqlserver-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--sqlserver-password)`=`SQLSERVER_PASSWORD` | `[--sqlserver-prompt-for-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--sqlserver-prompt-for-password)` | `[--sqlserver-secret-manager-stored-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--sqlserver-secret-manager-stored-password)`=`SQLSERVER_SECRET_MANAGER_STORED_PASSWORD`)] [`[--private-connection](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--private-connection)`=`PRIVATE_CONNECTION`     | `[--static-ip-connectivity](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--static-ip-connectivity)`     | [`[--forward-ssh-hostname](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--forward-ssh-hostname)`=`FORWARD_SSH_HOSTNAME` `[--forward-ssh-username](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--forward-ssh-username)`=`FORWARD_SSH_USERNAME` (`[--forward-ssh-password](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--forward-ssh-password)`=`FORWARD_SSH_PASSWORD` | `[--forward-ssh-private-key](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--forward-ssh-private-key)`=`FORWARD_SSH_PRIVATE_KEY`) : `[--forward-ssh-port](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#--forward-ssh-port)`=`FORWARD_SSH_PORT`; default=22]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/datastream/connection-profiles/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Datastream connection profile

**EXAMPLES**

: To create a connection profile for Oracle:

```
gcloud datastream connection-profiles create CONNECTION_PROFILE --location=us-central1 --type=oracle --oracle-password=fakepassword --oracle-username=fakeuser --display-name=my-profile --oracle-hostname=35.188.150.50 --oracle-port=1521 --database-service=ORCL --static-ip-connectivity
```

To create a connection profile for MySQL:

```
gcloud datastream connection-profiles create CONNECTION_PROFILE --location=us-central1 --type=mysql --mysql-password=fakepassword --mysql-username=fakeuser --display-name=my-profile --mysql-hostname=35.188.150.50 --mysql-port=3306 --static-ip-connectivity
```

To create a connection profile for PostgreSQL:

```
gcloud datastream connection-profiles create CONNECTION_PROFILE --location=us-central1 --type=postgresql --postgresql-password=fakepassword --postgresql-username=fakeuser --display-name=my-profile --postgresql-hostname=35.188.150.50 --postgresql-port=5432 --postgresql-database=db --static-ip-connectivity
```

To create a connection profile for SQL Server:

```
gcloud datastream connection-profiles create CONNECTION_PROFILE --location=us-central1 --type=sqlserver --sqlserver-password=fakepassword --sqlserver-username=fakeuser --display-name=my-profile --sqlserver-hostname=35.188.150.50 --sqlserver-port=1433 --sqlserver-database=db --static-ip-connectivity
```

To create a connection profile for Salesforce using Username, Password and
Security Token:

```
gcloud datastream connection-profiles create CONNECTION_PROFILE --location=us-central1 --type=salesforce --salesforce-password=fakepassword --salesforce-username=fakeuser --salesforce-security-token=fakesecuritytoken --display-name=my-profile --salesforce-hostname=35.188.150.50 --salesforce-port=1433 --salesforce-database=db --static-ip-connectivity
```

To create a connection profile for Salesforce using OAuth:

```
gcloud datastream connection-profiles create CONNECTION_PROFILE --location=us-central1 --type=salesforce --salesforce-client-secret=fakesecret --salesforce-client-id=fake-client-id --display-name=my-profile --salesforce-domain=fakecompany.my.salesforce.com --static-ip-connectivity
```

To create a connection profile for Google Cloud Storage:

```
gcloud datastream connection-profiles create CONNECTION_PROFILE --location=us-central1 --type=google-cloud-storage --bucket=fake-bucket --root-path=/root/path --display-name=my-profile
```

To create a connection profile for BigQuery:

```
gcloud datastream connection-profiles create CONNECTION_PROFILE --location=us-central1 --type=bigquery --display-name=my-profile
```

To create a connection profile for MongoDB:

```
gcloud datastream connection-profiles create CONNECTION_PROFILE --location=us-central1 --type=mongodb --mongodb-password=fakepassword --mongodb-username=fakeuser --display-name=my-profile --mongodb-host-addresses=35.188.150.50:27017
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

**--location**:
The Cloud location for the connection_profile.
To set the `location` attribute:

- provide the argument `connection_profile` on the command line with a
fully specified name;
- provide the argument `--location` on the command line.**

**REQUIRED FLAGS**

: **--display-name**:
Friendly name for the connection profile.

**--type**:
Type can be MYSQL, ORACLE, POSTGRESQL, GOOGLE-CLOUD-STORAGE or BIGQUERY

**OPTIONAL FLAGS**

: **--force**:
Create the connection profile without validating it.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--bucket**

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

**NOTES**

: This variant is also available:

```
gcloud beta datastream connection-profiles create
```