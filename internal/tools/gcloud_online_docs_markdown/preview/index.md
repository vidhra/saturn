# gcloud preview  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/preview](https://cloud.google.com/sdk/gcloud/reference/preview)*

**NAME**

: **gcloud preview - preview versions of gcloud commands**

**SYNOPSIS**

: **`gcloud preview` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/preview#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/preview#COMMAND)` [`[--account](https://cloud.google.com/sdk/gcloud/reference/preview#--account)`=`ACCOUNT`] [`[--billing-project](https://cloud.google.com/sdk/gcloud/reference/preview#--billing-project)`=`BILLING_PROJECT`] [`[--configuration](https://cloud.google.com/sdk/gcloud/reference/preview#--configuration)`=`CONFIGURATION`] [`[--flags-file](https://cloud.google.com/sdk/gcloud/reference/preview#--flags-file)`=`YAML_FILE`] [`[--flatten](https://cloud.google.com/sdk/gcloud/reference/preview#--flatten)`=[`KEY`,…]] [`[--format](https://cloud.google.com/sdk/gcloud/reference/preview#--format)`=`FORMAT`] [`[--help](https://cloud.google.com/sdk/gcloud/reference/preview#--help)`] [`[--project](https://cloud.google.com/sdk/gcloud/reference/preview#--project)`=`PROJECT_ID`] [`[--quiet](https://cloud.google.com/sdk/gcloud/reference/preview#--quiet)`, `[-q](https://cloud.google.com/sdk/gcloud/reference/preview#-q)`] [`[--verbosity](https://cloud.google.com/sdk/gcloud/reference/preview#--verbosity)`=`VERBOSITY`; default="warning"] [`[--version](https://cloud.google.com/sdk/gcloud/reference/preview#--version)`, `[-v](https://cloud.google.com/sdk/gcloud/reference/preview#-v)`] [`[-h](https://cloud.google.com/sdk/gcloud/reference/preview#-h)`] [`[--access-token-file](https://cloud.google.com/sdk/gcloud/reference/preview#--access-token-file)`=`ACCESS_TOKEN_FILE`] [`[--impersonate-service-account](https://cloud.google.com/sdk/gcloud/reference/preview#--impersonate-service-account)`=`SERVICE_ACCOUNT_EMAILS`] [`[--log-http](https://cloud.google.com/sdk/gcloud/reference/preview#--log-http)`] [`[--trace-token](https://cloud.google.com/sdk/gcloud/reference/preview#--trace-token)`=`TRACE_TOKEN`] [`[--no-user-output-enabled](https://cloud.google.com/sdk/gcloud/reference/preview#--user-output-enabled)`]**

**DESCRIPTION**

: `(PREVIEW)` Preview versions of gcloud commands.

**GLOBAL FLAGS**

: **--account**:
Google Cloud user account to use for invocation. Overrides the default
`core/account` property value for this command invocation.

**--billing-project**:
The Google Cloud project that will be charged quota for operations performed in
`[gcloud](https://cloud.google.com/sdk/gcloud/reference)`. If you need to operate
on one project, but need quota against a different project, you can use this
flag to specify the billing project. If both `billing/quota_project`
and `--billing-project` are specified, `--billing-project`
takes precedence. Run `$ [gcloud
config set](https://cloud.google.com/sdk/gcloud/reference/config/set) --help` to see more information about
`billing/quota_project`.

**--configuration**:
File name of the configuration to use for this command invocation. For more
information on how to use configurations, run: `[gcloud topic
configurations](https://cloud.google.com/sdk/gcloud/reference/topic/configurations)`. You can also use the CLOUDSDK_ACTIVE_CONFIG_NAME
environment variable to set the equivalent of this flag for a terminal session.

