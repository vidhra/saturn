# gcloud iap web get-iam-policy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iap/web/get-iam-policy](https://cloud.google.com/sdk/gcloud/reference/iap/web/get-iam-policy)*

**NAME**

: **gcloud iap web get-iam-policy - get IAM policy for an IAP IAM resource**

**SYNOPSIS**

: **`gcloud iap web get-iam-policy` [`[--region](https://cloud.google.com/sdk/gcloud/reference/iap/web/get-iam-policy#--region)`=`REGION` `[--resource-type](https://cloud.google.com/sdk/gcloud/reference/iap/web/get-iam-policy#--resource-type)`=`RESOURCE_TYPE` `[--service](https://cloud.google.com/sdk/gcloud/reference/iap/web/get-iam-policy#--service)`=`SERVICE` `[--version](https://cloud.google.com/sdk/gcloud/reference/iap/web/get-iam-policy#--version)`=`VERSION`] [`[--filter](https://cloud.google.com/sdk/gcloud/reference/iap/web/get-iam-policy#--filter)`=`EXPRESSION`] [`[--limit](https://cloud.google.com/sdk/gcloud/reference/iap/web/get-iam-policy#--limit)`=`LIMIT`] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/iap/web/get-iam-policy#--page-size)`=`PAGE_SIZE`] [`[--sort-by](https://cloud.google.com/sdk/gcloud/reference/iap/web/get-iam-policy#--sort-by)`=[`FIELD`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iap/web/get-iam-policy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud iap web get-iam-policy` displays the IAM policy associated
with an IAP IAM resource. If formatted as JSON, the output can be edited and
used as a policy file for set-iam-policy. The output includes an "etag" field
identifying the version emitted and allowing detection of concurrent policy
updates; see $ [gcloud iap
web set-iam-policy](https://cloud.google.com/sdk/gcloud/reference/iap/web/set-iam-policy) for additional details.

**EXAMPLES**

: To get the IAM policy for the web accesses to the IAP protected resources within
the active project, run:

```
gcloud iap web get-iam-policy
```

To get the IAM policy for the web accesses to the IAP protected resources within
a project, run:

```
gcloud iap web get-iam-policy --project=PROJECT_ID
```

To get the IAM policy for the web accesses to the IAP protected resources within
an App Engine application, run:

```
gcloud iap web get-iam-policy --resource-type=app-engine
```

To get the IAM policy for the web accesses to the IAP protected resources within
an App Engine service, run:

```
gcloud iap web get-iam-policy --resource-type=app-engine --service=SERVICE_ID
```

To get the IAM policy for the web accesses to the IAP protected resources within
an App Engine service version, run:

```
gcloud iap web get-iam-policy --resource-type=app-engine --service=SERVICE_ID --version=VERSION
```

To get the IAM policy for the web accesses to the IAP protected resources within
all backend services, run:

```
gcloud iap web get-iam-policy --resource-type=backend-services
```

To get the IAM policy for the web accesses to the IAP protected resources within
a backend service, run:

```
gcloud iap web get-iam-policy --resource-type=backend-services --service=SERVICE_ID
```

To get the IAM policy for the web accesses to the IAP protected resources within
a regional backend service, run:

```
gcloud iap web get-iam-policy --resource-type=backend-services --service=SERVICE_ID --region=REGION
```

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

**LIST COMMAND FLAGS**

: **--filter**:
Apply a Boolean filter `EXPRESSION` to each resource item
to be listed. If the expression evaluates `True`, then that item is
listed. For more details and examples of filter expressions, run $ [gcloud topic filters](https://cloud.google.com/sdk/gcloud/reference/topic/filters). This flag
interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--limit**:
Maximum number of resources to list. The default is `unlimited`. This
flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--page-size**:
Some services group resource list output into pages. This flag specifies the
maximum number of resources per page. The default is determined by the service
if it supports paging, otherwise it is `unlimited` (no paging).
Paging may be applied before or after `--filter` and
`--limit` depending on the service.

**--sort-by**:
Comma-separated list of resource field key names to sort by. The default order
is ascending. Prefix a field with ``~´´ for descending order on that
field. This flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

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
gcloud alpha iap web get-iam-policy
```

```
gcloud beta iap web get-iam-policy
```