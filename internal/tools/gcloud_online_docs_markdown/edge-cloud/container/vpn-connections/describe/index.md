# gcloud edge-cloud container vpn-connections describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/vpn-connections/describe](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/vpn-connections/describe)*

**NAME**

: **gcloud edge-cloud container vpn-connections describe - show details about a VPN connection**

**SYNOPSIS**

: **`gcloud edge-cloud container vpn-connections describe` (`[VPN_CONNECTION](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/vpn-connections/describe#VPN_CONNECTION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/vpn-connections/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/container/vpn-connections/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Show details about a VPN connection.

**EXAMPLES**

: To show details about the VPN connection 'test-vpn-connection' at region
us-central1, run:

```
gcloud edge-cloud container vpn-connections describe test-vpn-connection --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Vpn connection resource - VPN connection you want to describe. The arguments in
this group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `vpn_connection` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`VPN_CONNECTION`**:
ID of the vpn connection or fully qualified identifier for the vpn connection.
To set the `vpn_connection` attribute:

- provide the argument `vpn_connection` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The global location name.
To set the `location` attribute:

- provide the argument `vpn_connection` on the command line with a
fully specified name;
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
gcloud alpha edge-cloud container vpn-connections describe
```