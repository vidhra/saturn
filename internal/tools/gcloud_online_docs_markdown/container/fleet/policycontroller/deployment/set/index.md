# gcloud container fleet policycontroller deployment set  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller/deployment/set](https://cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller/deployment/set)*

**NAME**

: **gcloud container fleet policycontroller deployment set - sets configuration of the Policy Controller components**

**SYNOPSIS**

: **`gcloud container fleet policycontroller deployment set` `[DEPLOYMENT](https://cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller/deployment/set#DEPLOYMENT)` `[PROPERTY](https://cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller/deployment/set#PROPERTY)` `[VALUE](https://cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller/deployment/set#VALUE)` [`[--effect](https://cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller/deployment/set#--effect)`=`EFFECT`] [`[--all-memberships](https://cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller/deployment/set#--all-memberships)`     | [`[--memberships](https://cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller/deployment/set#--memberships)`=[`MEMBERSHIPS`,…] : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller/deployment/set#--location)`=`LOCATION`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller/deployment/set#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Customizes on-cluster components of Policy Controller. Supported properties may
be set with this command, or removed with 'remove'. These components are managed
as individual kubernetes deployments (e.g. 'admission') in the gatekeeper-system
namespace.
When setting cpu or memory limits and requests, Kubernetes-standard resource
units are used.
All properties set using this command will overwrite previous properties, with
the exception of tolerations which can only be added, and any number may be
added. To edit a toleration, use 'remove' to first delete it, and then 'set' the
desired toleration.

**EXAMPLES**

: To set the replica count for a component:

```
gcloud container fleet policycontroller deployment set admission replica-count 3
```

To set the replica count for a component across all fleet memberships:

```
gcloud container fleet policycontroller deployment set admission replica-count 3 --all-memberships
```

To set a toleration with key 'my-key' on a component (which is an 'Exists'
operator):

```
gcloud container fleet policycontroller deployment set admission toleration my-key
```

To set a toleration with key 'my-key' and 'my-value' on a component (which is an
'Equal' operator):

```
gcloud container fleet policycontroller deployment set admission toleration my-key=my-value
```

To set a toleration with key 'my-key' and 'my-value' on a component, along with
the effect 'NoSchedule' (which is an 'Equal' operator):

```
gcloud container fleet policycontroller deployment set admission toleration my-key=my-value --effect=NoSchedule
```

To set a memory limit:

```
gcloud container fleet policycontroller deployment set audit memory-limit 4Gi
```

To set a memory request:

```
gcloud container fleet policycontroller deployment set mutation memory-request 2Gi
```

To set a cpu limit:

```
gcloud container fleet policycontroller deployment set admission cpu-limit 500m
```

To set a cpu request:

```
gcloud container fleet policycontroller deployment set audit cpu-request 250m
```

To set anti-affinity to achieve high availability on the mutation deployment:

```
gcloud container fleet policycontroller deployment set mutation pod-affinity anti
```

**POSITIONAL ARGUMENTS**

: **`DEPLOYMENT`**:
The PolicyController deployment component (e.g. "admission", "audit" or
"mutation") upon which to set configuration.

**`PROPERTY`**:
Property to be set.

**`VALUE`**:
The value to set the property to. Valid input varies based on the property being
set.

**FLAGS**

: **--effect**:
Applies only to "toleration" property. `EFFECT` must be
one of: `NoSchedule`, `PreferNoSchedule`,
`NoExecute`.

**--all-memberships**

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
gcloud alpha container fleet policycontroller deployment set
```

```
gcloud beta container fleet policycontroller deployment set
```