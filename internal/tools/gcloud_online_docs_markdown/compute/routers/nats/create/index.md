# gcloud compute routers nats create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create)*

**NAME**

: **gcloud compute routers nats create - add a NAT to a Compute Engine router**

**SYNOPSIS**

: **`gcloud compute routers nats create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#NAME)` `[--router](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#--router)`=`ROUTER` [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#--async)`] [`[--auto-network-tier](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#--auto-network-tier)`=`AUTO_NETWORK_TIER`] [`[--[no-]enable-dynamic-port-allocation](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#--[no-]enable-dynamic-port-allocation)`] [`[--enable-endpoint-independent-mapping](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#--enable-endpoint-independent-mapping)`] [`[--enable-logging](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#--enable-logging)`] [`[--endpoint-types](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#--endpoint-types)`=[`ENDPOINT_TYPE`,…]] [`[--icmp-idle-timeout](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#--icmp-idle-timeout)`=`ICMP_IDLE_TIMEOUT`] [`[--log-filter](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#--log-filter)`=`LOG_FILTER`] [`[--max-ports-per-vm](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#--max-ports-per-vm)`=`MAX_PORTS_PER_VM`] [`[--min-ports-per-vm](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#--min-ports-per-vm)`=`MIN_PORTS_PER_VM`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#--region)`=`REGION`] [`[--rules](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#--rules)`=`RULES`] [`[--tcp-established-idle-timeout](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#--tcp-established-idle-timeout)`=`TCP_ESTABLISHED_IDLE_TIMEOUT`] [`[--tcp-time-wait-timeout](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#--tcp-time-wait-timeout)`=`TCP_TIME_WAIT_TIMEOUT`] [`[--tcp-transitory-idle-timeout](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#--tcp-transitory-idle-timeout)`=`TCP_TRANSITORY_IDLE_TIMEOUT`] [`[--type](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#--type)`=`TYPE`] [`[--udp-idle-timeout](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#--udp-idle-timeout)`=`UDP_IDLE_TIMEOUT`] [`[--auto-allocate-nat-external-ips](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#--auto-allocate-nat-external-ips)`     | `[--nat-external-ip-pool](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#--nat-external-ip-pool)`=`IP_ADDRESS`,[`[IP_ADDRESS](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#IP_ADDRESS)`,…]] [`[--nat-all-subnet-ip-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#--nat-all-subnet-ip-ranges)`     | `[--nat-custom-subnet-ip-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#--nat-custom-subnet-ip-ranges)`=`SUBNETWORK`[:`[RANGE_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#RANGE_NAME)`|:`[ALL](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#ALL)`],[…]     | `[--nat-primary-subnet-ip-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#--nat-primary-subnet-ip-ranges)`] [`[--nat64-all-v6-subnet-ip-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#--nat64-all-v6-subnet-ip-ranges)`     | `[--nat64-custom-v6-subnet-ip-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#--nat64-custom-v6-subnet-ip-ranges)`=`SUBNETWORK`,[`[SUBNETWORK](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#SUBNETWORK)`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute routers nats create` is used to create a NAT on a
Compute Engine router.

**EXAMPLES**

: Auto-allocate NAT for all IP addresses of all subnets in the region:

```
gcloud compute routers nats create nat1 --router=my-router --auto-allocate-nat-external-ips --nat-all-subnet-ip-ranges
```

Specify IP addresses for NAT: Each IP address is the name of a reserved static
IP address resource in the same region.

```
gcloud compute routers nats create nat1 --router=my-router --nat-external-ip-pool=ip-address1,ip-address2
```

Specify subnet ranges for NAT:
By default, NAT works for all primary and secondary IP ranges for all subnets in
the region for the given VPC network. You can restrict which subnet primary and
secondary ranges can use NAT.

```
gcloud compute routers nats create nat1 --router=my-router --auto-allocate-nat-external-ips --nat-custom-subnet-ip-ranges=subnet-1,subnet-3:secondary-range-1
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the NAT to create

**REQUIRED FLAGS**

: **--router**:
The Router to use for NAT.

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--auto-network-tier**:
The network tier to use when automatically reserving NAT IP addresses.
`AUTO_NETWORK_TIER` must be one of:

**`PREMIUM`**:
High quality, Google-grade network tier with support for all networking
products.

**`STANDARD`**:
Public internet quality, with only limited support for other networking
products.

**--[no-]enable-dynamic-port-allocation**:
Enable dynamic port allocation.
If not specified, Dynamic Port Allocation is disabled by default.
Use `--enable-dynamic-port-allocation` to enable and
`--no-enable-dynamic-port-allocation` to disable.

**--enable-endpoint-independent-mapping**:
Enable endpoint-independent mapping for the NAT (as defined in RFC 5128).
If not specified, NATs have endpoint-independent mapping disabled by default.
Use `--no-enable-endpoint-independent-mapping` to disable
endpoint-independent mapping.

**--enable-logging**:
Enable logging for the NAT. Logs will be exported to Stackdriver. NAT logging is
disabled by default. To disable logging for the NAT, use $ [gcloud compute routers
nats update](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update) MY-NAT --no-enable-logging \ --router ROUTER --region REGION

**--endpoint-types**:
Endpoint Types supported by the NAT Gateway.

```
ENDPOINT_TYPE must be one of:
```

```
ENDPOINT_TYPE_VM
  For VM Endpoints
ENDPOINT_TYPE_SWG
  For Secure Web Gateway Endpoints
ENDPOINT_TYPE_MANAGED_PROXY_LB
  For regional Application Load Balancers (internal and external) and regional proxy Network Load Balancers (internal and external) endpoints
```

The default is ENDPOINT_TYPE_VM.
`ENDPOINT_TYPE` must be one of:
`ENDPOINT_TYPE_VM`, `ENDPOINT_TYPE_SWG`,
`ENDPOINT_TYPE_MANAGED_PROXY_LB`.

**--icmp-idle-timeout**:
Timeout for ICMP connections. See [https://cloud.google.com/sdk/gcloud/reference/topic/datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes)
for information on duration formats.

**--log-filter**:
Filter for logs exported to stackdriver.
The default is ALL.
If logging is not enabled, filter settings will be persisted but will have no
effect.
Use --[no-]enable-logging to enable and disable logging.
`LOG_FILTER` must be one of:

**`ALL`**:
Export logs for all connections handled by this NAT.

**`ERRORS_ONLY`**:
Export logs for connection failures only.

**`TRANSLATIONS_ONLY`**:
Export logs for successful connections only.

**--max-ports-per-vm**:
Maximum ports to be allocated to a VM.
This field can only be set when Dynamic Port Allocation is enabled and defaults
to 65536. It must be set to a power of 2 that is greater than minPortsPerVm and
at most 65536.

**--min-ports-per-vm**:
Minimum ports to be allocated to a VM.
If Dynamic Port Allocation is disabled, this defaults to 64.
If Dynamic Port Allocation is enabled, this defaults to 32 and must be set to a
power of 2 that is at least 32 and lower than maxPortsPerVm.

**--region**:
Region of the NAT to create. If not specified, you might be prompted to select a
region (interactive mode only).
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

**--rules**:
Path to YAML file containing NAT Rules applied to the NAT. The YAML file format
must follow the REST API schema for NAT Rules. See [API
Discovery docs](https://www.googleapis.com/discovery/v1/apis/compute/alpha/rest) for reference.

**--tcp-established-idle-timeout**:
Timeout for TCP established connections. See [https://cloud.google.com/sdk/gcloud/reference/topic/datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes)
for information on duration formats.

**--tcp-time-wait-timeout**:
Timeout for TCP connections in the TIME_WAIT state. See [https://cloud.google.com/sdk/gcloud/reference/topic/datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes)
for information on duration formats.

**--tcp-transitory-idle-timeout**:
Timeout for TCP transitory connections. See [https://cloud.google.com/sdk/gcloud/reference/topic/datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes)
for information on duration formats.

**--type**:
Type of the NAT Gateway. Defaults to PUBLIC if not specified.
`TYPE` must be one of:

**`PRIVATE`**:
Used for private-to-private NAT translations. Allows communication between VPC
Networks.

**`PUBLIC`**:
Used for private-to-public NAT translations. Allows VM instances to communicate
with the internet.

**--udp-idle-timeout**:
Timeout for UDP connections. See [https://cloud.google.com/sdk/gcloud/reference/topic/datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes)
for information on duration formats.

**--auto-allocate-nat-external-ips**

**--nat-all-subnet-ip-ranges**

**--nat64-all-v6-subnet-ip-ranges**

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

: This command, when specified without alpha or beta, uses the compute/v1/routers
API. The full documentation for this API can be found at: [https://cloud.google.com/compute/docs/reference/rest/v1/routers/](https://cloud.google.com/compute/docs/reference/rest/v1/routers/)
The beta command uses the compute/beta/routers API. The full documentation for
this API can be found at: [https://cloud.google.com/compute/docs/reference/rest/beta/routers/](https://cloud.google.com/compute/docs/reference/rest/beta/routers/)
The alpha command uses the compute/alpha/routers API. Full documentation is not
available for the alpha API.

**NOTES**

: These variants are also available:

```
gcloud alpha compute routers nats create
```

```
gcloud beta compute routers nats create
```