# gcloud container hub memberships get-credentials  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/get-credentials](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/get-credentials)*

**NAME**

: **gcloud container hub memberships get-credentials - fetch credentials for a fleet-registered cluster to be used in Connect Gateway**

**SYNOPSIS**

: **`gcloud container hub memberships get-credentials` (`[MEMBERSHIP_NAME](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/get-credentials#MEMBERSHIP_NAME)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/get-credentials#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/get-credentials#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: gcloud container hub memberships get-credentials updates the
`kubeconfig` file with the appropriate credentials and endpoint
information to send `kubectl` commands to a fleet-registered and
-connected cluster through the Connect Gateway service.
It takes a project, passed through by set defaults or flags. By default,
credentials are written to `$HOME/.kube/config`. You can provide an
alternate path by setting the `KUBECONFIG` environment variable. If
`KUBECONFIG` contains multiple paths, the first one is used.
Upon success, this command will switch the current context to the target cluster
if other contexts are already present in the `kubeconfig` file.

**EXAMPLES**

: Get the Gateway kubeconfig for a globally registered cluster:

```
gcloud container hub memberships get-credentials my-cluster
gcloud container hub memberships get-credentials my-cluster --location=global
```

Get the Gateway kubeconfig for a cluster registered in us-central1:

```
gcloud container hub memberships get-credentials my-cluster --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **Membership resource - The group of arguments defining a membership. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `MEMBERSHIP_NAME` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`MEMBERSHIP_NAME`**:
ID of the membership or fully qualified identifier for the membership.
To set the `membership` attribute:

- provide the argument `MEMBERSHIP_NAME` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the membership resource, e.g. `us-central1`. If not
specified, attempts to automatically choose the correct region.
To set the `location` attribute:

- provide the argument `MEMBERSHIP_NAME` on the command line with a
fully specified name;
- provide the argument `--location` on the command line;
- set the property `gkehub/location`.**

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
gcloud alpha container hub memberships get-credentials
```

```
gcloud beta container hub memberships get-credentials
```