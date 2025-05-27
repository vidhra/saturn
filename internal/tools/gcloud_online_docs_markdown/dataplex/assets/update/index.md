# gcloud dataplex assets update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/update](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/update)*

**NAME**

: **gcloud dataplex assets update - update a Dataplex asset resource**

**SYNOPSIS**

: **`gcloud dataplex assets update` (`[ASSET](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/update#ASSET)` : `[--lake](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/update#--lake)`=`LAKE` `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/update#--location)`=`LOCATION` `[--zone](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/update#--zone)`=`ZONE`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/update#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/update#--display-name)`=`DISPLAY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/update#--labels)`=[`KEY`=`VALUE`,…]] [`[--resource-read-access-mode](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/update#--resource-read-access-mode)`=`RESOURCE_READ_ACCESS_MODE`] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/update#--validate-only)`] [`[--[no-]discovery-enabled](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/update#--[no-]discovery-enabled)` `[--discovery-exclude-patterns](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/update#--discovery-exclude-patterns)`=[`EXCLUDE_PATTERNS`,…] `[--discovery-include-patterns](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/update#--discovery-include-patterns)`=[`INCLUDE_PATTERNS`,…] `[--discovery-schedule](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/update#--discovery-schedule)`=`DISCOVERY_SCHEDULE` `[--csv-delimiter](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/update#--csv-delimiter)`=`CSV_DELIMITER` `[--[no-]csv-disable-type-inference](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/update#--[no-]csv-disable-type-inference)` `[--csv-encoding](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/update#--csv-encoding)`=`CSV_ENCODING` `[--csv-header-rows](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/update#--csv-header-rows)`=`CSV_HEADER_ROWS` `[--[no-]json-disable-type-inference](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/update#--[no-]json-disable-type-inference)` `[--json-encoding](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/update#--json-encoding)`=`JSON_ENCODING`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/assets/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Dataplex asset resource.

**EXAMPLES**

: To update a Dataplex asset `test-asset` in zone
`test-zone` in lake `test-lake` in location
`us-central1` to have the display name
`first-dataplex-asset` and discovery include patterns
`abc`, `def`, run:

```
gcloud dataplex assets update test-asset --location=us-central1 --lake=test-lake --zone=test-zone --display-name="first-dataplex-asset" --discovery-include-patterns=abc,def
```

**POSITIONAL ARGUMENTS**

: **Assets resource - Arguments and flags that define the Dataplex asset you want to
update. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `asset` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ASSET`**:
ID of the assets or fully qualified identifier for the assets.
To set the `asset` attribute:

- provide the argument `asset` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--lake**:
The identifier of the Dataplex lake resource.
To set the `lake` attribute:

- provide the argument `asset` on the command line with a fully
specified name;
- provide the argument `--lake` on the command line.

**--location**:
The location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `asset` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.

**--zone**:
The identifier of the Dataplex zone resource.
To set the `zone` attribute:

- provide the argument `asset` on the command line with a fully
specified name;
- provide the argument `--zone` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Description of the asset

**--display-name**:
Display Name

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--resource-read-access-mode**

**--validate-only**:
Validate the update action, but don't actually perform it.

**--[no-]discovery-enabled**

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

: This variant is also available:

```
gcloud alpha dataplex assets update
```