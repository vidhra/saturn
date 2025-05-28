# gcloud transfer agent-pools list  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/list](https://cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/list)*

**NAME**

: **gcloud transfer agent-pools list - list Transfer Service transfer agent pools**

**SYNOPSIS**

: **`gcloud transfer agent-pools list` [`[--limit](https://cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/list#--limit)`=`LIMIT`] [`[--names](https://cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/list#--names)`=[`NAMES`,…]] [`[--page-size](https://cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/list#--page-size)`=`PAGE_SIZE`; default=256] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/list#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: List Transfer Service transfer pools in a given project to show their
configurations.

**EXAMPLES**

: To list all agent pools in your current project, run:

```
gcloud transfer agent-pools list
```

To list agent pools named "foo" and "bar" in your project, run:

```
gcloud transfer agent-pools list --names=foo,bar
```

To list all information about jobs 'foo' and 'bar' formatted as JSON, run:

```
gcloud transfer agent-pools list --names=foo,bar --format=json
```

**FLAGS**

: **--limit**:
Return the first items from the API up to this limit.

**--names**:
The names of the agent pools you want to list. Separate multiple names with
commas (e.g., --name=foo,bar). If not specified, all agent pools in your current
project will be listed.

**--page-size**:
Retrieve batches of this many items from the API.

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
gcloud alpha transfer agent-pools list
```