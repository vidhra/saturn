# gcloud compute target-vpn-gateways create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/target-vpn-gateways/create](https://cloud.google.com/sdk/gcloud/reference/compute/target-vpn-gateways/create)*

**NAME**

: **gcloud compute target-vpn-gateways create - create a Cloud VPN Classic Target VPN Gateway**

**SYNOPSIS**

: **`gcloud compute target-vpn-gateways create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/target-vpn-gateways/create#NAME)` `[--network](https://cloud.google.com/sdk/gcloud/reference/compute/target-vpn-gateways/create#--network)`=`NETWORK` [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/target-vpn-gateways/create#--description)`=`DESCRIPTION`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/target-vpn-gateways/create#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/target-vpn-gateways/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute target-vpn-gateways create` is used to create a Cloud
VPN Classic Target VPN Gateway. A Target VPN Gateway can reference one or more
VPN tunnels that connect it to the remote tunnel endpoint. A Target VPN Gateway
may also be referenced by one or more forwarding rules that define which packets
the gateway is responsible for routing.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the Target VPN Gateway to create.

**REQUIRED FLAGS**

: **--network**:
A reference to a network in this project to contain the VPN Gateway.

**OPTIONAL FLAGS**

: **--description**:
An optional, textual description for the target VPN Gateway.

**--region**:
Region of the Target VPN Gateway to create. If not specified, you might be
prompted to select a region (interactive mode only).
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
gcloud alpha compute target-vpn-gateways create
```

```
gcloud beta compute target-vpn-gateways create
```