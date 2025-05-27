# gcloud container hub scopes namespaces describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/describe](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/describe)*

**NAME**

: **gcloud container hub scopes namespaces describe - show fleet namespace info**

**SYNOPSIS**

: **`gcloud container hub scopes namespaces describe` (`[NAMESPACE](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/describe#NAMESPACE)` : `[--scope](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/describe#--scope)`=`SCOPE`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/namespaces/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command can fail for the following reasons:

- The project specified does not exist.
- The namespace specified does not exist in the project.
- The caller does not have permission to access the project or namespace.

**EXAMPLES**

: To print metadata for the namespace `NAMESPACE` in the active
project, run:

```
gcloud container hub scopes namespaces describe NAMESPACE
```

To print metadata for the namespace `NAMESPACE` in project
`PROJECT_ID`, run:

```
gcloud container hub scopes namespaces describe NAMESPACE --project=PROJECT_ID
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
gcloud alpha container hub scopes namespaces describe
```

```
gcloud beta container hub scopes namespaces describe
```