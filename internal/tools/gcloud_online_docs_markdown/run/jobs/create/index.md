# gcloud run jobs create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/run/jobs/create](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create)*

**NAME**

: **gcloud run jobs create - create a Cloud Run job**

**SYNOPSIS**

: **`gcloud run jobs create` [`[JOB](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#JOB)`] [`[--binary-authorization](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--binary-authorization)`=`POLICY`] [`[--breakglass](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--breakglass)`=`JUSTIFICATION`] [`[--container](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--container)`=`CONTAINER`] [`[--key](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--key)`=`KEY`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--max-retries](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--max-retries)`=`MAX_RETRIES`] [`[--parallelism](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--parallelism)`=`PARALLELISM`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--region)`=`REGION`] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--service-account)`=`SERVICE_ACCOUNT`] [`[--set-cloudsql-instances](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--set-cloudsql-instances)`=[`CLOUDSQL-INSTANCES`,…]] [`[--task-timeout](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--task-timeout)`=`TASK_TIMEOUT`] [`[--tasks](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--tasks)`=`TASKS`; default=1] [`[--vpc-connector](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--vpc-connector)`=`VPC_CONNECTOR`] [`[--vpc-egress](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--vpc-egress)`=`VPC_EGRESS`] [`[--add-volume](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--add-volume)`=[`KEY`=`VALUE`,…] `[--clear-volumes](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--clear-volumes)` `[--remove-volume](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--remove-volume)`=[`VOLUME`,…]] [`[--add-volume-mount](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--add-volume-mount)`=[`volume`=`NAME`,`mount-path`=`MOUNT_PATH`,…] `[--args](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--args)`=[`ARG`,…] `[--clear-volume-mounts](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--clear-volume-mounts)` `[--command](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--command)`=[`COMMAND`,…] `[--cpu](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--cpu)`=`CPU` `[--depends-on](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--depends-on)`=[`CONTAINER`,…] `[--image](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--image)`=`IMAGE` `[--memory](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--memory)`=`MEMORY` `[--remove-volume-mount](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--remove-volume-mount)`=[`MOUNT_PATH`,…] `[--clear-env-vars](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--clear-env-vars)`     | `[--env-vars-file](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--env-vars-file)`=`FILE_PATH`     | `[--set-env-vars](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--set-env-vars)`=[`KEY`=`VALUE`,…]     | `[--remove-env-vars](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--remove-env-vars)`=[`KEY`,…] `[--update-env-vars](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--update-env-vars)`=[`KEY`=`VALUE`,…] `[--clear-secrets](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--clear-secrets)`     | `[--set-secrets](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--set-secrets)`=[`KEY`=`VALUE`,…]     | `[--remove-secrets](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--remove-secrets)`=[`KEY`,…] `[--update-secrets](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--update-secrets)`=[`KEY`=`VALUE`,…]] [`[--async](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--async)`     | `[--execute-now](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--execute-now)` `[--wait](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--wait)`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--network)`=`NETWORK` `[--network-tags](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--network-tags)`=[`TAG`,…] `[--subnet](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#--subnet)`=`SUBNET`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/run/jobs/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates a new Cloud Run job.

**EXAMPLES**

: To deploy a new job `my-data-transformation` on Cloud Run:

```
gcloud run jobs create my-data-transformation --image=us-docker.pkg.dev/project/image
```

You may also omit the job name. Then a prompt will be displayed with a suggested
default value:

```
gcloud run jobs create --image=us-docker.pkg.dev/project/image
```

**POSITIONAL ARGUMENTS**

: **Job resource - Job to create. This represents a Cloud resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `JOB` on the command line with a fully specified
name;
- specify the job name from an interactive prompt with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**[`JOB`]**:
ID of the Job or fully qualified identifier for the Job.
To set the `jobs` attribute:

- provide the argument `JOB` on the command line;
- specify the job name from an interactive prompt.**

**FLAGS**

: **--binary-authorization**:
Binary Authorization policy to check against. This must be set to "default".

