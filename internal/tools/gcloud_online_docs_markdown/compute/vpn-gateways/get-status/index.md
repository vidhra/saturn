# gcloud compute vpn-gateways get-status  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/vpn-gateways/get-status](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-gateways/get-status)*

**NAME**

: **gcloud compute vpn-gateways get-status - get status of a Compute Engine Highly Available VPN Gateway**

**SYNOPSIS**

: **`gcloud compute vpn-gateways get-status` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-gateways/get-status#NAME)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-gateways/get-status#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-gateways/get-status#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute vpn-gateways get-status` is used to display high
availability configuration status for the Cloud VPN gateway, the command will
show you the high availability configuration status for VPN tunnels associated
with each peer gateway to which the Cloud VPN gateway is connected; the peer
gateway could be either a Cloud VPN gateway or an external VPN gateway.

**EXAMPLES**

: To get status of a VPN gateway, run:

```
gcloud compute vpn-gateways get-status my-gateway --region=us-central1
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the VPN Gateway to describe.

**FLAGS**

: **--region**:
Region of the VPN Gateway to describe. If not specified, you might be prompted
to select a region (interactive mode only).
To avoid prompting when this flag is omitted, you can set the
``compute/region`` property:

```
gcloud config set compute/region REGION
```

A list of regions can be fetched by running:

```
gcloud compute regions list
```

To unset the property, run:

```
gcloud config unset compute/region
```

Alternatively, the region can be stored in the environment variable
``CLOUDSDK_COMPUTE_REGION``.

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

: These variants are also available:

```
gcloud alpha compute vpn-gateways get-status
```

```
gcloud beta compute vpn-gateways get-status
```