# gcloud alpha ai index-endpoints mutate-deployed-index  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/mutate-deployed-index](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/mutate-deployed-index)*

**NAME**

: **gcloud alpha ai index-endpoints mutate-deployed-index - mutate an existing deployed index from a Vertex AI index endpoint**

**SYNOPSIS**

: **`gcloud alpha ai index-endpoints mutate-deployed-index` (`[INDEX_ENDPOINT](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/mutate-deployed-index#INDEX_ENDPOINT)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/mutate-deployed-index#--region)`=`REGION`) `[--deployed-index-id](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/mutate-deployed-index#--deployed-index-id)`=`DEPLOYED_INDEX_ID` [`[--allowed-issuers](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/mutate-deployed-index#--allowed-issuers)`=[`ALLOWED_ISSUERS`,…]] [`[--audiences](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/mutate-deployed-index#--audiences)`=[`AUDIENCES`,…]] [`[--deployment-group](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/mutate-deployed-index#--deployment-group)`=`DEPLOYMENT_GROUP`] [`[--enable-access-logging](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/mutate-deployed-index#--enable-access-logging)`] [`[--machine-type](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/mutate-deployed-index#--machine-type)`=`MACHINE_TYPE`] [`[--max-replica-count](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/mutate-deployed-index#--max-replica-count)`=`MAX_REPLICA_COUNT`] [`[--min-replica-count](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/mutate-deployed-index#--min-replica-count)`=`MIN_REPLICA_COUNT`] [`[--reserved-ip-ranges](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/mutate-deployed-index#--reserved-ip-ranges)`=[`RESERVED_IP_RANGES`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/index-endpoints/mutate-deployed-index#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Mutate an existing deployed index from a Vertex AI index
endpoint.

**EXAMPLES**

: To mutated a deployed index
``deployed-index-123`` from an index endpoint
``456`` with 2 min replica count and 10 max
replica count under project ``example`` in
region ``us-central1``, within
``vertex-ai-ip-ranges-1`` and
``vertex-ai-ip-ranges-2``, within deployment
group ``test``, enabling access logging, with
JWT audiences ``aud1`` and
``aud2``, JWT issuers
``issuer1`` and
``issuer2`` run:

```
gcloud alpha ai index-endpoints mutate-deployed-index 456 --project=example --region=us-central1 --deployed-index-id=deployed-index-123 --min-replica-count=2 --max-replica-count=10 --reserved-ip-ranges=vertex-ai-ip-ranges-1,vertex-ai-ip-ranges-2 --enable-access-logging --audiences=aud1,aud2 --allowed-issuers=issuer1,issuer2 --deployment-group=test
```

**POSITIONAL ARGUMENTS**

: **Index endpoint resource - The index endpoint ID of the index endpoint.. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `index_endpoint` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INDEX_ENDPOINT`**:
ID of the index_endpoint or fully qualified identifier for the index_endpoint.
To set the `name` attribute:

- provide the argument `index_endpoint` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
Cloud region for the index_endpoint.
To set the `region` attribute:

- provide the argument `index_endpoint` on the command line with a
fully specified name;
- provide the argument `--region` on the command line;
- set the property `ai/region`;
- choose one from the prompted list of available regions.**

**REQUIRED FLAGS**

: **--deployed-index-id**:
Id of the deployed index.

**OPTIONAL FLAGS**

: **--allowed-issuers**:
List of allowed JWT issuers for a deployed index.
Each entry must be a valid Google service account, in the following format:
`service-account-name@project-id.iam.gserviceaccount.com`

**--audiences**:
List of JWT audiences that are allowed to access a deployed index.
JWT containing any of these audiences ([https://tools.ietf.org/html/draft-ietf-oauth-json-web-token-32#section](https://tools.ietf.org/html/draft-ietf-oauth-json-web-token-32#section)
-4.1.3) will be accepted.

**--deployment-group**:
Deployment group can be no longer than 64 characters (eg:`test`,
`prod`). If not set, we will use the `default` deployment
group.
Creating deployment_groups with `reserved_ip_ranges` is a recommended
practice when the peered network has multiple peering ranges.This creates your
deployments from predictable IP spaces for easier traffic administration.

**--enable-access-logging**:
If true, online prediction access logs are sent to Cloud Logging.
These logs are standard server access logs, containing information like
timestamp and latency for each prediction request.

**--machine-type**:
The machine resources to be used for each node of this deployment. For available
machine types, see [https://cloud.google.com/ai-platform-unified/docs/predictions/machine-types](https://cloud.google.com/ai-platform-unified/docs/predictions/machine-types).

**--max-replica-count**:
Maximum number of machine replicas the deployed index will be always deployed
on.

**--min-replica-count**:
Minimum number of machine replicas the deployed index will be always deployed
on. If specified, the value must be equal to or larger than 1.

**--reserved-ip-ranges**:
List of reserved IP ranges deployed index will be deployed to.

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
allowlist. These variants are also available:

```
gcloud ai index-endpoints mutate-deployed-index
```

```
gcloud beta ai index-endpoints mutate-deployed-index
```