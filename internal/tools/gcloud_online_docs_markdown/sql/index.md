# gcloud sql  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql](https://cloud.google.com/sdk/gcloud/reference/sql)*

**NAME**

: **gcloud sql - create and manage Google Cloud SQL databases**

**SYNOPSIS**

: **`gcloud sql` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/sql#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/sql#COMMAND)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: The gcloud sql command group lets you create and manage Google Cloud SQL
databases.
Cloud SQL is a fully-managed database service that makes it easy to set up,
maintain, manage, and administer your relational databases in the cloud.
More information on Cloud SQL can be found here: [https://cloud.google.com/sql](https://cloud.google.com/sql) and
detailed documentation can be found here: [https://cloud.google.com/sql/docs/](https://cloud.google.com/sql/docs/)

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**GROUPS**

: ``GROUP`` is one of the following:

**`[backups](https://cloud.google.com/sdk/gcloud/reference/sql/backups)`**:
Provide commands for working with backups of Cloud SQL instances.

**`[databases](https://cloud.google.com/sdk/gcloud/reference/sql/databases)`**:
Provide commands for managing databases of Cloud SQL instances.

**`[export](https://cloud.google.com/sdk/gcloud/reference/sql/export)`**:
Provide commands to export Cloud SQL instances.

**`[flags](https://cloud.google.com/sdk/gcloud/reference/sql/flags)`**:
Provide a command to list flags.

**`[import](https://cloud.google.com/sdk/gcloud/reference/sql/import)`**:
Provides commands to import Cloud SQL instances.

**`[instances](https://cloud.google.com/sdk/gcloud/reference/sql/instances)`**:
Provide commands for managing Cloud SQL instances.

**`[operations](https://cloud.google.com/sdk/gcloud/reference/sql/operations)`**:
Provide commands for working with Cloud SQL instance operations.

**`[ssl](https://cloud.google.com/sdk/gcloud/reference/sql/ssl)`**:
Provide commands for managing SSL certificates of Cloud SQL instances.

**`[ssl-certs](https://cloud.google.com/sdk/gcloud/reference/sql/ssl-certs)`**:
`(DEPRECATED)` Provide commands for managing SSL certificates of
Cloud SQL instances.

**`[tiers](https://cloud.google.com/sdk/gcloud/reference/sql/tiers)`**:
Provide a command to list tiers.

**`[users](https://cloud.google.com/sdk/gcloud/reference/sql/users)`**:
Provide commands for managing Cloud SQL users.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[connect](https://cloud.google.com/sdk/gcloud/reference/sql/connect)`**:
Connects to a Cloud SQL instance.

**`[generate-login-token](https://cloud.google.com/sdk/gcloud/reference/sql/generate-login-token)`**:
Generate an IAM login token for Cloud SQL.

**`[reschedule-maintenance](https://cloud.google.com/sdk/gcloud/reference/sql/reschedule-maintenance)`**:
Reschedule a Cloud SQL instance's maintenance.

**NOTES**

: These variants are also available:

```
gcloud alpha sql
```

```
gcloud beta sql
```