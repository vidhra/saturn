# gcloud edge-cloud networking subnets create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/subnets/create](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/subnets/create)*

**NAME**

: **gcloud edge-cloud networking subnets create - create a Distributed Cloud Edge Network subnet**

**SYNOPSIS**

: **`gcloud edge-cloud networking subnets create` (`[SUBNET](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/subnets/create#SUBNET)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/subnets/create#--location)`=`LOCATION` `[--zone](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/subnets/create#--zone)`=`ZONE`) `[--network](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/subnets/create#--network)`=`NETWORK` [`[--async](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/subnets/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/subnets/create#--description)`=`DESCRIPTION`] [`[--ipv4-range](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/subnets/create#--ipv4-range)`=[`IPV4_RANGE`,…]] [`[--ipv6-range](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/subnets/create#--ipv6-range)`=[`IPV6_RANGE`,…]] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/subnets/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--vlan-id](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/subnets/create#--vlan-id)`=`VLAN_ID`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/edge-cloud/networking/subnets/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Distributed Cloud Edge Network subnet.

**EXAMPLES**

: To create a Distributed Cloud Edge Network subnet called `my-subnet`
with VLAN ID and owned ip ranges specified in the edge zone
'us-central1-edge-den1', run:

```
gcloud edge-cloud networking subnets create my-subnet --network=my-network --location=us-central1 --zone=us-central1-edge-den1 --ipv4-range=192.168.1.1/24,172.10.10.1/24 --ipv6-range=2001:db8::1/64,4001:230::1/64 --vlan-id=100 --bonding-type=bonded
```

**POSITIONAL ARGUMENTS**

: **Subnet resource - Distributed Cloud Edge Network subnet to create. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `subnet` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SUBNET`**:
ID of the subnet or fully qualified identifier for the subnet.
To set the `subnet` attribute:

- provide the argument `subnet` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The global location name.
To set the `location` attribute:

- provide the argument `subnet` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--zone**:
The name of the Google Distributed Cloud Edge zone.
To set the `zone` attribute:

- provide the argument `subnet` on the command line with a fully
specified name;
- provide the argument `--zone` on the command line.**

**REQUIRED FLAGS**

: **--network**:
The network that this subnetwork belongs to.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
An optional, textual description for the subnet.

**--ipv4-range**:
The ranges of ipv4 addresses that are owned by this subnetwork in CIDR format.

**--ipv6-range**:
The ranges of ipv6 addresses that are owned by this subnetwork in CIDR format.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--vlan-id**:
The ID of the VLAN to tag the subnetwork. If not specified we assign one
automatically.

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

: This command uses the `edgenetwork/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/distributed-cloud-edge/docs](https://cloud.google.com/distributed-cloud-edge/docs)

**NOTES**

: This variant is also available:

```
gcloud alpha edge-cloud networking subnets create
```