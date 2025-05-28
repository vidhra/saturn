# gcloud alpha  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha](https://cloud.google.com/sdk/gcloud/reference/alpha)*

**NAME**

: **gcloud alpha - alpha versions of gcloud commands**

**SYNOPSIS**

: **`gcloud alpha` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/alpha#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/alpha#COMMAND)` [`[--account](https://cloud.google.com/sdk/gcloud/reference/alpha#--account)`=`ACCOUNT`] [`[--billing-project](https://cloud.google.com/sdk/gcloud/reference/alpha#--billing-project)`=`BILLING_PROJECT`] [`[--configuration](https://cloud.google.com/sdk/gcloud/reference/alpha#--configuration)`=`CONFIGURATION`] [`[--flags-file](https://cloud.google.com/sdk/gcloud/reference/alpha#--flags-file)`=`YAML_FILE`] [`[--flatten](https://cloud.google.com/sdk/gcloud/reference/alpha#--flatten)`=[`KEY`,…]] [`[--format](https://cloud.google.com/sdk/gcloud/reference/alpha#--format)`=`FORMAT`] [`[--help](https://cloud.google.com/sdk/gcloud/reference/alpha#--help)`] [`[--project](https://cloud.google.com/sdk/gcloud/reference/alpha#--project)`=`PROJECT_ID`] [`[--quiet](https://cloud.google.com/sdk/gcloud/reference/alpha#--quiet)`, `[-q](https://cloud.google.com/sdk/gcloud/reference/alpha#-q)`] [`[--verbosity](https://cloud.google.com/sdk/gcloud/reference/alpha#--verbosity)`=`VERBOSITY`; default="warning"] [`[--version](https://cloud.google.com/sdk/gcloud/reference/alpha#--version)`, `[-v](https://cloud.google.com/sdk/gcloud/reference/alpha#-v)`] [`[-h](https://cloud.google.com/sdk/gcloud/reference/alpha#-h)`] [`[--access-token-file](https://cloud.google.com/sdk/gcloud/reference/alpha#--access-token-file)`=`ACCESS_TOKEN_FILE`] [`[--impersonate-service-account](https://cloud.google.com/sdk/gcloud/reference/alpha#--impersonate-service-account)`=`SERVICE_ACCOUNT_EMAILS`] [`[--log-http](https://cloud.google.com/sdk/gcloud/reference/alpha#--log-http)`] [`[--trace-token](https://cloud.google.com/sdk/gcloud/reference/alpha#--trace-token)`=`TRACE_TOKEN`] [`[--no-user-output-enabled](https://cloud.google.com/sdk/gcloud/reference/alpha#--user-output-enabled)`]**

**DESCRIPTION**

: `(ALPHA)` Alpha versions of gcloud commands.

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

**`[access-approval](https://cloud.google.com/sdk/gcloud/reference/alpha/access-approval)`**:
`(ALPHA)` Manage Access Approval requests and settings.

**`[access-context-manager](https://cloud.google.com/sdk/gcloud/reference/alpha/access-context-manager)`**:
`(ALPHA)` Manage Access Context Manager resources.

**`[active-directory](https://cloud.google.com/sdk/gcloud/reference/alpha/active-directory)`**:
`(ALPHA)` Manage Managed Microsoft AD resources.

**`[ai](https://cloud.google.com/sdk/gcloud/reference/alpha/ai)`**:
`(ALPHA)` Manage entities in Vertex AI.

**`[ai-platform](https://cloud.google.com/sdk/gcloud/reference/alpha/ai-platform)`**:
`(ALPHA)` Manage AI Platform jobs and models.

**`[alloydb](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb)`**:
`(ALPHA)` Create and manage AlloyDB databases.

**`[anthos](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos)`**:
`(ALPHA)` Anthos command Group.

**`[api-gateway](https://cloud.google.com/sdk/gcloud/reference/alpha/api-gateway)`**:
`(ALPHA)` Manage Cloud API Gateway resources.

