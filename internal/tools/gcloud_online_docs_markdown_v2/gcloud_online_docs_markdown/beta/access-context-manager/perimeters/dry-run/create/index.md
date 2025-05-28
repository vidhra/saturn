# gcloud beta access-context-manager perimeters dry-run create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/create](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/create)*

**NAME**

: **gcloud beta access-context-manager perimeters dry-run create - create a dry-run mode configuration for a new or existing Service         Perimeter**

**SYNOPSIS**

: **`gcloud beta access-context-manager perimeters dry-run create` (`[PERIMETER](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/create#PERIMETER)` : `[--policy](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/create#--policy)`=`POLICY`) (`[--access-levels](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/create#--access-levels)`=[`access_levels`,…] `[--egress-policies](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/create#--egress-policies)`=`YAML_FILE` `[--ingress-policies](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/create#--ingress-policies)`=`YAML_FILE` `[--resources](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/create#--resources)`=[`resources`,…] `[--restricted-services](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/create#--restricted-services)`=[`restricted_services`,…] `[--enable-vpc-accessible-services](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/create#--enable-vpc-accessible-services)` `[--vpc-allowed-services](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/create#--vpc-allowed-services)`=[`vpc_allowed_services`,…]     | [`[--perimeter-title](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/create#--perimeter-title)`=`PERIMETER_TITLE` `[--perimeter-type](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/create#--perimeter-type)`=`PERIMETER_TYPE` : `[--perimeter-access-levels](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/create#--perimeter-access-levels)`=[`access_levels`,…] `[--perimeter-description](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/create#--perimeter-description)`=`PERIMETER_DESCRIPTION` `[--perimeter-egress-policies](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/create#--perimeter-egress-policies)`=`YAML_FILE` `[--perimeter-ingress-policies](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/create#--perimeter-ingress-policies)`=`YAML_FILE` `[--perimeter-resources](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/create#--perimeter-resources)`=[`resources`,…] `[--perimeter-restricted-services](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/create#--perimeter-restricted-services)`=[`restricted_services`,…] `[--perimeter-enable-vpc-accessible-services](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/create#--perimeter-enable-vpc-accessible-services)` `[--perimeter-vpc-allowed-services](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/create#--perimeter-vpc-allowed-services)`=[`vpc_allowed_services`,…]]) [`[--async](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/create#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(BETA)` When a Service Perimeter with the specified name does not
exist, a new Service Perimeter will be created. In this case, the newly created
Service Perimeter will not have any enforcement mode configuration, and,
therefore, all policy violations will be logged.
When a perimeter with the specified name does exist, a dry-run mode
configuration will be created for it. The behavior of the enforcement mode
configuration, if present, will not be impacted in this case. Requests that
violate the existing enforcement mode configuration of the Service Perimeter
will continue being denied. Requests that only violate the policy in the dry-run
mode configuration will be logged but will not be denied.

**EXAMPLES**

: To create a dry-run configuration for an existing Service Perimeter:

```
gcloud beta access-context-manager perimeters dry-run create my-perimeter --resources="projects/0123456789" --access-levels="accessPolicies/a_policy/accessLevels/a_level" --restricted-services="storage.googleapis.com"
```

To create a dry-run configuration for a new Service Perimeter:

```
gcloud beta access-context-manager perimeters dry-run create my-perimeter --perimeter-title="My New Perimeter" --perimeter-description="Perimeter description" --perimeter-type="regular" --perimeter-resources="projects/0123456789" --perimeter-access-levels="accessPolicies/a_policy/accessLevels/a_level" --perimeter-restricted-services="storage.googleapis.com"
```

**POSITIONAL ARGUMENTS**

: **Perimeter resource - The service perimeter to update. The arguments in this
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
- set the property `access_context_manager/policy`.**

**REQUIRED FLAGS**

: **--access-levels**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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

: This command is currently in beta and might change without notice. These
variants are also available:

```
gcloud access-context-manager perimeters dry-run create
```

```
gcloud alpha access-context-manager perimeters dry-run create
```