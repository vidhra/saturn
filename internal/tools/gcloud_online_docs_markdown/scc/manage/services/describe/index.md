# gcloud scc manage services describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/scc/manage/services/describe](https://cloud.google.com/sdk/gcloud/reference/scc/manage/services/describe)*

**NAME**

: **gcloud scc manage services describe - get the details of a Security Command Center service**

**SYNOPSIS**

: **`gcloud scc manage services describe` `[SERVICE_NAME](https://cloud.google.com/sdk/gcloud/reference/scc/manage/services/describe#SERVICE_NAME)` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/scc/manage/services/describe#--folder)`=`FOLDER_ID`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/scc/manage/services/describe#--organization)`=`ORGANIZATION_ID`     | `[--parent](https://cloud.google.com/sdk/gcloud/reference/scc/manage/services/describe#--parent)`=`PARENT`     | `[--project](https://cloud.google.com/sdk/gcloud/reference/scc/manage/services/describe#--project)`=`PROJECT_ID_OR_NUMBER`) [`[--filter-modules](https://cloud.google.com/sdk/gcloud/reference/scc/manage/services/describe#--filter-modules)`=`FILTER_MODULES`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/scc/manage/services/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Get the details of a Security Command Center service. It resolves INHERITED
enablement states to ENABLED or DISABLED for services at ancestor levels. For
example, if the service is enabled at the ancestor level, services for all child
resources will have the enablement state set to ENABLED.

**EXAMPLES**

: To get the details of a Security Command Center service with name
`sha` for organization `123`, run:

```
gcloud scc manage services describe sha --organization=123
```

To get the details of a Security Command Center service with name
`sha` for folder `456`, run:

```
gcloud scc manage services describe sha --folder=456
```

To get the details of a Security Command Center service with ID `sha`
for project `789`, run:

```
gcloud scc manage services describe sha --project=789
```

You can also specify the parent more generally:

```
gcloud scc manage services describe sha --parent=organizations/123
```

To get the details of modules, `[ABC, DEF]` of a Security Command
Center service with name `sha` for organization `123`,
run:

```
gcloud scc manage services describe sha --module-list=[ABC, DEF] --organization=123
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

: **--folder**

**OPTIONAL FLAGS**

: **--filter-modules**:
If provided, only prints module information for modules specified in the list.
Provided as a comma separated list of module names in SCREAMING_SNAKE_CASE
format (e.g. WEB_UI_ENABLED, API_KEY_NOT_ROTATED). A single module name is also
valid.

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
gcloud alpha scc manage services describe
```