# gcloud network-connectivity hubs accept-spoke  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/accept-spoke](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/accept-spoke)*

**NAME**

: **gcloud network-connectivity hubs accept-spoke - accept a spoke into a hub**

**SYNOPSIS**

: **`gcloud network-connectivity hubs accept-spoke` `[HUB](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/accept-spoke#HUB)` `[--spoke](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/accept-spoke#--spoke)`=`SPOKE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/accept-spoke#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-connectivity/hubs/accept-spoke#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Accept a proposed or previously rejected VPC spoke. By accepting a spoke, you
permit connectivity between the associated VPC network and other VPC networks
that are attached to the same hub.

**EXAMPLES**

: To accept a spoke named ``my-spoke`` into a hub
named ``my-hub``, run:

```
gcloud network-connectivity hubs accept-spoke my-hub --spoke="https://www.googleapis.com/networkconnectivity/v1/proje\
 cts/spoke-project/locations/global/hubs/my-spoke"
```

**POSITIONAL ARGUMENTS**

: **Hub resource - Name of the hub to accept the spoke into. This represents a Cloud
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

**REQUIRED FLAGS**

: **--spoke**:
URI of the spoke to accept

**OPTIONAL FLAGS**

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

: This command uses the networkconnectivity/v1 API. The full documentation for
this API can be found at: [https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest](https://cloud.google.com/network-connectivity/docs/reference/networkconnectivity/rest)

**NOTES**

: This variant is also available:

```
gcloud beta network-connectivity hubs accept-spoke
```