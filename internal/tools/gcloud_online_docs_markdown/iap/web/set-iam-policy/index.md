# gcloud iap web set-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iap/web/set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/iap/web/set-iam-policy)*

**NAME**

: **gcloud iap web set-iam-policy - set the IAM policy for an IAP IAM resource**

**SYNOPSIS**

: **`gcloud iap web set-iam-policy` `[POLICY_FILE](https://cloud.google.com/sdk/gcloud/reference/iap/web/set-iam-policy#POLICY_FILE)` [`[--region](https://cloud.google.com/sdk/gcloud/reference/iap/web/set-iam-policy#--region)`=`REGION` `[--resource-type](https://cloud.google.com/sdk/gcloud/reference/iap/web/set-iam-policy#--resource-type)`=`RESOURCE_TYPE` `[--service](https://cloud.google.com/sdk/gcloud/reference/iap/web/set-iam-policy#--service)`=`SERVICE` `[--version](https://cloud.google.com/sdk/gcloud/reference/iap/web/set-iam-policy#--version)`=`VERSION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iap/web/set-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command replaces the existing IAM policy for an IAP IAM resource, given a
file encoded in JSON or YAML that contains the IAM policy. If the given policy
file specifies an "etag" value, then the replacement will succeed only if the
policy already in place matches that etag. (An etag obtained via $ [gcloud iap web
get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/iap/web/get-iam-policy) will prevent the replacement if the policy for the resource
has been subsequently updated.) A policy file that does not contain an etag
value will replace any existing policy for the resource.

**EXAMPLES**

: To set the IAM policy for the web accesses to the IAP protected resources within
the active project, run:

```
gcloud iap web set-iam-policy POLICY_FILE
```

To set the IAM policy for the web accesses to the IAP protected resources within
a project, run:

```
gcloud iap web set-iam-policy POLICY_FILE --project=PROJECT_ID
```

To set the IAM policy for the web accesses to the IAP protected resources within
an App Engine application, run:

```
gcloud iap web set-iam-policy POLICY_FILE --resource-type=app-engine
```

To set the IAM policy for the web accesses to the IAP protected resources within
an App Engine service, run:

```
gcloud iap web set-iam-policy POLICY_FILE --resource-type=app-engine --service=SERVICE_ID
```

To set the IAM policy for the web accesses to the IAP protected resources within
an App Engine service version, run:

```
gcloud iap web set-iam-policy POLICY_FILE --resource-type=app-engine --service=SERVICE_ID --version=VERSION
```

To set the IAM policy for the web accesses to the IAP protected resources within
all backend services, run:

```
gcloud iap web set-iam-policy POLICY_FILE --resource-type=backend-services
```

To set the IAM policy for the web accesses to the IAP protected resources within
a backend service, run:

```
gcloud iap web set-iam-policy POLICY_FILE --resource-type=backend-services --service=SERVICE_ID
```

To set the IAM policy for the web accesses to the IAP protected resources within
a regional backend service, run:

```
gcloud iap web set-iam-policy POLICY_FILE --resource-type=backend-services --service=SERVICE_ID --region=REGION
```

**POSITIONAL ARGUMENTS**

: **`POLICY_FILE`**:
JSON or YAML file containing the IAM policy.

**FLAGS**

: **--region**:
Region name. Should only be specified with
`--resource-type=backend-services` if it is a regional scoped. Not
applicable for global scoped backend services.

**--resource-type**:
Resource type of the IAP resource. `RESOURCE_TYPE` must be
one of: `app-engine`, `backend-services`,
`forwarding-rule`.

**--service**:
Service name.

**--version**:
Service version. Should only be specified with
`--resource-type=app-engine`.

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
gcloud alpha iap web set-iam-policy
```

```
gcloud beta iap web set-iam-policy
```