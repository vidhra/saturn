# gcloud apphub applications services create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/apphub/applications/services/create](https://cloud.google.com/sdk/gcloud/reference/apphub/applications/services/create)*

**NAME**

: **gcloud apphub applications services create - create an Apphub application service**

**SYNOPSIS**

: **`gcloud apphub applications services create` (`[SERVICE](https://cloud.google.com/sdk/gcloud/reference/apphub/applications/services/create#SERVICE)` : `[--application](https://cloud.google.com/sdk/gcloud/reference/apphub/applications/services/create#--application)`=`APPLICATION` `[--location](https://cloud.google.com/sdk/gcloud/reference/apphub/applications/services/create#--location)`=`LOCATION`) `[--discovered-service](https://cloud.google.com/sdk/gcloud/reference/apphub/applications/services/create#--discovered-service)`=`DISCOVERED_SERVICE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/apphub/applications/services/create#--async)`] [`[--business-owners](https://cloud.google.com/sdk/gcloud/reference/apphub/applications/services/create#--business-owners)`=[`display-name`=`DISPLAY-NAME`],[`email`=`EMAIL`]] [`[--criticality-type](https://cloud.google.com/sdk/gcloud/reference/apphub/applications/services/create#--criticality-type)`=`CRITICALITY_TYPE`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/apphub/applications/services/create#--description)`=`DESCRIPTION`] [`[--developer-owners](https://cloud.google.com/sdk/gcloud/reference/apphub/applications/services/create#--developer-owners)`=[`display-name`=`DISPLAY-NAME`],[`email`=`EMAIL`]] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/apphub/applications/services/create#--display-name)`=`DISPLAY_NAME`] [`[--environment-type](https://cloud.google.com/sdk/gcloud/reference/apphub/applications/services/create#--environment-type)`=`ENVIRONMENT_TYPE`] [`[--operator-owners](https://cloud.google.com/sdk/gcloud/reference/apphub/applications/services/create#--operator-owners)`=[`display-name`=`DISPLAY-NAME`],[`email`=`EMAIL`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/apphub/applications/services/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create an Apphub application service.

**EXAMPLES**

: To create the Service `my-service` with discovered service
`my-discovered-service` in the Application `my-app` in
location `us-east1`, run:

```
gcloud apphub applications services create my-service --application=my-app --location=us-east1 --discovered-service=my-discovered-service
```

**POSITIONAL ARGUMENTS**

: **Service resource - The Service resource. The arguments in this group can be used
to specify the attributes of this resource. (NOTE) Some attributes are not given
arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `SERVICE` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`SERVICE`**:
ID of the service or fully qualified identifier for the service.
To set the `service` attribute:

- provide the argument `SERVICE` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--application**:
Name for the application
To set the `application` attribute:

- provide the argument `SERVICE` on the command line with a fully
specified name;
- provide the argument `--application` on the command line.

**--location**:
The Cloud location for the service.
To set the `location` attribute:

- provide the argument `SERVICE` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**REQUIRED FLAGS**

: **DiscoveredService resource - The discovered service resource. This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `--discovered-service` on the command line with
a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--discovered-service` on the command line with
a fully specified name;
- provide the argument `--location` on the command line.

This must be specified.

**--discovered-service**:
ID of the discoveredService or fully qualified identifier for the
discoveredService.
To set the `discovered_service` attribute:

- provide the argument `--discovered-service` on the command line.**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--business-owners**:
Business owners of the service

**--criticality-type**:
Criticality Type of the service. `CRITICALITY_TYPE` must
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
Description of the service

**--developer-owners**:
Developer owners of the service

**--display-name**:
Human-friendly display name

**--environment-type**:
Environment Type of the service. `ENVIRONMENT_TYPE` must
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
Operator owners of the service

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
gcloud alpha apphub applications services create
```