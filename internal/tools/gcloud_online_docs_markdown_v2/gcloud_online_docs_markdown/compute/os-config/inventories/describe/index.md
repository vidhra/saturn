# gcloud compute os-config inventories describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/os-config/inventories/describe](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/inventories/describe)*

**NAME**

: **gcloud compute os-config inventories describe - describe the inventory data for a Compute Engine VM instance**

**SYNOPSIS**

: **`gcloud compute os-config inventories describe` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/inventories/describe#INSTANCE)` [`[--location](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/inventories/describe#--location)`=`LOCATION`] [`[--view](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/inventories/describe#--view)`=`VIEW`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/os-config/inventories/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe the inventory data for a Compute Engine VM instance.

**EXAMPLES**

: To describe the inventory of an instance `my-instance` that has the
instance ID `5678` in the current project and location
'us-central1-a', run:

```
gcloud compute os-config inventories describe my-instance --location=us-central1-a
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE`**:
ID or name of the Compute Engine VM instance to describe. For details on valid
instance IDs, refer to the criteria documented under the field `id`
at: [https://cloud.google.com/compute/docs/reference/rest/v1/instances](https://cloud.google.com/compute/docs/reference/rest/v1/instances)

**FLAGS**

: **--location**:
Location of the Compute Engine VM instance to describe. If not specified, the
property `compute/zone` is used. For details on setting properties,
see: [https://cloud.google.com/sdk/docs/properties](https://cloud.google.com/sdk/docs/properties)

**--view**:
Specifies what information should be included in the output. If unspecified, the
default view is `basic`. `VIEW` must be one of:

**`basic`**:
Output is limited to operating system details.

**`full`**:
Output includes operating system details and package information.

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

: This command uses the `osconfig/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/compute/docs/osconfig/rest](https://cloud.google.com/compute/docs/osconfig/rest)

**NOTES**

: This variant is also available:

```
gcloud alpha compute os-config inventories describe
```