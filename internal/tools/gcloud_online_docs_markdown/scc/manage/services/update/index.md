# gcloud scc manage services update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/manage/services/update](https://cloud.google.com/sdk/gcloud/reference/scc/manage/services/update)*

**NAME**

: **gcloud scc manage services update - update a Security Command Center service**

**SYNOPSIS**

: **`gcloud scc manage services update` `[SERVICE_NAME](https://cloud.google.com/sdk/gcloud/reference/scc/manage/services/update#SERVICE_NAME)` (`[--enablement-state](https://cloud.google.com/sdk/gcloud/reference/scc/manage/services/update#--enablement-state)`=`ENABLEMENT_STATE` `[--module-config-file](https://cloud.google.com/sdk/gcloud/reference/scc/manage/services/update#--module-config-file)`=`PATH_TO_FILE`) (`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/manage/services/update#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/manage/services/update#--organization)`=`ORGANIZATION_ID`     | `[--parent](https://cloud.google.com/sdk/gcloud/reference/scc/manage/services/update#--parent)`=`PARENT`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/manage/services/update#--project)`=`PROJECT_ID_OR_NUMBER`) [`[--validate-only](https://cloud.google.com/sdk/gcloud/reference/scc/manage/services/update#--validate-only)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/manage/services/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update the enablement state of the Security Center service and its corresponding
modules for the specified folder, project or organization.

**EXAMPLES**

: To update a Security Center Service with name `sha` for organization
123, run:

```
gcloud scc manage services update sha --organization=organizations/123 --enablement-state="ENABLED"
```

To update a Security Center Service with name `sha` and its modules
for organization 123, run:

```
gcloud scc manage services update sha --organization=organizations/123 --enablement-state="ENABLED" --module-config-file=module_config.yaml
```

To validate an update of Security Center Service with name `sha` and
its modules for organization 123, run:

```
gcloud scc manage services update sha --organization=organizations/123 --enablement-state="ENABLED" --module-config-file=module_config.yaml --validate-only
```

**POSITIONAL ARGUMENTS**

: **`SERVICE_NAME`**:
The service name, provided either in lowercase hyphenated form (e.g.
security-health-analytics), or in abbreviated form (e.g. sha) if applicable.
The list of supported services is:

- security-health-analytics (can be abbreviated as sha)

- event-threat-detection (can be abbreviated as etd)

- container-threat-detection (can be abbreviated as ctd)

- vm-threat-detection (can be abbreviated as vmtd)

- web-security-scanner (can be abbreviated as wss)

- vm-threat-detection-aws (can be abbreviated as vmtd-aws)

- cloud-run-threat-detection (can be abbreviated as crtd)

**REQUIRED FLAGS**

: **--enablement-state**

**--folder**

**OPTIONAL FLAGS**

: **--validate-only**:
If present, the request is validated (including IAM checks) but no action is
taken.

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
gcloud alpha scc manage services update
```