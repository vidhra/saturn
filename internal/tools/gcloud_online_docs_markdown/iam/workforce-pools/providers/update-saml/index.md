# gcloud iam workforce-pools providers update-saml  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/update-saml](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/update-saml)*

**NAME**

: **gcloud iam workforce-pools providers update-saml - update a new SAML workforce pool provider**

**SYNOPSIS**

: **`gcloud iam workforce-pools providers update-saml` (`[PROVIDER](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/update-saml#PROVIDER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/update-saml#--location)`=`LOCATION` `[--workforce-pool](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/update-saml#--workforce-pool)`=`WORKFORCE_POOL`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/update-saml#--async)`] [`[--attribute-condition](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/update-saml#--attribute-condition)`=`ATTRIBUTE_CONDITION`] [`[--attribute-mapping](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/update-saml#--attribute-mapping)`=[`KEY`=`VALUE`,…]] [`[--description](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/update-saml#--description)`=`DESCRIPTION`] [`[--disabled](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/update-saml#--disabled)`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/update-saml#--display-name)`=`DISPLAY_NAME`] [`[--idp-metadata-path](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/update-saml#--idp-metadata-path)`=`PATH_TO_FILE`] [`[--clear-extra-attributes-config](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/update-saml#--clear-extra-attributes-config)`     | `[--extra-attributes-client-id](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/update-saml#--extra-attributes-client-id)`=`EXTRA_ATTRIBUTES_CLIENT_ID` `[--extra-attributes-client-secret-value](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/update-saml#--extra-attributes-client-secret-value)`=`EXTRA_ATTRIBUTES_CLIENT_SECRET_VALUE` `[--extra-attributes-filter](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/update-saml#--extra-attributes-filter)`=`EXTRA_ATTRIBUTES_FILTER` `[--extra-attributes-issuer-uri](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/update-saml#--extra-attributes-issuer-uri)`=`EXTRA_ATTRIBUTES_ISSUER_URI` `[--extra-attributes-type](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/update-saml#--extra-attributes-type)`=`EXTRA_ATTRIBUTES_TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/workforce-pools/providers/update-saml#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a new SAML workforce pool provider.

**EXAMPLES**

: The following command updates the SAML workforce pool provider with the ID
`my-workforce-pool-provider`. Explicit values for all required and
optional parameters are provided.

```
gcloud iam workforce-pools providers update-saml my-workforce-pool-provider --workforce-pool="my-workforce-pool" --location="global" --display-name="My Workforce Pool Provider" --description="My workforce pool provider description." --disabled --detailed_audit_logging --attribute-mapping="google.subject=assertion.sub" --attribute-condition="true" --idp-metadata-path="path/to/metdata/file.xml"
```

**POSITIONAL ARGUMENTS**

: **Workforce pool provider resource - The workforce pool provider to update. The
arguments in this group can be used to specify the attributes of this resource.
This must be specified.

**`PROVIDER`**:
ID of the workforce pool provider or fully qualified identifier for the
workforce pool provider.
To set the `provider` attribute:

- provide the argument `provider` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location for the workforce pool.
To set the `location` attribute:

- provide the argument `provider` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--workforce-pool**:
The ID to use for the workforce pool, which becomes the final component of the
resource name. This value must be a globally unique string of 6 to 63 lowercase
letters, digits, or hyphens. It must start with a letter, and cannot have a
trailing hyphen. The prefix `gcp-` is reserved for use by Google, and
may not be specified.
To set the `workforce-pool` attribute:

- provide the argument `provider` on the command line with a fully
specified name;
- provide the argument `--workforce-pool` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--attribute-condition**:
A [Common Expression
Language](https://opensource.google/projects/cel) expression, in plain text, to restrict which otherwise valid
authentication credentials issued by the provider should be accepted.
The expression must output a boolean representing whether to allow the
federation.
The following keywords may be referenced in the expressions:

- `assertion`: JSON representing the authentication credential issued
by the Provider.
- `google`: The Google attributes mapped from the assertion in the
`attribute_mappings`. `google.profile_photo` and
`google.display_name` are not supported.
- `attribute`: The custom attributes mapped from the assertion in the
`attribute_mappings`.

The maximum length of the attribute condition expression is 4096 characters. If
unspecified, all valid authentication credential will be accepted.
Example: Only allow credentials with a mapped `google.groups` value
of `admins`.

```
"'admins' in google.groups"
```

**--attribute-mapping**:
Maps claims from the authentication credentials issued by the Identity Provider
into Google Cloud IAM attributes, e.g. subject, segment.
Each key must be a string specifying the Google Cloud IAM attribute to be
produced.
The following predefined keys are currently supported:

- `google.subject`: required field that indicates the principal that is
being authenticated to IAM, and will be logged in all API accesses for which
Cloud Audit Logging is configured.

- `google.groups`: optional field that indicates asserted groups that
the user should be considered to belong to. You can create IAM bindings using
the groups attribute and access to a resource will be granted if any of the
groups asserted here match a group in the respective binding.

- `google.display_name`: optional field that overrides the name of the
user. If not set, `google.subject` will be displayed instead. This
attribute cannot be used in IAM policies. The maximum length of this field is
100 characters.

- `google.profile_photo`: optional fields that may be set to a valid
URL specifying the user's thumbnail photo. When set, the image will be visible
as the user's profile picture. If not set, a generic user icon will be displayed
instead. This attribute cannot be used in IAM policies.

Custom attributes can also be mapped by specifying
`attribute.{custom_attribute}`, replacing
`{custom_attribute}` with the name of the custom attribute to be
mapped. A maximum of 50 custom attribute mappings can be defined. The maximum
length of a mapped attribute key is 2048 characters and may only contain the
characters [a-z0-9`].
These attributes can then be referenced in IAM policies to define fine-grained
access for the workforce pool to Google Cloud resources by specifying:

- `google.subject`:
`principal://iam.googleapis.com/locations/global/workforcePools/{pool}/subject/{value}`

- `google.groups`:
`principalSet://iam.googleapis.com/locations/global/workforcePools/{pool}/group/{value}`

- `attribute.{custom_attribute}`:
`principalSet://iam.googleapis.com/locations/global/workforcePools/{pool}/attribute.{custom_attribute}/{value}`

Each value must be a [Common
Expression Language](https://opensource.google/projects/cel) function that maps an Identity Provider credential to
the normalized attribute specified by the corresponding map key.
The following keywords may be referenced in the expressions:

- `assertion`: JSON representing the authentication credential issued
by the Identity Provider.

The maximum length of an attribute mapping expression is 2048 characters. When
evaluated, the total size of all mapped attributes must not exceed 8KB.
Example: Map the `sub` claim of the incoming credential to the
`subject` Google Cloud IAM attribute.

```
{"google.subject": "assertion.sub"}
````

**--description**:
A description for the workforce pool provider. Cannot exceed 256 characters in
length.

**--disabled**:
Disables the workforce pool provider. You cannot use a disabled provider to
perform new token exchanges or sign-ins. However, existing tokens still grant
access. Specify `--no-disabled` to enable a disabled pool.

**--display-name**:
A display name for the workforce pool provider. Cannot exceed 32 characters in
length.

**--idp-metadata-path**:
XML file with configuration metadata for the SAML identity provider. The
metadata file must follow the [SAML
2.0 metadata specification](https://www.oasis-open.org/committees/download.php/35391/sstc-saml-metadata-errata-2.0-wd-04-diff.pdf). Use a full or relative path to a local file
containing the value of idp_metadata_path.

**--clear-extra-attributes-config**

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

: This command uses the `iam/v1` API. The full documentation for this
API can be found at: [https://cloud.google.com/iam/](https://cloud.google.com/iam/)