# gcloud iam workload-identity-pools providers update-oidc  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/providers/update-oidc](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/providers/update-oidc)*

**NAME**

: **gcloud iam workload-identity-pools providers update-oidc - update an OIDC workload identity pool provider**

**SYNOPSIS**

: **`gcloud iam workload-identity-pools providers update-oidc` (`[PROVIDER](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/providers/update-oidc#PROVIDER)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/providers/update-oidc#--location)`=`LOCATION` `[--workload-identity-pool](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/providers/update-oidc#--workload-identity-pool)`=`WORKLOAD_IDENTITY_POOL`) [`[--allowed-audiences](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/providers/update-oidc#--allowed-audiences)`=[`ALLOWED_AUDIENCES`,…]] [`[--attribute-condition](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/providers/update-oidc#--attribute-condition)`=`ATTRIBUTE_CONDITION`] [`[--attribute-mapping](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/providers/update-oidc#--attribute-mapping)`=[`KEY`=`VALUE`,…]] [`[--description](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/providers/update-oidc#--description)`=`DESCRIPTION`] [`[--disabled](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/providers/update-oidc#--disabled)`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/providers/update-oidc#--display-name)`=`DISPLAY_NAME`] [`[--issuer-uri](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/providers/update-oidc#--issuer-uri)`=`ISSUER_URI`] [`[--jwk-json-path](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/providers/update-oidc#--jwk-json-path)`=`PATH_TO_FILE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/workload-identity-pools/providers/update-oidc#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an OIDC workload identity pool provider.

**EXAMPLES**

: The following command updates the OIDC workload identity pool provider with the
ID ``my-workload-identity-pool-provider``.
Explicit values for all required and optional parameters are provided:

```
gcloud iam workload-identity-pools providers update-oidc my-workload-identity-pool-provider --location="global" --workload-identity-pool="my-workload-identity-pool" --display-name="My workload pool provider" --description="My workload pool provider description" --disabled --attribute-mapping="google.subject=assertion.sub" --attribute-condition="true" --issuer-uri="https://test-idp.com" --allowed-audiences=https://test-audience-1.com,https://\
test-audience-2.com --jwk-json-path="path/to/jwk.json"
```

**POSITIONAL ARGUMENTS**

: **Workload identity pool provider resource - The workload identity pool provider
to update. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `provider` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`PROVIDER`**:
ID of the workload identity pool provider or fully qualified identifier for the
workload identity pool provider.
To set the `provider` attribute:

- provide the argument `provider` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location name.
To set the `location` attribute:

- provide the argument `provider` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

**--workload-identity-pool**:
The ID to use for the pool, which becomes the final component of the resource
name. This value should be 4-32 characters, and may contain the characters
[a-z0-9-]. The prefix `gcp-` is reserved for use by Google, and may
not be specified.
To set the `workload-identity-pool` attribute:

- provide the argument `provider` on the command line with a fully
specified name;
- provide the argument `--workload-identity-pool` on the command line.**

**FLAGS**

: **--allowed-audiences**:
Acceptable values for the `aud` field (audience) in the OIDC token.
Token exchange requests are rejected if the token audience does not match one of
the configured values. Each audience may be at most 256 characters. A maximum of
10 audiences may be configured.
If this list is empty, the OIDC token audience must be equal to the full
canonical resource name of the workload identity pool provider, with or without
the HTTPS prefix. For example:

```
//iam.googleapis.com/projects/<project-number>/locations/<location>/workloadIdentityPools/<pool-id>/providers/<provider-id>
https://iam.googleapis.com/projects/<project-number>/locations/<location>/workloadIdentityPools/<pool-id>/providers/<provider-id>
```

**--attribute-condition**:
[A Common Expression
Language](https://opensource.google/projects/cel) expression, in plain text, to restrict what otherwise valid
authentication credentials issued by the provider should not be accepted.
The expression must output a boolean representing whether to allow the
federation.
The following keywords may be referenced in the expressions:

- `assertion`: JSON representing the authentication credential issued
by the provider.
- `google`: The Google attributes mapped from the assertion in the
`attribute_mappings`.
- `attribute`: The custom attributes mapped from the assertion in the
`attribute_mappings`.

The maximum length of the attribute condition expression is 4096 characters. If
unspecified, all valid authentication credential are accepted.
The following example shows how to only allow credentials with a mapped
`google.groups` value of `admins`:

```
"'admins' in google.groups"
```

**--attribute-mapping**:
Maps attributes from authentication credentials issued by an external identity
provider to Google Cloud attributes, such as `subject` and
`segment`.
Each key must be a string specifying the Google Cloud IAM attribute to map to.
The following keys are supported:

- `google.subject`: The principal IAM is authenticating. You can
reference this value in IAM bindings. This is also the subject that appears in
Cloud Logging logs. Cannot exceed 127 bytes.

- `google.groups`: Groups the external identity belongs to. You can
grant groups access to resources using an IAM `principalSet` binding;
access applies to all members of the group.

You can also provide custom attributes by specifying
`attribute.{custom_attribute}`, where `{custom_attribute}`
is the name of the custom attribute to be mapped. You can define a maximum of 50
custom attributes. The maximum length of a mapped attribute key is 100
characters, and the key may only contain the characters `[a-z_0-9]`.
You can reference these attributes in IAM policies to define fine-grained access
for a workload to Google Cloud resources. For example:

- `google.subject`:
`principal://iam.googleapis.com/projects/{project}/locations/{location}/workloadIdentityPools/{pool}/subject/{value}`

- `google.groups`:
`principalSet://iam.googleapis.com/projects/{project}/locations/{location}/workloadIdentityPools/{pool}/group/{value}`

- `attribute.{custom_attribute}`:
`principalSet://iam.googleapis.com/projects/{project}/locations/{location}/workloadIdentityPools/{pool}/attribute.{custom_attribute}/{value}`

Each value must be a [Common Expression Language]
(https://opensource.google/projects/cel) function that maps an identity provider
credential to the normalized attribute specified by the corresponding map key.
You can use the `assertion` keyword in the expression to access a
JSON representation of the authentication credential issued by the provider.
The maximum length of an attribute mapping expression is 2048 characters. When
evaluated, the total size of all mapped attributes must not exceed 8KB.
For AWS providers, the following rules apply:

- If no attribute mapping is defined, the following default mapping applies:

```
{
  "google.subject":"assertion.arn",
  "attribute.aws_role":
      "assertion.arn.contains('assumed-role')"
      " ? assertion.arn.extract('{account_arn}assumed-role/')"
      "   + 'assumed-role/'"
      "   + assertion.arn.extract('assumed-role/{role_name}/')"
      " : assertion.arn",
}
```

- If any custom attribute mappings are defined, they must include a mapping to the
`google.subject` attribute.

For OIDC providers, the following rules apply:

- Custom attribute mappings must be defined, and must include a mapping to the
`google.subject` attribute. For example, the following maps the
`sub` claim of the incoming credential to the `subject`
attribute on a Google token.

```
{"google.subject": "assertion.sub"}
```

**--description**:
A description for the provider. Cannot exceed 256 characters.

**--disabled**:
Whether the provider is disabled. You cannot use a disabled provider to exchange
tokens. However, existing tokens still grant access.

**--display-name**:
A display name for the provider. Cannot exceed 32 characters.

**--issuer-uri**:
The OIDC issuer URL.

**--jwk-json-path**:
Optional file containing jwk public keys. The file format must follow [jwk specifications](https://www.rfc-editor.org/rfc/rfc7517#section-4).
Example file format:
```
{
  "keys": [
     {
          "kty": "RSA/EC",
          "alg": "<algorithm>",
          "use": "sig",
          "kid": "<key-id>",
          "n": "",
          "e": "",
          "x": "",
          "y": "",
          "crv": ""
     }
  ]
}
```. Use a full or relative path to a local file containing the value of jwk_json_path.
```

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: --access-token-file, --account, --billing-project, --configuration, --flags-file, --flatten, --format, --help, --impersonate-service-account, --log-http, --project, --quiet, --trace-token, --user-output-enabled, --verbosity.

Run *$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)* for details.

**API REFERENCE**

: This command uses the *iam/v1* API. The full documentation for this API can be found at: [https://cloud.google.com/iam/](https://cloud.google.com/iam/)

**NOTES**

: These variants are also available:

`[gcloud alpha iam workload-identity-pools providers update-oidc](https://cloud.google.com/sdk/gcloud/reference/alpha/iam/workload-identity-pools/providers/update-oidc)`
`[gcloud beta iam workload-identity-pools providers update-oidc](https://cloud.google.com/sdk/gcloud/reference/beta/iam/workload-identity-pools/providers/update-oidc)`