**`[apigee](https://cloud.google.com/sdk/gcloud/reference/alpha/apigee)`**:
`(ALPHA)` Manage Apigee resources.

**`[app](https://cloud.google.com/sdk/gcloud/reference/alpha/app)`**:
`(ALPHA)` Manage your App Engine deployments.

**`[apphub](https://cloud.google.com/sdk/gcloud/reference/alpha/apphub)`**:
`(ALPHA)` Manage App Hub resources.

**`[artifacts](https://cloud.google.com/sdk/gcloud/reference/alpha/artifacts)`**:
`(ALPHA)` Manage Artifact Registry resources.

**`[asset](https://cloud.google.com/sdk/gcloud/reference/alpha/asset)`**:
`(ALPHA)` Manage the Cloud Asset Inventory.

**`[assured](https://cloud.google.com/sdk/gcloud/reference/alpha/assured)`**:
`(ALPHA)` Read and manipulate Assured Workloads data controls.

**`[audit-manager](https://cloud.google.com/sdk/gcloud/reference/alpha/audit-manager)`**:
`(ALPHA)` Enroll resources, audit workloads and generate reports.

**`[auth](https://cloud.google.com/sdk/gcloud/reference/alpha/auth)`**:
`(ALPHA)` Manage oauth2 credentials for the Google Cloud CLI.

**`[backup-dr](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr)`**:
`(ALPHA)` Manage Backup and DR resources.

**`[batch](https://cloud.google.com/sdk/gcloud/reference/alpha/batch)`**:
`(ALPHA)` Manage Batch resources.

**`[beyondcorp](https://cloud.google.com/sdk/gcloud/reference/alpha/beyondcorp)`**:
`(ALPHA)` Manage secure access to applications with integrated threat
and data protection.

**`[bigtable](https://cloud.google.com/sdk/gcloud/reference/alpha/bigtable)`**:
`(ALPHA)` Manage your Cloud Bigtable storage.

**`[billing](https://cloud.google.com/sdk/gcloud/reference/alpha/billing)`**:
`(ALPHA)` Manage billing accounts and associate them with projects.

**`[blockchain-node-engine](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-node-engine)`**:
`(ALPHA)` Create and manipulate Blockchain Node Engine resources.

**`[blockchain-validator](https://cloud.google.com/sdk/gcloud/reference/alpha/blockchain-validator)`**:
`(ALPHA)` Manage blockchain validator configurations.

**`[bms](https://cloud.google.com/sdk/gcloud/reference/alpha/bms)`**:
`(ALPHA)` Manage Bare Metal Solution resources.

**`[bq](https://cloud.google.com/sdk/gcloud/reference/alpha/bq)`**:
`(ALPHA)` Interact with and manage resources in Google BigQuery.

**`[builds](https://cloud.google.com/sdk/gcloud/reference/alpha/builds)`**:
`(ALPHA)` Create and manage builds for Google Cloud Build.

**`[certificate-manager](https://cloud.google.com/sdk/gcloud/reference/alpha/certificate-manager)`**:
`(ALPHA)` Manage SSL certificates for your Google Cloud projects.

**`[cloud-shell](https://cloud.google.com/sdk/gcloud/reference/alpha/cloud-shell)`**:
`(ALPHA)` Manage Google Cloud Shell.

**`[code](https://cloud.google.com/sdk/gcloud/reference/alpha/code)`**:
`(ALPHA)` Create and manage a local development environment for Cloud
Run.

**`[composer](https://cloud.google.com/sdk/gcloud/reference/alpha/composer)`**:
`(ALPHA)` Create and manage Cloud Composer Environments.

**`[compute](https://cloud.google.com/sdk/gcloud/reference/alpha/compute)`**:
`(ALPHA)` Create and manipulate Compute Engine resources.

**`[config](https://cloud.google.com/sdk/gcloud/reference/alpha/config)`**:
`(ALPHA)` View and edit Google Cloud CLI properties.

**`[container](https://cloud.google.com/sdk/gcloud/reference/alpha/container)`**:
`(ALPHA)` Deploy and manage clusters of machines for running
containers.

**`[data-catalog](https://cloud.google.com/sdk/gcloud/reference/alpha/data-catalog)`**:
`(ALPHA)` Manage Data Catalog resources.

**`[database-migration](https://cloud.google.com/sdk/gcloud/reference/alpha/database-migration)`**:
`(ALPHA)` Manage Database Migration Service resources.

**`[dataflow](https://cloud.google.com/sdk/gcloud/reference/alpha/dataflow)`**:
`(ALPHA)` Manage Google Cloud Dataflow resources.

**`[dataplex](https://cloud.google.com/sdk/gcloud/reference/alpha/dataplex)`**:
`(ALPHA)` Manage Dataplex resources.

**`[dataproc](https://cloud.google.com/sdk/gcloud/reference/alpha/dataproc)`**:
`(ALPHA)` Create and manage Google Cloud Dataproc clusters and jobs.

**`[datastore](https://cloud.google.com/sdk/gcloud/reference/alpha/datastore)`**:
`(ALPHA)` Manage your Cloud Datastore resources.

**`[deploy](https://cloud.google.com/sdk/gcloud/reference/alpha/deploy)`**:
`(ALPHA)` Create and manage Cloud Deploy resources.

**`[deployment-manager](https://cloud.google.com/sdk/gcloud/reference/alpha/deployment-manager)`**:
`(ALPHA)` Manage deployments of cloud resources.

**`[developer-connect](https://cloud.google.com/sdk/gcloud/reference/alpha/developer-connect)`**:
`(ALPHA)` Manage Developer Connect resources.

**`[dialogflow](https://cloud.google.com/sdk/gcloud/reference/alpha/dialogflow)`**:
`(ALPHA)` Interact with and manage Dialogflow agents, entities, and
intents.

**`[dlp](https://cloud.google.com/sdk/gcloud/reference/alpha/dlp)`**:
`(ALPHA)` Manage sensitive data with Cloud Data Loss Prevention.

**`[dns](https://cloud.google.com/sdk/gcloud/reference/alpha/dns)`**:
`(ALPHA)` Manage your Cloud DNS managed-zones and record-sets.

**`[domains](https://cloud.google.com/sdk/gcloud/reference/alpha/domains)`**:
`(ALPHA)` Manage domains for your Google Cloud projects.

**`[edge-cache](https://cloud.google.com/sdk/gcloud/reference/alpha/edge-cache)`**:
`(ALPHA)` Manage Media CDN resources.

**`[edge-cloud](https://cloud.google.com/sdk/gcloud/reference/alpha/edge-cloud)`**:
`(ALPHA)` Manage edge-cloud resources.

**`[emulators](https://cloud.google.com/sdk/gcloud/reference/alpha/emulators)`**:
`(ALPHA)` Set up your local development environment using emulators.

**`[endpoints](https://cloud.google.com/sdk/gcloud/reference/alpha/endpoints)`**:
`(ALPHA)` Create, enable and manage API services.

**`[essential-contacts](https://cloud.google.com/sdk/gcloud/reference/alpha/essential-contacts)`**:
`(ALPHA)` Manage Essential Contacts.

**`[filestore](https://cloud.google.com/sdk/gcloud/reference/alpha/filestore)`**:
`(ALPHA)` Create and manipulate Filestore resources.

**`[firebase](https://cloud.google.com/sdk/gcloud/reference/alpha/firebase)`**:
`(ALPHA)` Work with Google Firebase.

**`[firestore](https://cloud.google.com/sdk/gcloud/reference/alpha/firestore)`**:
`(ALPHA)` Manage your Cloud Firestore resources.

