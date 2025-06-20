# gcloud container hub memberships bindings update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/bindings/update](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/bindings/update)*

**NAME**

: **gcloud container hub memberships bindings update - update the Binding in a Membership**

**SYNOPSIS**

: **`gcloud container hub memberships bindings update` (`[BINDING](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/bindings/update#BINDING)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/bindings/update#--location)`=`LOCATION` `[--membership](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/bindings/update#--membership)`=`MEMBERSHIP`) `[--scope](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/bindings/update#--scope)`=`SCOPE` [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/bindings/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/bindings/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/bindings/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/bindings/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command can fail for the following reasons:

- The Membership specified does not exist.
- The Binding does not exist in the Membership.
- The caller does not have permission to access the Membership/Binding.
- The Scope specified does not exist.
- The caller did not specify the location (--location) if referring to location
other than global.

**EXAMPLES**

: To update the binding `BINDING_NAME` in global membership
`MEMBERSHIP_NAME` in the active project:

```
gcloud container hub memberships bindings update BINDING_NAME --membership=MEMBERSHIP_NAME
```

To update a Binding `BINDING_NAME` associated with regional
membership `MEMBERSHIP_NAME`, provide the location LOCATION_NAME for
the Membership where the Binding belongs along with membership name and
associated Scope `SCOPE_NAME`.

```
gcloud container hub memberships bindings update BINDING_NAME --membership=MEMBERSHIP_NAME --scope=SCOPE_NAME --location=LOCATION_NAME
```

**POSITIONAL ARGUMENTS**

: **Binding resource - The group of arguments defining a Membership Binding. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `BINDING` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`BINDING`**:
ID of the binding or fully qualified identifier for the binding.
To set the `binding` attribute:

- provide the argument `BINDING` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Location for the binding.
To set the `location` attribute:

- provide the argument `BINDING` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `gkehub/location`.

**--membership**:
Name of the binding.
To set the `membership` attribute:

- provide the argument `BINDING` on the command line with a fully
specified name;
- provide the argument `--membership` on the command line.**

**REQUIRED FLAGS**

: **--scope**:
ID of the scope or fully qualified identifier for the scope.
To set the `scope` attribute:

- provide the argument `--scope` on the command line.

**OPTIONAL FLAGS**

: **--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--clear-labels**

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
gcloud alpha container hub memberships bindings update
```

```
gcloud beta container hub memberships bindings update
```