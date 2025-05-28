# gcloud run deploy  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/run/deploy](https://cloud.google.com/sdk/gcloud/reference/run/deploy)*

**NAME**

: **gcloud run deploy - create or update a Cloud Run service**

**SYNOPSIS**

: **`gcloud run deploy` [[`[SERVICE](https://cloud.google.com/sdk/gcloud/reference/run/deploy#SERVICE)`] `[--namespace](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--namespace)`=`NAMESPACE`] [`[--[no-]allow-unauthenticated](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--[no-]allow-unauthenticated)`] [`[--[no-]allow-unencrypted-build](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--[no-]allow-unencrypted-build)`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--async)`] [`[--breakglass](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--breakglass)`=`JUSTIFICATION`] [`[--clear-vpc-connector](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--clear-vpc-connector)`] [`[--concurrency](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--concurrency)`=`CONCURRENCY`] [`[--container](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--container)`=`CONTAINER`] [`[--[no-]cpu-boost](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--[no-]cpu-boost)`] [`[--[no-]cpu-throttling](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--[no-]cpu-throttling)`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--description)`=`DESCRIPTION`] [`[--execution-environment](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--execution-environment)`=`EXECUTION_ENVIRONMENT`] [`[--gpu-type](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--gpu-type)`=`GPU_TYPE`] [`[--[no-]gpu-zonal-redundancy](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--[no-]gpu-zonal-redundancy)`] [`[--ingress](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--ingress)`=`INGRESS`; default="all"] [`[--[no-]invoker-iam-check](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--[no-]invoker-iam-check)`] [`[--max-instances](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--max-instances)`=`MAX_INSTANCES`] [`[--min](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--min)`=`MIN`] [`[--min-instances](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--min-instances)`=`MIN_INSTANCES`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--region)`=`REGION`] [`[--remove-containers](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--remove-containers)`=[`CONTAINER`,…]] [`[--revision-suffix](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--revision-suffix)`=`REVISION_SUFFIX`] [`[--service-account](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--service-account)`=`SERVICE_ACCOUNT`] [`[--[no-]session-affinity](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--[no-]session-affinity)`] [`[--tag](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--tag)`=`TAG`] [`[--timeout](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--timeout)`=`TIMEOUT`] [`[--no-traffic](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--traffic)`] [`[--vpc-connector](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--vpc-connector)`=`VPC_CONNECTOR`] [`[--vpc-egress](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--vpc-egress)`=`VPC_EGRESS`] [`[--add-cloudsql-instances](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--add-cloudsql-instances)`=[`CLOUDSQL-INSTANCES`,…]     | `[--clear-cloudsql-instances](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--clear-cloudsql-instances)`     | `[--remove-cloudsql-instances](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--remove-cloudsql-instances)`=[`CLOUDSQL-INSTANCES`,…]     | `[--set-cloudsql-instances](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--set-cloudsql-instances)`=[`CLOUDSQL-INSTANCES`,…]] [`[--add-custom-audiences](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--add-custom-audiences)`=[`CUSTOM-AUDIENCES`,…]     | `[--clear-custom-audiences](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--clear-custom-audiences)`     | `[--remove-custom-audiences](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--remove-custom-audiences)`=[`CUSTOM-AUDIENCES`,…]     | `[--set-custom-audiences](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--set-custom-audiences)`=[`CUSTOM-AUDIENCES`,…]] [`[--add-volume](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--add-volume)`=[`KEY`=`VALUE`,…] `[--clear-volumes](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--clear-volumes)` `[--remove-volume](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--remove-volume)`=[`VOLUME`,…]] [`[--add-volume-mount](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--add-volume-mount)`=[`volume`=`NAME`,`mount-path`=`MOUNT_PATH`,…] `[--args](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--args)`=[`ARG`,…] `[--[no-]automatic-updates](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--[no-]automatic-updates)` `[--clear-volume-mounts](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--clear-volume-mounts)` `[--cpu](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--cpu)`=`CPU` `[--depends-on](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--depends-on)`=[`CONTAINER`,…] `[--gpu](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--gpu)`=`GPU` `[--liveness-probe](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--liveness-probe)`=[`KEY`=`VALUE`,…] `[--memory](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--memory)`=`MEMORY` `[--port](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--port)`=`PORT` `[--remove-volume-mount](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--remove-volume-mount)`=[`MOUNT_PATH`,…] `[--startup-probe](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--startup-probe)`=[`KEY`=`VALUE`,…] `[--[no-]use-http2](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--[no-]use-http2)` `[--base-image](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--base-image)`=`BASE_IMAGE`     | `[--clear-base-image](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--clear-base-image)` `[--build-env-vars-file](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--build-env-vars-file)`=`FILE_PATH`     | `[--clear-build-env-vars](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--clear-build-env-vars)`     | `[--set-build-env-vars](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--set-build-env-vars)`=[`KEY`=`VALUE`,…]     | `[--remove-build-env-vars](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--remove-build-env-vars)`=[`KEY`,…] `[--update-build-env-vars](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--update-build-env-vars)`=[`KEY`=`VALUE`,…] `[--build-service-account](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--build-service-account)`=`BUILD_SERVICE_ACCOUNT`     | `[--clear-build-service-account](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--clear-build-service-account)` `[--build-worker-pool](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--build-worker-pool)`=`BUILD_WORKER_POOL`     | `[--clear-build-worker-pool](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--clear-build-worker-pool)` `[--clear-env-vars](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--clear-env-vars)`     | `[--env-vars-file](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--env-vars-file)`=`FILE_PATH`     | `[--set-env-vars](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--set-env-vars)`=[`KEY`=`VALUE`,…]     | `[--remove-env-vars](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--remove-env-vars)`=[`KEY`,…] `[--update-env-vars](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--update-env-vars)`=[`KEY`=`VALUE`,…] `[--clear-secrets](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--clear-secrets)`     | `[--set-secrets](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--set-secrets)`=[`KEY`=`VALUE`,…]     | `[--remove-secrets](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--remove-secrets)`=[`KEY`,…] `[--update-secrets](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--update-secrets)`=[`KEY`=`VALUE`,…] `[--command](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--command)`=[`COMMAND`,…]     | `[--function](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--function)`=`FUNCTION` `[--image](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--image)`=`IMAGE` `[--source](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--source)`=`SOURCE`] [`[--binary-authorization](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--binary-authorization)`=`POLICY`     | `[--clear-binary-authorization](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--clear-binary-authorization)`] [`[--clear-encryption-key-shutdown-hours](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--clear-encryption-key-shutdown-hours)`     | `[--encryption-key-shutdown-hours](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--encryption-key-shutdown-hours)`=`ENCRYPTION_KEY_SHUTDOWN_HOURS`] [`[--clear-key](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--clear-key)`     | `[--key](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--key)`=`KEY`] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--remove-labels)`=[`KEY`,…] `[--labels](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--labels)`=[`KEY`=`VALUE`,…]     | `[--update-labels](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--clear-network](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--clear-network)`     | `[--network](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--network)`=`NETWORK` `[--subnet](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--subnet)`=`SUBNET` `[--clear-network-tags](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--clear-network-tags)`     | `[--network-tags](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--network-tags)`=[`TAG`,…]] [`[--clear-post-key-revocation-action-type](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--clear-post-key-revocation-action-type)`     | `[--post-key-revocation-action-type](https://cloud.google.com/sdk/gcloud/reference/run/deploy#--post-key-revocation-action-type)`=`POST_KEY_REVOCATION_ACTION_TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/run/deploy#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Creates or updates a Cloud Run service.

**EXAMPLES**

: To deploy a container to the service `my-backend` on Cloud Run:

```
gcloud run deploy my-backend --image=us-docker.pkg.dev/project/image
```

You may also omit the service name. Then a prompt will be displayed with a
suggested default value:

```
gcloud run deploy --image=us-docker.pkg.dev/project/image
```

To deploy to Cloud Run on Kubernetes Engine, you need to specify a cluster:

```
gcloud run deploy --image=us-docker.pkg.dev/project/image --cluster=my-cluster
```

**POSITIONAL ARGUMENTS**

: **Service resource - Service to deploy to. The arguments in this group can be used
to specify the attributes of this resource.

**[`SERVICE`]**:
ID of the service or fully qualified identifier for the service.
To set the `service` attribute:

- provide the argument `SERVICE` on the command line;
- specify the service name from an interactive prompt.

**--namespace**:
Specific to Cloud Run for Anthos: Kubernetes namespace for the service.
To set the `namespace` attribute:

- provide the argument `SERVICE` on the command line with a fully
specified name;
- specify the service name from an interactive prompt with a fully specified name;
- provide the argument `--namespace` on the command line;
- set the property `run/namespace`;
- For Cloud Run on Kubernetes Engine, defaults to "default". Otherwise, defaults
to project ID.;
- provide the argument `project` on the command line;
- set the property `core/project`.**

**FLAGS**

: **--[no-]allow-unauthenticated**:
Whether to enable allowing unauthenticated access to the service. This may take
a few moments to take effect. Use `--allow-unauthenticated` to enable
and `--no-allow-unauthenticated` to disable.

**--[no-]allow-unencrypted-build**:
Whether to allow customer-managed encryption key (CMEK) deployments without
encrypting the build process. This means that only the deployed container will
be encrypted. Use `--allow-unencrypted-build` to enable and
`--no-allow-unencrypted-build` to disable.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--breakglass**:
Justification to bypass Binary Authorization policy constraints and allow the
operation. See [https://cloud.google.com/binary-authorization/docs/using-breakglass](https://cloud.google.com/binary-authorization/docs/using-breakglass)
for more information. Next update or deploy command will automatically clear
existing breakglass justification.

**--clear-vpc-connector**:
Remove the VPC connector for this resource.

**--concurrency**:
Set the maximum number of concurrent requests allowed per container instance.
Leave concurrency unspecified or provide the special value 'default' to receive
the server default value.

**--container**:
Specifies a container by name. Flags following --container will apply to the
specified container.
Flags that are not container-specific must be specified before --container.

**--[no-]cpu-boost**:
Whether to allocate extra CPU to containers on startup to reduce the perceived
latency of a cold start request. Enabled by default when unspecified on new
services. Use `--cpu-boost` to enable and `--no-cpu-boost`
to disable.

**--[no-]cpu-throttling**:
Whether to throttle the CPU when the container is not actively serving requests.
Use `--cpu-throttling` to enable and `--no-cpu-throttling`
to disable.

**--description**:
Provides an optional, human-readable description of the service.

**--execution-environment**:
Selects the execution environment where the application will run.
`EXECUTION_ENVIRONMENT` must be one of:

**`gen1`**:
Run the application in a first generation execution environment.

**`gen2`**:
Run the application in a second generation execution environment.

**--gpu-type**:
The GPU type to use.

**--[no-]gpu-zonal-redundancy**:
Set GPU zonal redundancy. Use `--gpu-zonal-redundancy` to enable and
`--no-gpu-zonal-redundancy` to disable.

**--ingress**:
Set the ingress traffic sources allowed to call the service. For Cloud Run the
`--[no-]allow-unauthenticated` flag separately controls the
identities allowed to call the service. `INGRESS` must be
one of:

**`all`**:
Inbound requests from all sources are allowed.

**`internal`**:
For Cloud Run, only inbound requests from VPC networks in the same project or
VPC Service Controls perimeter, as well as Pub/Sub subscriptions and Eventarc
events in the same project or VPC Service Controls perimeter are allowed. All
other requests are rejected. See [https://cloud.google.com/run/docs/securing/ingress](https://cloud.google.com/run/docs/securing/ingress)
for full details on the definition of internal traffic for Cloud Run.

**`internal-and-cloud-load-balancing`**:
Only inbound requests from Google Cloud Load Balancing or a traffic source
allowed by the internal option are allowed.

**--[no-]invoker-iam-check**:
Optionally disable invoker IAM checks. This feature is available by invitation
only. More info at [https://cloud.google.com/run/docs/securing/managing-access#invoker_check](https://cloud.google.com/run/docs/securing/managing-access#invoker_check).
Use `--invoker-iam-check` to enable and
`--no-invoker-iam-check` to disable.

**--max-instances**:
The maximum number of container instances for this Revision to run or 'default'
to remove. This setting is immutably set on each new Revision and modifying its
value will deploy another Revision.

**--min**:
The minimum number of container instances to run for this Service or 'default'
to remove. These instances will be divided among all Revisions receiving a
percentage of traffic and can be modified without deploying a new Revision.

**--min-instances**:
The minimum number of container instances to run for this Revision or 'default'
to remove. This setting is immutably set on each new Revision and modifying its
value will deploy a another Revision. Consider using --min to set the minimum
number of instances across all revisions of the Service which may be modified
dynamically.

**--region**:
Region in which the resource can be found. Alternatively, set the property
[run/region].

**--remove-containers**:
List of containers to remove.

**--revision-suffix**:
Specify the suffix of the revision name. Revision names always start with the
service name automatically. For example, specifying [--revision-suffix=v1] for a
service named 'helloworld', would lead to a revision named 'helloworld-v1'. Set
empty string to clear the suffix and resume server-assigned naming.

**--service-account**:
the email address of an IAM service account associated with the revision of the
service. The service account represents the identity of the running revision,
and determines what permissions the revision has.

**--[no-]session-affinity**:
Whether to enable session affinity for connections to the service. Use
`--session-affinity` to enable and `--no-session-affinity`
to disable.

**--tag**:
Traffic tag to assign to the newly created revision.

**--timeout**:
Set the maximum request execution time (timeout). It is specified as a duration;
for example, "10m5s" is ten minutes, and five seconds. If you don't specify a
unit, seconds is assumed. For example, "10" is 10 seconds.

**--no-traffic**:
True to avoid sending traffic to the revision being deployed. Setting this flag
assigns any traffic assigned to the LATEST revision to the specific revision
bound to LATEST before the deployment. The effect is that the revision being
deployed will not receive traffic.
After a deployment with this flag the LATEST revision will not receive traffic
on future deployments. To restore sending traffic to the LATEST revision by
default, run the `[gcloud run services
update-traffic](https://cloud.google.com/sdk/gcloud/reference/run/services/update-traffic)` command with `--to-latest`.

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

**--add-cloudsql-instances**

**--add-custom-audiences**

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
The following flags apply to a single container. If the --container flag is
specified these flags may only be specified after a --container flag. Otherwise
they will apply to the primary ingress container.

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

**--[no-]automatic-updates**:
Indicates whether automatic base image updates should be enabled for an image
built from source. Use `--automatic-updates` to enable and
`--no-automatic-updates` to disable.

**--clear-volume-mounts**:
Remove all existing mounts from the current container.

**--cpu**:
Set a CPU limit in Kubernetes cpu units.
Cloud Run supports values fractional values below 1, 1, 2, 4, and 8. Some CPU
values requires a minimum Memory `--memory` value.

**--depends-on**:
List of container dependencies to add to the current container.

**--gpu**:
Cloud Run supports values 0 or 1. 1 gpu also requires a minimum 4
`--cpu` value and a minimum 8Gi `--memory` value.

**--liveness-probe**:
Comma separated settings for liveness probe in the form KEY=VALUE. Each key
stands for a field of the probe described in [https://cloud.google.com/run/docs/reference/rest/v1/Container#Probe](https://cloud.google.com/run/docs/reference/rest/v1/Container#Probe).
Currently supported keys are: initialDelaySeconds, timeoutSeconds,
periodSeconds, failureThreshold, httpGet.port, httpGet.path, grpc.port,
grpc.service.
For example, to set a probe with 10s timeout and HTTP probe requests sent to
8080 port of the container:

```
--liveness-probe=timeoutSeconds=10,httpGet.port=8080
```

To remove existing probe:

```
--liveness-probe=""
```

**--memory**:
Set a memory limit. Ex: 1024Mi, 4Gi.

**--port**:
Container port to receive requests at. Also sets the $PORT environment variable.
Must be a number between 1 and 65535, inclusive. To unset this field, pass the
special value "default". If updating an existing service with a TCP startup
probe pointing to the previous container port, this will also update the probe
port.

**--remove-volume-mount**:
Removes the volume mounted at the specified path from the current container.

**--startup-probe**:
Comma separated settings for startup probe in the form KEY=VALUE. Each key
stands for a field of the probe described in [https://cloud.google.com/run/docs/reference/rest/v1/Container#Probe](https://cloud.google.com/run/docs/reference/rest/v1/Container#Probe).
Currently supported keys are: initialDelaySeconds, timeoutSeconds,
periodSeconds, failureThreshold, httpGet.port, httpGet.path, grpc.port,
grpc.service, tcpSocket.port.
For example, to set a probe with 10s timeout and HTTP probe requests sent to
8080 port of the container:

```
--startup-probe=timeoutSeconds=10,httpGet.port=8080
```

To remove existing probe:

```
--startup-probe=""
```

**--[no-]use-http2**:
Whether to use HTTP/2 for connections to the service. Use
`--use-http2` to enable and `--no-use-http2` to disable.

**--base-image**

**--build-env-vars-file**

**--build-service-account**

**--build-worker-pool**

**--clear-env-vars**

**--clear-secrets**

**--command**

**--image**:
Name of the container image to deploy (e.g.
`us-docker.pkg.dev/cloudrun/container/hello:latest`). When used with
--source, the image must be the URI of an Artifact Registry Docker repository in
the Docker format ($REGION-docker.pkg.dev/$PROJECT/$REPOSITORY") or
($REGION-docker.pkg.dev/$PROJECT/$REPOSITORY/$IMAGE_NAME"). The image name must
be the same as the name of the service.

**--source**:
The location of the source to build. If a Dockerfile is present in the source
code directory, it will be built using that Dockerfile, otherwise it will use
Google Cloud buildpacks. See [https://cloud.google.com/run/docs/deploying-source-code](https://cloud.google.com/run/docs/deploying-source-code)
for more details. The location can be a directory on a local disk or a gzipped
archive file (.tar.gz) in Google Cloud Storage. If the source is a local
directory, this command skips the files specified in the
`--ignore-file`. If `--ignore-file` is not specified, use
`.gcloudignore` file. If a `.gcloudignore` file is absent
and a `.gitignore` file is present in the local source directory,
gcloud will use a generated Git-compatible `.gcloudignore` file that
respects your .gitignored files. The global `.gitignore` is not
respected. For more information on `.gcloudignore`, see `[gcloud topic
gcloudignore](https://cloud.google.com/sdk/gcloud/reference/topic/gcloudignore)`.

**--binary-authorization**

**--clear-encryption-key-shutdown-hours**

**--clear-key**

**--clear-labels**

**--labels**

**--clear-network**

**--clear-post-key-revocation-action-type**

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
gcloud alpha run deploy
```

```
gcloud beta run deploy
```