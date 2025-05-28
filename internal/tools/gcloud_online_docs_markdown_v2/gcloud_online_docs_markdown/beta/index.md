# gcloud beta  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/beta](https://cloud.google.com/sdk/gcloud/reference/beta)*

**NAME**

: **gcloud beta - beta versions of gcloud commands**

**SYNOPSIS**

: **`gcloud beta` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/beta#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/beta#COMMAND)` [`[--account](https://cloud.google.com/sdk/gcloud/reference/beta#--account)`=`ACCOUNT`] [`[--billing-project](https://cloud.google.com/sdk/gcloud/reference/beta#--billing-project)`=`BILLING_PROJECT`] [`[--configuration](https://cloud.google.com/sdk/gcloud/reference/beta#--configuration)`=`CONFIGURATION`] [`[--flags-file](https://cloud.google.com/sdk/gcloud/reference/beta#--flags-file)`=`YAML_FILE`] [`[--flatten](https://cloud.google.com/sdk/gcloud/reference/beta#--flatten)`=[`KEY`,…]] [`[--format](https://cloud.google.com/sdk/gcloud/reference/beta#--format)`=`FORMAT`] [`[--help](https://cloud.google.com/sdk/gcloud/reference/beta#--help)`] [`[--project](https://cloud.google.com/sdk/gcloud/reference/beta#--project)`=`PROJECT_ID`] [`[--quiet](https://cloud.google.com/sdk/gcloud/reference/beta#--quiet)`, `[-q](https://cloud.google.com/sdk/gcloud/reference/beta#-q)`] [`[--verbosity](https://cloud.google.com/sdk/gcloud/reference/beta#--verbosity)`=`VERBOSITY`; default="warning"] [`[--version](https://cloud.google.com/sdk/gcloud/reference/beta#--version)`, `[-v](https://cloud.google.com/sdk/gcloud/reference/beta#-v)`] [`[-h](https://cloud.google.com/sdk/gcloud/reference/beta#-h)`] [`[--access-token-file](https://cloud.google.com/sdk/gcloud/reference/beta#--access-token-file)`=`ACCESS_TOKEN_FILE`] [`[--impersonate-service-account](https://cloud.google.com/sdk/gcloud/reference/beta#--impersonate-service-account)`=`SERVICE_ACCOUNT_EMAILS`] [`[--log-http](https://cloud.google.com/sdk/gcloud/reference/beta#--log-http)`] [`[--trace-token](https://cloud.google.com/sdk/gcloud/reference/beta#--trace-token)`=`TRACE_TOKEN`] [`[--no-user-output-enabled](https://cloud.google.com/sdk/gcloud/reference/beta#--user-output-enabled)`]**

**DESCRIPTION**

: `(BETA)` Beta versions of gcloud commands.

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

**`[access-approval](https://cloud.google.com/sdk/gcloud/reference/beta/access-approval)`**:
`(BETA)` Manage Access Approval requests and settings.

**`[access-context-manager](https://cloud.google.com/sdk/gcloud/reference/beta/access-context-manager)`**:
`(BETA)` Manage Access Context Manager resources.

**`[active-directory](https://cloud.google.com/sdk/gcloud/reference/beta/active-directory)`**:
`(BETA)` Manage Managed Microsoft AD resources.

**`[ai](https://cloud.google.com/sdk/gcloud/reference/beta/ai)`**:
`(BETA)` Manage entities in Vertex AI.

**`[ai-platform](https://cloud.google.com/sdk/gcloud/reference/beta/ai-platform)`**:
`(BETA)` Manage AI Platform jobs and models.

**`[alloydb](https://cloud.google.com/sdk/gcloud/reference/beta/alloydb)`**:
`(BETA)` Create and manage AlloyDB databases.

**`[anthos](https://cloud.google.com/sdk/gcloud/reference/beta/anthos)`**:
`(BETA)` Anthos command Group.

**`[api-gateway](https://cloud.google.com/sdk/gcloud/reference/beta/api-gateway)`**:
`(BETA)` Manage Cloud API Gateway resources.

