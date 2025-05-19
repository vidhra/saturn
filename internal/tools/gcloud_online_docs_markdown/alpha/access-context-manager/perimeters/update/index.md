# gcloud alpha access-context-manager perimeters update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update)*

**NAME**

: **gcloud alpha access-context-manager perimeters update - update the enforced configuration for an existing Service Perimeter**

**SYNOPSIS**

: **`gcloud alpha access-context-manager perimeters update` (`[PERIMETER](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update#PERIMETER)` : `[--policy](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update#--policy)`=`POLICY`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update#--description)`=`DESCRIPTION`] [`[--etag](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update#--etag)`=`etag`] [`[--title](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update#--title)`=`TITLE`] [`[--type](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update#--type)`=`TYPE`] [`[--add-access-levels](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update#--add-access-levels)`=[`LEVEL`,…]     | `[--clear-access-levels](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update#--clear-access-levels)`     | `[--remove-access-levels](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update#--remove-access-levels)`=[`LEVEL`,…]     | `[--set-access-levels](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update#--set-access-levels)`=[`LEVEL`,…]] [`[--add-resources](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update#--add-resources)`=[`RESOURCES`,…]     | `[--clear-resources](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update#--clear-resources)`     | `[--remove-resources](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update#--remove-resources)`=[`RESOURCES`,…]     | `[--set-resources](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update#--set-resources)`=[`RESOURCES`,…]] [`[--add-restricted-services](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update#--add-restricted-services)`=[`SERVICE`,…]     | `[--clear-restricted-services](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update#--clear-restricted-services)`     | `[--remove-restricted-services](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update#--remove-restricted-services)`=[`SERVICE`,…]     | `[--set-restricted-services](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update#--set-restricted-services)`=[`SERVICE`,…]] [`[--clear-egress-policies](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update#--clear-egress-policies)`     | `[--set-egress-policies](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update#--set-egress-policies)`=`YAML_FILE`] [`[--clear-ingress-policies](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update#--clear-ingress-policies)`     | `[--set-ingress-policies](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update#--set-ingress-policies)`=`YAML_FILE`] [`[--enable-vpc-accessible-services](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update#--enable-vpc-accessible-services)` `[--add-vpc-allowed-services](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update#--add-vpc-allowed-services)`=[`VPC_SERVICE`,…]     | `[--clear-vpc-allowed-services](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update#--clear-vpc-allowed-services)`     | `[--remove-vpc-allowed-services](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update#--remove-vpc-allowed-services)`=[`VPC_SERVICE`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager/perimeters/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` This command updates the enforced configuration
(`status`) of a Service Perimeter.

**EXAMPLES**

: To update the enforced configuration for a Service Perimeter:

```
gcloud alpha access-context-manager perimeters update my-perimeter --add-resources="projects/123,projects/456" --remove-restricted-services="storage.googleapis.com" --add-access-levels="accessPolicies/123/accessLevels/a_level" --enable-vpc-accessible-services --clear-vpc-allowed-services
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

: **--description**:
Long-form description of service perimeter.

**--etag**:
The etag for the version of the Access Policy that this operation is to be
performed on. If, at the time of the operation, the etag for the Access Policy
stored in Access Context Manager is different from the specified etag, then the
commit operation will not be performed and the call will fail. If etag is not
provided, the operation will be performed as if a valid etag is provided.

**--title**:
Short human-readable title of the service perimeter.

**--type**:
Type of the perimeter.
A `regular` perimeter allows resources within this service perimeter
to import and export data amongst themselves. A project may belong to at most
one regular service perimeter.
A `bridge` perimeter allows resources in different regular service
perimeters to import and export data between each other. A project may belong to
multiple bridge service perimeters (only if it also belongs to a regular service
perimeter). Both restricted and unrestricted service lists, as well as access
level lists, must be empty.
`TYPE` must be one of: `bridge`,
`regular`.

**These flags modify the member access levels of this perimeter. An
intra-perimeter request must satisfy these access levels (for example,
`MY_LEVEL`; must be in the same access policy as this perimeter) to
be allowed.
At most one of these can be specified:

**--add-access-levels**:
Append the given values to the current access levels.

**--clear-access-levels**:
Empty the current access levels.

**--remove-access-levels**:
Remove the given values from the current access levels.

**--set-access-levels**:
Completely replace the current access levels with the given values.**

**These flags modify the member resources of this perimeter. Resources must be
projects, in the form `projects/<projectnumber>`.
At most one of these can be specified:

**--add-resources**:
Append the given values to the current resources.

**--clear-resources**:
Empty the current resources.

**--remove-resources**:
Remove the given values from the current resources.

**--set-resources**:
Completely replace the current resources with the given values.**

**These flags modify the member restricted services of this perimeter. The
perimeter boundary DOES apply to these services (for example,
`storage.googleapis.com`).
At most one of these can be specified:

**--add-restricted-services**:
Append the given values to the current restricted services.

**--clear-restricted-services**:
Empty the current restricted services.

**--remove-restricted-services**:
Remove the given values from the current restricted services.

**--set-restricted-services**:
Completely replace the current restricted services with the given values.**

**--clear-egress-policies**

**--clear-ingress-policies**

**--enable-vpc-accessible-services**:
When specified restrict API calls within the Service Perimeter to the set of vpc
allowed services. To disable use '--no-enable-vpc-accessible-services'.

**--add-vpc-allowed-services**

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud access-context-manager perimeters update
```

```
gcloud beta access-context-manager perimeters update
```