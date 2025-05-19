# gcloud alpha compute backend-services set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/set-iam-policy)*

**NAME**

: **gcloud alpha compute backend-services set-iam-policy - set the IAM policy binding for a Compute Engine backend service**

**SYNOPSIS**

: **`gcloud alpha compute backend-services set-iam-policy` `[BACKEND_SERVICE_NAME](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/set-iam-policy#BACKEND_SERVICE_NAME)` `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/set-iam-policy#POLICY_FILE)` [`[--global](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/set-iam-policy#--global)`     | `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/set-iam-policy#--region)`=`REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/backend-services/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Sets the IAM policy for the given backend service as
defined in a JSON or YAML file.

**EXAMPLES**

: The following command will read an IAM policy defined in a JSON file
'policy.json' and set it for the backend service
`my-backend-service`:

```
gcloud alpha compute backend-services set-iam-policy my-backend-service policy.json --region=REGION
```

```
gcloud alpha compute backend-services set-iam-policy my-backend-service policy.json --global
```

See [https://cloud.google.com/iam/docs/managing-policies](https://cloud.google.com/iam/docs/managing-policies)
for details of the policy file format and contents.

**POSITIONAL ARGUMENTS**

: **`BACKEND_SERVICE_NAME`**:
Name of the backend service to operate on.

**`POLICY_FILE`**:
Path to a local JSON or YAML formatted file containing a valid policy.
The output of the `get-iam-policy` command is a valid file, as is any
JSON or YAML file conforming to the structure of a [Policy](https://cloud.google.com/iam/reference/rest/v1/Policy).

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute backend-services set-iam-policy
```

```
gcloud beta compute backend-services set-iam-policy
```