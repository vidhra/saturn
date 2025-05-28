# gcloud transfer agent-pools update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/update](https://cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/update)*

**NAME**

: **gcloud transfer agent-pools update - update a Transfer Service agent pool**

**SYNOPSIS**

: **`gcloud transfer agent-pools update` `[NAME](https://cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/update#NAME)` [`[--bandwidth-limit](https://cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/update#--bandwidth-limit)`=`BANDWIDTH_LIMIT`] [`[--clear-bandwidth-limit](https://cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/update#--clear-bandwidth-limit)`] [`[--clear-display-name](https://cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/update#--clear-display-name)`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/update#--display-name)`=`DISPLAY_NAME`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Update an agent pool.

**EXAMPLES**

: To remove the bandwidth limit for agent pool 'foo', run:

```
gcloud transfer agent-pools update foo --clear-bandwidth-limit
```

To remove the display name for agent pool 'foo', run:

```
gcloud transfer agent-pools update foo --clear-display-name
```

To update the bandwidth limit for agent pool 'foo' to 100 MB/s, run:

```
gcloud transfer agent-pools update foo --bandwidth-limit=100
```

To update the display name for agent pool 'foo' to 'example name', run:

```
gcloud transfer agent-pools update foo --display-name="example name"
```

**POSITIONAL ARGUMENTS**

: **`NAME`**:
A unique, permanent identifier for this pool.

**FLAGS**

: **--bandwidth-limit**:
Set how much of your bandwidth to make available to this pool's agents. A
bandwidth limit applies to all agents in a pool and can help prevent the pool's
transfer workload from disrupting other operations that share your bandwidth.
For example, enter '50' to set a bandwidth limit of 50 MB/s. By leaving this
flag unspecified, this flag unspecified, this pool's agents will use all
bandwidth available to them.

**--clear-bandwidth-limit**:
Remove the agent pool's bandwidth limit, which enables the pool's agents to use
all bandwidth available to them.

**--clear-display-name**:
Remove the display name from the agent pool.

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
gcloud alpha transfer agent-pools update
```