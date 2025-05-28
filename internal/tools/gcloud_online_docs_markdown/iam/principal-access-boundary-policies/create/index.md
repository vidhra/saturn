# gcloud iam principal-access-boundary-policies create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies/create](https://cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies/create)*

**NAME**

: **gcloud iam principal-access-boundary-policies create - create PrincipalAccessBoundaryPolicy instance**

**SYNOPSIS**

: **`gcloud iam principal-access-boundary-policies create` (`[PRINCIPAL_ACCESS_BOUNDARY_POLICY](https://cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies/create#PRINCIPAL_ACCESS_BOUNDARY_POLICY)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies/create#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies/create#--organization)`=`ORGANIZATION`) [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies/create#--annotations)`=[`ANNOTATIONS`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies/create#--async)`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies/create#--display-name)`=`DISPLAY_NAME`] [`[--etag](https://cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies/create#--etag)`=`ETAG`] [[`[--details-rules](https://cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies/create#--details-rules)`=[`description`=`DESCRIPTION`],[`effect`=`EFFECT`],[`resources`=`RESOURCES`] : `[--details-enforcement-version](https://cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies/create#--details-enforcement-version)`=`DETAILS_ENFORCEMENT_VERSION`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create PrincipalAccessBoundaryPolicy instance.

**EXAMPLES**

: To create a policy instance called `my-policy`, run:

```
gcloud iam principal-access-boundary-policies create my-policy --organization=123 --location=global
```

**POSITIONAL ARGUMENTS**

: **PrincipalAccessBoundaryPolicy resource - Identifier. The resource name of the
principal access boundary policy.
The following format is supported:
`organizations/{organization_id}/locations/{location}/principalAccessBoundaryPolicies/{policy_id}`
The arguments in this group can be used to specify the attributes of this
resource.
This must be specified.

**`PRINCIPAL_ACCESS_BOUNDARY_POLICY`**:
ID of the principalAccessBoundaryPolicy or fully qualified identifier for the
principalAccessBoundaryPolicy.
To set the `principal_access_boundary_policy` attribute:

- provide the argument `principal_access_boundary_policy` on the
command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location id of the principalAccessBoundaryPolicy resource.
To set the `location` attribute:

- provide the argument `principal_access_boundary_policy` on the
command line with a fully specified name;
- provide the argument `--location` on the command line.

**--organization**:
The organization id of the principalAccessBoundaryPolicy resource.
To set the `organization` attribute:

- provide the argument `principal_access_boundary_policy` on the
command line with a fully specified name;
- provide the argument `--organization` on the command line.**

**FLAGS**

: **--annotations**:
User defined annotations. See [https://google.aip.dev/148#annotations](https://google.aip.dev/148#annotations)
for more details such as format and size limitations.

**`KEY`**:
Sets `KEY` value.

**`VALUE`**:
Sets `VALUE` value.

`Shorthand Example:`

```
--annotations=string=string
```

`JSON Example:`

```
--annotations='{"string": "string"}'
```

`File Example:`

```
--annotations=path_to_file.(yaml|json)
```

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--display-name**:
The description of the principal access boundary policy. Must be less than or
equal to 63 characters.

**--etag**:
The etag for the principal access boundary. If this is provided on update, it
must match the server's etag.

**--details-rules**

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

: This command uses the `iam/v3` API. The full documentation for this
API can be found at: [https://cloud.google.com/iam/](https://cloud.google.com/iam/)

**NOTES**

: This variant is also available:

```
gcloud beta iam principal-access-boundary-policies create
```