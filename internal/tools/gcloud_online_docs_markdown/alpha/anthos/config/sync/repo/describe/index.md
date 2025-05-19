# gcloud alpha anthos config sync repo describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/sync/repo/describe](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/sync/repo/describe)*

**NAME**

: **gcloud alpha anthos config sync repo describe - describe a repository that is synced across clusters in Config Sync**

**SYNOPSIS**

: **`gcloud alpha anthos config sync repo describe` [`[--cluster](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/sync/repo/describe#--cluster)`=`CLUSTER`] [`[--managed-resources](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/sync/repo/describe#--managed-resources)`=`MANAGED_RESOURCES`; default="failed"] [`[--source](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/sync/repo/describe#--source)`=`SOURCE`] [`[--sync-name](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/sync/repo/describe#--sync-name)`=`SYNC_NAME`] [`[--sync-namespace](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/sync/repo/describe#--sync-namespace)`=`SYNC_NAMESPACE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/config/sync/repo/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Describe a repository that is synced across clusters in
Config Sync.

**EXAMPLES**

: To describe a repository with source as <SOURCE> where the source is from
the output of the list command:

```
gcloud alpha anthos config sync repo describe describe --source=<SOURCE>
```

To describe the repository that is synced by a RootSync or RepoSync CR in the
namespace <NAMESPACE> with the name <NAME>:

```
gcloud alpha anthos config sync repo describe describe --sync-namespace=<NAMESPACE> --sync-name=<NAME>
```

To describe the repository that is synced by a RootSync or RepoSync CR in the
namespace <NAMESPACE> with the name <NAME> from a specific cluster
<CLUSTER>:

```
gcloud alpha anthos config sync repo describe describe --sync-namespace=<NAMESPACE> --sync-name=<NAME> --cluster=<CLUSTER>
```

To describe a repository with source as <SOURCE> and list all the managed
resources from this repositry:

```
gcloud alpha anthos config sync repo describe describe --source=<SOURCE> --managed-resources=all
```

To describe a repository with source as <SOURCE> and only print the failed
managed resources from this repositry:

```
gcloud alpha anthos config sync repo describe describe --source=<SOURCE> --managed-resources=failed --format="multi(statuses:format=none,managed_resources:format='table[box](group,kind,name,namespace,conditions)')"
```

**FLAGS**

: **--cluster**:
The cluster name or the membership name that a repository is synced to.

**--managed-resources**:
Specify the managed resource status that should beincluded in the describe
output.The supported values areall, current, failed, inprogress, notfound,
unknown.

**--source**:
The source of the repository. It should be copied fromthe output of the listing
repo command.

**--sync-name**:
Name of the RootSync or RepoSync CR to sync a repository.

**--sync-namespace**:
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

: Please setup Connect Gateway if your registered clusters are non-GKE clusters.
The instructions can be found at [https://cloud.google.com/anthos/multicluster-management/gateway/setup](https://cloud.google.com/anthos/multicluster-management/gateway/setup).
For registered clusters that are GKE clusters, no need to setup the Connect
Gateway.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist.