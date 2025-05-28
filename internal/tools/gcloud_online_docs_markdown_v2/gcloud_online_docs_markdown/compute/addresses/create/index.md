# gcloud compute addresses create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/addresses/create](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/create)*

**NAME**

: **gcloud compute addresses create - reserve IP addresses**

**SYNOPSIS**

: **`gcloud compute addresses create` [`[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/create#NAME)` …] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/create#--description)`=`DESCRIPTION`] [`[--endpoint-type](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/create#--endpoint-type)`=`ENDPOINT_TYPE`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/create#--network)`=`NETWORK`] [`[--network-tier](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/create#--network-tier)`=`NETWORK_TIER`] [`[--prefix-length](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/create#--prefix-length)`=`PREFIX_LENGTH`] [`[--purpose](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/create#--purpose)`=`PURPOSE`] [`[--subnet](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/create#--subnet)`=`SUBNET`] [`[--addresses](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/create#--addresses)`=`ADDRESS`,[`[ADDRESS](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/create#ADDRESS)`,…]     | `[--ip-version](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/create#--ip-version)`=`IP_VERSION`] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/create#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/create#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/addresses/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute addresses create` is used to reserve one or more IP
addresses. Once an IP address is reserved, it will be associated with the
project until it is released using 'gcloud compute addresses delete'. Ephemeral
IP addresses that are in use by resources in the project can be reserved using
the '--addresses' flag.

**EXAMPLES**

: To reserve three IP addresses in the 'us-central1' region, run:

```
gcloud compute addresses create address-1 address-2 address-3 --region=us-central1
```

To reserve ephemeral IP addresses '162.222.181.198' and '23.251.146.189' which
are being used by virtual machine instances in the 'us-central1' region, run:

```
gcloud compute addresses create --addresses=162.222.181.198,23.251.146.189 --region=us-central1
```

In the above invocation, the two addresses will be assigned random names.
To reserve an IP address named subnet-address-1 from the subnet 'default' in the
'us-central1' region, run:

```
gcloud compute addresses create subnet-address-1 --region=us-central1 --subnet=default
```

To reserve an IP range '10.110.0.0/16' from the network 'default' for
'VPC_PEERING', run:

```
gcloud compute addresses create ip-range-1 --global --addresses=10.110.0.0 --prefix-length=16 --purpose=VPC_PEERING --network=default
```

To reserve any IP range with prefix length '16' from the network 'default' for
'VPC_PEERING', run:

```
gcloud compute addresses create ip-range-1 --global --prefix-length=16 --purpose=VPC_PEERING --network=default
```

To reserve an address from network 'default' for PRIVATE_SERVICE_CONNECT, run:

```
gcloud compute addresses create psc-address-1 --global --addresses=10.110.0.10 --purpose=PRIVATE_SERVICE_CONNECT --network=default
```

**POSITIONAL ARGUMENTS**

: **[`NAME` …]**:
Names of the addresses to create.

**FLAGS**

: **--description**:
An optional textual description for the addresses.

**--endpoint-type**:
The endpoint type of the external IPv6 address to be reserved.
`ENDPOINT_TYPE` must be one of: `VM`,
`NETLB`.

**--network**:
If specified, the network resource in which the address(es) should be reserved.
This is only available for global internal address, which represents an internal
IP range reservation from within the network.

**--network-tier**:
The network tier to assign to the reserved IP addresses.
``NETWORK_TIER`` must be one of:
`PREMIUM`, `STANDARD`. The default value is
`PREMIUM`.
While regional external addresses (`--region` specified,
`--subnet` omitted) can use either `PREMIUM` or
`STANDARD`, global external addresses (`--global`
specified, `--subnet` omitted) can only use `PREMIUM`.
Internal addresses can only use `PREMIUM`.

**--prefix-length**:
The prefix length of the IP range. If the address is an IPv4 address, it must be
a value between 8 and 30 inclusive. If the address is an IPv6 address, the only
allowed value is 96. If not present, it means the address field is a single IP
address.
This field is not applicable to external IPv4 addresses or global IPv6
addresses.

**--purpose**:
The purpose of the address resource. This field is not applicable to external
addresses. `PURPOSE` must be one of:
`VPC_PEERING`, `SHARED_LOADBALANCER_VIP`,
`GCE_ENDPOINT`, `IPSEC_INTERCONNECT`,
`PRIVATE_SERVICE_CONNECT`.

**--subnet**:
If specified, the subnet name in which the address(es) should be reserved. The
subnet must be in the same region as the address.
The address will represent an internal IP reservation from within the subnet. If
--address is specified, it must be within the subnet's IP range.
May not be specified with --global.

**--addresses**

**--global**

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
gcloud alpha compute addresses create
```

```
gcloud beta compute addresses create
```