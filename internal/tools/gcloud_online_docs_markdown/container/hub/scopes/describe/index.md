# gcloud container hub scopes describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/describe](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/describe)*

**NAME**

: **gcloud container hub scopes describe - describe a fleet scope**

**SYNOPSIS**

: **`gcloud container hub scopes describe` (`[SCOPE](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/describe#SCOPE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/describe#--location)`=`LOCATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a Fleet Scope.

**EXAMPLES**

: First retrieve the ID of the scope using the command below. The output of this
command lists all the fleet's members, with their unique IDs in the Names
column:

```
gcloud container hub scopes list
```

Then describe it:

```
gcloud container hub scopes describe SCOPE_NAME
```

**POSITIONAL ARGUMENTS**

: **Scope resource - The scope to describe. The arguments in this group can be used
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
gcloud alpha container hub scopes describe
```

```
gcloud beta container hub scopes describe
```