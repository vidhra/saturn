# gcloud firestore databases update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/firestore/databases/update](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/update)*

**NAME**

: **gcloud firestore databases update - update the database configuration of a Cloud Firestore database**

**SYNOPSIS**

: **`gcloud firestore databases update` [`[--async](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/update#--async)`] [`[--database](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/update#--database)`=`DATABASE`] [`[--delete-protection](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/update#--delete-protection)`] [`[--enable-pitr](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/update#--enable-pitr)`] [`[--type](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/update#--type)`=`TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/firestore/databases/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the database configuration of a Cloud Firestore database.

**EXAMPLES**

: The following command updates the database type of a Cloud Firestore database.

```
gcloud firestore databases update --type=firestore-native
```

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**Database resource - Cloud Firestore database to update. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `--database` on the command line with a fully
specified name;
- the default value of argument [--database] is `(default)` with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--database**:
ID of the database or fully qualified identifier for the database.
To set the `database` attribute:

- provide the argument `--database` on the command line;
- the default value of argument [--database] is `(default)`.**

**--delete-protection**:
If set to true, the Firestore database will be updated to have database delete
protection enabled. A database with delete protection enabled cannot be deleted.
You can disable the delete protection via --no-delete-protection.

**--enable-pitr**:
If set to true, the Firestore database will be updated to enable Point In Time
Recovery. You can disable the this feature via --no-enable-pitr.

**--type**:
The database type. `TYPE` must be one of:
`datastore-mode`, `firestore-native`.

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

: This command uses the `firestore/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/firestore](https://cloud.google.com/firestore)

**NOTES**

: These variants are also available:

```
gcloud alpha firestore databases update
```

```
gcloud beta firestore databases update
```