# gcloud app create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/app/create](https://cloud.google.com/sdk/gcloud/reference/app/create)*

**NAME**

: **gcloud app create - create an App Engine app within the current Google Cloud Project**

**SYNOPSIS**

: **`gcloud app create` [`[--region](https://cloud.google.com/sdk/gcloud/reference/app/create#--region)`=`REGION`] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/app/create#--service-account)`=`SERVICE_ACCOUNT`] [`[--ssl-policy](https://cloud.google.com/sdk/gcloud/reference/app/create#--ssl-policy)`=`SSL_POLICY`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/app/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create an App Engine app within the current Google Cloud Project.

**EXAMPLES**

: To create an app with region chosen interactively, run:

```
gcloud app create
```

To create an app in the us-central region, run:

```
gcloud app create --region=us-central
```

To create an app that with a user-managed service account, run:

```
gcloud app create --service-account=SERVICE_ACCOUNT
```

To create an app with minimum SSL policy allowing TLS 1.2 and above, run:

```
gcloud app create --ssl-policy=TLS_VERSION_1_2
```

**FLAGS**

: **--region**:
The region to create the app within. Use `[gcloud app regions list](https://cloud.google.com/sdk/gcloud/reference/app/regions/list)`
to list available regions. If not provided, select region interactively.

**--service-account**:
The app-level default service account to create the app with. Note that you can
specify a distinct service account for each App Engine version with `gcloud
app deploy --service-account`. However if you do not specify a
version-level service account, this default will be used. If this parameter is
not provided for app creation, the app-level default will be set to be the
out-of-box App Engine Default Service Account, [https://cloud.google.com/appengine/docs/standard/python3/service-account](https://cloud.google.com/appengine/docs/standard/python3/service-account)
outlines the limitation of that service account.

**--ssl-policy**:
The app-level SSL policy to create the app with.
`SSL_POLICY` must be one of: `TLS_VERSION_1_0`,
`TLS_VERSION_1_2`.

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

: This variant is also available:

```
gcloud beta app create
```