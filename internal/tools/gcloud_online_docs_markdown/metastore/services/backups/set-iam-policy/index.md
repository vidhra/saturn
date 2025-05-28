# gcloud metastore services backups set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/metastore/services/backups/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/metastore/services/backups/set-iam-policy)*

**NAME**

: **gcloud metastore services backups set-iam-policy - set the IAM policy for a backup**

**SYNOPSIS**

: **`gcloud metastore services backups set-iam-policy` (`[BACKUP](https://cloud.google.com/sdk/gcloud/reference/metastore/services/backups/set-iam-policy#BACKUP)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/metastore/services/backups/set-iam-policy#--location)`=`LOCATION` `[--service](https://cloud.google.com/sdk/gcloud/reference/metastore/services/backups/set-iam-policy#--service)`=`SERVICE`) `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/metastore/services/backups/set-iam-policy#POLICY_FILE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/metastore/services/backups/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Sets the IAM policy for the given backup as defined in a JSON or YAML file.
See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of the policy file format and contents.

**EXAMPLES**

: The following command will read an IAM policy defined in a JSON file
'policy.json' and set it for the backup 'my-backup':

```
gcloud metastore services backups set-iam-policy my-backup policy.json
```

**POSITIONAL ARGUMENTS**

: **Backup resource - Backup for which to display the IAM policy. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
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

**`POLICY_FILE`**:
Path to a local JSON or YAML formatted file containing a valid policy.
The output of the `get-iam-policy` command is a valid file, as is any
JSON or YAML file conforming to the structure of a [Policy](https://cloud.google.com/iam/reference/rest/v1/Policy).

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
gcloud alpha metastore services backups set-iam-policy
```

```
gcloud beta metastore services backups set-iam-policy
```