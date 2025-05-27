# gcloud container hub scopes rbacrolebindings create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/rbacrolebindings/create](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/rbacrolebindings/create)*

**NAME**

: **gcloud container hub scopes rbacrolebindings create - create an RBAC RoleBinding**

**SYNOPSIS**

: **`gcloud container hub scopes rbacrolebindings create` (`[NAME](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/rbacrolebindings/create#NAME)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/rbacrolebindings/create#--location)`=`LOCATION` `[--scope](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/rbacrolebindings/create#--scope)`=`SCOPE`) `[--role](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/rbacrolebindings/create#--role)`=`ROLE` (`[--group](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/rbacrolebindings/create#--group)`=`GROUP`     | `[--user](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/rbacrolebindings/create#--user)`=`USER`) [`[--labels](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/rbacrolebindings/create#--labels)`=[`KEY`=`VALUE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/hub/scopes/rbacrolebindings/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command can fail for the following reasons:

- The RBAC RoleBinding already exists.
- The caller does not have permission to access the given scope.

**EXAMPLES**

: To create an admin RBAC RoleBinding `RBRB` in scope
`SCOPE` for user `person@google.com`, run:

```
gcloud container hub scopes rbacrolebindings create RBRB --scope=SCOPE --role=admin --user=person@google.com
```

To create a viewer RBAC RoleBinding `RBRB` in scope
`SCOPE` for group `people@google.com`, run:

```
gcloud container hub scopes rbacrolebindings create RBRB --scope=SCOPE --role=viewer --group=people@google.com
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

**REQUIRED FLAGS**

: **--role**:
Predefined role to assign to principal (admin, edit, view).
`ROLE` must be one of: `admin`,
`edit`, `view`.

**--group**

**OPTIONAL FLAGS**

: **--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

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
gcloud alpha container hub scopes rbacrolebindings create
```

```
gcloud beta container hub scopes rbacrolebindings create
```