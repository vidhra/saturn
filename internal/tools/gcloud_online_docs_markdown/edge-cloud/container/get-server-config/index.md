# gcloud edge-cloud container get-server-config  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/get-server-config](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/get-server-config)*

**NAME**

: **gcloud edge-cloud container get-server-config - get server config**

**SYNOPSIS**

: **`gcloud edge-cloud container get-server-config` [`[--location](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/get-server-config#--location)`=`LOCATION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/get-server-config#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud edge-cloud container get-server-config` gets the server
configuration for an Edge Container location. This configuration includes the
default cluster version, the supported cluster versions and version
configuration for each release channel.

**EXAMPLES**

: To get server config in region us-central1, run:

```
gcloud edge-cloud container get-server-config --location=us-central1
```

**FLAGS**

: **Location resource - The location of the server configuration. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- set the property `edge_container/location` with a fully specified
name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--location**:
ID of the location or fully qualified identifier for the location.
To set the `location` attribute:

- provide the argument `--location` on the command line;
- set the property `edge_container/location`.**

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
gcloud alpha edge-cloud container get-server-config
```