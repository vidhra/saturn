# gcloud edge-cloud container zones describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/zones/describe](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/zones/describe)*

**NAME**

: **gcloud edge-cloud container zones describe - describe an Edge Container zone**

**SYNOPSIS**

: **`gcloud edge-cloud container zones describe` `[ZONE](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/zones/describe#ZONE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/zones/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe an Edge Container zone.

**EXAMPLES**

: To display the metadata for the zone `us-central1-edge-operator-a`,
run:

```
gcloud edge-cloud container zones describe us-central1-edge-operator-a
```

**POSITIONAL ARGUMENTS**

: **Zone resource - The zone name. This represents a Cloud resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `zone` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ZONE`**:
ID of the zone or fully qualified identifier for the zone.
To set the `zone` attribute:

- provide the argument `zone` on the command line.**

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

: This command uses the `edgecontainer/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/edge-cloud](https://cloud.google.com/edge-cloud)

**NOTES**

: This variant is also available:

```
gcloud alpha edge-cloud container zones describe
```