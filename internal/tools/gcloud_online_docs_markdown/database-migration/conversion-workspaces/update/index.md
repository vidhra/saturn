# gcloud database-migration conversion-workspaces update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/update](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/update)*

**NAME**

: **gcloud database-migration conversion-workspaces update - update a Database Migration Service conversion workspace**

**SYNOPSIS**

: **`gcloud database-migration conversion-workspaces update` (`[CONVERSION_WORKSPACE](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/update#CONVERSION_WORKSPACE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/update#--region)`=`REGION`) [`[--no-async](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/update#--async)`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/update#--display-name)`=`DISPLAY_NAME`] [`[--global-filter](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/update#--global-filter)`=`GLOBAL_FILTER`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/database-migration/conversion-workspaces/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Database Migration Service conversion workspace.

**EXAMPLES**

: To update a conversion workspace:

```
gcloud database-migration conversion-workspaces update my-conversion-workspace --region=us-central1 --display-name=new-display-name
```

**POSITIONAL ARGUMENTS**

: **Conversion workspace resource - The conversion workspace to update. The
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

**FLAGS**

: **--no-async**:
Waits for the operation in progress to complete before returning.

**--display-name**:
A user-friendly name for the conversion workspace. The display name can include
letters, numbers, spaces, and hyphens, and must start with a letter. The maximum
length allowed is 60 characters.

**--global-filter**:
Filter the source entities based on [AIP-160](https://google.aip.dev/160) standard. This filter will be
applied to all subsequent operations on the source entities, such as convert and
describe-entities.

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