# gcloud iam policy-bindings describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/describe](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/describe)*

**NAME**

: **gcloud iam policy-bindings describe - get PolicyBinding instance**

**SYNOPSIS**

: **`gcloud iam policy-bindings describe` (`[POLICY_BINDING](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/describe#POLICY_BINDING)` : `[--folder](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/describe#--folder)`=`FOLDER` `[--location](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/describe#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/describe#--organization)`=`ORGANIZATION`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get PolicyBinding instance.

**EXAMPLES**

: To get the details of a single policy binding `my-binding` in
organization `123` run:

```
gcloud iam policy-bindings describe my-binding --organization=123 --location=global
```

**POSITIONAL ARGUMENTS**

: **PolicyBinding resource - The name of the policy binding to retrieve.
Format:

- `projects/{project_id}/locations/{location}/policyBindings/{policy_binding_id}`
- `projects/{project_number}/locations/{location}/policyBindings/{policy_binding_id}`
- `folders/{folder_id}/locations/{location}/policyBindings/{policy_binding_id}`
- `organizations/{organization_id}/locations/{location}/policyBindings/{policy_binding_id}`
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.

To set the `project` attribute:

- provide the argument `policy_binding` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`. This resource can be one of the
following types: [iam.folders.locations.policyBindings,
iam.organizations.locations.policyBindings,
iam.projects.locations.policyBindings].

This must be specified.

**`POLICY_BINDING`**:
ID of the policyBinding or fully qualified identifier for the policyBinding.
To set the `policy_binding` attribute:

- provide the argument `policy_binding` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--folder**:
The folder id of the policyBinding resource.
To set the `folder` attribute:

- provide the argument `policy_binding` on the command line with a
fully specified name;
- provide the argument `--folder` on the command line. Must be
specified for resource of type [iam.folders.locations.policyBindings].

**--location**:
The location id of the policyBinding resource.
To set the `location` attribute:

- provide the argument `policy_binding` on the command line with a
fully specified name;
- provide the argument `--location` on the command line.

**--organization**:
The organization id of the policyBinding resource.
To set the `organization` attribute:

- provide the argument `policy_binding` on the command line with a
fully specified name;
- provide the argument `--organization` on the command line. Must be
specified for resource of type [iam.organizations.locations.policyBindings].**

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
gcloud beta iam policy-bindings describe
```