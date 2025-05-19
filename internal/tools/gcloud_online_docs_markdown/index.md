# gcloud  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/](https://cloud.google.com/sdk/gcloud/reference/)*

**NAME**

: **gcloud - manage Google Cloud resources and developer workflow**

**SYNOPSIS**

: **`[gcloud](https://cloud.google.com/sdk/gcloud/reference/#gcloud)` `[GROUP](https://cloud.google.com/sdk/gcloud/reference/#GROUP)` | `[COMMAND](https://cloud.google.com/sdk/gcloud/reference/#COMMAND)` [`[--account](https://cloud.google.com/sdk/gcloud/reference/#--account)`=`ACCOUNT`] [`[--billing-project](https://cloud.google.com/sdk/gcloud/reference/#--billing-project)`=`BILLING_PROJECT`] [`[--configuration](https://cloud.google.com/sdk/gcloud/reference/#--configuration)`=`CONFIGURATION`] [`[--flags-file](https://cloud.google.com/sdk/gcloud/reference/#--flags-file)`=`YAML_FILE`] [`[--flatten](https://cloud.google.com/sdk/gcloud/reference/#--flatten)`=[`KEY`,…]] [`[--format](https://cloud.google.com/sdk/gcloud/reference/#--format)`=`FORMAT`] [`[--help](https://cloud.google.com/sdk/gcloud/reference/#--help)`] [`[--project](https://cloud.google.com/sdk/gcloud/reference/#--project)`=`PROJECT_ID`] [`[--quiet](https://cloud.google.com/sdk/gcloud/reference/#--quiet)`, `[-q](https://cloud.google.com/sdk/gcloud/reference/#-q)`] [`[--verbosity](https://cloud.google.com/sdk/gcloud/reference/#--verbosity)`=`VERBOSITY`; default="warning"] [`[--version](https://cloud.google.com/sdk/gcloud/reference/#--version)`, `[-v](https://cloud.google.com/sdk/gcloud/reference/#-v)`] [`[-h](https://cloud.google.com/sdk/gcloud/reference/#-h)`] [`[--access-token-file](https://cloud.google.com/sdk/gcloud/reference/#--access-token-file)`=`ACCESS_TOKEN_FILE`] [`[--impersonate-service-account](https://cloud.google.com/sdk/gcloud/reference/#--impersonate-service-account)`=`SERVICE_ACCOUNT_EMAILS`] [`[--log-http](https://cloud.google.com/sdk/gcloud/reference/#--log-http)`] [`[--trace-token](https://cloud.google.com/sdk/gcloud/reference/#--trace-token)`=`TRACE_TOKEN`] [`[--no-user-output-enabled](https://cloud.google.com/sdk/gcloud/reference/#--user-output-enabled)`]**

**DESCRIPTION**

