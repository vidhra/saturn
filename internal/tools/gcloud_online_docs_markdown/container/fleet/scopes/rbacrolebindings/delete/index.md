# gcloud container fleet scopes rbacrolebindings delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/fleet/scopes/rbacrolebindings/delete](https://cloud.google.com/sdk/gcloud/reference/container/fleet/scopes/rbacrolebindings/delete)*

**NAME**

: **gcloud container fleet scopes rbacrolebindings delete - delete a fleet scope RBAC RoleBinding**

**SYNOPSIS**

: **`gcloud container fleet scopes rbacrolebindings delete` (`[NAME](https://cloud.google.com/sdk/gcloud/reference/container/fleet/scopes/rbacrolebindings/delete#NAME)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/fleet/scopes/rbacrolebindings/delete#--location)`=`LOCATION` `[--scope](https://cloud.google.com/sdk/gcloud/reference/container/fleet/scopes/rbacrolebindings/delete#--scope)`=`SCOPE`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/fleet/scopes/rbacrolebindings/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command can fail for the following reasons:

- The RoleBinding specified does not exist.
- The caller does not have permission to access the given RoleBinding.

**EXAMPLES**

: To delete RBAC RoleBinding `RBRB` in scope `SCOPE` in the
active project:

```
gcloud container fleet scopes rbacrolebindings delete RBRB --scope=SCOPE
```

**POSITIONAL ARGUMENTS**

: **Rbacrolebinding resource - The group of arguments defining an RBACRoleBinding.
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `NAME` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`NAME`**:
ID of the rbacrolebinding or fully qualified identifier for the rbacrolebinding.
To set the `rbacrolebinding` attribute:

- provide the argument `NAME` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location for the rbacrolebinding.
To set the `location` attribute:

- provide the argument `NAME` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `gkehub/location`.

**--scope**:
Name of the rbacrolebinding.
To set the `scope` attribute:

- provide the argument `NAME` on the command line with a fully
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
gcloud alpha container fleet scopes rbacrolebindings delete
```

```
gcloud beta container fleet scopes rbacrolebindings delete
```