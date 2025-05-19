# gcloud compute vpn-tunnels create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels/create](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels/create)*

**NAME**

: **gcloud compute vpn-tunnels create - create a VPN tunnel**

**SYNOPSIS**

: **`gcloud compute vpn-tunnels create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels/create#NAME)` `[--shared-secret](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels/create#--shared-secret)`=`SHARED_SECRET` (`[--peer-address](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels/create#--peer-address)`=`PEER_ADDRESS`     | `[--peer-external-gateway](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels/create#--peer-external-gateway)`=`PEER_EXTERNAL_GATEWAY`     | `[--peer-gcp-gateway](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels/create#--peer-gcp-gateway)`=`PEER_GCP_GATEWAY`     | `[--peer-gcp-gateway-region](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels/create#--peer-gcp-gateway-region)`=`PEER_GCP_GATEWAY_REGION`) (`[--target-vpn-gateway](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels/create#--target-vpn-gateway)`=`TARGET_VPN_GATEWAY`     | `[--target-vpn-gateway-region](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels/create#--target-vpn-gateway-region)`=`TARGET_VPN_GATEWAY_REGION`     | `[--vpn-gateway](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels/create#--vpn-gateway)`=`VPN_GATEWAY`     | `[--vpn-gateway-region](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels/create#--vpn-gateway-region)`=`VPN_GATEWAY_REGION`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels/create#--description)`=`DESCRIPTION`] [`[--ike-version](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels/create#--ike-version)`=`IKE_VERSION`] [`[--interface](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels/create#--interface)`=`INTERFACE`] [`[--local-traffic-selector](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels/create#--local-traffic-selector)`=`CIDR`,[`[CIDR](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels/create#CIDR)`,…]] [`[--peer-external-gateway-interface](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels/create#--peer-external-gateway-interface)`=`PEER_EXTERNAL_GATEWAY_INTERFACE`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels/create#--region)`=`REGION`] [`[--remote-traffic-selector](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels/create#--remote-traffic-selector)`=`CIDR`,[`[CIDR](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels/create#CIDR)`,…]] [`[--router](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels/create#--router)`=`ROUTER`] [`[--router-region](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels/create#--router-region)`=`ROUTER_REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/vpn-tunnels/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute vpn-tunnels create` is used to create a Classic VPN
tunnel between a target VPN gateway in Google Cloud Platform and a peer address;
or create Highly Available VPN tunnel between HA VPN gateway and another HA VPN
gateway, or Highly Available VPN tunnel between HA VPN gateway and an external
VPN gateway.

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the VPN Tunnel to create.

**REQUIRED FLAGS**

: **--shared-secret**:
Shared secret consisting of printable characters. Valid arguments match the
regular expression [ -~]+

**--peer-address**

**--target-vpn-gateway**

**OPTIONAL FLAGS**

: **--description**:
An optional, textual description for the VPN tunnel.

**--ike-version**:
Internet Key Exchange protocol version number. Default is 2.
`IKE_VERSION` must be one of: `1`,
`2`.

**--interface**:
Numeric interface ID of the VPN gateway with which this VPN tunnel is
associated. This flag is required if the tunnel is being attached to a Highly
Available VPN gateway. This option is only available for use with Highly
Available VPN gateway and must be omitted if the tunnel is going to be connected
to a Classic VPN gateway. `INTERFACE` must be one of:
`0`, `1`.

**--local-traffic-selector**:
Traffic selector is an agreement between IKE peers to permit traffic through a
tunnel if the traffic matches a specified pair of local and remote addresses.
--local-traffic-selector allows to configure the local addresses that are
permitted. The value should be a comma separated list of CIDR formatted strings.
Example: 192.168.0.0/16,10.0.0.0/24.
Local traffic selector must be specified only for VPN tunnels that do not use
dynamic routing with a Cloud Router. Omit this flag when creating a tunnel using
dynamic routing, including a tunnel for a Highly Available VPN gateway.

**--peer-external-gateway-interface**:
Interface ID of the external VPN gateway to which this VPN tunnel is connected
to. This flag is required if the tunnel is being created from a Highly Available
VPN gateway to an External Vpn Gateway.
`PEER_EXTERNAL_GATEWAY_INTERFACE` must be one of:
`0`, `1`, `2`, `3`.

**--region**:
Region of the VPN Tunnel to create. If not specified, you might be prompted to
select a region (interactive mode only).
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

**--remote-traffic-selector**:
Traffic selector is an agreement between IKE peers to permit traffic through a
tunnel if the traffic matches a specified pair of local and remote addresses.
--remote-traffic-selector allows to configure the remote addresses that are
permitted. The value should be a comma separated list of CIDR formatted strings.
Example: 192.168.0.0/16,10.0.0.0/24.
Remote traffic selector must be specified for VPN tunnels that do not use
dynamic routing with a Cloud Router. Omit this flag when creating a tunnel using
dynamic routing, including a tunnel for a Highly Available VPN gateway.

**--router**:
The Router to use for dynamic routing.

**--router-region**:
Region of the router to operate on. If not specified, you might be prompted to
select a region (interactive mode only).
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
gcloud alpha compute vpn-tunnels create
```

```
gcloud beta compute vpn-tunnels create
```