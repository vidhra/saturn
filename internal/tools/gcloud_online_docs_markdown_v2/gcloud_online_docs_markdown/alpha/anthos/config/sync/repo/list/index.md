# gcloud alpha anthos config sync repo list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/sync/repo/list](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/sync/repo/list)*

**NAME**

: **gcloud alpha anthos config sync repo list - list repositories and their status that are synced by Config Sync**

**SYNOPSIS**

: **`gcloud alpha anthos config sync repo list` [`[--membership](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/sync/repo/list#--membership)`=`MEMBERSHIP`] [`[--namespace](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/sync/repo/list#--namespace)`=`NAMESPACE`] [`[--selector](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/sync/repo/list#--selector)`=`SELECTOR`] [`[--status](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/sync/repo/list#--status)`=`STATUS`; default="all"] [`[--targets](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/sync/repo/list#--targets)`=`TARGETS`; default="all"] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/sync/repo/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` List repositories and their status that are synced by
Config Sync.

**EXAMPLES**

: To list all repositories synced to the registered clusters or to the Config
Controller cluster in the current project:

```
gcloud alpha anthos config sync repo list list
```

To list all repositories synced to the registered clusters to the fleet hosted
in the current project:

```
gcloud alpha anthos config sync repo list list --targets=fleet-clusters
```

To list all repositories synced to the Config Controller cluster in the current
project:

```
gcloud alpha anthos config sync repo list list --targets=fleet-clusters
```

To list repositories in namespace <NAMESPACE> synced to the registered
clusters to the current fleet:

```
gcloud alpha anthos config sync repo list list --targets=fleet-clusters --namespace=<NAMESPACE>
```

To list repositories synced to the registered clusters that are in a "pending"
status:

```
gcloud alpha anthos config sync repo list list --targets=fleet-clusters --status=pending
```

**FLAGS**

: **--membership**:
The membership name that the listed Config Sync repos are synced to.A membership
is for a registered cluster to a fleet. It supportsa single membership or
multiple memberships with the format membership1,membership2 or
membership`.It can only be specified when --targets=fleet-clusters is used.`

**--namespace`=`NAMESPACE``**:
The namespace that the listed Config Sync repos are from.It supports a single
namespace or multiple namespaces with the format namespace1,namespace2 or
namespace.

**--selector**:
The label selector that the listed Config Sync repos should match. It supports
the selector with the format key1=value1,key2=value2

**--status**:
The status for the Config Sync repos that the list command should include. The
supported values are all, synced, pending, error, stalled.

**--targets**:
The targets of the clusters. It must be one of the three values: all,
fleet-clusters, config-controller.

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

**PREREQUISITES**

: Please setup Connect Gateway if your registered clusters are non-GKE clusters.
The instructions can be found at [https://cloud.google.com/anthos/multicluster-management/gateway/setup](https://cloud.google.com/anthos/multicluster-management/gateway/setup).
For registered clusters that are GKE clusters, no need to setup the Connect
Gateway.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist.