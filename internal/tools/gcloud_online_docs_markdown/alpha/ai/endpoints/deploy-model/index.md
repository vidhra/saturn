# gcloud alpha ai endpoints deploy-model  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/deploy-model](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/deploy-model)*

**NAME**

: **gcloud alpha ai endpoints deploy-model - deploy a model to an existing Vertex AI endpoint**

**SYNOPSIS**

: **`gcloud alpha ai endpoints deploy-model` (`[ENDPOINT](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/deploy-model#ENDPOINT)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/deploy-model#--region)`=`REGION`) `[--display-name](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/deploy-model#--display-name)`=`DISPLAY_NAME` `[--model](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/deploy-model#--model)`=`MODEL` [`[--accelerator](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/deploy-model#--accelerator)`=[`count`=`COUNT`],[`type`=`TYPE`]] [`[--autoscaling-metric-specs](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/deploy-model#--autoscaling-metric-specs)`=[`METRIC-NAME`=`TARGET`,…]] [`[--deployed-model-id](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/deploy-model#--deployed-model-id)`=`DEPLOYED_MODEL_ID`] [`[--enable-access-logging](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/deploy-model#--enable-access-logging)`] [`[--enable-container-logging](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/deploy-model#--enable-container-logging)`] [`[--machine-type](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/deploy-model#--machine-type)`=`MACHINE_TYPE`] [`[--max-replica-count](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/deploy-model#--max-replica-count)`=`MAX_REPLICA_COUNT`] [`[--min-replica-count](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/deploy-model#--min-replica-count)`=`MIN_REPLICA_COUNT`] [`[--multihost-gpu-node-count](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/deploy-model#--multihost-gpu-node-count)`=`MULTIHOST_GPU_NODE_COUNT`] [`[--reservation-affinity](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/deploy-model#--reservation-affinity)`=[`key`=`KEY`],[`reservation-affinity-type`=`RESERVATION-AFFINITY-TYPE`],[`values`=`VALUES`]] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/deploy-model#--service-account)`=`SERVICE_ACCOUNT`] [`[--spot](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/deploy-model#--spot)`] [`[--tpu-topology](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/deploy-model#--tpu-topology)`=`TPU_TOPOLOGY`] [`[--traffic-split](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/deploy-model#--traffic-split)`=[`DEPLOYED_MODEL_ID`=`VALUE`,…]] [`[--shared-resources](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/deploy-model#--shared-resources)`=`SHARED_RESOURCES` : `[--shared-resources-region](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/deploy-model#--shared-resources-region)`=`SHARED_RESOURCES_REGION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/ai/endpoints/deploy-model#GCLOUD-WIDE-FLAGS) …`]**

**EXAMPLES**

: To deploy a model ``456`` to an endpoint
``123`` under project
``example`` in region
``us-central1``, run:

```
gcloud alpha ai endpoints deploy-model 123 --project=example --region=us-central1 --model=456 --display-name=my_deployed_model
```

**POSITIONAL ARGUMENTS**

: **Endpoint resource - The endpoint to deploy a model to. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `endpoint` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`ENDPOINT`**:
ID of the endpoint or fully qualified identifier for the endpoint.
To set the `name` attribute:

- provide the argument `endpoint` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
Cloud region for the endpoint.
To set the `region` attribute:

- provide the argument `endpoint` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `ai/region`;
- choose one from the prompted list of available regions.**

**REQUIRED FLAGS**

: **--display-name**:
Display name of the deployed model.

**--model**:
Id of the uploaded model.

**OPTIONAL FLAGS**

: **--accelerator**:
Manage the accelerator config for GPU serving. When deploying a model with
Compute Engine Machine Types, a GPU accelerator may also be selected.

**`type`**:
The type of the accelerator. Choices are 'nvidia-a100-80gb', 'nvidia-b200',
'nvidia-h100-80gb', 'nvidia-h100-mega-80gb', 'nvidia-h200-141gb', 'nvidia-l4',
'nvidia-tesla-a100', 'nvidia-tesla-k80', 'nvidia-tesla-p100', 'nvidia-tesla-p4',
'nvidia-tesla-t4', 'nvidia-tesla-v100'.

**`count`**:
The number of accelerators to attach to each machine running the job. This is
usually 1. If not specified, the default value is 1.
For example: `--accelerator=type=nvidia-tesla-k80,count=1`

**--autoscaling-metric-specs**:
Metric specifications that overrides a resource utilization metric's target
value. At most one entry is allowed per metric.

**`METRIC-NAME`**:
Resource metric name. Choices are 'cpu-usage', 'gpu-duty-cycle'.

**`TARGET`**:
Target resource utilization in percentage (1% - 100%) for the given metric. If
the value is set to 60, the target resource utilization is 60%.
For example: `--autoscaling-metric-specs=cpu-usage=70`

**--deployed-model-id**:
User-specified ID of the deployed-model.

**--enable-access-logging**:
If true, online prediction access logs are sent to Cloud Logging.
These logs are standard server access logs, containing information like
timestamp and latency for each prediction request.

**--enable-container-logging**:
If true, the container of the deployed model instances will send
`stderr` and `stdout` streams to Cloud Logging.
Currently, only supported for custom-trained Models and AutoML Tabular Models.

**--machine-type**:
The machine resources to be used for each node of this deployment. For available
machine types, see [https://cloud.google.com/ai-platform-unified/docs/predictions/machine-types](https://cloud.google.com/ai-platform-unified/docs/predictions/machine-types).

**--max-replica-count**:
Maximum number of machine replicas for the deployment resources the model will
be deployed on.

**--min-replica-count**:
Minimum number of machine replicas for the deployment resources the model will
be deployed on. If specified, the value must be equal to or larger than 1.
If not specified and the uploaded models use dedicated resources, the default
value is 1.

**--multihost-gpu-node-count**:
The number of nodes per replica for multihost GPU deployments. Required for
multihost GPU deployments.

**--reservation-affinity**:
A ReservationAffinity can be used to configure a Vertex AI resource (e.g., a
DeployedModel) to draw its Compute Engine resources from a Shared Reservation,
or exclusively from on-demand capacity.

**--service-account**:
Service account that the deployed model's container runs as. Specify the email
address of the service account. If this service account is not specified, the
container runs as a service account that doesn't have access to the resource
project.

**--spot**:
If true, schedule the deployment workload on Spot VMs.

**--tpu-topology**:
CloudTPU topology to use for this deployment. Required for multihost CloudTPU
deployments: [https://cloud.google.com/kubernetes-engine/docs/concepts/tpus#topology](https://cloud.google.com/kubernetes-engine/docs/concepts/tpus#topology).

**--traffic-split**:
List of pairs of deployed model id and value to set as traffic split.

**Deployment resource pool resource - The deployment resource pool to co-host a
model on. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `--shared-resources` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--shared-resources**:
ID of the deployment_resource_pool or fully qualified identifier for the
deployment_resource_pool.
To set the `name` attribute:

- provide the argument `--shared-resources` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--shared-resources-region**:
Cloud region for the deployment_resource_pool.
To set the `region` attribute:

- provide the argument `--shared-resources` on the command line with a
fully specified name;
- provide the argument `--shared-resources-region` on the command line;
- provide the argument `--region` on the command line;
- set the property `ai/region`;
- choose one from the prompted list of available regions.**

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
gcloud ai endpoints deploy-model
```

```
gcloud beta ai endpoints deploy-model
```