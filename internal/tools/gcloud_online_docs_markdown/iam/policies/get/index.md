# gcloud iam policies get  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/policies/get](https://cloud.google.com/sdk/gcloud/reference/iam/policies/get)*

**NAME**

: **gcloud iam policies get - get a policy on the given attachment point with the given name**

**SYNOPSIS**

: **`gcloud iam policies get` `[POLICY_ID](https://cloud.google.com/sdk/gcloud/reference/iam/policies/get#POLICY_ID)` `[--attachment-point](https://cloud.google.com/sdk/gcloud/reference/iam/policies/get#--attachment-point)`=`ATTACHMENT_POINT` `[--kind](https://cloud.google.com/sdk/gcloud/reference/iam/policies/get#--kind)`=`KIND` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/policies/get#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get a policy on the given attachment point with the given name.

**EXAMPLES**

: The following command gets the IAM policy defined at the resource project
``123`` of kind
``denypolicies`` and id
``my-deny-policy``:

```
gcloud iam policies get my-deny-policy --attachment-point=cloudresourcemanager.googleapis.com/projects/123 --kind=denypolicies
```

**POSITIONAL ARGUMENTS**

: **`POLICY_ID`**:
Policy ID that is unique for the resource to which the policy is attached.

**REQUIRED FLAGS**

: **--attachment-point**:
Resource to which the policy is attached. For valid formats, see [https://cloud.google.com/iam/help/deny/attachment-point](https://cloud.google.com/iam/help/deny/attachment-point).

**--kind**:
Policy type. Use `denypolicies` for deny policies.

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
gcloud alpha iam policies get
```

```
gcloud beta iam policies get
```