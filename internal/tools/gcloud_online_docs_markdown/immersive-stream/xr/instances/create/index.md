# gcloud immersive-stream xr instances create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/instances/create](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/instances/create)*

**NAME**

: **gcloud immersive-stream xr instances create - create an Immersive Stream for XR service instance**

**SYNOPSIS**

: **`gcloud immersive-stream xr instances create` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/instances/create#INSTANCE)` `[--add-region](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/instances/create#--add-region)`=[`autoscaling_buffer`=`AUTOSCALING_BUFFER`],[`autoscaling_min_capacity`=`AUTOSCALING_MIN_CAPACITY`],[`capacity`=`CAPACITY`],[`enable_autoscaling`=`ENABLE_AUTOSCALING`],[`region`=`REGION`] `[--version](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/instances/create#--version)`=`VERSION` (`[--content](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/instances/create#--content)`=`CONTENT` : `[--location](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/instances/create#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/instances/create#--async)`] [`[--fallback-url](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/instances/create#--fallback-url)`=`FALLBACK_URL`] [`[--gpu-class](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/instances/create#--gpu-class)`=`GPU_CLASS`] [`[--mode](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/instances/create#--mode)`=`MODE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/instances/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create an Immersive Stream for XR service instance.

**EXAMPLES**

: To create a service instance called `my-instance` serving content
`my-content` with version `my-version` that has
availablilty for 2 concurent sessions in us-west1 region and 3 concurrent
sessions in us-east4 region, run:

```
gcloud immersive-stream xr instances create my-instance --content=my-content --version=my-version --add-region=region=us-west1,capacity=2 --add-region=region=us-east4,capacity=3
```

Optionally, a fallback url may be specified. Users will be redirected to this
fallback url when the service instance is unable to provide the streaming
experience. To create a service instance called `my-instance` serving
content `my-content` with version `my-version` that has
availablilty for 2 concurent sessions in us-west1 and uses fallback url
`https://www.google.com` run:

```
gcloud immersive-stream xr instances create my-instance --content=my-content --version=my-version --add-region=region=us-west1,capacity=2 --fallback-url="https://www.google.com"
```

```
By default, the instance is created with mode=ar, which supports both
3D and AR experiences. Instances can also be configured to use
3D-only mode. This configuration cannot be updated later.
To use 3D-only mode, include:
```

```
--mode=3d
```

```
By default, the instance is created with gpu-class=t4. This uses the
NVIDIA T4 GPU for the instance. Instances can also be configured to
use NVIDIA L4 GPUs at creation. Note that only certain regions are
available for L4, and only 3D-only mode is supported. This
configuration cannot be updated later.
To use NVIDIA L4 GPU for the instance, include:
```

```
--gpu-class=l4
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE`**:
Name of the instance to be created

**REQUIRED FLAGS**

: **--add-region**:
Flag used to specify region and capacity required for the service instance's
availability.

```
'region' is the region in which the instance is deployed.
```

```
'capacity' is the maxium number of concurrent streaming sessions that the instance can support in the given region.
```

This is a repeatable flag.

**--version**:
Build version tag of the content served by this instance

**Content resource - Immersive Stream for XR content resource served by the
instance. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `--content` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**--content**:
ID of the content or fully qualified identifier for the content.
To set the `name` attribute:

- provide the argument `--content` on the command line.

This flag argument must be specified if any of the other arguments in this group
are specified.

**--location**:
Google Cloud location for the content.
To set the `location` attribute:

- provide the argument `--content` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- location is always global.**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--fallback-url**:
Fallback url to redirect users to when this service instance is unable to
provide the streaming experience

**--gpu-class**:
The class of GPU that is used by this service instance

**--mode**:
The rendering mode that is supported by this service instance

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
gcloud alpha immersive-stream xr instances create
```