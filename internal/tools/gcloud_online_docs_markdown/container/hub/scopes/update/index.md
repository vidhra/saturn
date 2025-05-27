# gcloud container hub scopes update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/update](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/update)*

**NAME**

: **gcloud container hub scopes update - update a scope**

**SYNOPSIS**

: **`gcloud container hub scopes update` (`[SCOPE](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/update#SCOPE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/update#--location)`=`LOCATION`) [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--update-namespace-labels](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/update#--update-namespace-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/update#--remove-labels)`=[`KEY`,…]] [`[--clear-namespace-labels](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/update#--clear-namespace-labels)`     | `[--remove-namespace-labels](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/update#--remove-namespace-labels)`=[`KEY`,…]] [`[--default-upgrade-soaking](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/update#--default-upgrade-soaking)`=`DEFAULT_UPGRADE_SOAKING` `[--remove-upgrade-soaking-overrides](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/update#--remove-upgrade-soaking-overrides)`     | `[--add-upgrade-soaking-override](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/update#--add-upgrade-soaking-override)`=`ADD_UPGRADE_SOAKING_OVERRIDE` `[--upgrade-selector](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/update#--upgrade-selector)`=[`name`=`NAME`],[`version`=`VERSION`] `[--reset-upstream-scope](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/update#--reset-upstream-scope)`     | `[--upstream-scope](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/update#--upstream-scope)`=`UPSTREAM_SCOPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an existing Fleet Scope.

**EXAMPLES**

: First retrieve the ID of the scope using the command below.

```
gcloud container hub scopes list
```

Update a scope.

```
gcloud container hub scopes update SCOPE_NAME
```

**POSITIONAL ARGUMENTS**

: **Scope resource - fleet scope resource. The arguments in this group can be used
to specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `scope` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SCOPE`**:
ID of the scope or fully qualified identifier for the scope.
To set the `scope` attribute:

- provide the argument `scope` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location name.
To set the `location` attribute:

- provide the argument `scope` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- global is the only supported location.**

**FLAGS**

: **--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--update-namespace-labels**:
List of scope-level label KEY=VALUE pairs to update in the cluster namespace. If
a label exists, its value is modified. Otherwise, a new label is' created.

**--clear-labels**

**--clear-namespace-labels**

**--default-upgrade-soaking**

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
gcloud alpha container hub scopes update
```

```
gcloud beta container hub scopes update
```