# gcloud container hub clusterupgrade describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/hub/clusterupgrade/describe](https://cloud.google.com/sdk/gcloud/reference/container/hub/clusterupgrade/describe)*

**NAME**

: **gcloud container hub clusterupgrade describe - describe the clusterupgrade feature for a fleet within a given project**

**SYNOPSIS**

: **`gcloud container hub clusterupgrade describe` [`[--show-linked-cluster-upgrade](https://cloud.google.com/sdk/gcloud/reference/container/hub/clusterupgrade/describe#--show-linked-cluster-upgrade)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/hub/clusterupgrade/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe the Fleet clusterupgrade feature used for configuring fleet-based
rollout sequencing.

**EXAMPLES**

: To view the cluster upgrade feature information for the current fleet, run:

```
gcloud container hub clusterupgrade describe
```

**FLAGS**

: **--show-linked-cluster-upgrade**:
Shows the cluster upgrade feature information for the current fleet as well as
information for all other fleets linked in the same rollout sequence (provided
that the caller has permission to view the upstream and downstream fleets). This
displays cluster upgrade information for fleets in the current fleet's rollout
sequence in order of furthest upstream to downstream.
To view the cluster upgrade feature information for the rollout sequence
containing the current fleet, run:

```
gcloud container hub clusterupgrade describe --show-linked-cluster-upgrade
```

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
gcloud alpha container hub clusterupgrade describe
```

```
gcloud beta container hub clusterupgrade describe
```