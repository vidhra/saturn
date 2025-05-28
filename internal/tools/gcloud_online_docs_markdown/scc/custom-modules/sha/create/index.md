# gcloud scc custom-modules sha create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/create](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/create)*

**NAME**

: **gcloud scc custom-modules sha create - create a Security Health Analytics custom module**

**SYNOPSIS**

: **`gcloud scc custom-modules sha create` `[--custom-config-from-file](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/create#--custom-config-from-file)`=`PATH_TO_FILE` `[--display-name](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/create#--display-name)`=`DISPLAY_NAME` `[--enablement-state](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/create#--enablement-state)`=`ENABLEMENT_STATE` [`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/create#--folder)`=`FOLDER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/create#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/create#--project)`=`PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Security Health Analytics custom module.

**EXAMPLES**

: To create a Security Health Analytics custom module for given organization
`123`, run:

```
gcloud scc custom-modules sha create --organization=organizations/123 --display-name="test_display_name" --enablement-state="ENABLED" --custom-config-from-file=custom_config.yaml
```

To create a Security Health Analytics custom module for given folder
`456`, run:

```
gcloud scc custom-modules sha create --folder=folders/456 --display-name="test_display_name" --enablement-state="ENABLED" --custom-config-from-file=custom_config.yaml
```

To create a Security Health Analytics custom module for given project
`789`, run:

```
gcloud scc custom-modules sha create --project=projects/789 --display-name="test_display_name" --enablement-state="ENABLED" --custom-config-from-file=custom_config.yaml
```

**REQUIRED FLAGS**

: **--custom-config-from-file**:
Path to a YAML file that contains the configuration for the Security Health
Analytics custom module. Use a full or relative path to a local file containing
the value of custom_config.

**--display-name**:
Sets the display name of the Security Health Analytics custom module. This
display name becomes the finding category for all findings that are returned by
this custom module. The display name must be between 1 and 128 characters, start
with a lowercase letter, and contain alphanumeric characters or underscores
only.

**--enablement-state**:
Sets the enablement state of the Security Health Analytics custom module. From
the following list of possible enablement states, specify either enabled or
disabled only. `ENABLEMENT_STATE` must be one of:
`disabled`, `enabled`,
`enablement-state-unspecified`, `inherited`.

**OPTIONAL FLAGS**

: **--folder**

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
gcloud alpha scc custom-modules sha create
```