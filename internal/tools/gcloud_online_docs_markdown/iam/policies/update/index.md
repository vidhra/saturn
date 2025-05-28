# gcloud iam policies update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/policies/update](https://cloud.google.com/sdk/gcloud/reference/iam/policies/update)*

**NAME**

: **gcloud iam policies update - update the policy on the given attachment point with the given name**

**SYNOPSIS**

: **`gcloud iam policies update` `[POLICY_ID](https://cloud.google.com/sdk/gcloud/reference/iam/policies/update#POLICY_ID)` `[--attachment-point](https://cloud.google.com/sdk/gcloud/reference/iam/policies/update#--attachment-point)`=`ATTACHMENT_POINT` `[--kind](https://cloud.google.com/sdk/gcloud/reference/iam/policies/update#--kind)`=`KIND` `[--policy-file](https://cloud.google.com/sdk/gcloud/reference/iam/policies/update#--policy-file)`=`POLICY_FILE` [`[--etag](https://cloud.google.com/sdk/gcloud/reference/iam/policies/update#--etag)`=`ETAG`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/policies/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the policy on the given attachment point with the given name.

**EXAMPLES**

: The following command updates the IAM policy
``my-deny-policy``, which is attached to the
resource project ``123`` and has the etag
``abc``:

```
gcloud iam policies update my-deny-policy --attachment-point=cloudresourcemanager.googleapis.com/projects/123 --kind=denypolicies --policy-file=policy.json --etag=abc
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

**OPTIONAL FLAGS**

: **--etag**:
Etag that identifies the version of the existing policy. It can be obtained by
running `[gcloud iam
policies get](https://cloud.google.com/sdk/gcloud/reference/iam/policies/get)`. When deleting a policy, if the etag is omitted, the
policy is deleted regardless of its current etag. When updating a policy, if the
etag is omitted, the update uses the etag provided in the policy file.

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
gcloud alpha iam policies update
```

```
gcloud beta iam policies update
```