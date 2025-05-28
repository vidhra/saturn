# gcloud endpoints services check-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/endpoints/services/check-iam-policy](https://cloud.google.com/sdk/gcloud/reference/endpoints/services/check-iam-policy)*

**NAME**

: **gcloud endpoints services check-iam-policy - returns information about a principal's permissions on a service**

**SYNOPSIS**

: **`gcloud endpoints services check-iam-policy` `[SERVICE](https://cloud.google.com/sdk/gcloud/reference/endpoints/services/check-iam-policy#SERVICE)` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/endpoints/services/check-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command lists the permissions that the current authenticated gcloud user
has for a service. For example, if the authenticated user is able to delete the
service, `servicemanagement.services.delete` will be among the
returned permissions.

**EXAMPLES**

: To check the permissions for the currently authenticated gcloud, run:

```
gcloud endpoints services check-iam-policy my_produced_service_name
```

**POSITIONAL ARGUMENTS**

: **`SERVICE`**:
The name of the service for which to check the IAM policy.

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
gcloud alpha endpoints services check-iam-policy
```

```
gcloud beta endpoints services check-iam-policy
```