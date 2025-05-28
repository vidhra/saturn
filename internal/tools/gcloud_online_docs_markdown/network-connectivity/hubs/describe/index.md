# gcloud network-connectivity hubs describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/describe](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/describe)*

**NAME**

: **gcloud network-connectivity hubs describe - describe a hub**

**SYNOPSIS**

: **`gcloud network-connectivity hubs describe` `[HUB](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/describe#HUB)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Retrieve and display details about a hub.

**EXAMPLES**

: To display details about a hub named
``my-hub``, run:

```
gcloud network-connectivity hubs describe my-hub
```

**POSITIONAL ARGUMENTS**

: **Hub resource - Name of the hub to be described. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `hub` on the command line with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`HUB`**:
ID of the hub or fully qualified identifier for the hub.
To set the `hub` attribute:

- provide the argument `hub` on the command line.**

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

: This command uses the `networkconnectivity/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest](https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest)

**NOTES**

: These variants are also available:

```
gcloud alpha network-connectivity hubs describe
```

```
gcloud beta network-connectivity hubs describe
```