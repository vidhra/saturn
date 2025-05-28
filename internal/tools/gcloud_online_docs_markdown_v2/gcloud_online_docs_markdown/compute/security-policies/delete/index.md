# gcloud compute security-policies delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/delete](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/delete)*

**NAME**

: **gcloud compute security-policies delete - delete security policies**

**SYNOPSIS**

: **`gcloud compute security-policies delete` `[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/delete#NAME)` [`[NAME](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/delete#NAME)` …] [`[--global](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/delete#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/delete#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute security-policies delete` deletes Compute Engine
security policies. Security policies can only be deleted when no other resources
(e.g., backend services) refer to them.

**EXAMPLES**

: To delete a security policy, run:

```
gcloud compute security-policies delete my-policy
```

**POSITIONAL ARGUMENTS**

: **`NAME` [`NAME` …]**:
Names of the security policies to delete.

**FLAGS**

: **--global**

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
gcloud alpha compute security-policies delete
```

```
gcloud beta compute security-policies delete
```