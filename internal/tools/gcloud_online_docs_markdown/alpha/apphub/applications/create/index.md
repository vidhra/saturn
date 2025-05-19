# gcloud alpha apphub applications create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/apphub/applications/create](https://cloud.google.com/sdk/gcloud/reference/alpha/apphub/applications/create)*

**NAME**

: **gcloud alpha apphub applications create - create an Apphub application**

**SYNOPSIS**

: **`gcloud alpha apphub applications create` (`[APPLICATION](https://cloud.google.com/sdk/gcloud/reference/alpha/apphub/applications/create#APPLICATION)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/alpha/apphub/applications/create#--location)`=`LOCATION`) `[--scope-type](https://cloud.google.com/sdk/gcloud/reference/alpha/apphub/applications/create#--scope-type)`=`SCOPE_TYPE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/apphub/applications/create#--async)`] [`[--business-owners](https://cloud.google.com/sdk/gcloud/reference/alpha/apphub/applications/create#--business-owners)`=[`channel-uri`=`CHANNEL-URI`],[`display-name`=`DISPLAY-NAME`],[`email`=`EMAIL`]] [`[--criticality-type](https://cloud.google.com/sdk/gcloud/reference/alpha/apphub/applications/create#--criticality-type)`=`CRITICALITY_TYPE`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/apphub/applications/create#--description)`=`DESCRIPTION`] [`[--developer-owners](https://cloud.google.com/sdk/gcloud/reference/alpha/apphub/applications/create#--developer-owners)`=[`channel-uri`=`CHANNEL-URI`],[`display-name`=`DISPLAY-NAME`],[`email`=`EMAIL`]] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/alpha/apphub/applications/create#--display-name)`=`DISPLAY_NAME`] [`[--environment-type](https://cloud.google.com/sdk/gcloud/reference/alpha/apphub/applications/create#--environment-type)`=`ENVIRONMENT_TYPE`] [`[--operator-owners](https://cloud.google.com/sdk/gcloud/reference/alpha/apphub/applications/create#--operator-owners)`=[`channel-uri`=`CHANNEL-URI`],[`display-name`=`DISPLAY-NAME`],[`email`=`EMAIL`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/apphub/applications/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Create an Apphub application.

**EXAMPLES**

: To create the Application `my-app` with scope type
`REGIONAL` in location `us-east1`, run:

```
gcloud alpha apphub applications create my-app --location=us-east1 --scope-type=REGIONAL
```

**POSITIONAL ARGUMENTS**

: **Application resource - The Application ID. The arguments in this group can be
used to specify the attributes of this resource. (NOTE) Some attributes are not
given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `application` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`APPLICATION`**:
ID of the application or fully qualified identifier for the application.
To set the `application` attribute:

- provide the argument `application` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The Cloud location for the application.
To set the `location` attribute:

- provide the argument `application` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.**

**REQUIRED FLAGS**

: **--scope-type**:
Scope of the Application. `SCOPE_TYPE` must be one of:

**`GLOBAL`**:
Represents a global application

**`REGIONAL`**:
Represents a regional application

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--business-owners**:
Business owners of the application

**--criticality-type**:
Criticality Type of the application. `CRITICALITY_TYPE`
must be one of:

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
Description of the Application

**--developer-owners**:
Developer owners of the application

**--display-name**:
Human-friendly display name

**--environment-type**:
Environment Type of the application. `ENVIRONMENT_TYPE`
must be one of:

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
Operator owners of the application

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. This variant is also available:

```
gcloud apphub applications create
```