**--flags-file**:
A YAML or JSON file that specifies a `--flag`:`value`
dictionary. Useful for specifying complex flag values with special characters
that work with any command interpreter. Additionally, each
`--flags-file` arg is replaced by its constituent flags. See $ [gcloud topic flags-file](https://cloud.google.com/sdk/gcloud/reference/topic/flags-file) for
more information.

**--flatten**:
Flatten `name`[] output resource slices in
`KEY` into separate records for each item in each slice.
Multiple keys and slices may be specified. This also flattens keys for
`--format` and `--filter`. For example,
`--flatten=abc.def` flattens `abc.def[].ghi` references to
`abc.def.ghi`. A resource record containing `abc.def[]`
with N elements will expand to N records in the flattened output. This allows us
to specify what `resource-key` the `filter` will operate
on. This flag interacts with other flags that are applied in this order:
`--flatten`, `--sort-by`, `--filter`,
`--limit`.

**--format**:
Sets the format for printing command output resources. The default is a
command-specific human-friendly output format. If both `core/format`
and `--format` are specified, `--format` takes precedence.
`--format` and `core/format` both take precedence over
`core/default_format`. The supported formats are limited to:
`config`, `csv`, `default`, `diff`,
`disable`, `flattened`, `get`,
`json`, `list`, `multi`, `none`,
`object`, `table`, `text`, `value`,
`yaml`. For more details run $ [gcloud](https://cloud.google.com/sdk/gcloud/reference) topic formats. Run `$ [gcloud config set](https://cloud.google.com/sdk/gcloud/reference/config/set) --help` to
see more information about `core/format`

**--help**:
Display detailed help.

**--project**:
The Google Cloud project ID to use for this invocation. If omitted, then the
current project is assumed; the current project can be listed using `gcloud
config list --format='text(core.project)'` and can be set using
`gcloud config set project PROJECTID`.
`--project` and its fallback `core/project` property play
two roles in the invocation. It specifies the project of the resource to operate
on. It also specifies the project for API enablement check, quota, and billing.
To specify a different project for quota and billing, use
`--billing-project` or `billing/quota_project` property.

**--quiet**:
Disable all interactive prompts when running `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` commands. If input is required,
defaults will be used, or an error will be raised.
Overrides the default core/disable_prompts property value for this command
invocation. This is equivalent to setting the environment variable
`CLOUDSDK_CORE_DISABLE_PROMPTS` to 1.

**--verbosity**:
Override the default verbosity for this command. Overrides the default
`core/verbosity` property value for this command invocation.
`VERBOSITY` must be one of: `debug`,
`info`, `warning`, `error`,
`critical`, `none`.

**--version**:
Print version information and exit. This flag is only available at the global
level.

**-h**:
Print a summary help and exit.

**OTHER FLAGS**

: **--access-token-file**:
A file path to read the access token. Use this flag to authenticate `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` with an access token. The
credentials of the active account (if exists) will be ignored. The file should
only contain an access token with no other information. Overrides the default
`auth/access_token_file` property value for this command invocation.

**--impersonate-service-account**:
For this `[gcloud](https://cloud.google.com/sdk/gcloud/reference)` invocation, all
API requests will be made as the given service account or target service account
in an impersonation delegation chain instead of the currently selected account.
You can specify either a single service account as the impersonator, or a
comma-separated list of service accounts to create an impersonation delegation
chain. The impersonation is done without needing to create, download, and
activate a key for the service account or accounts.
In order to make API requests as a service account, your currently selected
account must have an IAM role that includes the
`iam.serviceAccounts.getAccessToken` permission for the service
account or accounts.
The `roles/iam.serviceAccountTokenCreator` role has the
`iam.serviceAccounts.getAccessToken permission`. You can also create
a custom role.
You can specify a list of service accounts, separated with commas. This creates
an impersonation delegation chain in which each service account delegates its
permissions to the next service account in the chain. Each service account in
the list must have the `roles/iam.serviceAccountTokenCreator` role on
the next service account in the list. For example, when
`--impersonate-service-account=`
``SERVICE_ACCOUNT_1``,``SERVICE_ACCOUNT_2``,
the active account must have the
`roles/iam.serviceAccountTokenCreator` role on
``SERVICE_ACCOUNT_1``, which must have the
`roles/iam.serviceAccountTokenCreator` role on
``SERVICE_ACCOUNT_2``.
``SERVICE_ACCOUNT_1`` is the impersonated
service account and ``SERVICE_ACCOUNT_2`` is
the delegate.
Overrides the default `auth/impersonate_service_account` property
value for this command invocation.

**--log-http**:
Log all HTTP server requests and responses to stderr. Overrides the default
`core/log_http` property value for this command invocation.

**--trace-token**:
Token used to route traces of service requests for investigation of issues.
Overrides the default `core/trace_token` property value for this
command invocation.

**--user-output-enabled**:
Print user intended output to the console. Overrides the default
`core/user_output_enabled` property value for this command
invocation. Use `--no-user-output-enabled` to disable.

**GROUPS**

: ``GROUP`` is one of the following:

**`[config](https://cloud.google.com/sdk/gcloud/reference/preview/config)`**:
`(PREVIEW)` View and edit Google Cloud CLI properties.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[help](https://cloud.google.com/sdk/gcloud/reference/preview)`**:
`(PREVIEW)` Search gcloud help text.

**`[init](https://cloud.google.com/sdk/gcloud/reference/preview/init)`**:
`(PREVIEW)` Initialize or reinitialize gcloud.

**`[survey](https://cloud.google.com/sdk/gcloud/reference/preview/survey)`**:
`(PREVIEW)` Invoke a customer satisfaction survey for Google Cloud
CLI.

**NOTES**

: This command is currently in DEVELOPER PREVIEW and may change without notice. If
this command fails with API permission errors despite specifying the correct
project, you might be trying to access an API with an invitation-only early
access allowlist.