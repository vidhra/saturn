# gcloud pam entitlements search  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/search](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/search)*

**NAME**

: **gcloud pam entitlements search - search and list all Privileged Access Manager entitlements in a parent for which you are a requester/approver**

**SYNOPSIS**

: **`gcloud pam entitlements search` `[--caller-access-type](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/search#--caller-access-type)`=`CALLER_ACCESS_TYPE` (`[--location](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/search#--location)`=`LOCATION` : `[--folder](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/search#--folder)`=`FOLDER` `[--organization](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/search#--organization)`=`ORGANIZATION`) [`[--filter](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/search#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/search#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/search#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/search#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/pam/entitlements/search#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Search and list all Privileged Access Manager (PAM) entitlements in a
project/folder/organization location for which you are a requester/approver.

**EXAMPLES**

: The following command searches for and lists all entitlements for which you are
a requester, in a project named `sample-project`, and in location
`global`:

```
gcloud pam entitlements search --project=sample-project --location=global --caller-access-type=grant-requester
```

The following command searches for and lists all entitlements for which you are
an approver, in a project named `sample-project`, and in location
`global`:

```
gcloud pam entitlements search --project=sample-project --location=global --caller-access-type=grant-approver
```

The following command searches for and lists all entitlements for which you are
a requester, in a folder with ID ``FOLDER_ID``,
and in location `global`:

```
gcloud pam entitlements search --folder=FOLDER_ID --location=global --caller-access-type=grant-requester
```

The following command searches for and lists all entitlements for which you are
an approver, in a folder with ID ``FOLDER_ID``,
and in location `global`:

```
gcloud pam entitlements search --folder=FOLDER_ID --location=global --caller-access-type=grant-approver
```

The following command searches for and lists all entitlements for which you are
a requester, in an organization with ID
``ORGANIZATION_ID``, and in location
`global`:

```
gcloud pam entitlements search --organization=ORGANIZATION_ID --location=global --caller-access-type=grant-requester
```

The following command searches for and lists all entitlements for which you are
an approver, in an organization with ID
``ORGANIZATION_ID``, and in location
`global`:

```
gcloud pam entitlements search --organization=ORGANIZATION_ID --location=global --caller-access-type=grant-approver
```

**REQUIRED FLAGS**

: **--caller-access-type**:
Search for entitlements based on whether you are a requester or approver.
`CALLER_ACCESS_TYPE` must be one of:
`grant-approver`, `grant-requester`.

**Location resource - Location of the entitlements. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`. This resource can be one of the
following types: [privilegedaccessmanager.projects.locations,
privilegedaccessmanager.folders.locations,
privilegedaccessmanager.organizations.locations].

This must be specified.

**--location**:
ID of the location or fully qualified identifier for the location.
To set the `location` attribute:

- provide the argument `--location` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--folder**:
The name of the folder
To set the `folder` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- provide the argument `--folder` on the command line. Must be
specified for resource of type [privilegedaccessmanager.folders.locations].

**--organization**:
The name of the organization
To set the `organization` attribute:

- provide the argument `--location` on the command line with a fully
specified name;
- provide the argument `--organization` on the command line. Must be
specified for resource of type
[privilegedaccessmanager.organizations.locations].**

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
gcloud alpha pam entitlements search
```

```
gcloud beta pam entitlements search
```