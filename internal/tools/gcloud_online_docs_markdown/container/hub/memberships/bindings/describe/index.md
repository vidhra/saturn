# gcloud container hub memberships bindings describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/bindings/describe](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/bindings/describe)*

**NAME**

: **gcloud container hub memberships bindings describe - show Membership-Binding info**

**SYNOPSIS**

: **`gcloud container hub memberships bindings describe` (`[BINDING](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/bindings/describe#BINDING)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/bindings/describe#--location)`=`LOCATION` `[--membership](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/bindings/describe#--membership)`=`MEMBERSHIP`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/container/hub/memberships/bindings/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command can fail for the following reasons:

- The Membership specified does not exist.
- The Membership Binding specified does not exist in the project.
- The caller does not have permission to access the Membership Binding.
- The caller did not specify the location (--location) if referring to location
other than global.

**EXAMPLES**

: To print metadata for the membership Binding `BINDING_NAME` in a
global membership `MEMBERSHIP_NAME`, run:

```
gcloud container hub memberships bindings describe BINDING_NAME --membership=MEMBERSHIP_NAME
```

To print metadata for the Binding `BINDING_NAME` associated with
regional membership `MEMBERSHIP_NAME`, provide the location
LOCATION_NAME for the Membership where the Binding belongs along with membership
name.

```
gcloud container hub memberships bindings describe BINDING_NAME --membership=MEMBERSHIP_NAME --location=LOCATION_NAME
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
gcloud alpha container hub memberships bindings describe
```

```
gcloud beta container hub memberships bindings describe
```