# gcloud transfer agent-pools create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/create](https://cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/create)*

**NAME**

: **gcloud transfer agent-pools create - create a Transfer Service agent pool**

**SYNOPSIS**

: **`gcloud transfer agent-pools create` `[NAME](https://cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/create#NAME)` [`[--no-async](https://cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/create#--async)`] [`[--bandwidth-limit](https://cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/create#--bandwidth-limit)`=`BANDWIDTH_LIMIT`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/create#--display-name)`=`DISPLAY_NAME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create an agent pool -- a group of agents used to connect to a source or
destination filesystem.

**EXAMPLES**

: To create an agent pool with name 'my-pool', display name 'daily backups', and
no bandwidth limit, run:

```
gcloud transfer agent-pools create my-pool --display-name='daily backups'
```

To create an agent pool with name 'my-pool', display name 'daily backups', and a
bandwidth limit of 50 MB/s, run:

```
gcloud transfer agent-pools create my-pool --display-name="daily backups" --bandwidth-limit=50
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
A unique, permanent identifier for this pool.

**FLAGS**

: **--no-async**:
Block other tasks in your terminal until the pool has been created. If not
included, pool creation will run asynchronously.

**--bandwidth-limit**:
Set how much of your bandwidth to make available to this pool's agents. A
bandwidth limit applies to all agents in a pool and can help prevent the pool's
transfer workload from disrupting other operations that share your bandwidth.
For example, enter '50' to set a bandwidth limit of 50 MB/s. By leaving this
flag unspecified, this flag unspecified, this pool's agents will use all
bandwidth available to them.

**--display-name**:
A modifiable name to help you identify this pool. You can include details that
might not fit in the pool's unique full resource name.

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
gcloud alpha transfer agent-pools create
```