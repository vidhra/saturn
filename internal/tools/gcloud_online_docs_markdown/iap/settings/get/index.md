# gcloud iap settings get  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/iap/settings/get](https://cloud.google.com/sdk/gcloud/reference/iap/settings/get)*

**NAME**

: **gcloud iap settings get - get the setting for an IAP resource**

**SYNOPSIS**

: **`gcloud iap settings get` [`[--folder](https://cloud.google.com/sdk/gcloud/reference/iap/settings/get#--folder)`=`FOLDER` `[--organization](https://cloud.google.com/sdk/gcloud/reference/iap/settings/get#--organization)`=`ORGANIZATION` `[--project](https://cloud.google.com/sdk/gcloud/reference/iap/settings/get#--project)`=`PROJECT` `[--region](https://cloud.google.com/sdk/gcloud/reference/iap/settings/get#--region)`=`REGION` `[--resource-type](https://cloud.google.com/sdk/gcloud/reference/iap/settings/get#--resource-type)`=`RESOURCE_TYPE` `[--service](https://cloud.google.com/sdk/gcloud/reference/iap/settings/get#--service)`=`SERVICE` `[--version](https://cloud.google.com/sdk/gcloud/reference/iap/settings/get#--version)`=`VERSION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/iap/settings/get#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get the setting for an IAP resource.

**EXAMPLES**

: To get the IAP setting for the resources within an organization, run:

```
gcloud iap settings get --organization=ORGANIZATION_ID
```

To get the IAP setting for the resources within a folder, run:

```
gcloud iap settings get --folder=FOLDER_ID
```

To get the IAP setting for the resources within a project, run:

```
gcloud iap settings get --project=PROJECT_ID
```

To get the IAP setting for web type resources within a project, run:

```
gcloud iap settings get --project=PROJECT_ID --resource-type=iap_web
```

To get the IAP setting for all app engine services within a project, run:

```
gcloud iap settings get --project=PROJECT_ID --resource-type=app-engine
```

To get the IAP setting for an app engine service within a project, run:

```
gcloud iap settings get --project=PROJECT_ID --resource-type=app-engine --service=SERVICE_ID
```

To get the IAP setting for an app engine service version within a project, run:

```
gcloud iap settings get --project=PROJECT_ID --resource-type=app-engine --service=SERVICE_ID --version=VERSION_ID
```

To get the IAP setting for all backend services within a project, run:

```
gcloud iap settings get --project=PROJECT_ID --resource-type=backend-services
```

To get the IAP setting for a backend service within a project, run:

```
gcloud iap settings get --project=PROJECT_ID --resource-type=backend-services --service=SERVICE_ID
```

To get the IAP setting for a regional backend service within a project, run:

```
gcloud iap settings get --project=PROJECT_ID --resource-type=backend-services --service=SERVICE_ID --region=REGION_ID
```

To get the IAP setting for all forwarding rules within a project, run:

```
gcloud iap settings get --project=PROJECT_ID --resource-type=forwarding-rule
```

To get the IAP setting for a forwarding rule within a project, run:

```
gcloud iap settings get --project=PROJECT_ID --resource-type=forwarding-rule --service=SERVICE_ID
```

To get the IAP setting for a regional forwarding rule within a project, run:

```
gcloud iap settings get --project=PROJECT_ID --resource-type=forwarding-rule --service=SERVICE_ID --region=REGION_ID
```

**FLAGS**

: **--folder**:
Folder ID.

**--organization**:
Organization ID.

**--project**:
Project ID.

**--region**:
Region name. Not applicable for `app-engine`. Required when
`resource-type=compute` and regional scoped. Not applicable for
global scoped compute.

**--resource-type**:
Resource type of the IAP resource. For Backend Services, you can use both
`compute` and `backend-services` as resource type.
`RESOURCE_TYPE` must be one of: `app-engine`,
`iap_web`, `compute`, `organization`,
`folder`, `backend-services`,
`forwarding-rule`.

**--service**:
Service name. Optional when `resource-type` is `compute`
or `app-engine`.

**--version**:
Version name. Not applicable for `compute`. Optional when
`resource-type=app-engine`.

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
gcloud alpha iap settings get
```

```
gcloud beta iap settings get
```