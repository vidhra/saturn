# gcloud anthos config controller get-config-connector-identity  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/anthos/config/controller/get-config-connector-identity](https://cloud.google.com/sdk/gcloud/reference/anthos/config/controller/get-config-connector-identity)*

**NAME**

: **gcloud anthos config controller get-config-connector-identity - fetch default Config Connector identity**

**SYNOPSIS**

: **`gcloud anthos config controller get-config-connector-identity` `[NAME](https://cloud.google.com/sdk/gcloud/reference/anthos/config/controller/get-config-connector-identity#NAME)` `[--location](https://cloud.google.com/sdk/gcloud/reference/anthos/config/controller/get-config-connector-identity#--location)`=`LOCATION` [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/anthos/config/controller/get-config-connector-identity#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: gcloud anthos config controller get-config-connector-identity prints the default
Config Connector Google Service Account in a specific Anthos Config Controller.

**EXAMPLES**

: To print the default Config Connector identity used by your Config Controller
'main' in the location 'us-central1', run:

```
gcloud anthos config controller get-config-connector-identity main --location=us-central1
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
Name of the Anthos Config Controller.

**REQUIRED FLAGS**

: **--location**:
The location (region) of the Anthos Config Controller.

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
gcloud alpha anthos config controller get-config-connector-identity
```