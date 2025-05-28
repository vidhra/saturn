# gcloud network-services service-lb-policies update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/network-services/service-lb-policies/update](https://cloud.google.com/sdk/gcloud/reference/network-services/service-lb-policies/update)*

**NAME**

: **gcloud network-services service-lb-policies update - update a service LB policy**

**SYNOPSIS**

: **`gcloud network-services service-lb-policies update` (`[SERVICE_LB_POLICY](https://cloud.google.com/sdk/gcloud/reference/network-services/service-lb-policies/update#SERVICE_LB_POLICY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/network-services/service-lb-policies/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/network-services/service-lb-policies/update#--async)`] [`[--auto-capacity-drain](https://cloud.google.com/sdk/gcloud/reference/network-services/service-lb-policies/update#--auto-capacity-drain)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/network-services/service-lb-policies/update#--description)`=`DESCRIPTION`] [`[--failover-health-threshold](https://cloud.google.com/sdk/gcloud/reference/network-services/service-lb-policies/update#--failover-health-threshold)`=`FAILOVER_HEALTH_THRESHOLD`] [`[--load-balancing-algorithm](https://cloud.google.com/sdk/gcloud/reference/network-services/service-lb-policies/update#--load-balancing-algorithm)`=`LOAD_BALANCING_ALGORITHM`; default="waterfall-by-region"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/network-services/service-lb-policies/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the detail of a service LB Policy.

**EXAMPLES**

: Update load-balancing-algorithm of a service LB policy named
``my-service-lb-policy``:

```
gcloud network-services service-lb-policies update my-service-lb-policy --load-balancing-algorithm=waterfall-by-zone
```

**POSITIONAL ARGUMENTS**

: **Service lb policy resource - Name of the service LB policy to be updated. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `service_lb_policy` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SERVICE_LB_POLICY`**:
ID of the service lb policy or fully qualified identifier for the service lb
policy.
To set the `service_lb_policy` attribute:

- provide the argument `service_lb_policy` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location Id.
To set the `location` attribute:

- provide the argument `service_lb_policy` on the command line with a
fully specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--auto-capacity-drain**:
If specified, an unhealthy MIG/NEG will be removed from Global load balancing
and traffic routing for the service. A MIG/NEG is considered to be unhealthy if
less than 25% of the instance/endpoints in the MIG/NEG are healthy.
autoCapacityDrain will never drain more than 50% of the configured MIGs/NEGs of
a Backend Service.

**--description**:
The description for the service LB policy.

**--failover-health-threshold**:
The percentage threshold that a load balancer will begin to send traffic to
failover backends. If the percentage of endpoints in a MIG/NEG is smaller than
this value, traffic would be sent to failover backends if possible. This field
should be set to a value between 1 and 99. The default value is 50 for Proxyless
service mesh, and 70 for others.

**--load-balancing-algorithm**:
The global load balancing algorithm to be used.
`LOAD_BALANCING_ALGORITHM` must be one of:

**`spray-to-region`**:
Spread the traffic from each client to all the MIGs/NEGs in a region.

**`spray-to-world`**:
Balance traffic across all backends across the world proportionally based on
capacity.

**`waterfall-by-region`**:
Direct traffic to the nearest region with endpoints and capacity before spilling
over to other regions.

**`waterfall-by-zone`**:
Attempt to keep traffic in a single zone closest to the client, before spilling
over to other zones.

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

: This command uses the `networkservices/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/networking](https://cloud.google.com/networking)

**NOTES**

: These variants are also available:

```
gcloud alpha network-services service-lb-policies update
```

```
gcloud beta network-services service-lb-policies update
```