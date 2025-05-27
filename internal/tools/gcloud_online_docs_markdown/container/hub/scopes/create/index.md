# gcloud container hub scopes create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/create](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/create)*

**NAME**

: **gcloud container hub scopes create - create a new fleet scope**

**SYNOPSIS**

: **`gcloud container hub scopes create` `[SCOPE](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/create#SCOPE)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/create#--async)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--namespace-labels](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/create#--namespace-labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Fleet Scope resource.

**EXAMPLES**

: Create a new scope `SCOPE_NAME` in the active project's fleet:

```
gcloud container hub scopes create SCOPE_NAME
```

**POSITIONAL ARGUMENTS**

: **Scope resource - The fleet scope resourse to be created. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `scope` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `scope` on the command line with a fully
specified name;
- global is the only supported location.

This must be specified.

**`SCOPE`**:
ID of the scope or fully qualified identifier for the scope.
To set the `scope` attribute:

- provide the argument `scope` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--namespace-labels**:
List of scope-level label KEY=VALUE pairs to add.

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

: This command uses the `gkehub/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster](https://cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster)

**NOTES**

: These variants are also available:

```
gcloud alpha container hub scopes create
```

```
gcloud beta container hub scopes create
```