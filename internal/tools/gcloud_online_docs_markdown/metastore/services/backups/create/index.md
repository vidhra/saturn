# gcloud metastore services backups create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/metastore/services/backups/create](https://cloud.google.com/sdk/gcloud/reference/metastore/services/backups/create)*

**NAME**

: **gcloud metastore services backups create - backup a service**

**SYNOPSIS**

: **`gcloud metastore services backups create` (`[BACKUP](https://cloud.google.com/sdk/gcloud/reference/metastore/services/backups/create#BACKUP)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/metastore/services/backups/create#--location)`=`LOCATION` `[--service](https://cloud.google.com/sdk/gcloud/reference/metastore/services/backups/create#--service)`=`SERVICE`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/metastore/services/backups/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/metastore/services/backups/create#--description)`=`DESCRIPTION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/metastore/services/backups/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Backup metadata and the resource configuration of a service.

**EXAMPLES**

: To make a backup named `my-backup` and description `test
description` of the service `my-service`, run:

```
gcloud metastore services backups create my-backup --service=my-service --description='test description'
```

**POSITIONAL ARGUMENTS**

: **Backup resource - Arguments and flags that specify the backup you want to
create. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `backup` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`BACKUP`**:
ID of the backup or fully qualified identifier for the backup.
To set the `backup` attribute:

- provide the argument `backup` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the Dataproc Metastore service.
If not specified, will use `default` metastore/location.
To set the `location` attribute:

- provide the argument `backup` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `metastore/location`.

**--service**:
The identifier of the Dataproc Metastore service
To set the `service` attribute:

- provide the argument `backup` on the command line with a fully
specified name;
- provide the argument `--service` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
The description of this backup.

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

**API REFERENCE**

: This command uses the `metastore/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/dataproc-metastore/docs](https://cloud.google.com/dataproc-metastore/docs)

**NOTES**

: These variants are also available:

```
gcloud alpha metastore services backups create
```

```
gcloud beta metastore services backups create
```