**`[apigee](https://cloud.google.com/sdk/gcloud/reference/beta/apigee)`**:
`(BETA)` Manage Apigee resources.

**`[app](https://cloud.google.com/sdk/gcloud/reference/beta/app)`**:
`(BETA)` Manage your App Engine deployments.

**`[artifacts](https://cloud.google.com/sdk/gcloud/reference/beta/artifacts)`**:
`(BETA)` Manage Artifact Registry resources.

**`[asset](https://cloud.google.com/sdk/gcloud/reference/beta/asset)`**:
`(BETA)` Manage the Cloud Asset Inventory.

**`[assured](https://cloud.google.com/sdk/gcloud/reference/beta/assured)`**:
`(BETA)` Read and manipulate Assured Workloads data controls.

**`[auth](https://cloud.google.com/sdk/gcloud/reference/beta/auth)`**:
`(BETA)` Manage oauth2 credentials for the Google Cloud CLI.

**`[backup-dr](https://cloud.google.com/sdk/gcloud/reference/beta/backup-dr)`**:
`(BETA)` Manage Backup and DR resources.

**`[batch](https://cloud.google.com/sdk/gcloud/reference/beta/batch)`**:
`(BETA)` Manage Batch resources.

**`[beyondcorp](https://cloud.google.com/sdk/gcloud/reference/beta/beyondcorp)`**:
`(BETA)` Manage secure access to applications with integrated threat
and data protection.

**`[bigtable](https://cloud.google.com/sdk/gcloud/reference/beta/bigtable)`**:
`(BETA)` Manage your Cloud Bigtable storage.

**`[billing](https://cloud.google.com/sdk/gcloud/reference/beta/billing)`**:
`(BETA)` Manage billing accounts and associate them with projects.

**`[bq](https://cloud.google.com/sdk/gcloud/reference/beta/bq)`**:
`(BETA)` Manage Bq resources.

**`[builds](https://cloud.google.com/sdk/gcloud/reference/beta/builds)`**:
`(BETA)` Create and manage builds for Google Cloud Build.

**`[certificate-manager](https://cloud.google.com/sdk/gcloud/reference/beta/certificate-manager)`**:
`(BETA)` Manage SSL certificates for your Google Cloud projects.

**`[cloud-shell](https://cloud.google.com/sdk/gcloud/reference/beta/cloud-shell)`**:
`(BETA)` Manage Google Cloud Shell.

**`[code](https://cloud.google.com/sdk/gcloud/reference/beta/code)`**:
`(BETA)` Create and manage a local development environment for Cloud
Run.

**`[colab](https://cloud.google.com/sdk/gcloud/reference/beta/colab)`**:
`(BETA)` Manage Colab Enterprise resources.

**`[composer](https://cloud.google.com/sdk/gcloud/reference/beta/composer)`**:
`(BETA)` Create and manage Cloud Composer Environments.

**`[compute](https://cloud.google.com/sdk/gcloud/reference/beta/compute)`**:
`(BETA)` Create and manipulate Compute Engine resources.

**`[config](https://cloud.google.com/sdk/gcloud/reference/beta/config)`**:
`(BETA)` View and edit Google Cloud CLI properties.

**`[container](https://cloud.google.com/sdk/gcloud/reference/beta/container)`**:
`(BETA)` Deploy and manage clusters of machines for running
containers.

**`[data-catalog](https://cloud.google.com/sdk/gcloud/reference/beta/data-catalog)`**:
`(BETA)` Manage Data Catalog resources.

**`[data-fusion](https://cloud.google.com/sdk/gcloud/reference/beta/data-fusion)`**:
`(BETA)` Create and manage Cloud Data Fusion Instances.

**`[dataflow](https://cloud.google.com/sdk/gcloud/reference/beta/dataflow)`**:
`(BETA)` Manage Google Cloud Dataflow resources.

**`[datapipelines](https://cloud.google.com/sdk/gcloud/reference/beta/datapipelines)`**:
`(BETA)` Manage Data Pipelines resources.

