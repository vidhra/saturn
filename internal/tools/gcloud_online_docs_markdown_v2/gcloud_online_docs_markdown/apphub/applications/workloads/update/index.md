# gcloud apphub applications workloads update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/apphub/applications/workloads/update](https://cloud.google.com/sdk/gcloud/reference/apphub/applications/workloads/update)*

**NAME**

: **gcloud apphub applications workloads update - update an Apphub application workload**

**SYNOPSIS**

: **`gcloud apphub applications workloads update` (`[WORKLOAD](https://cloud.google.com/sdk/gcloud/reference/apphub/applications/workloads/update#WORKLOAD)` : `[--application](https://cloud.google.com/sdk/gcloud/reference/apphub/applications/workloads/update#--application)`=`APPLICATION` `[--location](https://cloud.google.com/sdk/gcloud/reference/apphub/applications/workloads/update#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/apphub/applications/workloads/update#--async)`] [`[--business-owners](https://cloud.google.com/sdk/gcloud/reference/apphub/applications/workloads/update#--business-owners)`=[`display-name`=`DISPLAY-NAME`],[`email`=`EMAIL`]] [`[--criticality-type](https://cloud.google.com/sdk/gcloud/reference/apphub/applications/workloads/update#--criticality-type)`=`CRITICALITY_TYPE`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/apphub/applications/workloads/update#--description)`=`DESCRIPTION`] [`[--developer-owners](https://cloud.google.com/sdk/gcloud/reference/apphub/applications/workloads/update#--developer-owners)`=[`display-name`=`DISPLAY-NAME`],[`email`=`EMAIL`]] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/apphub/applications/workloads/update#--display-name)`=`DISPLAY_NAME`] [`[--environment-type](https://cloud.google.com/sdk/gcloud/reference/apphub/applications/workloads/update#--environment-type)`=`ENVIRONMENT_TYPE`] [`[--operator-owners](https://cloud.google.com/sdk/gcloud/reference/apphub/applications/workloads/update#--operator-owners)`=[`display-name`=`DISPLAY-NAME`],[`email`=`EMAIL`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/apphub/applications/workloads/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an Apphub application workload.

**EXAMPLES**

: To update the Workload `my-workload` with a new environment
`prod` in the Application `my-app` in location
`us-east1`, run:

```
gcloud apphub applications workloads update my-workload --environment-type=TEST --application=my-app --location=us-east1
```

**POSITIONAL ARGUMENTS**

: **Workload resource - The Workload ID. The arguments in this group can be used to
specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `workload` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`WORKLOAD`**:
ID of the workload or fully qualified identifier for the workload.
To set the `workload` attribute:

- provide the argument `workload` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--application**:
Name for the application
To set the `application` attribute:

- provide the argument `workload` on the command line with a fully
specified name;
- provide the argument `--application` on the command line.

**--location**:
The Cloud location for the workload.
To set the `location` attribute:

- provide the argument `workload` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--business-owners**:
Business owners of the workload

**--criticality-type**:
Criticality Type of the workload. `CRITICALITY_TYPE` must
be one of:

**`HIGH`**:
High impact

**`LOW`**:
Low impact

**`MEDIUM`**:
Medium impact

**`MISSION_CRITICAL`**:
Mission critical service, application or workload

**`TYPE_UNSPECIFIED`**:
Unspecified criticality type

**--description**:
Description of the Workload

**--developer-owners**:
Developer owners of the workload

**--display-name**:
Human-friendly display name

**--environment-type**:
Environment Type of the workload. `ENVIRONMENT_TYPE` must
be one of:

**`DEVELOPMENT`**:
Development environment

**`PRODUCTION`**:
Production environment

**`STAGING`**:
Staging environment

**`TEST`**:
Test environment

**`TYPE_UNSPECIFIED`**:
Unspecified environment type

**--operator-owners**:
Operator owners of the workload

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
gcloud alpha apphub applications workloads update
```