# gcloud immersive-stream xr instances update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/instances/update](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/instances/update)*

**NAME**

: **gcloud immersive-stream xr instances update - update an Immersive Stream for XR service instance**

**SYNOPSIS**

: **`gcloud immersive-stream xr instances update` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/instances/update#INSTANCE)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/instances/update#--location)`=`LOCATION`) (`[--add-region](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/instances/update#--add-region)`=[`autoscaling_buffer`=`AUTOSCALING_BUFFER`],[`autoscaling_min_capacity`=`AUTOSCALING_MIN_CAPACITY`],[`capacity`=`CAPACITY`],[`enable_autoscaling`=`ENABLE_AUTOSCALING`],[`region`=`REGION`]     | `[--fallback-url](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/instances/update#--fallback-url)`=`FALLBACK_URL`     | `[--remove-region](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/instances/update#--remove-region)`=`REMOVE_REGION`     | `[--update-region](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/instances/update#--update-region)`=[`autoscaling_buffer`=`AUTOSCALING_BUFFER`],[`autoscaling_min_capacity`=`AUTOSCALING_MIN_CAPACITY`],[`capacity`=`CAPACITY`],[`enable_autoscaling`=`ENABLE_AUTOSCALING`],[`region`=`REGION`]     | `[--version](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/instances/update#--version)`=`VERSION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/instances/update#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/immersive-stream/xr/instances/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an Immersive Stream for XR service instance. This command can be used to
update one of the following:

- the capacity for an existing region of the service instance
- the content build version served by the instance
- the fallback url to redirect users to when the service instance is unable to
provide the streaming experience

If updating the capacity, only one region may be updated for each command
execution, and the new capacity may not be 0 or exceed the quota limit.

**EXAMPLES**

: To update the service instance `my-instance` to have capacity 2 for
an existing region us-west1, run:

```
gcloud immersive-stream xr instances update my-instance --update-region=region=us-west1,capacity=2
```

To update the service instance `my-instance` to have capacity 1 for a
new region us-east4, run:

```
gcloud immersive-stream xr instances update my-instance --add-region=region=us-east4,capacity=1
```

To update the service instance `my-instance` to remove the existing
region us-east4, run:

```
gcloud immersive-stream xr instances update my-instance --remove-region=us-east4
```

To update the service instance `my-instance` to serve content version
`my-version`, run:

```
gcloud immersive-stream xr instances update my-instance --version=my-version
```

To update the service instance `my-instance` to use fallback url
`https://www.google.com`, run:

```
gcloud immersive-stream xr instances update my-instance --fallback-url="https://www.google.com"
```

**POSITIONAL ARGUMENTS**

: **Instance resource - Immersive Stream for XR service instance to update. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INSTANCE`**:
ID of the instance or fully qualified identifier for the instance.
To set the `name` attribute:

- provide the argument `instance` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
Google Cloud location for the instance.
To set the `location` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- location is always global.**

**REQUIRED FLAGS**

: **--add-region**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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
gcloud alpha immersive-stream xr instances update
```