**`[functions](https://cloud.google.com/sdk/gcloud/reference/alpha/functions)`**:
`(ALPHA)` Manage Google Cloud Functions.

**`[gemini-cloud-assist](https://cloud.google.com/sdk/gcloud/reference/alpha/gemini-cloud-assist)`**:
`(ALPHA)` Create and manage Gemini Cloud Assist.

**`[genomics](https://cloud.google.com/sdk/gcloud/reference/alpha/genomics)`**:
`(ALPHA)` Manage Genomics resources.

**`[healthcare](https://cloud.google.com/sdk/gcloud/reference/alpha/healthcare)`**:
`(ALPHA)` Manage Cloud Healthcare resources.

**`[iam](https://cloud.google.com/sdk/gcloud/reference/alpha/iam)`**:
`(ALPHA)` Manage IAM service accounts and keys.

**`[iap](https://cloud.google.com/sdk/gcloud/reference/alpha/iap)`**:
`(ALPHA)` Manage IAP policies.

**`[identity](https://cloud.google.com/sdk/gcloud/reference/alpha/identity)`**:
`(ALPHA)` Manage Cloud Identity Groups and Memberships resources.

**`[ids](https://cloud.google.com/sdk/gcloud/reference/alpha/ids)`**:
`(ALPHA)` Manage Cloud IDS.

**`[immersive-stream](https://cloud.google.com/sdk/gcloud/reference/alpha/immersive-stream)`**:
`(ALPHA)` Manage Immersive Stream resources.

**`[kms](https://cloud.google.com/sdk/gcloud/reference/alpha/kms)`**:
`(ALPHA)` Manage cryptographic keys in the cloud.

**`[lifesciences](https://cloud.google.com/sdk/gcloud/reference/alpha/lifesciences)`**:
`(ALPHA)` Manage Cloud Life Sciences resources.

**`[logging](https://cloud.google.com/sdk/gcloud/reference/alpha/logging)`**:
`(ALPHA)` Manage Cloud Logging.

**`[looker](https://cloud.google.com/sdk/gcloud/reference/alpha/looker)`**:
`(ALPHA)` Manage Looker resources.

**`[lustre](https://cloud.google.com/sdk/gcloud/reference/alpha/lustre)`**:
`(ALPHA)` Manage Lustre resources.

**`[managed-flink](https://cloud.google.com/sdk/gcloud/reference/alpha/managed-flink)`**:
`(ALPHA)` Manage Managed Flink resources.

**`[managed-kafka](https://cloud.google.com/sdk/gcloud/reference/alpha/managed-kafka)`**:
`(ALPHA)` Administer Managed Service for Apache Kafka clusters,
topics, and consumer groups.

**`[media](https://cloud.google.com/sdk/gcloud/reference/alpha/media)`**:
`(ALPHA)` Manage Cloud Media Services.

**`[memcache](https://cloud.google.com/sdk/gcloud/reference/alpha/memcache)`**:
`(ALPHA)` Manage Cloud Memorystore Memcached resources.

**`[memorystore](https://cloud.google.com/sdk/gcloud/reference/alpha/memorystore)`**:
`(ALPHA)` Manage Memorystore resources.

**`[metastore](https://cloud.google.com/sdk/gcloud/reference/alpha/metastore)`**:
`(ALPHA)` Manage Dataproc Metastore resources.

**`[migration](https://cloud.google.com/sdk/gcloud/reference/alpha/migration)`**:
`(ALPHA)` The root group for various Cloud Migration teams.

**`[ml](https://cloud.google.com/sdk/gcloud/reference/alpha/ml)`**:
`(ALPHA)` Use Google Cloud machine learning capabilities.

**`[ml-engine](https://cloud.google.com/sdk/gcloud/reference/alpha/ml-engine)`**:
`(ALPHA)` Manage AI Platform jobs and models.

