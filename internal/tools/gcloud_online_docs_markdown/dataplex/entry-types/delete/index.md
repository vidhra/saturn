# gcloud dataplex entry-types delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/delete](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/delete)*

**NAME**

: **gcloud dataplex entry-types delete - delete a Dataplex Entry Type**

**SYNOPSIS**

: **`gcloud dataplex entry-types delete` (`[ENTRY_TYPE](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/delete#ENTRY_TYPE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/delete#--async)`] [`[--etag](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/delete#--etag)`=`ETAG`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataplex/entry-types/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a Dataplex Entry Type.

**EXAMPLES**

: To delete Entry Type `test-entry-type` in project
`test-project` and in location `us-central1`, run:

```
gcloud dataplex entry-types delete test-entry-type --location=us-central1 --project=test-project
```

**POSITIONAL ARGUMENTS**

: **Entry type resource - Arguments and flags that define the Dataplex Entry Type
you want to delete. The arguments in this group can be used to specify the
attributes of this resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `entry_type` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ENTRY_TYPE`**:
ID of the entry type or fully qualified identifier for the entry type.
To set the `entry_type` attribute:

- provide the argument `entry_type` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location of the Dataplex resource.
To set the `location` attribute:

- provide the argument `entry_type` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `dataplex/location`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--etag**:
etag for the Entry Type you want to delete.

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
gcloud alpha dataplex entry-types delete
```