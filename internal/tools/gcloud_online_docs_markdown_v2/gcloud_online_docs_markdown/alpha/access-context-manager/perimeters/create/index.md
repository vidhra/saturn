# gcloud alpha access-context-manager perimeters create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/create](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/create)*

**NAME**

: **gcloud alpha access-context-manager perimeters create - create a new service perimeter**

**SYNOPSIS**

: **`gcloud alpha access-context-manager perimeters create` (`[PERIMETER](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/create#PERIMETER)` : `[--policy](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/create#--policy)`=`POLICY`) `[--title](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/create#--title)`=`TITLE` [`[--access-levels](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/create#--access-levels)`=[`LEVEL`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/create#--async)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/create#--description)`=`DESCRIPTION`] [`[--egress-policies](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/create#--egress-policies)`=`YAML_FILE`] [`[--ingress-policies](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/create#--ingress-policies)`=`YAML_FILE`] [`[--perimeter-type](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/create#--perimeter-type)`=`PERIMETER_TYPE`; default="regular"] [`[--resources](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/create#--resources)`=[`RESOURCES`,…]] [`[--restricted-services](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/create#--restricted-services)`=[`SERVICE`,…]] [`[--enable-vpc-accessible-services](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/create#--enable-vpc-accessible-services)` `[--vpc-allowed-services](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/create#--vpc-allowed-services)`=[`VPC_SERVICE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create a new service perimeter in a given access policy.

**EXAMPLES**

: To create a new basic Service Perimeter:

```
gcloud alpha access-context-manager perimeters create --title=my_perimeter_title --resources=projects/12345 --restricted-services="storage.googleapis.com" --policy=9876543
```

**POSITIONAL ARGUMENTS**

: **Perimeter resource - The service perimeter to create. The arguments in this
group can be used to specify the attributes of this resource.
This must be specified.

**`PERIMETER`**:
ID of the perimeter or fully qualified identifier for the perimeter.
To set the `perimeter` attribute:

- provide the argument `perimeter` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--policy**:
The ID of the access policy.
To set the `policy` attribute:

- provide the argument `perimeter` on the command line with a fully
specified name;
- provide the argument `--policy` on the command line;
- set the property `access_context_manager/policy`;
- automatically, if the current account belongs to an organization with exactly
one access policy..**

**REQUIRED FLAGS**

: **--title**:
Short human-readable title for the service perimeter.

**OPTIONAL FLAGS**

: **--access-levels**:
Comma-separated list of IDs for access levels (in the same policy) that an
intra-perimeter request must satisfy to be allowed.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--description**:
Long-form description of service perimeter.

**--egress-policies**:
Path to a file containing a list of Engress Policies.
This file contains a list of YAML-compliant objects representing Engress
Policies described in the API reference.
For more information about the alpha version, see: [https://cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.servicePerimeters](https://cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.servicePerimeters)
For more information about non-alpha versions, see: [https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters](https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters)

**--ingress-policies**:
Path to a file containing a list of Ingress Policies.
This file contains a list of YAML-compliant objects representing Ingress
Policies described in the API reference.
For more information about the alpha version, see: [https://cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.servicePerimeters](https://cloud.google.com/access-context-manager/docs/reference/rest/v1alpha/accessPolicies.servicePerimeters)
For more information about non-alpha versions, see: [https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters](https://cloud.google.com/access-context-manager/docs/reference/rest/v1/accessPolicies.servicePerimeters)

**--perimeter-type**:
Type of the perimeter. `PERIMETER_TYPE` must be one of:

**`bridge`**:
Allows resources in different regular service perimeters to import and export
data between each other.
A project may belong to multiple bridge service perimeters (only if it also
belongs to a regular service perimeter). Both restricted and unrestricted
service lists, as well as access level lists, must be empty.

**`regular`**:
Allows resources within this service perimeter to import and export data amongst
themselves.
A project may belong to at most one regular service perimeter.

**--resources**:
Comma-separated list of resources (currently only projects, in the form
`projects/<projectnumber>`) in this perimeter.

**--restricted-services**:
Comma-separated list of services to which the perimeter boundary
`does` apply (for example, `storage.googleapis.com`).

**--enable-vpc-accessible-services**:
Whether to restrict API calls within the perimeter to those in the
vpc-allowed-services list.

**--vpc-allowed-services**:
Comma-separated list of APIs accessible from within the Service Perimeter. In
order to include all restricted services, use reference "RESTRICTED-SERVICES".
Requires vpc-accessible-services be enabled.

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

: This command uses the `accesscontextmanager/v1alpha` API. The full
documentation for this API can be found at: [https://cloud.google.com/access-context-manager/docs/reference/rest/](https://cloud.google.com/access-context-manager/docs/reference/rest/)

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud access-context-manager perimeters create
```

```
gcloud beta access-context-manager perimeters create
```