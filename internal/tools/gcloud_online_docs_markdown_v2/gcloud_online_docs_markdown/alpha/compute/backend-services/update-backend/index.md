# gcloud alpha compute backend-services update-backend  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/update-backend](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/update-backend)*

**NAME**

: **gcloud alpha compute backend-services update-backend - update an existing backend in a backend service**

**SYNOPSIS**

: **`gcloud alpha compute backend-services update-backend` `[BACKEND_SERVICE_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/update-backend#BACKEND_SERVICE_NAME)` ([`[--instance-group](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/update-backend#--instance-group)`=`INSTANCE_GROUP` : `[--instance-group-region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/update-backend#--instance-group-region)`=`INSTANCE_GROUP_REGION` | `[--instance-group-zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/update-backend#--instance-group-zone)`=`INSTANCE_GROUP_ZONE`]     | [`[--network-endpoint-group](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/update-backend#--network-endpoint-group)`=`NETWORK_ENDPOINT_GROUP` : `[--network-endpoint-group-zone](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/update-backend#--network-endpoint-group-zone)`=`NETWORK_ENDPOINT_GROUP_ZONE`]) [`[--balancing-mode](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/update-backend#--balancing-mode)`=`BALANCING_MODE`] [`[--capacity-scaler](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/update-backend#--capacity-scaler)`=`CAPACITY_SCALER`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/update-backend#--description)`=`DESCRIPTION`] [`[--failover](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/update-backend#--failover)`] [`[--max-utilization](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/update-backend#--max-utilization)`=`MAX_UTILIZATION`] [`[--preference](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/update-backend#--preference)`=`PREFERENCE`] [`[--clear-custom-metrics](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/update-backend#--clear-custom-metrics)`     | `[--custom-metrics](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/update-backend#--custom-metrics)`=[`CUSTOM_METRICS`,…]     | `[--custom-metrics-file](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/update-backend#--custom-metrics-file)`=[`CUSTOM_METRICS`,…]] [`[--global](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/update-backend#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/update-backend#--region)`=`REGION`] [`[--max-connections](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/update-backend#--max-connections)`=`MAX_CONNECTIONS`     | `[--max-connections-per-endpoint](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/update-backend#--max-connections-per-endpoint)`=`MAX_CONNECTIONS_PER_ENDPOINT`     | `[--max-connections-per-instance](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/update-backend#--max-connections-per-instance)`=`MAX_CONNECTIONS_PER_INSTANCE`     | `[--max-rate](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/update-backend#--max-rate)`=`MAX_RATE`     | `[--max-rate-per-endpoint](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/update-backend#--max-rate-per-endpoint)`=`MAX_RATE_PER_ENDPOINT`     | `[--max-rate-per-instance](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/update-backend#--max-rate-per-instance)`=`MAX_RATE_PER_INSTANCE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/update-backend#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute backend-services
update-backend` updates a backend that is part of a backend service. This
is useful for changing the way a backend behaves. Example changes that can be
made include changing the load balancing policy and draining a backend by
setting its capacity scaler to zero.
Backends are instance groups or network endpoint groups. One of the
`--network-endpoint-group` or `--instance-group` flags is
required to identify the backend that you are modifying. You cannot change the
instance group or network endpoint group associated with a backend, but you can
remove a backend and add a new one with `backend-services
remove-backend` and `backend-services add-backend`.
The `[gcloud
compute backend-services edit](https://cloud.google.com/sdk/gcloud/reference/compute/backend-services/edit)` command can also update a backend if
the use of a text editor is desired.
For more information about the available settings, see [https://cloud.google.com/load-balancing/docs/backend-service](https://cloud.google.com/load-balancing/docs/backend-service).

**POSITIONAL ARGUMENTS**

: **`BACKEND_SERVICE_NAME`**:
Name of the backend service to operate on.

**REQUIRED FLAGS**

: **--instance-group**

**OPTIONAL FLAGS**

: **--balancing-mode**:
Defines how to measure whether a backend can handle additional traffic or is
fully loaded. For more information, see [https://cloud.google.com/load-balancing/docs/backend-service#balancing-mode](https://cloud.google.com/load-balancing/docs/backend-service#balancing-mode).
`BALANCING_MODE` must be one of:

**`CONNECTION`**:
Available if the backend service's load balancing scheme is either
`INTERNAL` or `EXTERNAL`. Available if the backend
service's protocol is one of `SSL`, `TCP`, or
`UDP`.
Spreads load based on how many concurrent connections the backend can handle.
For backend services with --load-balancing-scheme `EXTERNAL`, you
must specify exactly one of these additional parameters:
`--max-connections`, `--max-connections-per-instance`, or
`--max-connections-per-endpoint`.
For backend services where `--load-balancing-scheme` is
`INTERNAL`, you must omit all of these parameters.

**`CUSTOM_METRICS`**:
Spreads load based on custom defined and reported metrics.

**`RATE`**:
Available if the backend service's load balancing scheme is
`INTERNAL_MANAGED`, `INTERNAL_SELF_MANAGED`, or
`EXTERNAL`. Available if the backend service's protocol is one of
HTTP, HTTPS, or HTTP/2.
Spreads load based on how many HTTP requests per second (RPS) the backend can
handle.
You must specify exactly one of these additional parameters:
`--max-rate`, `--max-rate-per-instance`, or
`--max-rate-per-endpoint`.

**`UTILIZATION`**:
Available if the backend service's load balancing scheme is
`INTERNAL_MANAGED`, `INTERNAL_SELF_MANAGED`, or
`EXTERNAL`. Available only for managed or unmanaged instance group
backends.
Spreads load based on the backend utilization of instances in a backend instance
group.
The following additional parameters may be specified:
`--max-utilization`, `--max-rate`,
`--max-rate-per-instance`, `--max-connections`,
`--max-connections-per-instance`. For valid combinations, see
`--max-utilization`.

**--capacity-scaler**:
Scales down the target capacity (max utilization, max rate, or max connections)
without changing the target capacity. For usage guidelines and examples, see [Capacity
scaler](https://cloud.google.com/load-balancing/docs/backend-service#capacity_scaler).

**--description**:
An optional, textual description for the backend.

**--failover**:
Designates whether this is a failover backend. More than one failover backend
can be configured for a given BackendService. Not compatible with the --global
flag

**--max-utilization**:
Defines the maximum target for average utilization of the backend instance
group. Supported values are `0.0` (0%) through `1.0`
(100%). This is an optional parameter for the `UTILIZATION` balancing
mode.
You can use this parameter with other parameters for defining target capacity.
For usage guidelines, see [Balancing
mode combinations](https://cloud.google.com/load-balancing/docs/backend-service#balancing-mode-combos).

**--preference**:
This parameter specifies whether a backend should be fully utilized before
sending traffic to backends with the default preference. This parameter cannot
be used with regional managed instance groups and when the endpoint type of an
attached network endpoint group is INTERNET_IP_PORT, INTERNET_FQDN_PORT, or
SERVERLESS. `PREFERENCE` must be one of:

**`DEFAULT`**:
This is the default setting. If the designated preferred backends don't have
enough capacity, backends in the default category are used. Traffic is
distributed between default backends based on the load balancing algorithm used.

**`PREFERRED`**:
Backends with this preference setting are used up to their capacity limits
first, while optimizing overall network latency.

**--clear-custom-metrics**

**--global**

**--max-connections**

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute backend-services update-backend
```

```
gcloud beta compute backend-services update-backend
```