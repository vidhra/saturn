# gcloud dataplex zones create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/create](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/create)*

**NAME**

: **gcloud dataplex zones create - create a zone**

**SYNOPSIS**

: **`gcloud dataplex zones create` (`[ZONE](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/create#ZONE)` : `[--lake](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/create#--lake)`=`LAKE` `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/create#--location)`=`LOCATION`) `[--resource-location-type](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/create#--resource-location-type)`=`RESOURCE_LOCATION_TYPE` `[--type](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/create#--type)`=`TYPE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/create#--description)`=`DESCRIPTION`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/create#--display-name)`=`DISPLAY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/create#--validate-only)`] [`[--[no-]discovery-enabled](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/create#--[no-]discovery-enabled)` `[--discovery-exclude-patterns](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/create#--discovery-exclude-patterns)`=[`EXCLUDE_PATTERNS`,…] `[--discovery-include-patterns](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/create#--discovery-include-patterns)`=[`INCLUDE_PATTERNS`,…] `[--discovery-schedule](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/create#--discovery-schedule)`=`DISCOVERY_SCHEDULE` `[--csv-delimiter](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/create#--csv-delimiter)`=`CSV_DELIMITER` `[--[no-]csv-disable-type-inference](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/create#--[no-]csv-disable-type-inference)` `[--csv-encoding](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/create#--csv-encoding)`=`CSV_ENCODING` `[--csv-header-rows](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/create#--csv-header-rows)`=`CSV_HEADER_ROWS` `[--[no-]json-disable-type-inference](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/create#--[no-]json-disable-type-inference)` `[--json-encoding](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/create#--json-encoding)`=`JSON_ENCODING`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: A zone represents a logical group of related assets within a lake. A zone can be
used to map to organizational structure or represent stages of data readiness
from raw to curated. It provides managing behavior that is shared or inherited
by all contained assets.
The Zone ID is used to generate names such as database and dataset names when
publishing metadata to Hive Metastore and BigQuery.

- Must contain only lowercase letters, numbers, and hyphens.
- Must start with a letter.
- Must end with a number or a letter.
- Must be between 1-63 characters.
- Must be unique across all lakes from all locations in a project.

**EXAMPLES**

: To create a Dataplex zone with name `test-zone` within lake
`test-lake` in location `us-central1` with type
`RAW`, and resource location type `SINGLE_REGION`, run:

```
gcloud dataplex zones create test-zone --location=us-central --lake=test-lake --resource-location-type=SINGLE_REGION --type=RAW
```

To create a Dataplex zone with name `test-zone` within lake
`test-lake` in location `us-central1` with type
`RAW`,resource location type `SINGLE_REGION` with
discovery-enabled and discovery schedule `0 * * * *`, run:

```
gcloud dataplex zones create test-zone --location=us-central --lake=test-lake --resource-location-type=SINGLE_REGION --type=RAW --discovery-enabled --discovery-schedule="0 * * * *"
```

**POSITIONAL ARGUMENTS**

: **Zones resource - Arguments and flags that define the Dataplex zone you want to
create. The arguments in this group can be used to specify the attributes of
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

**REQUIRED FLAGS**

: **--resource-location-type**

**--type**:
Type. `TYPE` must be one of:

**`CURATED`**:
A zone that contains data that is considered to be ready for broader consumption
and analytics workloads. Curated structured data stored in Cloud Storage must
conform to certain file formats (Parquet, Avro, and Orc) and organized in a
hive-compatible directory layout.

**`RAW`**:
A zone that contains data that needs further processing before it is considered
generally ready for consumption and analytics workloads.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Description of the zone.

**--display-name**:
Display name of the zone.

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
gcloud alpha dataplex zones create
```