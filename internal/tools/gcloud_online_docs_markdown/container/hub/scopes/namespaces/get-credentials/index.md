# gcloud container hub scopes namespaces get-credentials  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/get-credentials](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/get-credentials)*

**NAME**

: **gcloud container hub scopes namespaces get-credentials - fetch credentials for a membership with a particular namespace**

**SYNOPSIS**

: **`gcloud container hub scopes namespaces get-credentials` `[NAMESPACE](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/get-credentials#NAMESPACE)` [`[--membership](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/get-credentials#--membership)`=`MEMBERSHIP`] [`[--membership-location](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/get-credentials#--membership-location)`=`MEMBERSHIP_LOCATION`] [`[--set-namespace-in-config](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/get-credentials#--set-namespace-in-config)`=`SET_NAMESPACE_IN_CONFIG`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/get-credentials#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: Get the Connect Gateway kubeconfig for global membership
`MEMBERSHIP`, using namespace `NAMESPACE` in the config:

```
gcloud container hub scopes namespaces get-credentials NAMESPACE --membership=MEMBERSHIP --membership-location=global --set-namespace-in-config=true
```

Get the Connect Gateway kubeconfig for global membership
`MEMBERSHIP`:

```
gcloud container hub scopes namespaces get-credentials NAMESPACE --membership=MEMBERSHIP --membership-location=global
```

**POSITIONAL ARGUMENTS**

: **`NAMESPACE`**:
Name of the namespace for which to get access to memberships.

**FLAGS**

: **--membership**:
Membership ID to get credentials from. If not provided, a prompt will offer a
list of memberships in the fleet.

**--membership-location**:
The location of the membership resource, e.g. `us-central1`. If not
specified, defaults to `global`.

**--set-namespace-in-config**:
If true, the default namespace for the context in the generated kubeconfig will
be set to the Fleet namespace (i.e. the name given as the positional argument in
this command).
Otherwise, no default namespace will be set, functioning the same as `[gcloud
container fleet memberships get-credentials](https://cloud.google.com/sdk/gcloud/reference/container/fleet/memberships/get-credentials)`.

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
gcloud alpha container hub scopes namespaces get-credentials
```

```
gcloud beta container hub scopes namespaces get-credentials
```