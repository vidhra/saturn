# gcloud alpha anthos config sync resources list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/sync/resources/list](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/sync/resources/list)*

**NAME**

: **gcloud alpha anthos config sync resources list - list resources and their status that are synced by Config Sync**

**SYNOPSIS**

: **`gcloud alpha anthos config sync resources list` [`[--cluster](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/sync/resources/list#--cluster)`=`CLUSTER`] [`[--membership](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/sync/resources/list#--membership)`=`MEMBERSHIP`] [`[--sync-name](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/sync/resources/list#--sync-name)`=`SYNC_NAME`] [`[--sync-namespace](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/sync/resources/list#--sync-namespace)`=`SYNC_NAMESPACE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/sync/resources/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` List resources and their status that are synced by Config
Sync.

**EXAMPLES**

: To list all managed resources in the current project, run:

```
gcloud alpha anthos config sync resources list list
```

To list all managed resources in a specific Config Controller cluster, run:

```
gcloud alpha anthos config sync resources list list --cluster=<CLUSTER>
```

To list managed resources from a Git repo synced by Config Sync across multiple
clusters, run:

```
gcloud alpha anthos config sync resources list list --sync-name=root-sync --sync-namespace=config-management-system
```

To list managed resources from a Git repo synced by Config Sync from a specific
cluster, run:

```
gcloud alpha anthos config sync resources list list --sync-namespace=<NAMESPACE> --sync-name=repo-sync --cluster=<CLUSTER>
```

**FLAGS**

: **--cluster**:
The cluster name or the membership name that a repository is synced to.

**--membership**:
The membership name that the listed Config Sync repos are synced to. A
membership is for a registered cluster to a fleet. It supports a single
membership or multiple memberships with the format membership1,membership2 or
membership`.`

**--sync-name`=`SYNC_NAME``**:
Name of the RootSync or RepoSync CR to sync a repository.

**--sync-namespace`=`SYNC_NAMESPACE``**:
Namespace of the RootSync or RepoSync CR to sync a repository.

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

: Please setup Connect Gateway in order to use this command with non-GKE
registered clusters. The instructions can be found at [https://cloud.google.com/anthos/multicluster-management/gateway/setup](https://cloud.google.com/anthos/multicluster-management/gateway/setup).

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist.