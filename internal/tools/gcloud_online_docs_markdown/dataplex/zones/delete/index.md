# gcloud dataplex zones delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/delete](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/delete)*

**NAME**

: **gcloud dataplex zones delete - delete a Dataplex zone resource**

**SYNOPSIS**

: **`gcloud dataplex zones delete` (`[ZONE](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/delete#ZONE)` : `[--lake](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/delete#--lake)`=`LAKE` `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/zones/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a Dataplex zone resource.

**EXAMPLES**

: To delete a Dataplex zone `test-zone` within lake
`test-lake` in location `us-central1`, run:

```
gcloud dataplex zones delete test-lake --location=us-central1 --lake=test-lake
```

**POSITIONAL ARGUMENTS**

: **Zone resource - Arguments and flags that define the Dataplex zone you want to
delete. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `zone` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ZONE`**:
ID of the zone or fully qualified identifier for the zone.
To set the `zone` attribute:

- provide the argument `zone` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--lake**:
Identifier of the Dataplex lake resource.
To set the `lake` attribute:

- provide the argument `zone` on the command line with a fully
specified name;
- provide the argument `--lake` on the command line.

**--location**:
Location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `zone` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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

: This command uses the `dataplex/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/dataplex/docs](https://cloud.google.com/dataplex/docs)

**NOTES**

: This variant is also available:

```
gcloud alpha dataplex zones delete
```