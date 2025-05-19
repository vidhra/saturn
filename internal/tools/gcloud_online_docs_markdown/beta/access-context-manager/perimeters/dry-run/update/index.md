# gcloud beta access-context-manager perimeters dry-run update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/update](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/update)*

**NAME**

: **gcloud beta access-context-manager perimeters dry-run update - update the dry-run mode configuration for a Service Perimeter**

**SYNOPSIS**

: **`gcloud beta access-context-manager perimeters dry-run update` (`[PERIMETER](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/update#PERIMETER)` : `[--policy](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/update#--policy)`=`POLICY`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/update#--async)`] [`[--etag](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/update#--etag)`=`etag`] [`[--add-access-levels](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/update#--add-access-levels)`=[`ACCESS-LEVELS`,…]     | `[--clear-access-levels](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/update#--clear-access-levels)`     | `[--remove-access-levels](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/update#--remove-access-levels)`=[`ACCESS-LEVELS`,…]] [`[--add-resources](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/update#--add-resources)`=[`RESOURCES`,…]     | `[--clear-resources](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/update#--clear-resources)`     | `[--remove-resources](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/update#--remove-resources)`=[`RESOURCES`,…]] [`[--add-restricted-services](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/update#--add-restricted-services)`=[`RESTRICTED-SERVICES`,…]     | `[--clear-restricted-services](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/update#--clear-restricted-services)`     | `[--remove-restricted-services](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/update#--remove-restricted-services)`=[`RESTRICTED-SERVICES`,…]] [`[--clear-egress-policies](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/update#--clear-egress-policies)`     | `[--set-egress-policies](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/update#--set-egress-policies)`=`YAML_FILE`] [`[--clear-ingress-policies](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/update#--clear-ingress-policies)`     | `[--set-ingress-policies](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/update#--set-ingress-policies)`=`YAML_FILE`] [`[--enable-vpc-accessible-services](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/update#--enable-vpc-accessible-services)` `[--add-vpc-allowed-services](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/update#--add-vpc-allowed-services)`=[`VPC-ALLOWED-SERVICES`,…]     | `[--clear-vpc-allowed-services](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/update#--clear-vpc-allowed-services)`     | `[--remove-vpc-allowed-services](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/update#--remove-vpc-allowed-services)`=[`VPC-ALLOWED-SERVICES`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/dry-run/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(BETA)` This command updates the dry-run mode configuration
(`spec`) for a Service Perimeter.
For Service Perimeters with an explicitly defined dry-run mode configuration
(i.e. an explicit `spec`), this operation updates that configuration
directly, ignoring enforcement mode configuration.
Service Perimeters that do not have explict dry-run mode configuration will
inherit the enforcement mode configuration in the dry-run mode. Therefore, this
command effectively clones the enforcement mode configuration, then applies the
update on that configuration, and uses that as the explicit dry-run mode
configuration.

**EXAMPLES**

: To update the dry-run mode configuration for a Service Perimeter:

```
gcloud beta access-context-manager perimeters dry-run update my-perimeter --add-resources="projects/123,projects/456" --remove-restricted-services="storage.googleapis.com" --add-access-levels="accessPolicies/123/accessLevels/a_level" --enable-vpc-accessible-services --clear-vpc-allowed-services
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

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--etag**:
The etag for the version of the Access Policy that this operation is to be
performed on. If, at the time of the operation, the etag for the Access Policy
stored in Access Context Manager is different from the specified etag, then the
commit operation will not be performed and the call will fail. If etag is not
provided, the operation will be performed as if a valid etag is provided.

**--add-access-levels**

**--add-resources**

**--add-restricted-services**

**--clear-egress-policies**

**--clear-ingress-policies**

**--enable-vpc-accessible-services**

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
gcloud access-context-manager perimeters dry-run update
```

```
gcloud alpha access-context-manager perimeters dry-run update
```