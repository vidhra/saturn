# gcloud database-migration conversion-workspaces seed  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/seed](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/seed)*

**NAME**

: **gcloud database-migration conversion-workspaces seed - seed a Database Migration Service conversion workspace**

**SYNOPSIS**

: **`gcloud database-migration conversion-workspaces seed` (`[CONVERSION_WORKSPACE](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/seed#CONVERSION_WORKSPACE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/seed#--region)`=`REGION`) (`[--destination-connection-profile](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/seed#--destination-connection-profile)`=`DESTINATION_CONNECTION_PROFILE`     | `[--source-connection-profile](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/seed#--source-connection-profile)`=`SOURCE_CONNECTION_PROFILE`) [`[--no-async](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/seed#--async)`] [`[--auto-commit](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/seed#--auto-commit)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/seed#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Seed a Database Migration Service conversion workspace.

**EXAMPLES**

: To seed a conversion workspace:

```
gcloud database-migration conversion-workspaces seed my-conversion-workspace --region=us-central1 --source-connection-profile=cp1
```

**POSITIONAL ARGUMENTS**

: **Conversion workspace resource - The conversion workspace to seed. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
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

: **Exactly one of these must be specified:

**Connection profile resource - The connection profile to seed from. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--destination-connection-profile` on the
command line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `region` attribute:

- provide the argument `--destination-connection-profile` on the
command line with a fully specified name;
- provide the argument `--region` on the command line.

**--destination-connection-profile**:
ID of the connection_profile or fully qualified identifier for the
connection_profile.
To set the `connection_profile` attribute:

- provide the argument `--destination-connection-profile` on the
command line.**

**Connection profile resource - The connection profile to seed from. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--source-connection-profile` on the command
line with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `region` attribute:

- provide the argument `--source-connection-profile` on the command
line with a fully specified name;
- provide the argument `--region` on the command line.

**--source-connection-profile**:
ID of the connection_profile or fully qualified identifier for the
connection_profile.
To set the `connection_profile` attribute:

- provide the argument `--source-connection-profile` on the command
line.****

**OPTIONAL FLAGS**

: **--no-async**:
Waits for the operation in progress to complete before returning.

**--auto-commit**:
Auto commits the conversion workspace.

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