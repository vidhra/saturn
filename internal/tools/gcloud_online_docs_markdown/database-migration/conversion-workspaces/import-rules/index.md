# gcloud database-migration conversion-workspaces import-rules  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/import-rules](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/import-rules)*

**NAME**

: **gcloud database-migration conversion-workspaces import-rules - import mapping rules in a Database Migration Service conversion workspace**

**SYNOPSIS**

: **`gcloud database-migration conversion-workspaces import-rules` (`[CONVERSION_WORKSPACE](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/import-rules#CONVERSION_WORKSPACE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/import-rules#--region)`=`REGION`) `[--config-files](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/import-rules#--config-files)`=`CONGIF_FILE`,[`[CONGIF_FILE](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/import-rules#CONGIF_FILE)`,…] [`[--auto-commit](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/import-rules#--auto-commit)`] [`[--file-format](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/import-rules#--file-format)`=`FILE_FORMAT`; default="ORA2PG"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/import-rules#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Import mapping rules in a Database Migration Service conversion workspace from a
configuration file. For example, for Oracle to PostgreSQL migrations that could
be an Ora2Pg config file.

**EXAMPLES**

: To import rules in a conversion workspace:

```
gcloud database-migration conversion-workspaces import-rules my-conversion-workspace --region=us-central1 --file-format=ORA2PG --config-files=PATH1/config1.conf,PATH2/config2.conf
```

**POSITIONAL ARGUMENTS**

: **Conversion workspace resource - The conversion workspace to import rules. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `conversion_workspace` on the command line with
a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CONVERSION_WORKSPACE`**:
ID of the conversion_workspace or fully qualified identifier for the
conversion_workspace.
To set the `conversion_workspace` attribute:

- provide the argument `conversion_workspace` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The Cloud region for the conversion_workspace.
To set the `region` attribute:

- provide the argument `conversion_workspace` on the command line with
a fully specified name;
- provide the argument `--region` on the command line.**

**REQUIRED FLAGS**

: **--config-files**:
A list of files to import rules from. Either provide a single file path or if
multiple files are to be provided, each file should correspond to one schema.
Provide file paths as a comma separated list.

**OPTIONAL FLAGS**

: **--auto-commit**:
Auto commits the conversion workspace.

**--file-format**:
File format type to import rules from. `FILE_FORMAT` must
be (only one value is supported): `ORA2PG`.

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