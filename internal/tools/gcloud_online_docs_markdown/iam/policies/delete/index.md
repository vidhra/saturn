# gcloud iam policies delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/policies/delete](https://cloud.google.com/sdk/gcloud/reference/iam/policies/delete)*

**NAME**

: **gcloud iam policies delete - delete a policy on the given attachment point with the given name**

**SYNOPSIS**

: **`gcloud iam policies delete` `[POLICY_ID](https://cloud.google.com/sdk/gcloud/reference/iam/policies/delete#POLICY_ID)` `[--attachment-point](https://cloud.google.com/sdk/gcloud/reference/iam/policies/delete#--attachment-point)`=`ATTACHMENT_POINT` `[--kind](https://cloud.google.com/sdk/gcloud/reference/iam/policies/delete#--kind)`=`KIND` [`[--etag](https://cloud.google.com/sdk/gcloud/reference/iam/policies/delete#--etag)`=`ETAG`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/policies/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a policy on the given attachment point with the given name.

**EXAMPLES**

: The following command deletes the IAM policy defined at the resource project
``123`` of kind
``denypolicies`` and id
``my-deny-policy``, with etag
``abc``:

```
gcloud iam policies delete my-deny-policy --attachment-point=cloudresourcemanager.googleapis.com/projects/123 --kind=denypolicies --etag=abc
```

**POSITIONAL ARGUMENTS**

: **`POLICY_ID`**:
Policy ID that is unique for the resource to which the policy is attached.

**REQUIRED FLAGS**

: **--attachment-point**:
Resource to which the policy is attached. For valid formats, see [https://cloud.google.com/iam/help/deny/attachment-point](https://cloud.google.com/iam/help/deny/attachment-point).

**--kind**:
Policy type. Use `denypolicies` for deny policies.

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
gcloud alpha iam policies delete
```

```
gcloud beta iam policies delete
```