**`[model-armor](https://cloud.google.com/sdk/gcloud/reference/alpha/model-armor)`**:
`(ALPHA)` Model Armor is a service offering LLM-agnostic security and
AI safety measures to mitigate risks associated with large language models
(LLMs).

**`[monitoring](https://cloud.google.com/sdk/gcloud/reference/alpha/monitoring)`**:
`(ALPHA)` Manage Cloud Monitoring alerting policies, dashboards,
notification channels, and uptime checks.

**`[mps](https://cloud.google.com/sdk/gcloud/reference/alpha/mps)`**:
`(ALPHA)` Manage Marketplace Solutions resources.

**`[netapp](https://cloud.google.com/sdk/gcloud/reference/alpha/netapp)`**:
`(ALPHA)` Create and manipulate Cloud NetApp Files resources.

**`[network-connectivity](https://cloud.google.com/sdk/gcloud/reference/alpha/network-connectivity)`**:
`(ALPHA)` Manage Network Connectivity Center resources.

**`[network-management](https://cloud.google.com/sdk/gcloud/reference/alpha/network-management)`**:
`(ALPHA)` Manage Network Management resources.

**`[network-security](https://cloud.google.com/sdk/gcloud/reference/alpha/network-security)`**:
`(ALPHA)` Manage Network Security resources.

**`[network-services](https://cloud.google.com/sdk/gcloud/reference/alpha/network-services)`**:
`(ALPHA)` Manage Network Services resources.

**`[notebooks](https://cloud.google.com/sdk/gcloud/reference/alpha/notebooks)`**:
`(ALPHA)` `(DEPRECATED)` Notebooks Command Group.

**`[organizations](https://cloud.google.com/sdk/gcloud/reference/alpha/organizations)`**:
`(ALPHA)` Create and manage Google Cloud Platform Organizations.

**`[pam](https://cloud.google.com/sdk/gcloud/reference/alpha/pam)`**:
`(ALPHA)` Manage Privileged Access Manager (PAM) entitlements and
grants.

**`[policy-troubleshoot](https://cloud.google.com/sdk/gcloud/reference/alpha/policy-troubleshoot)`**:
`(ALPHA)` Troubleshoot Google Cloud Platform policies.

**`[projects](https://cloud.google.com/sdk/gcloud/reference/alpha/projects)`**:
`(ALPHA)` Create and manage project access policies.

**`[publicca](https://cloud.google.com/sdk/gcloud/reference/alpha/publicca)`**:
`(ALPHA)` Manage accounts for Google Trust Services' Certificate
Authority.

**`[pubsub](https://cloud.google.com/sdk/gcloud/reference/alpha/pubsub)`**:
`(ALPHA)` Manage Cloud Pub/Sub topics, subscriptions, and snapshots.

**`[quotas](https://cloud.google.com/sdk/gcloud/reference/alpha/quotas)`**:
`(ALPHA)` Manage Cloud Quotas quota info and quota preferences.

**`[recaptcha](https://cloud.google.com/sdk/gcloud/reference/alpha/recaptcha)`**:
`(ALPHA)` Manage reCAPTCHA Enterprise Keys.

**`[recommender](https://cloud.google.com/sdk/gcloud/reference/alpha/recommender)`**:
`(ALPHA)` Manage Cloud recommendations and recommendation rules.

**`[redis](https://cloud.google.com/sdk/gcloud/reference/alpha/redis)`**:
`(ALPHA)` Manage Cloud Memorystore Redis resources.

**`[resource-config](https://cloud.google.com/sdk/gcloud/reference/alpha/resource-config)`**:
`(ALPHA)` Commands for declarative management of Google Cloud
Platform resources.

**`[resource-manager](https://cloud.google.com/sdk/gcloud/reference/alpha/resource-manager)`**:
`(ALPHA)` Manage Cloud Resources.

**`[run](https://cloud.google.com/sdk/gcloud/reference/alpha/run)`**:
`(ALPHA)` Manage your Cloud Run applications.

