# gcloud spanner databases execute-sql  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/databases/execute-sql](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/execute-sql)*

**NAME**

: **gcloud spanner databases execute-sql - executes a SQL query against a Cloud Spanner database**

**SYNOPSIS**

: **`gcloud spanner databases execute-sql` (`[DATABASE](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/execute-sql#DATABASE)` : `[--instance](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/execute-sql#--instance)`=`INSTANCE`) `[--sql](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/execute-sql#--sql)`=`SQL` [`[--database-role](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/execute-sql#--database-role)`=`DATABASE_ROLE`] [`[--enable-partitioned-dml](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/execute-sql#--enable-partitioned-dml)`] [`[--priority](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/execute-sql#--priority)`=`PRIORITY`] [`[--query-mode](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/execute-sql#--query-mode)`=`QUERY_MODE`; default="NORMAL"] [`[--timeout](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/execute-sql#--timeout)`=`TIMEOUT`; default="10m"] [`[--read-timestamp](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/execute-sql#--read-timestamp)`=`TIMESTAMP`     | `[--strong](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/execute-sql#--strong)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/execute-sql#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Executes a SQL query against a Cloud Spanner database.

**EXAMPLES**

: To execute a SQL SELECT statement against example-database under
example-instance, run:

```
gcloud spanner databases execute-sql example-database --instance=example-instance --sql='SELECT * FROM MyTable WHERE MyKey = 1'
```

**POSITIONAL ARGUMENTS**

: **Database resource - The Cloud Spanner database to execute the SQL query against.
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `database` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`DATABASE`**:
ID of the database or fully qualified identifier for the database.
To set the `database` attribute:

- provide the argument `database` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--instance**:
The Cloud Spanner instance for the database.
To set the `instance` attribute:

- provide the argument `database` on the command line with a fully
specified name;
- provide the argument `--instance` on the command line;
- set the property `spanner/instance`.**

**REQUIRED FLAGS**

: **--sql**:
The SQL query to issue to the database. Cloud Spanner SQL is described at [https://cloud.google.com/spanner/docs/query-syntax](https://cloud.google.com/spanner/docs/query-syntax)

**OPTIONAL FLAGS**

: **--database-role**:
Database role user assumes while accessing the database.

**--enable-partitioned-dml**:
Execute DML statement using Partitioned DML

**--priority**:
The priority for the execute SQL request. `PRIORITY` must
be one of: `high`, `low`, `medium`,
`unspecified`.

**--query-mode**:
Mode in which the query must be processed. `QUERY_MODE`
must be one of:

**`NORMAL`**:
Returns only the query result, without any information about the query plan.

**`PLAN`**:
Returns only the query plan, without any result rows or execution statistics
information.

**`PROFILE`**:
Returns the query plan, overall execution statistics, operator-level execution
statistics, along with the result rows.

**`WITH_PLAN_AND_STATS`**:
Returns the query plan, overall (but not operator-level) execution statistics,
along with the results.

**`WITH_STATS`**:
Returns the overall (but not operator-level) execution statistics along with the
results.

**--timeout**:
Maximum time to wait for the SQL query to complete. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on duration formats.

**--read-timestamp**

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

: These variants are also available:

```
gcloud alpha spanner databases execute-sql
```

```
gcloud beta spanner databases execute-sql
```