: The `gcloud` CLI manages authentication, local configuration,
developer workflow, and interactions with the Google Cloud APIs.
For a quick introduction to the `gcloud` CLI, a list of commonly used
commands, and a look at how these commands are structured, run `[gcloud cheat-sheet](https://cloud.google.com/sdk/gcloud/reference/cheat-sheet)` or see
the [`gcloud` CLI cheat
sheet](https://cloud.google.com/sdk/docs/cheatsheet).

**GLOBAL FLAGS**

: **--account**:
Google Cloud user account to use for invocation. Overrides the default
`core/account` property value for this command invocation.

**--billing-project**:
The Google Cloud project that will be charged quota for operations performed in
`gcloud`. If you need to operate on one project, but need quota
against a different project, you can use this flag to specify the billing
project. If both `billing/quota_project` and
`--billing-project` are specified, `--billing-project`
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
`yaml`. For more details run $ gcloud topic formats. Run `$ [gcloud config set](https://cloud.google.com/sdk/gcloud/reference/config/set) --help` to
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
Disable all interactive prompts when running `gcloud` commands. If
input is required, defaults will be used, or an error will be raised.
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
A file path to read the access token. Use this flag to authenticate
`gcloud` with an access token. The credentials of the active account
(if exists) will be ignored. The file should only contain an access token with
no other information. Overrides the default `auth/access_token_file`
property value for this command invocation.

**--impersonate-service-account**:
For this `gcloud` invocation, all API requests will be made as the
given service account or target service account in an impersonation delegation
chain instead of the currently selected account. You can specify either a single
service account as the impersonator, or a comma-separated list of service
accounts to create an impersonation delegation chain. The impersonation is done
without needing to create, download, and activate a key for the service account
or accounts.
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

**`[access-approval](https://cloud.google.com/sdk/gcloud/reference/access-approval)`**:
Manage Access Approval requests and settings.

**`[access-context-manager](https://cloud.google.com/sdk/gcloud/reference/access-context-manager)`**:
Manage Access Context Manager resources.

**`[active-directory](https://cloud.google.com/sdk/gcloud/reference/active-directory)`**:
Manage Managed Microsoft AD resources.

**`[ai](https://cloud.google.com/sdk/gcloud/reference/ai)`**:
Manage entities in Vertex AI.

**`[ai-platform](https://cloud.google.com/sdk/gcloud/reference/ai-platform)`**:
Manage AI Platform jobs and models.

**`[alloydb](https://cloud.google.com/sdk/gcloud/reference/alloydb)`**:
Create and manage AlloyDB databases.

**`[alpha](https://cloud.google.com/sdk/gcloud/reference/alpha)`**:
`(ALPHA)` Alpha versions of gcloud commands.

**`[anthos](https://cloud.google.com/sdk/gcloud/reference/anthos)`**:
Anthos command Group.

**`[api-gateway](https://cloud.google.com/sdk/gcloud/reference/api-gateway)`**:
Manage Cloud API Gateway resources.

**`[apigee](https://cloud.google.com/sdk/gcloud/reference/apigee)`**:
Manage Apigee resources.

**`[app](https://cloud.google.com/sdk/gcloud/reference/app)`**:
Manage your App Engine deployments.

**`[apphub](https://cloud.google.com/sdk/gcloud/reference/apphub)`**:
Manage App Hub resources.

**`[artifacts](https://cloud.google.com/sdk/gcloud/reference/artifacts)`**:
Manage Artifact Registry resources.

**`[asset](https://cloud.google.com/sdk/gcloud/reference/asset)`**:
Manage the Cloud Asset Inventory.

**`[assured](https://cloud.google.com/sdk/gcloud/reference/assured)`**:
Read and manipulate Assured Workloads data controls.

**`[audit-manager](https://cloud.google.com/sdk/gcloud/reference/audit-manager)`**:
Enroll resources, audit workloads and generate reports.

**`[auth](https://cloud.google.com/sdk/gcloud/reference/auth)`**:
Manage oauth2 credentials for the Google Cloud CLI.

**`[backup-dr](https://cloud.google.com/sdk/gcloud/reference/backup-dr)`**:
Manage Backup and DR resources.

**`[batch](https://cloud.google.com/sdk/gcloud/reference/batch)`**:
Manage Batch resources.

**`[beta](https://cloud.google.com/sdk/gcloud/reference/beta)`**:
`(BETA)` Beta versions of gcloud commands.

**`[bigtable](https://cloud.google.com/sdk/gcloud/reference/bigtable)`**:
Manage your Cloud Bigtable storage.

**`[billing](https://cloud.google.com/sdk/gcloud/reference/billing)`**:
Manage billing accounts and associate them with projects.

**`[bms](https://cloud.google.com/sdk/gcloud/reference/bms)`**:
Manage Bare Metal Solution resources.

**`[bq](https://cloud.google.com/sdk/gcloud/reference/bq)`**:
Manage Bq resources.

**`[builds](https://cloud.google.com/sdk/gcloud/reference/builds)`**:
Create and manage builds for Google Cloud Build.

**`[certificate-manager](https://cloud.google.com/sdk/gcloud/reference/certificate-manager)`**:
Manage SSL certificates for your Google Cloud projects.

**`[cloud-shell](https://cloud.google.com/sdk/gcloud/reference/cloud-shell)`**:
Manage Google Cloud Shell.

**`[colab](https://cloud.google.com/sdk/gcloud/reference/colab)`**:
Manage Colab Enterprise resources.

**`[components](https://cloud.google.com/sdk/gcloud/reference/components)`**:
List, install, update, or remove Google Cloud CLI components.

**`[composer](https://cloud.google.com/sdk/gcloud/reference/composer)`**:
Create and manage Cloud Composer Environments.

**`[compute](https://cloud.google.com/sdk/gcloud/reference/compute)`**:
Create and manipulate Compute Engine resources.

**`[config](https://cloud.google.com/sdk/gcloud/reference/config)`**:
View and edit Google Cloud CLI properties.

**`[container](https://cloud.google.com/sdk/gcloud/reference/container)`**:
Deploy and manage clusters of machines for running containers.

**`[data-catalog](https://cloud.google.com/sdk/gcloud/reference/data-catalog)`**:
Manage Data Catalog resources.

**`[database-migration](https://cloud.google.com/sdk/gcloud/reference/database-migration)`**:
Manage Database Migration Service resources.

**`[dataflow](https://cloud.google.com/sdk/gcloud/reference/dataflow)`**:
Manage Google Cloud Dataflow resources.

**`[dataplex](https://cloud.google.com/sdk/gcloud/reference/dataplex)`**:
Manage Dataplex resources.

**`[dataproc](https://cloud.google.com/sdk/gcloud/reference/dataproc)`**:
Create and manage Google Cloud Dataproc clusters and jobs.

**`[datastore](https://cloud.google.com/sdk/gcloud/reference/datastore)`**:
Manage your Cloud Datastore resources.

**`[datastream](https://cloud.google.com/sdk/gcloud/reference/datastream)`**:
Manage Cloud Datastream resources.

**`[deploy](https://cloud.google.com/sdk/gcloud/reference/deploy)`**:
Create and manage Cloud Deploy resources.

**`[deployment-manager](https://cloud.google.com/sdk/gcloud/reference/deployment-manager)`**:
Manage deployments of cloud resources.

**`[developer-connect](https://cloud.google.com/sdk/gcloud/reference/developer-connect)`**:
Manage Developer Connect resources.

**`[dns](https://cloud.google.com/sdk/gcloud/reference/dns)`**:
Manage your Cloud DNS managed-zones and record-sets.

**`[domains](https://cloud.google.com/sdk/gcloud/reference/domains)`**:
Manage domains for your Google Cloud projects.

**`[edge-cache](https://cloud.google.com/sdk/gcloud/reference/edge-cache)`**:
Manage Media CDN resources.

**`[edge-cloud](https://cloud.google.com/sdk/gcloud/reference/edge-cloud)`**:
Manage edge-cloud resources.

**`[emulators](https://cloud.google.com/sdk/gcloud/reference/emulators)`**:
Set up your local development environment using emulators.

**`[endpoints](https://cloud.google.com/sdk/gcloud/reference/endpoints)`**:
Create, enable and manage API services.

**`[essential-contacts](https://cloud.google.com/sdk/gcloud/reference/essential-contacts)`**:
Manage Essential Contacts.

**`[eventarc](https://cloud.google.com/sdk/gcloud/reference/eventarc)`**:
Manage Eventarc resources.

**`[filestore](https://cloud.google.com/sdk/gcloud/reference/filestore)`**:
Create and manipulate Filestore resources.

**`[firebase](https://cloud.google.com/sdk/gcloud/reference/firebase)`**:
Work with Google Firebase.

**`[firestore](https://cloud.google.com/sdk/gcloud/reference/firestore)`**:
Manage your Cloud Firestore resources.

**`[functions](https://cloud.google.com/sdk/gcloud/reference/functions)`**:
Manage Google Cloud Functions.

**`[gemini](https://cloud.google.com/sdk/gcloud/reference/gemini)`**:
Manage code repository index resources.

**`[healthcare](https://cloud.google.com/sdk/gcloud/reference/healthcare)`**:
Manage Cloud Healthcare resources.

**`[iam](https://cloud.google.com/sdk/gcloud/reference/iam)`**:
Manage IAM service accounts and keys.

**`[iap](https://cloud.google.com/sdk/gcloud/reference/iap)`**:
Manage IAP policies.

**`[identity](https://cloud.google.com/sdk/gcloud/reference/identity)`**:
Manage Cloud Identity Groups and Memberships resources.

**`[ids](https://cloud.google.com/sdk/gcloud/reference/ids)`**:
Manage Cloud IDS.

**`[immersive-stream](https://cloud.google.com/sdk/gcloud/reference/immersive-stream)`**:
Manage Immersive Stream resources.

**`[infra-manager](https://cloud.google.com/sdk/gcloud/reference/infra-manager)`**:
Manage Infra Manager resources.

**`[kms](https://cloud.google.com/sdk/gcloud/reference/kms)`**:
Manage cryptographic keys in the cloud.

**`[logging](https://cloud.google.com/sdk/gcloud/reference/logging)`**:
Manage Cloud Logging.

**`[looker](https://cloud.google.com/sdk/gcloud/reference/looker)`**:
Manage Looker resources.

**`[lustre](https://cloud.google.com/sdk/gcloud/reference/lustre)`**:
Manage Lustre resources.

**`[managed-kafka](https://cloud.google.com/sdk/gcloud/reference/managed-kafka)`**:
Administer Managed Service for Apache Kafka clusters, topics, and consumer
groups.

**`[memcache](https://cloud.google.com/sdk/gcloud/reference/memcache)`**:
Manage Cloud Memorystore Memcached resources.

**`[memorystore](https://cloud.google.com/sdk/gcloud/reference/memorystore)`**:
Manage Memorystore resources.

**`[metastore](https://cloud.google.com/sdk/gcloud/reference/metastore)`**:
Manage Dataproc Metastore resources.

**`[migration](https://cloud.google.com/sdk/gcloud/reference/migration)`**:
The root group for various Cloud Migration teams.

**`[ml](https://cloud.google.com/sdk/gcloud/reference/ml)`**:
Use Google Cloud machine learning capabilities.

**`[ml-engine](https://cloud.google.com/sdk/gcloud/reference/ml-engine)`**:
Manage AI Platform jobs and models.

**`[model-armor](https://cloud.google.com/sdk/gcloud/reference/model-armor)`**:
Model Armor is a service offering LLM-agnostic security and AI safety measures
to mitigate risks associated with large language models (LLMs).

**`[monitoring](https://cloud.google.com/sdk/gcloud/reference/monitoring)`**:
Manage Cloud Monitoring dashboards.

**`[netapp](https://cloud.google.com/sdk/gcloud/reference/netapp)`**:
Create and manipulate Cloud NetApp Files resources.

**`[network-connectivity](https://cloud.google.com/sdk/gcloud/reference/network-connectivity)`**:
Manage Network Connectivity Center resources.

**`[network-management](https://cloud.google.com/sdk/gcloud/reference/network-management)`**:
Manage Network Management resources.

**`[network-security](https://cloud.google.com/sdk/gcloud/reference/network-security)`**:
Manage Network Security resources.

**`[network-services](https://cloud.google.com/sdk/gcloud/reference/network-services)`**:
Manage Network Services resources.

**`[notebooks](https://cloud.google.com/sdk/gcloud/reference/notebooks)`**:
Notebooks Command Group.

**`[oracle-database](https://cloud.google.com/sdk/gcloud/reference/oracle-database)`**:
Manage Oracle Database resources.

**`[org-policies](https://cloud.google.com/sdk/gcloud/reference/org-policies)`**:
Create and manage Organization Policies.

**`[organizations](https://cloud.google.com/sdk/gcloud/reference/organizations)`**:
Create and manage Google Cloud Platform Organizations.

**`[pam](https://cloud.google.com/sdk/gcloud/reference/pam)`**:
Manage Privileged Access Manager (PAM) entitlements and grants.

**`[parametermanager](https://cloud.google.com/sdk/gcloud/reference/parametermanager)`**:
Parameter Manager is a single source of truth to store, access and manage the
lifecycle of your application parameters.

**`[policy-intelligence](https://cloud.google.com/sdk/gcloud/reference/policy-intelligence)`**:
A platform to help better understand, use, and manage policies at scale.

**`[policy-troubleshoot](https://cloud.google.com/sdk/gcloud/reference/policy-troubleshoot)`**:
Troubleshoot Google Cloud Platform policies.

**`[preview](https://cloud.google.com/sdk/gcloud/reference/preview)`**:
`(PREVIEW)` Preview versions of gcloud commands.

**`[privateca](https://cloud.google.com/sdk/gcloud/reference/privateca)`**:
Manage private Certificate Authorities on Google Cloud.

**`[projects](https://cloud.google.com/sdk/gcloud/reference/projects)`**:
Create and manage project access policies.

**`[publicca](https://cloud.google.com/sdk/gcloud/reference/publicca)`**:
Manage accounts for Google Trust Services' Certificate Authority.

**`[pubsub](https://cloud.google.com/sdk/gcloud/reference/pubsub)`**:
Manage Cloud Pub/Sub topics, subscriptions, and snapshots.

**`[recaptcha](https://cloud.google.com/sdk/gcloud/reference/recaptcha)`**:
Manage reCAPTCHA Enterprise Keys.

**`[recommender](https://cloud.google.com/sdk/gcloud/reference/recommender)`**:
Manage Cloud recommendations and recommendation rules.

**`[redis](https://cloud.google.com/sdk/gcloud/reference/redis)`**:
Manage Cloud Memorystore Redis resources.

**`[resource-manager](https://cloud.google.com/sdk/gcloud/reference/resource-manager)`**:
Manage Cloud Resources.

**`[run](https://cloud.google.com/sdk/gcloud/reference/run)`**:
Manage your Cloud Run applications.

**`[scc](https://cloud.google.com/sdk/gcloud/reference/scc)`**:
Manage Cloud SCC resources.

**`[scheduler](https://cloud.google.com/sdk/gcloud/reference/scheduler)`**:
Manage Cloud Scheduler jobs and schedules.

**`[secrets](https://cloud.google.com/sdk/gcloud/reference/secrets)`**:
Manage secrets on Google Cloud.

**`[service-directory](https://cloud.google.com/sdk/gcloud/reference/service-directory)`**:
Command groups for Service Directory.

**`[service-extensions](https://cloud.google.com/sdk/gcloud/reference/service-extensions)`**:
Manage Service Extensions resources.

**`[services](https://cloud.google.com/sdk/gcloud/reference/services)`**:
List, enable and disable APIs and services.

**`[source](https://cloud.google.com/sdk/gcloud/reference/source)`**:
Cloud git repository commands.

**`[spanner](https://cloud.google.com/sdk/gcloud/reference/spanner)`**:
Command groups for Cloud Spanner.

**`[sql](https://cloud.google.com/sdk/gcloud/reference/sql)`**:
Create and manage Google Cloud SQL databases.

**`[storage](https://cloud.google.com/sdk/gcloud/reference/storage)`**:
Create and manage Cloud Storage buckets and objects.

**`[tasks](https://cloud.google.com/sdk/gcloud/reference/tasks)`**:
Manage Cloud Tasks queues and tasks.

**`[telco-automation](https://cloud.google.com/sdk/gcloud/reference/telco-automation)`**:
Manage Telco Automation resources.

**`[topic](https://cloud.google.com/sdk/gcloud/reference/topic)`**:
gcloud supplementary help.

**`[transcoder](https://cloud.google.com/sdk/gcloud/reference/transcoder)`**:
Manage Transcoder jobs and job templates.

**`[transfer](https://cloud.google.com/sdk/gcloud/reference/transfer)`**:
Manage Transfer Service jobs, operations, and agents.

**`[vmware](https://cloud.google.com/sdk/gcloud/reference/vmware)`**:
Manage Google Cloud VMware Engine resources.

**`[workbench](https://cloud.google.com/sdk/gcloud/reference/workbench)`**:
Workbench Command Group.

**`[workflows](https://cloud.google.com/sdk/gcloud/reference/workflows)`**:
Manage your Cloud Workflows resources.

**`[workspace-add-ons](https://cloud.google.com/sdk/gcloud/reference/workspace-add-ons)`**:
Manage Google Workspace Add-ons resources.

**`[workstations](https://cloud.google.com/sdk/gcloud/reference/workstations)`**:
Manage Cloud Workstations resources.

**COMMANDS**

: ``COMMAND`` is one of the following:

**`[cheat-sheet](https://cloud.google.com/sdk/gcloud/reference/cheat-sheet)`**:
Display gcloud cheat sheet.

**`[docker](https://cloud.google.com/sdk/gcloud/reference/docker)`**:
`(DEPRECATED)` Enable Docker CLI access to Google Container Registry.

**`[feedback](https://cloud.google.com/sdk/gcloud/reference/feedback)`**:
Provide feedback to the Google Cloud CLI team.

**`[help](https://cloud.google.com/sdk/gcloud/reference)`**:
Search gcloud help text.

**`[info](https://cloud.google.com/sdk/gcloud/reference/info)`**:
Display information about the current gcloud environment.

**`[init](https://cloud.google.com/sdk/gcloud/reference/init)`**:
Initialize or reinitialize gcloud.

**`[survey](https://cloud.google.com/sdk/gcloud/reference/survey)`**:
Invoke a customer satisfaction survey for Google Cloud CLI.

**`[version](https://cloud.google.com/sdk/gcloud/reference/version)`**:
Print version information for Google Cloud CLI components.