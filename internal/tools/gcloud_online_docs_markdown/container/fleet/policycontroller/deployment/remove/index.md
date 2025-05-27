# gcloud container fleet policycontroller deployment remove  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller/deployment/remove](https://cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller/deployment/remove)*

**NAME**

: **gcloud container fleet policycontroller deployment remove - removes configuration properties from Policy Controller components**

**SYNOPSIS**

: **`gcloud container fleet policycontroller deployment remove` `[DEPLOYMENT](https://cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller/deployment/remove#DEPLOYMENT)` `[PROPERTY](https://cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller/deployment/remove#PROPERTY)` [`[VALUE](https://cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller/deployment/remove#VALUE)`] [`[--effect](https://cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller/deployment/remove#--effect)`=`EFFECT`] [`[--all-memberships](https://cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller/deployment/remove#--all-memberships)`     | [`[--memberships](https://cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller/deployment/remove#--memberships)`=[`MEMBERSHIPS`,…] : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller/deployment/remove#--location)`=`LOCATION`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller/deployment/remove#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Remove customizations of on-cluster components in Policy Controller. These
components are managed as individual kubernetes deployments (e.g. 'admission')
in the gatekeeper-system namespace.
When removing a 'toleration' property, it must match exactly, including the key,
value and effect flag (if originally specified).

**EXAMPLES**

: To remove the replica count for a component:

```
gcloud container fleet policycontroller deployment remove admission replica-count
```

To remove the replica count for a component across all fleet memberships:

```
gcloud container fleet policycontroller deployment remove admission replica-count --all-memberships
```

To remove a toleration with key 'my-key' on a component:

```
gcloud container fleet policycontroller deployment remove admission toleration my-key
```

To remove a toleration with key 'my-key' and 'my-value' on a component:

```
gcloud container fleet policycontroller deployment remove admission toleration my-key=my-value
```

To remove a toleration with key 'my-key' and 'my-value' on a component, along
with the effect 'NoSchedule':

```
gcloud container fleet policycontroller deployment remove admission toleration my-key=my-value --effect=NoSchedule
```

To remove a memory limit:

```
gcloud container fleet policycontroller deployment remove audit memory-limit
```

To remove a memory request:

```
gcloud container fleet policycontroller deployment remove mutation memory-request
```

To remove a cpu limit:

```
gcloud container fleet policycontroller deployment remove admission cpu-limit
```

To remove a cpu request:

```
gcloud container fleet policycontroller deployment remove audit cpu-request
```

To remove the anti-affinity configuration:

```
gcloud container fleet policycontroller deployment remove admission pod-affinity
```

**POSITIONAL ARGUMENTS**

: **`DEPLOYMENT`**:
The PolicyController deployment component (i.e, "admission", "audit" or
"mutation" from which to remove configuration.

**`PROPERTY`**:
Property to be removed.

**[`VALUE`]**:
This is only required to remove a toleration. It should not be included for any
other property.

**FLAGS**

: **--effect**:
Applies only to "toleration" property. To be removed, tolerations must match
exactly, including the effect setting. `EFFECT` must be
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
gcloud alpha container fleet policycontroller deployment remove
```

```
gcloud beta container fleet policycontroller deployment remove
```