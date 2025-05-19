# gcloud compute routers nats rules update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/update](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/update)*

**NAME**

: **gcloud compute routers nats rules update - update a Rule in a Compute Engine NAT**

**SYNOPSIS**

: **`gcloud compute routers nats rules update` `[RULE_NUMBER](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/update#RULE_NUMBER)` `[--nat](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/update#--nat)`=`NAT` `[--router](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/update#--router)`=`ROUTER` [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/update#--async)`] [`[--match](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/update#--match)`=`MATCH`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/update#--region)`=`REGION`] [`[--source-nat-active-ips](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/update#--source-nat-active-ips)`=`IP_ADDRESS`,[`[IP_ADDRESS](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/update#IP_ADDRESS)`,…]] [`[--source-nat-active-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/update#--source-nat-active-ranges)`=`SUBNETWORK`,[`[SUBNETWORK](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/update#SUBNETWORK)`,…]] [`[--clear-source-nat-drain-ips](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/update#--clear-source-nat-drain-ips)`     | `[--source-nat-drain-ips](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/update#--source-nat-drain-ips)`=`IP_ADDRESS`,[`[IP_ADDRESS](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/update#IP_ADDRESS)`,…]] [`[--clear-source-nat-drain-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/update#--clear-source-nat-drain-ranges)`     | `[--source-nat-drain-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/update#--source-nat-drain-ranges)`=`SUBNETWORK`,[`[SUBNETWORK](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/update#SUBNETWORK)`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/rules/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute routers nats rules update` is used to update a Rule
in a Compute Engine NAT.

**EXAMPLES**

: To drain connections established using address-1 and use address-2 for all new
connections matching Rule 1 in NAT nat-1, run:

```
gcloud compute routers nats rules update 1 --nat=nat1 --router=my-router --region=us-central1 --source-nat-drain-ips=address-1 --source-nat-active-ips=address-2
```

**POSITIONAL ARGUMENTS**

: **`RULE_NUMBER`**:
Number that uniquely identifies the Rule to update

**REQUIRED FLAGS**

: **--nat**:
Name of the NAT that contains the Rule

**--router**:
The Router to use for NAT.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--match**:
CEL Expression used to identify traffic to which this rule applies.

- Supported attributes (Public NAT): destination.ip
- Supported attributes (Private NAT): nexthop.hub
- Supported methods (Public Nat): inIpRange
- Supported operators (Public NAT): ||, ==
- Supported operators (Private NAT): ==

Examples of allowed Match expressions (Public NAT):

- 'inIpRange(destination.ip, "203.0.113.0/24")''
- 'destination.ip == "203.0.113.7"'
- 'destination.ip == "203.0.113.7" || inIpRange(destination.ip,
"203.0.113.16/25")'

Example of allowed Match expression (Private NAT):

- nexthop.hub ==
"//networkconnectivity.googleapis.com/projects/p1/locations/global/hubs/h1"

**--region**:
Region of the NAT containing the Rule to update. If not specified, you might be
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

**--source-nat-active-ips**:
External IP Addresses to use for connections matching this rule. This flag is
supported only for Public NAT and is required when creating a Public NAT
gateway.
These must be valid reserved external IP addresses in the same region.

**--source-nat-active-ranges**:
Subnetworks from which addresses are used for connections matching this rule.
This flag is supported only for Private NAT and is required when creating a
Private NAT gateway.
These must be subnetwork resources in the same region, with purpose set to
PRIVATE_NAT.

**--clear-source-nat-drain-ips**

**--clear-source-nat-drain-ranges**

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
gcloud alpha compute routers nats rules update
```

```
gcloud beta compute routers nats rules update
```