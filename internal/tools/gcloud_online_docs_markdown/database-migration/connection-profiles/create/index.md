# gcloud database-migration connection-profiles create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create)*

**NAME**

: **gcloud database-migration connection-profiles create - create Database Migration Service connection profiles**

**SYNOPSIS**

: **`gcloud database-migration connection-profiles create` `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Commands for creating Database Migration Service connection profiles.

- Create a source connection profile with the `mysql` or
`postgresql` commands.
- Create a destination connection profile for a Cloud SQL instance with the
`cloudsql` command. For Cloud SQL instance as a source, use the
`create` command for the relevant engine type (e.g.
`mysql`).

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[alloydb](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/alloydb)`**:
Create a Database Migration Service connection profile for AlloyDB.

**`[cloudsql](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/cloudsql)`**:
Create a Database Migration Service connection profile for Cloud SQL.

**`[mysql](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/mysql)`**:
Create a Database Migration Service connection profile for MySQL.

**`[oracle](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/oracle)`**:
Create a Database Migration Service connection profile for Oracle.

**`[postgresql](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/postgresql)`**:
Create a Database Migration Service connection profile for PostgreSQL.

**`[sqlserver](https://cloud.google.com/sdk/gcloud/reference/database-migration/connection-profiles/create/sqlserver)`**:
Create a Database Migration Service connection profile for SQL Server.

**NOTES**

: This variant is also available:

```
gcloud alpha database-migration connection-profiles create
```