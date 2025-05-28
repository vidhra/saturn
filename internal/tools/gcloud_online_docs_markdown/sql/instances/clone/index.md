# gcloud sql instances clone  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/sql/instances/clone](https://cloud.google.com/sdk/gcloud/reference/sql/instances/clone)*

**NAME**

: **gcloud sql instances clone - clones a Cloud SQL instance**

**SYNOPSIS**

: **`gcloud sql instances clone` `[SOURCE](https://cloud.google.com/sdk/gcloud/reference/sql/instances/clone#SOURCE)` `[DESTINATION](https://cloud.google.com/sdk/gcloud/reference/sql/instances/clone#DESTINATION)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/sql/instances/clone#--async)`] [`[--preferred-secondary-zone](https://cloud.google.com/sdk/gcloud/reference/sql/instances/clone#--preferred-secondary-zone)`=`PREFERRED_SECONDARY_ZONE`] [`[--preferred-zone](https://cloud.google.com/sdk/gcloud/reference/sql/instances/clone#--preferred-zone)`=`PREFERRED_ZONE`] [`[--bin-log-file-name](https://cloud.google.com/sdk/gcloud/reference/sql/instances/clone#--bin-log-file-name)`=`BIN_LOG_FILE_NAME` `[--bin-log-position](https://cloud.google.com/sdk/gcloud/reference/sql/instances/clone#--bin-log-position)`=`BIN_LOG_POSITION`     | [`[--point-in-time](https://cloud.google.com/sdk/gcloud/reference/sql/instances/clone#--point-in-time)`=`POINT_IN_TIME` : `[--restore-database-name](https://cloud.google.com/sdk/gcloud/reference/sql/instances/clone#--restore-database-name)`=`RESTORE_DATABASE_NAME`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/sql/instances/clone#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud sql instances clone` creates a clone of a Cloud SQL instance.
The clone is an independent copy of the source instance with the same data and
settings. Source and destination instances must be in the same project. An
instance can be cloned from its current state, or from an earlier point in time.
For MySQL: The binary log coordinates or timestamp (point in time), if
specified, act as the point in time the source instance is cloned from. If not
specified, the current state of the instance is cloned.
For PostgreSQL: The point in time, if specified, defines a past state of the
instance to clone. If not specified, the current state of the instance is
cloned.
For SQL Server: The point in time, if specified, defines a past state of the
instance to clone. If not specified, the current state of the instance is
cloned.

**EXAMPLES**

: To clone an instance from its current state (most recent binary log
coordinates):

```
gcloud sql instances clone instance-foo instance-bar
```

To clone a MySQL instance from an earlier point in time (past binary log
coordinates):

```
gcloud sql instances clone instance-foo instance-bar --bin-log-file-name mysql-bin.000020 --bin-log-position 170
```

To clone a MySQL source instance at a specific point in time:

```
gcloud sql instances clone instance-foo instance-bar --point-in-time '2012-11-15T16:19:00.094Z'
```

To clone a PostgreSQL source instance at a specific point in time:

```
gcloud sql instances clone instance-foo instance-bar --point-in-time '2012-11-15T16:19:00.094Z'
```

To clone a SQL Server source instance at a specific point in time:

```
gcloud sql instances clone instance-foo instance-bar --point-in-time '2012-11-15T16:19:00.094Z'
```

**POSITIONAL ARGUMENTS**

: **`SOURCE`**:
Cloud SQL instance ID of the source.

**`DESTINATION`**:
Cloud SQL instance ID of the clone.

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--preferred-secondary-zone**:
The preferred secondary zone for the cloned regional instance. If you specify a
value for this flag, then the destination instance uses the value as the
secondary zone. The secondary zone can't be the same as the primary zone.

**--preferred-zone**:
The preferred zone for the cloned instance. If you specify a value for this
flag, then the destination instance uses the value as the primary zone.

**--bin-log-file-name**

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
gcloud alpha sql instances clone
```

```
gcloud beta sql instances clone
```