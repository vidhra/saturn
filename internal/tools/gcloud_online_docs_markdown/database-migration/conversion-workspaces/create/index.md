# gcloud database-migration conversion-workspaces create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/create](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/create)*

**NAME**

: **gcloud database-migration conversion-workspaces create - create a Database Migration Service conversion workspace**

**SYNOPSIS**

: **`gcloud database-migration conversion-workspaces create` (`[CONVERSION_WORKSPACE](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/create#CONVERSION_WORKSPACE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/create#--region)`=`REGION`) `[--destination-database-engine](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/create#--destination-database-engine)`=`DESTINATION_DATABASE_ENGINE` `[--source-database-engine](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/create#--source-database-engine)`=`SOURCE_DATABASE_ENGINE` [`[--no-async](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/create#--async)`] [`[--destination-database-version](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/create#--destination-database-version)`=`DESTINATION_DATABASE_VERSION`; default="unspecified"] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/create#--display-name)`=`DISPLAY_NAME`] [`[--global-settings](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/create#--global-settings)`=[`KEY`=`VALUE`,…]] [`[--source-database-version](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/create#--source-database-version)`=`SOURCE_DATABASE_VERSION`; default="unspecified"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Database Migration Service conversion workspace.

**EXAMPLES**

: To create a conversion workspace:

```
gcloud database-migration conversion-workspaces create my-conversion-workspace --region=us-central1 --display-name=cw1 --source-database-engine=ORACLE --source-database-version=11 --destination-database-engine=POSTGRESQL --destination-database-version=8
```

**POSITIONAL ARGUMENTS**

: **Conversion workspace resource - The conversion workspace to create. The
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

: **--destination-database-engine**:
Destination database engine type.
`DESTINATION_DATABASE_ENGINE` must be (only one value is
supported): `POSTGRESQL`.

**--source-database-engine**:
Source database engine type. `SOURCE_DATABASE_ENGINE` must
be (only one value is supported): `ORACLE`.

**OPTIONAL FLAGS**

: **--no-async**:
Waits for the operation in progress to complete before returning.

**--destination-database-version**:
Version number for the database engine. The version number must contain numbers
and letters only. Example for PostgreSQL 17.0, version number will be 17.0.

**--display-name**:
A user-friendly name for the conversion workspace. The display name can include
letters, numbers, spaces, and hyphens, and must start with a letter. The maximum
length allowed is 60 characters.

**--global-settings**:
A generic list of settings for the workspace. The settings are database pair
dependant and can indicate default behavior for the mapping rules engine or turn
on or off specific features. An object containing a list of "key": "value"
pairs.

**--source-database-version**:
Version number for the database engine. The version number must contain numbers
and letters only. Example for Oracle 21c, version number will be 21c.

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