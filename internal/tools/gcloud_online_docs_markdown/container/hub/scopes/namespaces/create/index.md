# gcloud container hub scopes namespaces create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/create](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/create)*

**NAME**

: **gcloud container hub scopes namespaces create - create a fleet namespace**

**SYNOPSIS**

: **`gcloud container hub scopes namespaces create` (`[NAMESPACE](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/create#NAMESPACE)` : `[--scope](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/create#--scope)`=`SCOPE`) [`[--labels](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--namespace-labels](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/create#--namespace-labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command can fail for the following reasons:

- The project specified does not exist.
- The project has a fleet namespace with the same name.
- The caller does not have permission to access the given project.

**EXAMPLES**

: To create a fleet namespace with name `NAMESPACE` in the active
project, run:

```
gcloud container hub scopes namespaces create NAMESPACE
```

To create a fleet namespace in fleet scope `SCOPE` in project
`PROJECT_ID` with name `NAMESPACE`, run:

```
gcloud container hub scopes namespaces create NAMESPACE --scope=SCOPE --project=PROJECT_ID
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

: **--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--namespace-labels**:
List of namespace-level label KEY=VALUE pairs to add.

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
gcloud alpha container hub scopes namespaces create
```

```
gcloud beta container hub scopes namespaces create
```