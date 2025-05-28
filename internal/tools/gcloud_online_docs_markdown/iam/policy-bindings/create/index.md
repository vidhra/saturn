# gcloud iam policy-bindings create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/create](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/create)*

**NAME**

: **gcloud iam policy-bindings create - create PolicyBinding instance**

**SYNOPSIS**

: **`gcloud iam policy-bindings create` (`[POLICY_BINDING](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/create#POLICY_BINDING)` : `[--folder](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/create#--folder)`=`FOLDER` `[--location](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/create#--location)`=`LOCATION` `[--organization](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/create#--organization)`=`ORGANIZATION`) `[--policy](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/create#--policy)`=`POLICY` `[--target-principal-set](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/create#--target-principal-set)`=`TARGET_PRINCIPAL_SET` [`[--annotations](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/create#--annotations)`=[`ANNOTATIONS`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/create#--async)`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/create#--display-name)`=`DISPLAY_NAME`] [`[--etag](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/create#--etag)`=`ETAG`] [`[--policy-kind](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/create#--policy-kind)`=`POLICY_KIND`] [`[--condition-description](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/create#--condition-description)`=`CONDITION_DESCRIPTION` `[--condition-expression](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/create#--condition-expression)`=`CONDITION_EXPRESSION` `[--condition-location](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/create#--condition-location)`=`CONDITION_LOCATION` `[--condition-title](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/create#--condition-title)`=`CONDITION_TITLE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create PolicyBinding instance.

**EXAMPLES**

: To create a policy binding instance called `my-binding` that
references a principal access boundary policy run:

```
gcloud iam policy-bindings create my-binding --organization=123 --location=global --policy=organizations/123/locations/global/principalAccessBoundaryPolicies/my-policy --target-principal-set=//cloudresourcemanager.googleapis.com/organizations/123
```

**POSITIONAL ARGUMENTS**

: **PolicyBinding resource - Identifier. The name of the policy binding, in the
format
`{binding_parent/locations/{location}/policyBindings/{policy_binding_id}`.
The binding parent is the closest Resource Manager resource (i.e., Project,
Folder or Organization) to the binding target.
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

**REQUIRED FLAGS**

: **--policy**:
The resource name of the policy to be bound. The binding parent and policy must
belong to the same Organization (or Project).

**--target-principal-set**

**OPTIONAL FLAGS**

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
The description of the policy binding. Must be less than or equal to 63
characters.

**--etag**:
The etag for the policy binding. If this is provided on update, it must match
the server's etag.

**--policy-kind**:
The kind of the policy to attach in this binding. This field must be one of the
following:

- Left empty (will be automatically set to the policy kind)
- The input policy kind.

`POLICY_KIND` must be (only one value is supported):

**`principal-access-boundary`**:
Principal access boundary policy kind

**--condition-description**

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
gcloud beta iam policy-bindings create
```