**`[dataproc](https://cloud.google.com/sdk/gcloud/reference/beta/dataproc)`**:
`(BETA)` Create and manage Google Cloud Dataproc clusters and jobs.

**`[datastore](https://cloud.google.com/sdk/gcloud/reference/beta/datastore)`**:
`(BETA)` Manage your Cloud Datastore resources.

**`[datastream](https://cloud.google.com/sdk/gcloud/reference/beta/datastream)`**:
`(BETA)` Manage Cloud Datastream resources.

**`[deploy](https://cloud.google.com/sdk/gcloud/reference/beta/deploy)`**:
`(BETA)` Create and manage Cloud Deploy resources.

**`[deployment-manager](https://cloud.google.com/sdk/gcloud/reference/beta/deployment-manager)`**:
`(BETA)` Manage deployments of cloud resources.

**`[developer-connect](https://cloud.google.com/sdk/gcloud/reference/beta/developer-connect)`**:
`(BETA)` Manage Developer Connect resources.

**`[dns](https://cloud.google.com/sdk/gcloud/reference/beta/dns)`**:
`(BETA)` Manage your Cloud DNS managed-zones and record-sets.

**`[domains](https://cloud.google.com/sdk/gcloud/reference/beta/domains)`**:
`(BETA)` Manage domains for your Google Cloud projects.

**`[emulators](https://cloud.google.com/sdk/gcloud/reference/beta/emulators)`**:
`(BETA)` Set up your local development environment using emulators.

**`[endpoints](https://cloud.google.com/sdk/gcloud/reference/beta/endpoints)`**:
`(BETA)` Create, enable and manage API services.

**`[error-reporting](https://cloud.google.com/sdk/gcloud/reference/beta/error-reporting)`**:
`(BETA)` Manage Stackdriver Error Reporting.

**`[essential-contacts](https://cloud.google.com/sdk/gcloud/reference/beta/essential-contacts)`**:
`(BETA)` Manage Essential Contacts.

**`[eventarc](https://cloud.google.com/sdk/gcloud/reference/beta/eventarc)`**:
`(BETA)` Manage Eventarc resources.

**`[filestore](https://cloud.google.com/sdk/gcloud/reference/beta/filestore)`**:
`(BETA)` Create and manipulate Filestore resources.

**`[firebase](https://cloud.google.com/sdk/gcloud/reference/beta/firebase)`**:
`(BETA)` Work with Google Firebase.

**`[firestore](https://cloud.google.com/sdk/gcloud/reference/beta/firestore)`**:
`(BETA)` Manage your Cloud Firestore resources.

**`[functions](https://cloud.google.com/sdk/gcloud/reference/beta/functions)`**:
`(BETA)` Manage Google Cloud Functions.

**`[healthcare](https://cloud.google.com/sdk/gcloud/reference/beta/healthcare)`**:
`(BETA)` Manage Cloud Healthcare resources.

**`[iam](https://cloud.google.com/sdk/gcloud/reference/beta/iam)`**:
`(BETA)` Manage IAM service accounts and keys.

**`[iap](https://cloud.google.com/sdk/gcloud/reference/beta/iap)`**:
`(BETA)` Manage IAP policies.

**`[identity](https://cloud.google.com/sdk/gcloud/reference/beta/identity)`**:
`(BETA)` Manage Cloud Identity Groups and Memberships resources.

**`[ids](https://cloud.google.com/sdk/gcloud/reference/beta/ids)`**:
`(BETA)` Manage Cloud IDS.

**`[kms](https://cloud.google.com/sdk/gcloud/reference/beta/kms)`**:
`(BETA)` Manage cryptographic keys in the cloud.

**`[lifesciences](https://cloud.google.com/sdk/gcloud/reference/beta/lifesciences)`**:
`(BETA)` Manage Cloud Life Sciences resources.

**`[logging](https://cloud.google.com/sdk/gcloud/reference/beta/logging)`**:
`(BETA)` Manage Cloud Logging.

