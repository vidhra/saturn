# gcloud transfer agents delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/transfer/agents/delete](https://cloud.google.com/sdk/gcloud/reference/transfer/agents/delete)*

**NAME**

: **gcloud transfer agents delete - delete Transfer Service transfer agents**

**SYNOPSIS**

: **`gcloud transfer agents delete` [`[--ids](https://cloud.google.com/sdk/gcloud/reference/transfer/agents/delete#--ids)`=[`IDS`,…]     | `[--all](https://cloud.google.com/sdk/gcloud/reference/transfer/agents/delete#--all)`     | `[--uninstall](https://cloud.google.com/sdk/gcloud/reference/transfer/agents/delete#--uninstall)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/transfer/agents/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete Transfer Service agents from your machine.

**EXAMPLES**

: If you plan to delete specific agents, you can list which agents are running on
your machine by running:

```
docker container list --all --filter ancestor=gcr.io/cloud-ingest/tsop-agent
```

Then run:

```
gcloud transfer agents delete --ids=id1,id2,…
```

**FLAGS**

: **--ids**

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
gcloud alpha transfer agents delete
```