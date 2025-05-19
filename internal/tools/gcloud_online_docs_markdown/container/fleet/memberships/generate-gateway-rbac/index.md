# gcloud container fleet memberships generate-gateway-rbac  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/generate-gateway-rbac](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/generate-gateway-rbac)*

**NAME**

: **gcloud container fleet memberships generate-gateway-rbac - generate RBAC policy files for connected clusters by the user**

**SYNOPSIS**

: **`gcloud container fleet memberships generate-gateway-rbac` (`[--anthos-support](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/generate-gateway-rbac#--anthos-support)`     | `[--groups](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/generate-gateway-rbac#--groups)`=`GROUPS`     | `[--users](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/generate-gateway-rbac#--users)`=`USERS`) [`[--apply](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/generate-gateway-rbac#--apply)`] [`[--context](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/generate-gateway-rbac#--context)`=`CONTEXT`] [`[--kubeconfig](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/generate-gateway-rbac#--kubeconfig)`=`KUBECONFIG`] [`[--membership](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/generate-gateway-rbac#--membership)`=`MEMBERSHIP`] [`[--rbac-output-file](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/generate-gateway-rbac#--rbac-output-file)`=`RBAC_OUTPUT_FILE`] [`[--revoke](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/generate-gateway-rbac#--revoke)`] [`[--role](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/generate-gateway-rbac#--role)`=`ROLE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/generate-gateway-rbac#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: gcloud container fleet memberships generate-gateway-rbac generates RBAC policies
to be used by Connect Gateway API.
Upon success, this command will write the output RBAC policy to the designated
local file in dry run mode.
Override RBAC policy: Y to override previous RBAC policy, N to stop. If
overriding the --role, Y will clean up the previous RBAC policy and then apply
the new one.

**EXAMPLES**

: The current implementation supports multiple modes:
Dry run mode to generate the RBAC policy file, and write to local directory:

```
gcloud container fleet memberships generate-gateway-rbac --membership=my-cluster --users=foo@example.com,test-acct@test-project.iam.gserviceaccount.com --role=clusterrole/cluster-admin --rbac-output-file=./rbac.yaml
```

Dry run mode to generate the RBAC policy, and print on screen:

```
gcloud container fleet memberships generate-gateway-rbac --membership=my-cluster --users=foo@example.com,test-acct@test-project.iam.gserviceaccount.com --role=clusterrole/cluster-admin
```

Anthos support mode, generate the RBAC policy file with read-only permission for
TSE/Eng to debug customers' clusters:

```
gcloud container fleet memberships generate-gateway-rbac --membership=my-cluster --anthos-support
```

Apply mode, generate the RBAC policy and apply it to the specified cluster:

```
gcloud container fleet memberships generate-gateway-rbac --membership=my-cluster --users=foo@example.com,test-acct@test-project.iam.gserviceaccount.com --role=clusterrole/cluster-admin --context=my-cluster-context --kubeconfig=/home/user/custom_kubeconfig --apply
```

Revoke mode, revoke the RBAC policy for the specified users:

```
gcloud container fleet memberships generate-gateway-rbac --membership=my-cluster --users=foo@example.com,test-acct@test-project.iam.gserviceaccount.com --role=clusterrole/cluster-admin --context=my-cluster-context --kubeconfig=/home/user/custom_kubeconfig --revoke
```

The role to be granted to the users can either be cluster-scoped or
namespace-scoped. To grant a namespace-scoped role to the users in dry run mode,
run:

```
gcloud container fleet memberships generate-gateway-rbac --membership=my-cluster --users=foo@example.com,test-acct@test-project.iam.gserviceaccount.com --role=role/mynamespace/namespace-reader
```

The users provided can be using a Google identity (only email) or using external
identity providers (starting with "principal://iam.googleapis.com"):

```
gcloud container fleet memberships generate-gateway-rbac --membership=my-cluster --users=foo@example.com,principal://iam.googleapis.com/locations/global/workforcePools/pool/subject/user --role=clusterrole/cluster-admin --context=my-cluster-context --kubeconfig=/home/user/custom_kubeconfig --apply
```

The groups can be provided as a Google identity (only email) or an external
identity (starting with "principalSet://iam.googleapis.com"):

```
gcloud container fleet memberships generate-gateway-rbac --membership=my-cluster --groups=group@example.com,principalSet://iam.googleapis.com/locations/global/workforcePools/pool/group/ExampleGroup --role=clusterrole/cluster-admin --context=my-cluster-context --kubeconfig=/home/user/custom_kubeconfig --apply
```

**REQUIRED FLAGS**

: **--anthos-support**

**OPTIONAL FLAGS**

: **--apply**:
If specified, this command will generate RBAC policy and apply to the specified
cluster.

**--context**:
The cluster context as it appears in the kubeconfig file. You can get this value
from the command line by running command: `kubectl config
current-context`.

**--kubeconfig**:
The kubeconfig file containing an entry for the cluster. Defaults to $KUBECONFIG
if it is set in the environment, otherwise defaults to $HOME/.kube/config.

**--membership**:
Membership name to assign RBAC policy with.

**--rbac-output-file**:
If specified, this command will execute in dry run mode and write to the file
specified with this flag: the generated RBAC policy will not be applied to
Kubernetes clusters,instead it will be written to the designated local file.

**--revoke**:
If specified, this command will revoke the RBAC policy for the specified users.

**--role**:
Namespace scoped role or cluster role.

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
gcloud alpha container fleet memberships generate-gateway-rbac
```

```
gcloud beta container fleet memberships generate-gateway-rbac
```