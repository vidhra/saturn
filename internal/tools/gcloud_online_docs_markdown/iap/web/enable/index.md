# gcloud iap web enable  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iap/web/enable](https://cloud.google.com/sdk/gcloud/reference/iap/web/enable)*

**NAME**

: **gcloud iap web enable - enable Cloud Identity-Aware Proxy (Cloud IAP) on an IAP resource**

**SYNOPSIS**

: **`gcloud iap web enable` [`[--oauth2-client-id](https://cloud.google.com/sdk/gcloud/reference/iap/web/enable#--oauth2-client-id)`=`OAUTH2_CLIENT_ID` `[--oauth2-client-secret](https://cloud.google.com/sdk/gcloud/reference/iap/web/enable#--oauth2-client-secret)`=`OAUTH2_CLIENT_SECRET`] [`[--resource-type](https://cloud.google.com/sdk/gcloud/reference/iap/web/enable#--resource-type)`=`RESOURCE_TYPE` : `[--region](https://cloud.google.com/sdk/gcloud/reference/iap/web/enable#--region)`=`REGION` `[--service](https://cloud.google.com/sdk/gcloud/reference/iap/web/enable#--service)`=`SERVICE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iap/web/enable#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: This command enables Cloud Identity-Aware Proxy on an IAP resource. OAuth 2.0
credentials must be set, or must have been previously set, to enable IAP.

**EXAMPLES**

: To enable IAP on an App Engine application, run:

```
gcloud iap web enable --resource-type=app-engine --oauth2-client-id=CLIENT_ID --oauth2-client-secret=SECRET
```

To enable IAP on a global backend service, run:

```
gcloud iap web enable --resource-type=backend-services --oauth2-client-id=CLIENT_ID --oauth2-client-secret=SECRET --service=SERVICE_ID
```

To enable IAP on a region backend service, run:

```
gcloud iap web enable --resource-type=backend-services --oauth2-client-id=CLIENT_ID --oauth2-client-secret=SECRET --service=SERVICE_ID --region=REGION
```

**FLAGS**

: **--oauth2-client-id**:
OAuth 2.0 client ID to use.

**--oauth2-client-secret**:
OAuth 2.0 client secret to use.

**--resource-type**:
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
gcloud alpha iap web enable
```

```
gcloud beta iap web enable
```