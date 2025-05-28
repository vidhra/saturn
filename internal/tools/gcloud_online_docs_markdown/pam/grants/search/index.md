# gcloud pam grants search  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pam/grants/search](https://cloud.google.com/sdk/gcloud/reference/pam/grants/search)*

**NAME**

: **gcloud pam grants search - search for and list all Privileged Access Manager grants you have created, have approved, or can approve**

**SYNOPSIS**

: **`gcloud pam grants search` `[--caller-relationship](https://cloud.google.com/sdk/gcloud/reference/pam/grants/search#--caller-relationship)`=`CALLER_RELATIONSHIP` (`[--entitlement](https://cloud.google.com/sdk/gcloud/reference/pam/grants/search#--entitlement)`=`ENTITLEMENT` : `[--folder](https://cloud.google.com/sdk/gcloud/reference/pam/grants/search#--folder)`=`FOLDER` `[--location](https://cloud.google.com/sdk/gcloud/reference/pam/grants/search#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/pam/grants/search#--organization)`=`ORGANIZATION`) [`[--filter](https://cloud.google.com/sdk/gcloud/reference/pam/grants/search#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/pam/grants/search#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/pam/grants/search#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/pam/grants/search#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pam/grants/search#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Search for and list all Privileged Access Manager (PAM) grants you have created,
have approved, or can approve.

**EXAMPLES**

: The following command searches for and lists all grants you have created which
are associated with an entitlement with the full name
``ENTITLEMENT_NAME``:

```
gcloud pam grants search --entitlement=ENTITLEMENT_NAME --caller-relationship=had-created
```

The following command searches for and lists all grants you have approved or
denied which are associated with an entitlement with the full name
``ENTITLEMENT_NAME``:

```
gcloud pam grants search --entitlement=ENTITLEMENT_NAME --caller-relationship=had-approved
```

The following command searches for and lists all grants you can approve which
are associated with an entitlement with the full name
``ENTITLEMENT_NAME``:

```
gcloud pam grants search --entitlement=ENTITLEMENT_NAME --caller-relationship=can-approve
```

**REQUIRED FLAGS**

: **--caller-relationship**:
Whether to return grants you have created, have approved, or can approve.
`CALLER_RELATIONSHIP` must be one of:
`can-approve`, `had-approved`, `had-created`.

**Entitlement resource - Entitlement the grants are associated with. The arguments
in this group can be used to specify the attributes of this resource. (NOTE)
Some attributes are not given arguments in this group but can be set in other
ways.
To set the `project` attribute:

- provide the argument `--entitlement` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`. This resource can be one of the
following types: [privilegedaccessmanager.projects.locations.entitlements,
privilegedaccessmanager.folders.locations.entitlements,
privilegedaccessmanager.organizations.locations.entitlements].

This must be specified.

**--entitlement**:
ID of the entitlement or fully qualified identifier for the entitlement.
To set the `entitlement` attribute:

- provide the argument `--entitlement` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--folder**:
The name of the folder
To set the `folder` attribute:

- provide the argument `--entitlement` on the command line with a fully
specified name;
- provide the argument `--folder` on the command line. Must be
specified for resource of type
[privilegedaccessmanager.folders.locations.entitlements].

**--location**:
The resource location
To set the `location` attribute:

- provide the argument `--entitlement` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--organization**:
The name of the organization
To set the `organization` attribute:

- provide the argument `--entitlement` on the command line with a fully
specified name;
- provide the argument `--organization` on the command line. Must be
specified for resource of type
[privilegedaccessmanager.organizations.locations.entitlements].**

**LIST COMMAND FLAGS**

: **--filter**:
Apply a Boolean filter `EXPRESSION` to each resource item
to be listed. If the expression evaluates `True`, then that item is
listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://cloud.google.com/sdk/gcloud/reference/topic/filters). This flag
interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--limit**:
Maximum number of resources to list. The default is `unlimited`. This
flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--page-size**:
Some services group resource list output into pages. This flag specifies the
maximum number of resources per page. The default is determined by the service
if it supports paging, otherwise it is `unlimited` (no paging).
Paging may be applied before or after `--filter` and
`--limit` depending on the service.

**--sort-by**:
Comma-separated list of resource field key names to sort by. The default order
is ascending. Prefix a field with ``~´´ for descending order on that
field. This flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

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

: This command uses the `privilegedaccessmanager/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/iam/docs/pam-overview](https://cloud.google.com/iam/docs/pam-overview)

**NOTES**

: These variants are also available:

```
gcloud alpha pam grants search
```

```
gcloud beta pam grants search
```