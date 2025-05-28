# gcloud scc custom-modules sha simulate  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/simulate](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/simulate)*

**NAME**

: **gcloud scc custom-modules sha simulate - validates a Security Health Analytics custom module**

**SYNOPSIS**

: **`gcloud scc custom-modules sha simulate` `[--custom-config-from-file](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/simulate#--custom-config-from-file)`=`PATH_TO_FILE` `[--resource-from-file](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/simulate#--resource-from-file)`=`PATH_TO_FILE` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/simulate#--folder)`=`FOLDER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/simulate#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/simulate#--project)`=`PROJECT`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/simulate#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Validates a given Security Health Analytics custom module and resource.

**EXAMPLES**

: To validate a Security Health Analytics custom module against a custom resource
for organization `123`, run:

```
gcloud scc custom-modules sha simulate --organization=organizations/123 --custom-config-from-file=/tmp/custom_config.yaml --resource-from-file=/tmp/resource.yaml
```

To validate a Security Health Analytics custom module against a custom resource
for folder `456`, run:

```
gcloud scc custom-modules sha simulate --folder=folders/456 --custom-config-from-file=/tmp/custom_config.yaml --resource-from-file=/tmp/resource.yaml
```

To validate a Security Health Analytics custom module against a custom resource
for project `789`, run:

```
gcloud scc custom-modules sha simulate --project=projects/789 --custom-config-from-file=/tmp/custom_config.yaml --resource-from-file=/tmp/resource.yaml
```

**REQUIRED FLAGS**

: **--custom-config-from-file**:
Path to a YAML file that contains the configuration for the Security Health
Analytics custom module. Use a full or relative path to a local file containing
the value of custom_config.

**--resource-from-file**:
Path to a YAML file that contains the resource data to validate the Security
Health Analytics custom module against. Use a full or relative path to a local
file containing the value of resource.

**--folder**

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

**API REFERENCE**

: This command uses the `securitycenter/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/security-command-center](https://cloud.google.com/security-command-center)

**NOTES**

: This variant is also available:

```
gcloud alpha scc custom-modules sha simulate
```