**`[managed-kafka](https://cloud.google.com/sdk/gcloud/reference/beta/managed-kafka)`**:
`(BETA)` Administer Managed Service for Apache Kafka clusters,
topics, and consumer groups.

**`[memcache](https://cloud.google.com/sdk/gcloud/reference/beta/memcache)`**:
`(BETA)` Manage Cloud Memorystore Memcached resources.

**`[memorystore](https://cloud.google.com/sdk/gcloud/reference/beta/memorystore)`**:
`(BETA)` Manage Memorystore resources.

**`[metastore](https://cloud.google.com/sdk/gcloud/reference/beta/metastore)`**:
`(BETA)` Manage Dataproc Metastore resources.

**`[ml](https://cloud.google.com/sdk/gcloud/reference/beta/ml)`**:
`(BETA)` Use Google Cloud machine learning capabilities.

**`[ml-engine](https://cloud.google.com/sdk/gcloud/reference/beta/ml-engine)`**:
`(BETA)` Manage AI Platform jobs and models.

**`[monitoring](https://cloud.google.com/sdk/gcloud/reference/beta/monitoring)`**:
`(BETA)` Manage Cloud Monitoring dashboards and notification
channels.

**`[netapp](https://cloud.google.com/sdk/gcloud/reference/beta/netapp)`**:
`(BETA)` Create and manipulate Cloud NetApp Files resources.

**`[network-connectivity](https://cloud.google.com/sdk/gcloud/reference/beta/network-connectivity)`**:
`(BETA)` Manage Network Connectivity Center resources.

**`[network-management](https://cloud.google.com/sdk/gcloud/reference/beta/network-management)`**:
`(BETA)` Manage Network Management resources.

**`[network-security](https://cloud.google.com/sdk/gcloud/reference/beta/network-security)`**:
`(BETA)` Manage Network Security resources.

**`[network-services](https://cloud.google.com/sdk/gcloud/reference/beta/network-services)`**:
`(BETA)` Manage Network Services resources.

**`[notebooks](https://cloud.google.com/sdk/gcloud/reference/beta/notebooks)`**:
`(BETA)` `(DEPRECATED)` Notebooks Command Group.

**`[organizations](https://cloud.google.com/sdk/gcloud/reference/beta/organizations)`**:
`(BETA)` Create and manage Google Cloud Platform Organizations.

**`[pam](https://cloud.google.com/sdk/gcloud/reference/beta/pam)`**:
`(BETA)` Manage Privileged Access Manager (PAM) entitlements and
grants.

**`[policy-intelligence](https://cloud.google.com/sdk/gcloud/reference/beta/policy-intelligence)`**:
`(BETA)` A platform to help better understand, use, and manage
policies at scale.

**`[policy-troubleshoot](https://cloud.google.com/sdk/gcloud/reference/beta/policy-troubleshoot)`**:
`(BETA)` Troubleshoot Google Cloud Platform policies.

**`[projects](https://cloud.google.com/sdk/gcloud/reference/beta/projects)`**:
`(BETA)` Create and manage project access policies.

**`[publicca](https://cloud.google.com/sdk/gcloud/reference/beta/publicca)`**:
`(BETA)` Manage accounts for Google Trust Services' Certificate
Authority.

**`[pubsub](https://cloud.google.com/sdk/gcloud/reference/beta/pubsub)`**:
`(BETA)` Manage Cloud Pub/Sub topics, subscriptions, and snapshots.

**`[quotas](https://cloud.google.com/sdk/gcloud/reference/beta/quotas)`**:
`(BETA)` Manage Cloud Quotas quota info, quota preferences and quota
adjuster settings.

**`[recommender](https://cloud.google.com/sdk/gcloud/reference/beta/recommender)`**:
`(BETA)` Manage Cloud recommendations and recommendation rules.

**`[redis](https://cloud.google.com/sdk/gcloud/reference/beta/redis)`**:
`(BETA)` Manage Cloud Memorystore Redis resources.

