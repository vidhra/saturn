# gcloud scc custom-modules sha update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/update](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/update)*

**NAME**

: **gcloud scc custom-modules sha update - update a Security Health Analytics custom module**

**SYNOPSIS**

: **`gcloud scc custom-modules sha update` `[CUSTOM_MODULE](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/update#CUSTOM_MODULE)` [`[--custom-config-from-file](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/update#--custom-config-from-file)`=`PATH_TO_FILE`] [`[--enablement-state](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/update#--enablement-state)`=`ENABLEMENT_STATE`] [`[--update-mask](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/update#--update-mask)`=`UPDATE_MASK`] [`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/update#--folder)`=`FOLDER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/update#--organization)`=`ORGANIZATION`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/update#--project)`=`PROJECT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/custom-modules/sha/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Security Health Analytics custom module.

**EXAMPLES**

: To update a Security Health Analytics custom module with ID `123456`
for organization `123, run`:

```
gcloud scc custom-modules sha update 123456 --organization=organizations/123 --enablement-state="ENABLED" --custom-config-from-file=custom_config.yaml
```

To update a Security Health Analytics custom module with ID `123456`
for folder `456`, run:

```
gcloud scc custom-modules sha update 123456 --folder=folders/456 --enablement-state="ENABLED" --custom-config-from-file=custom_config.yaml
```

To update a Security Health Analytics custom module with ID `123456`
for project `789`, run:

```
gcloud scc custom-modules sha update 123456 --project=projects/789 --enablement-state="ENABLED" --custom-config-from-file=custom_config.yaml
```

**POSITIONAL ARGUMENTS**

: **`CUSTOM_MODULE`**:
ID or the full resource name of the Security Health Analytics custom module. If
you specify the full resource name, you do not need to specify the
--organization, --folder, or --project flags.

**FLAGS**

: **--custom-config-from-file**:
Path to a YAML file that contains the configuration for the Security Health
Analytics custom module. Use a full or relative path to a local file containing
the value of custom_config.

**--enablement-state**:
Sets the enablement state of the Security Health Analytics custom module. From
the following list of possible enablement states, specify either enabled,
disabled or inherited only. `ENABLEMENT_STATE` must be one
of: `disabled`, `enabled`,
`enablement-state-unspecified`, `inherited`.

**--update-mask**:
Optional: If left unspecified (default), an update-mask is automatically created
using the flags specified in the command and only those values are updated.

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
gcloud alpha scc custom-modules sha update
```