**`[scc](https://cloud.google.com/sdk/gcloud/reference/alpha/scc)`**:
`(ALPHA)` Manage Cloud SCC resources.

**`[scheduler](https://cloud.google.com/sdk/gcloud/reference/alpha/scheduler)`**:
`(ALPHA)` Manage Cloud Scheduler jobs and schedules.

**`[secrets](https://cloud.google.com/sdk/gcloud/reference/alpha/secrets)`**:
`(ALPHA)` Manage secrets on Google Cloud.

**`[service-directory](https://cloud.google.com/sdk/gcloud/reference/alpha/service-directory)`**:
`(ALPHA)` Command groups for Service Directory.

**`[service-extensions](https://cloud.google.com/sdk/gcloud/reference/alpha/service-extensions)`**:
`(ALPHA)` Manage Service Extensions resources.

**`[services](https://cloud.google.com/sdk/gcloud/reference/alpha/services)`**:
`(ALPHA)` List, enable and disable APIs and services.

**`[source](https://cloud.google.com/sdk/gcloud/reference/alpha/source)`**:
`(ALPHA)` Cloud git repository commands.

**`[source-manager](https://cloud.google.com/sdk/gcloud/reference/alpha/source-manager)`**:
`(ALPHA)` Manage Secure Source Manager resources.

**`[spanner](https://cloud.google.com/sdk/gcloud/reference/alpha/spanner)`**:
`(ALPHA)` Command groups for Cloud Spanner.

**`[sql](https://cloud.google.com/sdk/gcloud/reference/alpha/sql)`**:
`(ALPHA)` Create and manage Google Cloud SQL databases.

**`[storage](https://cloud.google.com/sdk/gcloud/reference/alpha/storage)`**:
`(ALPHA)` Create and manage Cloud Storage buckets and objects.

**`[tasks](https://cloud.google.com/sdk/gcloud/reference/alpha/tasks)`**:
`(ALPHA)` Manage Cloud Tasks queues and tasks.

**`[telco-automation](https://cloud.google.com/sdk/gcloud/reference/alpha/telco-automation)`**:
`(ALPHA)` Manage Telco Automation resources.

**`[terraform](https://cloud.google.com/sdk/gcloud/reference/alpha/terraform)`**:
`(ALPHA)` Commands related to Terraform management of Google Cloud
Platform resources.

**`[topic](https://cloud.google.com/sdk/gcloud/reference/alpha/topic)`**:
`(ALPHA)` gcloud supplementary help.

**`[trace](https://cloud.google.com/sdk/gcloud/reference/alpha/trace)`**:
`(ALPHA)` Manage Stackdriver Trace.

**`[transfer](https://cloud.google.com/sdk/gcloud/reference/alpha/transfer)`**:
`(ALPHA)` Manage Transfer Service jobs, operations, and agents.

**`[web-security-scanner](https://cloud.google.com/sdk/gcloud/reference/alpha/web-security-scanner)`**:
`(ALPHA)` Manage Cloud Web Security Scanner resources.

**`[workstations](https://cloud.google.com/sdk/gcloud/reference/alpha/workstations)`**:
`(ALPHA)` Manage Cloud Workstations resources.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[help](https://cloud.google.com/sdk/gcloud/reference/alpha)`**:
`(ALPHA)` Search gcloud help text.

**`[init](https://cloud.google.com/sdk/gcloud/reference/alpha/init)`**:
`(ALPHA)` Initialize or reinitialize gcloud.

**`[interactive](https://cloud.google.com/sdk/gcloud/reference/alpha/interactive)`**:
`(ALPHA)` Start the gcloud interactive shell.

**`[survey](https://cloud.google.com/sdk/gcloud/reference/alpha/survey)`**:
`(ALPHA)` Invoke a customer satisfaction survey for Google Cloud CLI.

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist.