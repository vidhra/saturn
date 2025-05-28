# gcloud compute routers nats update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update)*

**NAME**

: **gcloud compute routers nats update - update a NAT on a Compute Engine router**

**SYNOPSIS**

: **`gcloud compute routers nats update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#NAME)` `[--router](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--router)`=`ROUTER` [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--async)`] [`[--auto-network-tier](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--auto-network-tier)`=`AUTO_NETWORK_TIER`] [`[--[no-]enable-dynamic-port-allocation](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--[no-]enable-dynamic-port-allocation)`] [`[--enable-endpoint-independent-mapping](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--enable-endpoint-independent-mapping)`] [`[--enable-logging](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--enable-logging)`] [`[--log-filter](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--log-filter)`=`LOG_FILTER`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--region)`=`REGION`] [`[--rules](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--rules)`=`RULES`] [`[--auto-allocate-nat-external-ips](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--auto-allocate-nat-external-ips)`     | `[--nat-external-ip-pool](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--nat-external-ip-pool)`=`IP_ADDRESS`,[`[IP_ADDRESS](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#IP_ADDRESS)`,…]] [`[--clear-icmp-idle-timeout](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--clear-icmp-idle-timeout)`     | `[--icmp-idle-timeout](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--icmp-idle-timeout)`=`ICMP_IDLE_TIMEOUT`] [`[--clear-max-ports-per-vm](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--clear-max-ports-per-vm)`     | `[--max-ports-per-vm](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--max-ports-per-vm)`=`MAX_PORTS_PER_VM`] [`[--clear-min-ports-per-vm](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--clear-min-ports-per-vm)`     | `[--min-ports-per-vm](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--min-ports-per-vm)`=`MIN_PORTS_PER_VM`] [`[--clear-nat-external-drain-ip-pool](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--clear-nat-external-drain-ip-pool)`     | `[--nat-external-drain-ip-pool](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--nat-external-drain-ip-pool)`=`NAT_EXTERNAL_DRAIN_IP_POOL`,[…]] [`[--clear-nat-subnet-ip-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--clear-nat-subnet-ip-ranges)`     | `[--nat-all-subnet-ip-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--nat-all-subnet-ip-ranges)`     | `[--nat-custom-subnet-ip-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--nat-custom-subnet-ip-ranges)`=`SUBNETWORK`[:`[RANGE_NAME](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#RANGE_NAME)`|:`[ALL](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#ALL)`],[…]     | `[--nat-primary-subnet-ip-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--nat-primary-subnet-ip-ranges)`] [`[--clear-nat64-subnet-ip-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--clear-nat64-subnet-ip-ranges)`     | `[--nat64-all-v6-subnet-ip-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--nat64-all-v6-subnet-ip-ranges)`     | `[--nat64-custom-v6-subnet-ip-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--nat64-custom-v6-subnet-ip-ranges)`=`SUBNETWORK`,[`[SUBNETWORK](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#SUBNETWORK)`,…]] [`[--clear-tcp-established-idle-timeout](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--clear-tcp-established-idle-timeout)`     | `[--tcp-established-idle-timeout](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--tcp-established-idle-timeout)`=`TCP_ESTABLISHED_IDLE_TIMEOUT`] [`[--clear-tcp-time-wait-timeout](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--clear-tcp-time-wait-timeout)`     | `[--tcp-time-wait-timeout](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--tcp-time-wait-timeout)`=`TCP_TIME_WAIT_TIMEOUT`] [`[--clear-tcp-transitory-idle-timeout](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--clear-tcp-transitory-idle-timeout)`     | `[--tcp-transitory-idle-timeout](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--tcp-transitory-idle-timeout)`=`TCP_TRANSITORY_IDLE_TIMEOUT`] [`[--clear-udp-idle-timeout](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--clear-udp-idle-timeout)`     | `[--udp-idle-timeout](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#--udp-idle-timeout)`=`UDP_IDLE_TIMEOUT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/routers/nats/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute routers nats update` is used to update a NAT in a
Compute Engine router.

**EXAMPLES**

: Change subnetworks and IP address resources associated with NAT:

```
gcloud compute routers nats update nat1 --router=my-router --nat-external-ip-pool=ip-address2,ip-address3 --nat-custom-subnet-ip-ranges=subnet-2,subnet-3:secondary-range-2
```

Change minimum default ports allocated per VM associated with NAT:

```
gcloud compute routers nats update nat1 --router=my-router --min-ports-per-vm=128
```

Change connection timeouts associated with NAT:

```
gcloud compute routers nats update nat1 --router=my-router --udp-mapping-idle-timeout=60s --icmp-mapping-idle-timeout=60s --tcp-established-connection-idle-timeout=60s --tcp-transitory-connection-idle-timeout=60s
```

Reset connection timeouts associated NAT to default values:

```
gcloud compute routers nats update nat1 --router=my-router --clear-udp-mapping-idle-timeout --clear-icmp-mapping-idle-timeout --clear-tcp-established-connection-idle-timeout --clear-tcp-transitory-connection-idle-timeout
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
disabled by default. To disable logging for the NAT, use $ gcloud compute
routers nats update MY-NAT --no-enable-logging \ --router ROUTER --region REGION

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

**--auto-allocate-nat-external-ips**

**--clear-icmp-idle-timeout**

**--clear-max-ports-per-vm**

**--clear-min-ports-per-vm**

**--clear-nat-external-drain-ip-pool**

**--clear-nat-subnet-ip-ranges**

**--clear-nat64-subnet-ip-ranges**

**--clear-tcp-established-idle-timeout**

**--clear-tcp-time-wait-timeout**

**--clear-tcp-transitory-idle-timeout**

**--clear-udp-idle-timeout**

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
gcloud alpha compute routers nats update
```

```
gcloud beta compute routers nats update
```