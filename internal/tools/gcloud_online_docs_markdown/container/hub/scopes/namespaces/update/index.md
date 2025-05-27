# gcloud container hub scopes namespaces update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/update](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/update)*

**NAME**

: **gcloud container hub scopes namespaces update - update a fleet namespace**

**SYNOPSIS**

: **`gcloud container hub scopes namespaces update` (`[NAMESPACE](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/update#NAMESPACE)` : `[--scope](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/update#--scope)`=`SCOPE`) [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--update-namespace-labels](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/update#--update-namespace-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/update#--remove-labels)`=[`KEY`,…]] [`[--clear-namespace-labels](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/update#--clear-namespace-labels)`     | `[--remove-namespace-labels](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/update#--remove-namespace-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command can fail for the following reasons:

- The project specified does not exist.
- The fleet namespace does not exist in the project.
- The caller does not have permission to access the project or namespace.

**EXAMPLES**

: To update the namespace `NAMESPACE` in the active project:

```
gcloud container hub scopes namespaces update NAMESPACE
```

To update the namespace `NAMESPACE` in project
`PROJECT_ID`:

```
gcloud container hub scopes namespaces update NAMESPACE --project=PROJECT_ID
```

**POSITIONAL ARGUMENTS**

: **Namespace resource - The group of arguments defining the Fleet Namespace. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `NAMESPACE` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `NAMESPACE` on the command line with a fully
specified name;
- global is the only supported location.

This must be specified.

**`NAMESPACE`**:
ID of the namespace or fully qualified identifier for the namespace.
To set the `namespace` attribute:

- provide the argument `NAMESPACE` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--scope**:
the
To set the `scope` attribute:

- provide the argument `NAMESPACE` on the command line with a fully
specified name;
- provide the argument `--scope` on the command line.**

**FLAGS**

: **--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--update-namespace-labels**:
List of namespace-level label KEY=VALUE pairs to update in the cluster
namespace. If a label exists, its value is modified. Otherwise, a new label is'
created.

**--clear-labels**

**--clear-namespace-labels**

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
gcloud alpha container hub scopes namespaces update
```

```
gcloud beta container hub scopes namespaces update
```