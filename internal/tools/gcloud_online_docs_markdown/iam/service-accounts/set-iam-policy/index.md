# gcloud iam service-accounts set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/set-iam-policy)*

**NAME**

: **gcloud iam service-accounts set-iam-policy - set IAM policy for a service account**

**SYNOPSIS**

: **`gcloud iam service-accounts set-iam-policy` `[SERVICE_ACCOUNT](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/set-iam-policy#SERVICE_ACCOUNT)` `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/set-iam-policy#POLICY_FILE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command replaces the existing IAM policy for a service account, given an
IAM_ACCOUNT and a file encoded in JSON or YAML that contains the IAM policy. If
the given policy file specifies an "etag" value, then the replacement will
succeed only if the policy already in place matches that etag. (An etag obtained
via $ [gcloud
iam service-accounts get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/iam/service-accounts/get-iam-policy) will prevent the replacement if the
policy for the service account has been subsequently updated.) A policy file
that does not contain an etag value will replace any existing policy for the
service account.
If the service account does not exist, this command returns a
`PERMISSION_DENIED` error.
When managing IAM roles, you can treat a service account either as a resource or
as an identity. This command is to set the iam policy of a service account
resource. There are other gcloud commands to manage IAM policies for other types
of resources. For example, to manage IAM policies on a project, use the `$
[gcloud projects](https://cloud.google.com/sdk/gcloud/reference/projects)` commands.

**EXAMPLES**

: The following command will read an IAM policy from 'policy.json' and set it for
a service account with 'my-iam-account@my-project.iam.gserviceaccount.com' as
the identifier:

```
gcloud iam service-accounts set-iam-policy my-iam-account@my-project.iam.gserviceaccount.com policy.json
```

See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of the policy file format and contents.

**POSITIONAL ARGUMENTS**

: **`SERVICE_ACCOUNT`**:
The service account whose policy to set. The account should be formatted either
as a numeric service account ID or as an email, like this: 123456789876543212345
or my-iam-account@somedomain.com.

**`POLICY_FILE`**:
Path to a local JSON or YAML formatted file containing a valid policy.

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
gcloud alpha iam service-accounts set-iam-policy
```

```
gcloud beta iam service-accounts set-iam-policy
```