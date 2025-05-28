# gcloud iap web disable  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iap/web/disable](https://cloud.google.com/sdk/gcloud/reference/iap/web/disable)*

**NAME**

: **gcloud iap web disable - disable Cloud Identity-Aware Proxy (Cloud IAP) on an IAP resource**

**SYNOPSIS**

: **`gcloud iap web disable` [`[--resource-type](https://cloud.google.com/sdk/gcloud/reference/iap/web/disable#--resource-type)`=`RESOURCE_TYPE` : `[--region](https://cloud.google.com/sdk/gcloud/reference/iap/web/disable#--region)`=`REGION` `[--service](https://cloud.google.com/sdk/gcloud/reference/iap/web/disable#--service)`=`SERVICE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iap/web/disable#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command disables Cloud Identity-Aware Proxy on an IAP resource. Disabling
IAP does not clear the OAuth 2.0 credentials.

**EXAMPLES**

: To disable IAP on an App Engine application, run:

```
gcloud iap web disable --resource-type=app-engine
```

To disable IAP on a global backend service, run:

```
gcloud iap web disable --resource-type=backend-services --service=SERVICE_ID
```

To disable IAP on a region backend service, run:

```
gcloud iap web disable --resource-type=backend-services --service=SERVICE_ID --region=REGION
```

**FLAGS**

: **--resource-type**:
Resource type of the IAP resource. `RESOURCE_TYPE` must be
one of: `app-engine`, `backend-services`.

**--region**:
Region name. Not applicable for ``app-engine``.
Optional when ``resource-type`` is
``compute``.

**--service**:
Service name. Required with `--resource-type=backend-services`.

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
gcloud alpha iap web disable
```

```
gcloud beta iap web disable
```