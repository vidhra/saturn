# gcloud iam policies create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/policies/create](https://cloud.google.com/sdk/gcloud/reference/iam/policies/create)*

**NAME**

: **gcloud iam policies create - create a policy on the given attachment point with the given name**

**SYNOPSIS**

: **`gcloud iam policies create` `[POLICY_ID](https://cloud.google.com/sdk/gcloud/reference/iam/policies/create#POLICY_ID)` `[--attachment-point](https://cloud.google.com/sdk/gcloud/reference/iam/policies/create#--attachment-point)`=`ATTACHMENT_POINT` `[--kind](https://cloud.google.com/sdk/gcloud/reference/iam/policies/create#--kind)`=`KIND` `[--policy-file](https://cloud.google.com/sdk/gcloud/reference/iam/policies/create#--policy-file)`=`POLICY_FILE` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/policies/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a policy on the given attachment point with the given name.

**EXAMPLES**

: The following command creates the IAM policy defined at the resource project
``123`` of kind
``denypolicies`` and id
``my-deny-policy`` from the file
``policy.json``:

```
gcloud iam policies create my-deny-policy --attachment-point=cloudresourcemanager.googleapis.com/projects/123 --kind=denypolicies --policy-file=policy.json
```

**POSITIONAL ARGUMENTS**

: **`POLICY_ID`**:
Policy ID that is unique for the resource to which the policy is attached.

**REQUIRED FLAGS**

: **--attachment-point**:
Resource to which the policy is attached. For valid formats, see [https://cloud.google.com/iam/help/deny/attachment-point](https://cloud.google.com/iam/help/deny/attachment-point).

**--kind**:
Policy type. Use `denypolicies` for deny policies.

**--policy-file**:
Path to the file that contains the policy, in JSON or YAML format. For valid
syntax, see [https://cloud.google.com/iam/help/deny/policy-syntax](https://cloud.google.com/iam/help/deny/policy-syntax).

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

: These variants are also available:

```
gcloud alpha iam policies create
```

```
gcloud beta iam policies create
```