**`[resource-config](https://cloud.google.com/sdk/gcloud/reference/beta/resource-config)`**:
`(BETA)` Commands for declarative management of Google Cloud Platform
resources.

**`[resource-manager](https://cloud.google.com/sdk/gcloud/reference/beta/resource-manager)`**:
`(BETA)` Manage Cloud Resources.

**`[run](https://cloud.google.com/sdk/gcloud/reference/beta/run)`**:
`(BETA)` Manage your Cloud Run applications.

**`[runtime-config](https://cloud.google.com/sdk/gcloud/reference/beta/runtime-config)`**:
`(BETA)` Manage runtime configuration resources.

**`[saas-runtime](https://cloud.google.com/sdk/gcloud/reference/beta/saas-runtime)`**:
`(BETA)` Commands for SaaS Runtime.

**`[scc](https://cloud.google.com/sdk/gcloud/reference/beta/scc)`**:
`(BETA)` Manage Cloud SCC resources.

**`[scheduler](https://cloud.google.com/sdk/gcloud/reference/beta/scheduler)`**:
`(BETA)` Manage Cloud Scheduler jobs and schedules.

**`[secrets](https://cloud.google.com/sdk/gcloud/reference/beta/secrets)`**:
`(BETA)` Manage secrets on Google Cloud.

**`[service-directory](https://cloud.google.com/sdk/gcloud/reference/beta/service-directory)`**:
`(BETA)` Command groups for Service Directory.

**`[service-extensions](https://cloud.google.com/sdk/gcloud/reference/beta/service-extensions)`**:
`(BETA)` Manage Service Extensions resources.

**`[services](https://cloud.google.com/sdk/gcloud/reference/beta/services)`**:
`(BETA)` List, enable and disable APIs and services.

**`[source](https://cloud.google.com/sdk/gcloud/reference/beta/source)`**:
`(BETA)` Cloud git repository commands.

**`[source-manager](https://cloud.google.com/sdk/gcloud/reference/beta/source-manager)`**:
`(BETA)` Manage Secure Source Manager resources.

**`[spanner](https://cloud.google.com/sdk/gcloud/reference/beta/spanner)`**:
`(BETA)` Command groups for Cloud Spanner.

**`[sql](https://cloud.google.com/sdk/gcloud/reference/beta/sql)`**:
`(BETA)` Create and manage Google Cloud SQL databases.

**`[tasks](https://cloud.google.com/sdk/gcloud/reference/beta/tasks)`**:
`(BETA)` Manage Cloud Tasks queues and tasks.

**`[terraform](https://cloud.google.com/sdk/gcloud/reference/beta/terraform)`**:
`(BETA)` Commands related to Terraform management of Google Cloud
Platform resources.

**`[topic](https://cloud.google.com/sdk/gcloud/reference/beta/topic)`**:
`(BETA)` gcloud supplementary help.

**`[workbench](https://cloud.google.com/sdk/gcloud/reference/beta/workbench)`**:
`(BETA)` Workbench Command Group.

**`[workflows](https://cloud.google.com/sdk/gcloud/reference/beta/workflows)`**:
`(BETA)` Manage your Cloud Workflows resources.

**`[workstations](https://cloud.google.com/sdk/gcloud/reference/beta/workstations)`**:
`(BETA)` Manage Cloud Workstations resources.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[help](https://cloud.google.com/sdk/gcloud/reference/beta)`**:
`(BETA)` Search gcloud help text.

**`[init](https://cloud.google.com/sdk/gcloud/reference/beta/init)`**:
`(BETA)` Initialize or reinitialize gcloud.

**`[interactive](https://cloud.google.com/sdk/gcloud/reference/beta/interactive)`**:
`(BETA)` Start the gcloud interactive shell.

**`[survey](https://cloud.google.com/sdk/gcloud/reference/beta/survey)`**:
`(BETA)` Invoke a customer satisfaction survey for Google Cloud CLI.

**NOTES**

: This command is currently in beta and might change without notice.