# gcloud memcache instances update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/memcache/instances/update](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/update)*

**NAME**

: **gcloud memcache instances update - update a Memorystore Memcached instance**

**SYNOPSIS**

: **`gcloud memcache instances update` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/update#INSTANCE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/update#--region)`=`REGION`) (`[--parameters](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/update#--parameters)`=`KEY`=`VALUE`     | `[--display-name](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/update#--display-name)`=`DISPLAY_NAME` `[--labels](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/update#--labels)`=[`KEY`=`VALUE`,…] `[--node-count](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/update#--node-count)`=`NODE_COUNT` `[--maintenance-window-any](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/update#--maintenance-window-any)`     | `[--maintenance-window-day](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/update#--maintenance-window-day)`=`MAINTENANCE_WINDOW_DAY` `[--maintenance-window-duration](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/update#--maintenance-window-duration)`=`MAINTENANCE_WINDOW_DURATION` `[--maintenance-window-start-time](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/update#--maintenance-window-start-time)`=`MAINTENANCE_WINDOW_START_TIME`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/update#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/memcache/instances/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update a Memcached instance with one or more of the following actions:

- Scale up or down the number of nodes in the instance.
- Stage an update to instance configuration parameters.
- Update the instance metadata (display name, labels).

Updating parameters cannot be combined with any other update actions in the same
call. All other update actions can be combined in the same call.

**EXAMPLES**

: To scale a Memcached instance named 'my-memcache-instance' in region
'us-central1' to have 3 nodes, run:

```
gcloud memcache instances update my-memcache-instance --node-count=3 --region=us-central1
```

To stage an update to the parameters 'protocol' and 'track-sizes' for a
Memcached instance named 'my-memcache-instance' in region 'us-central1', run:

```
gcloud memcache instances update my-memcache-instance --parameters="protocol=ascii,track-sizes=true" --region=us-central1
```

To update a Memcached instance named 'my-memcache-instance' in region
'us-central1' to have the display name "Foo Cache Service" and the labels 'env'
and 'service', run:

```
gcloud memcache instances update my-memcache-instance --display-name="Foo Cache Service" --labels="env=test,service=foo"
```

**POSITIONAL ARGUMENTS**

: **Instance resource - Arguments and flags that specify the Memcached instance to
update. The arguments in this group can be used to specify the attributes of
this resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INSTANCE`**:
ID of the instance or fully qualified identifier for the instance.
To set the `instance` attribute:

- provide the argument `instance` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The name of the Memcached region of the instance. Overrides the default
memcache/region property value for this command invocation.
To set the `region` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `memcache/region`.**

**REQUIRED FLAGS**

: **--parameters**

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

**API REFERENCE**

: This command uses the `memcache/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/memorystore/](https://cloud.google.com/memorystore/)

**NOTES**

: These variants are also available:

```
gcloud alpha memcache instances update
```

```
gcloud beta memcache instances update
```