**--breakglass**:
Justification to bypass Binary Authorization policy constraints and allow the
operation. See [https://cloud.google.com/binary-authorization/docs/using-breakglass](https://cloud.google.com/binary-authorization/docs/using-breakglass)
for more information. Next update or deploy command will automatically clear
existing breakglass justification.

**--container**:
Specifies a container by name. Flags following --container will apply to the
specified container.
Flags that are not container-specific must be specified before --container.

**--key**:
CMEK key reference to encrypt the container with.

**--labels**:
List of label KEY=VALUE pairs to add.

**--max-retries**:
Number of times a task is allowed to restart in case of failure before being
failed permanently. This applies per-task, not per-job. If set to 0, tasks will
only run once and never be retried on failure.

**--parallelism**:
Number of tasks that may run concurrently. Must be less than or equal to the
number of tasks. Set to 0 to unset.

**--region**:
Region in which the resource can be found. Alternatively, set the property
[run/region].

**--service-account**:
the email address of an IAM service account associated with the revision of the
service. The service account represents the identity of the running revision,
and determines what permissions the revision has.

**--set-cloudsql-instances**:
You can specify a name of a Cloud SQL instance if it's in the same project and
region as your Cloud Run resource; otherwise specify
<project>:<region>:<instance> for the instance.

**--task-timeout**:
Set the maximum time (deadline) a job task attempt can run for. In the case of
retries, this deadline applies to each attempt of a task. If the task attempt
does not complete within this time, it will be killed. It is specified as a
duration; for example, "10m5s" is ten minutes, and five seconds. If you don't
specify a unit, seconds is assumed. For example, "10" is 10 seconds.

**--tasks**:
Number of tasks that must run to completion for the execution to be considered
done.

**--vpc-connector**:
Set a VPC connector for this resource.

**--vpc-egress**:
Specify which of the outbound traffic to send through Direct VPC egress or the
VPC connector for this resource. This resource must have Direct VPC egress
enabled or a VPC connector to set this flag. `VPC_EGRESS`
must be one of:

**`all`**:
(DEPRECATED) Sends all outbound traffic through Direct VPC egress or the VPC
connector. Provides the same functionality as 'all-traffic'. Prefer to use
'all-traffic' instead.

**`all-traffic`**:
Sends all outbound traffic through Direct VPC egress or the VPC connector.

**`private-ranges-only`**:
Default option. Sends outbound traffic to private IP addresses (RFC 1918 and
Private Google Access IPs) through Direct VPC egress or the VPC connector.
Traffic to other Cloud Run services might require additional configuration. See
[https://cloud.google.com/run/docs/securing/private-networking#send_requests_to_other_services_and_services](https://cloud.google.com/run/docs/securing/private-networking#send_requests_to_other_services_and_services)
for more information.

**--add-volume**:
Adds a volume to the Cloud Run resource. To add more than one volume, specify
this flag multiple times. Volumes must have a `name` and
`type` key. Only certain values are supported for `type`.
Depending on the provided type, other keys will be required. The following types
are supported with the specified additional keys:
`cloud-storage`: A volume representing a Cloud Storage bucket. This
volume type is mounted using Cloud Storage FUSE. See [https://cloud.google.com/storage/docs/gcs-fuse](https://cloud.google.com/storage/docs/gcs-fuse)
for the details and limitations of this filesystem. Additional keys:

- bucket: (required) the name of the bucket to use as the source of this volume
- readonly: (optional) A boolean. If true, this volume will be read-only from all
mounts.

`in-memory`: An ephemeral volume that stores data in the instance's
memory. With this type of volume, data is not shared between instances and all
data will be lost when the instance it is on is terminated. Additional keys:

- size-limit: (optional) A quantity representing the maximum amount of memory
allocated to this volume, such as "512Mi" or "3G". Data stored in an in-memory
volume consumes the memory allocation of the container that wrote the data. If
size-limit is not specified, the maximum size will be half the total memory
limit of all containers.

`nfs`: Represents a volume backed by an NFS server. Additional keys:

- location: (required) The location of the NFS Server, in the form SERVER:/PATH
- readonly: (optional) A boolean. If true, this volume will be read-only from all
mounts.

**--clear-volumes**:
Remove all existing volumes from the Cloud Run resource, including volumes
mounted as secrets

**--remove-volume**:
Removes volumes from the Cloud Run resource.

Container Flags

```
If the --container is specified the following arguments may only be specified after a --container flag.
```

**--add-volume-mount**:
Adds a mount to the current container. Must contain the keys
`volume=NAME` and `mount-path=/PATH` where NAME is the
name of a volume on this resource and PATH is the path within the container's
filesystem to mount this volume.

**--args**:
Comma-separated arguments passed to the command run by the container image. If
not specified and no '--command' is provided, the container image's default Cmd
is used. Otherwise, if not specified, no arguments are passed. To reset this
field to its default, pass an empty string.

**--clear-volume-mounts**:
Remove all existing mounts from the current container.

**--command**:
Entrypoint for the container image. If not specified, the container image's
default Entrypoint is run. To reset this field to its default, pass an empty
string.

**--cpu**:
Set a CPU limit in Kubernetes cpu units.
Cloud Run supports values fractional values below 1, 1, 2, 4, and 8. Some CPU
values requires a minimum Memory `--memory` value.

**--depends-on**:
List of container dependencies to add to the current container.

**--image**:
Name of the container image to deploy (e.g.
`us-docker.pkg.dev/cloudrun/container/job:latest`).

**--memory**:
Set a memory limit. Ex: 1024Mi, 4Gi.

**--remove-volume-mount**:
Removes the volume mounted at the specified path from the current container.

**--clear-env-vars**

**--clear-secrets**

**--async**

**--network**

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

: These variants are also available:

```
gcloud alpha run jobs create
```

```
gcloud beta run jobs create
```