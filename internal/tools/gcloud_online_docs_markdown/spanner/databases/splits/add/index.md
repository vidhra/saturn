# gcloud spanner databases splits add  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/spanner/databases/splits/add](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/splits/add)*

**NAME**

: **gcloud spanner databases splits add - add split points to a  Spanner database**

**SYNOPSIS**

: **`gcloud spanner databases splits add` (`[DATABASE](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/splits/add#DATABASE)` : `[--instance](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/splits/add#--instance)`=`INSTANCE`) `[--splits-file](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/splits/add#--splits-file)`=`SPLITS_FILE` [`[--initiator](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/splits/add#--initiator)`=`INITIATOR`] [`[--split-expiration-date](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/splits/add#--split-expiration-date)`=`SPLIT_EXPIRATION_DATE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/spanner/databases/splits/add#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Add split points to a Spanner database.

**EXAMPLES**

: To add split points to the given Spanner database, run:

```
gcloud spanner databases splits add my-database-id --instance=my-instance-id --splits-file=path/to/splits.txt --initiator=my-initiator-string --split-expiration-date=2024-08-15T15:55:10Z
```

**POSITIONAL ARGUMENTS**

: **Database resource - The Cloud Spanner database on which to add split points. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
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

: **--splits-file**:
The path of a file containing split points to add to the database. Separate
split points in the file with a new line. The file format is
<ObjectType>[space]<ObjectName>[space]<Split Value>, where the
ObjectType is one of TABLE or INDEX and the Split Value is the split point key.
For index, the split point key is the index key with or without a full table key
prefix.

**OPTIONAL FLAGS**

: **--initiator**:
The tag to identify the initiator of the split points.

**--split-expiration-date**:
The date when the split points become system managed and becomes eligible for
merging. The default is 10 days from the date of creation. The maximum is 30
days from the date of creation.

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
gcloud alpha spanner databases splits add
```

```
gcloud beta spanner databases splits add
```