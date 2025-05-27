# gcloud dataplex zones update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/update](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/update)*

**NAME**

: **gcloud dataplex zones update - update a Dataplex zone resource**

**SYNOPSIS**

: **`gcloud dataplex zones update` (`[ZONE](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/update#ZONE)` : `[--lake](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/update#--lake)`=`LAKE` `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/update#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/update#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/update#--display-name)`=`DISPLAY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/update#--labels)`=[`KEY`=`VALUE`,…]] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/update#--validate-only)`] [`[--[no-]discovery-enabled](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/update#--[no-]discovery-enabled)` `[--discovery-exclude-patterns](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/update#--discovery-exclude-patterns)`=[`EXCLUDE_PATTERNS`,…] `[--discovery-include-patterns](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/update#--discovery-include-patterns)`=[`INCLUDE_PATTERNS`,…] `[--discovery-schedule](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/update#--discovery-schedule)`=`DISCOVERY_SCHEDULE` `[--csv-delimiter](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/update#--csv-delimiter)`=`CSV_DELIMITER` `[--[no-]csv-disable-type-inference](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/update#--[no-]csv-disable-type-inference)` `[--csv-encoding](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/update#--csv-encoding)`=`CSV_ENCODING` `[--csv-header-rows](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/update#--csv-header-rows)`=`CSV_HEADER_ROWS` `[--[no-]json-disable-type-inference](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/update#--[no-]json-disable-type-inference)` `[--json-encoding](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/update#--json-encoding)`=`JSON_ENCODING`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Dataplex zone resource.

**EXAMPLES**

: To update a Dataplex zone `test-zone` in lake `test-lake`
in location `us-central1` to have the display name
`first-dataplex-zone` and discovery include patterns
`abc`, `def`, run:

```
gcloud dataplex zones update test-zone --location=us-central1 --lake=test-lake --display-name="first-dataplex-zone" --discovery-include-patterns=abc,def
```

**POSITIONAL ARGUMENTS**

: **Zones resource - Arguments and flags that define the Dataplex zone you want to
update. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `zone` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ZONE`**:
ID of the zones or fully qualified identifier for the zones.
To set the `zone` attribute:

- provide the argument `zone` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--lake**:
The identifier of the Dataplex lake resource.
To set the `lake` attribute:

- provide the argument `zone` on the command line with a fully
specified name;
- provide the argument `--lake` on the command line.

**--location**:
The location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `zone` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Description of the zone

**--display-name**:
Display Name

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--validate-only**:
Validate the create action, but don't actually perform it.

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
gcloud alpha dataplex zones update
```