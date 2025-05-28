# gcloud transfer agents install  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/transfer/agents/install](https://cloud.google.com/sdk/gcloud/reference/transfer/agents/install)*

**NAME**

: **gcloud transfer agents install - install Transfer Service agents**

**SYNOPSIS**

: **`gcloud transfer agents install` `[--pool](https://cloud.google.com/sdk/gcloud/reference/transfer/agents/install#--pool)`=`POOL` [`[--count](https://cloud.google.com/sdk/gcloud/reference/transfer/agents/install#--count)`=`COUNT`] [`[--creds-file](https://cloud.google.com/sdk/gcloud/reference/transfer/agents/install#--creds-file)`=`CREDS_FILE`] [`[--docker-network](https://cloud.google.com/sdk/gcloud/reference/transfer/agents/install#--docker-network)`=`NETWORK`] [`[--[no-]enable-multipart](https://cloud.google.com/sdk/gcloud/reference/transfer/agents/install#--[no-]enable-multipart)`] [`[--id-prefix](https://cloud.google.com/sdk/gcloud/reference/transfer/agents/install#--id-prefix)`=`ID_PREFIX`] [`[--logs-directory](https://cloud.google.com/sdk/gcloud/reference/transfer/agents/install#--logs-directory)`=`LOGS_DIRECTORY`; default="/tmp"] [`[--memlock-limit](https://cloud.google.com/sdk/gcloud/reference/transfer/agents/install#--memlock-limit)`=`MEMLOCK_LIMIT`; default=64000000] [`[--mount-directories](https://cloud.google.com/sdk/gcloud/reference/transfer/agents/install#--mount-directories)`=[`MOUNT-DIRECTORIES`,…]] [`[--proxy](https://cloud.google.com/sdk/gcloud/reference/transfer/agents/install#--proxy)`=`PROXY`] [`[--s3-compatible-mode](https://cloud.google.com/sdk/gcloud/reference/transfer/agents/install#--s3-compatible-mode)`] [`[--hdfs-namenode-uri](https://cloud.google.com/sdk/gcloud/reference/transfer/agents/install#--hdfs-namenode-uri)`=`HDFS_NAMENODE_URI` `[--hdfs-username](https://cloud.google.com/sdk/gcloud/reference/transfer/agents/install#--hdfs-username)`=`HDFS_USERNAME` `[--hdfs-data-transfer-protection](https://cloud.google.com/sdk/gcloud/reference/transfer/agents/install#--hdfs-data-transfer-protection)`=`HDFS_DATA_TRANSFER_PROTECTION`] [`[--kerberos-config-file](https://cloud.google.com/sdk/gcloud/reference/transfer/agents/install#--kerberos-config-file)`=`KERBEROS_CONFIG_FILE` `[--kerberos-keytab-file](https://cloud.google.com/sdk/gcloud/reference/transfer/agents/install#--kerberos-keytab-file)`=`KERBEROS_KEYTAB_FILE` `[--kerberos-user-principal](https://cloud.google.com/sdk/gcloud/reference/transfer/agents/install#--kerberos-user-principal)`=`KERBEROS_USER_PRINCIPAL` `[--kerberos-service-principal](https://cloud.google.com/sdk/gcloud/reference/transfer/agents/install#--kerberos-service-principal)`=`KERBEROS_SERVICE_PRINCIPAL`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/transfer/agents/install#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Install Transfer Service agents to enable you to transfer data to or from POSIX
filesystems, such as on-premises filesystems. Agents are installed locally on
your machine and run inside Docker containers.

**EXAMPLES**

: To create an agent pool for your agent, see the `[gcloud transfer
agent-pools create](https://cloud.google.com/sdk/gcloud/reference/transfer/agent-pools/create)` command.
To install an agent that authenticates with your user account credentials and
has default agent parameters, run:

```
gcloud transfer agents install --pool=AGENT_POOL
```

You will be prompted to run a command to generate a credentials file if one does
not already exist.
To install an agent that authenticates with a service account with credentials
stored at '/example/path.json', run:

```
gcloud transfer agents install --creds-file=/example/path.json --pool=AGENT_POOL
```

**REQUIRED FLAGS**

: **--pool**:
The agent pool to associate with the newly installed agent. When creating
transfer jobs, the agent pool parameter will determine which agents are
activated.

**FLAGS**

: **--count**:
Specify the number of agents to install on your current machine. System
requirements: 8 GB of memory and 4 CPUs per agent.
Note: If the 'id-prefix' flag is specified, Transfer Service increments a number
value after each prefix. Example: prefix1, prefix2, etc.

**--creds-file**:
Specify the path to the service account's credentials file.
No input required if authenticating with your user account credentials, which
Transfer Service will look for in your system.
Note that the credentials location will be mounted to the agent container.

**--docker-network**:
Specify the network to connect the container to. This flag maps directly to the
`--network` flag in the underlying 'docker run' command.
If binding directly to the host's network is an option, then setting this value
to 'host' can dramatically improve transfer performance.

**--[no-]enable-multipart**:
Split up files and transfer the resulting chunks in parallel before merging them
at the destination. Can be used make transfers of large files faster as long as
the network and disk speed are not limiting factors. If unset, agent decides
when to use the feature. Use `--enable-multipart` to enable and
`--no-enable-multipart` to disable.

**--id-prefix**:
An optional prefix to add to the agent ID to help identify the agent.

**--logs-directory**:
Specify the absolute path to the directory you want to store transfer logs in.
If not specified, gcloud transfer will mount your /tmp directory for logs.

**--memlock-limit**:
Set the agent container's memlock limit. A value of 64000000 (default) or higher
is required to ensure that agent versions 1.14 or later have enough locked
memory to be able to start.

**--mount-directories**:
If you want to grant agents access to specific parts of your filesystem instead
of the entire filesystem, specify which directory paths to mount to the agent
container. Multiple paths must be separated by commas with no spaces (e.g.,
--mount-directories=/system/path/to/dir1,/path/to/dir2). When mounting specific
directories, gcloud transfer will also mount a directory for logs (either /tmp
or what you've specified for --logs-directory) and your Google credentials file
for agent authentication.
It is strongly recommended that you use this flag. If this flag isn't specified,
gcloud transfer will mount your entire filesystem to the agent container and
give the agent root access.

**--proxy**:
Specify the HTTP URL and port of a proxy server if you want to use a forward
proxy. For example, to use the URL 'example.com' and port '8080' specify
'http://www.example.com:8080/'
Ensure that you specify the HTTP URL and not an HTTPS URL to avoid
double-wrapping requests in TLS encryption. Double-wrapped requests prevent the
proxy server from sending valid outbound requests.

**--s3-compatible-mode**:
Allow the agent to work with S3-compatible sources. This flag blocks the agent's
ability to work with other source types (e.g., file systems).
When using this flag, you must provide source credentials either as environment
variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`
or as default credentials in your system's configuration files.
To provide credentials as environment variables, run:

```
AWS_ACCESS_KEY_ID="id" AWS_SECRET_ACCESS_KEY="secret" gcloud transfer agents install --s3-compatible-mode
```

**HDFS FLAGS**

: **--hdfs-namenode-uri**:
A URI representing an HDFS cluster including a schema, namenode, and port.
Examples: "rpc://my-namenode:8020", "http://my-namenode:9870".
Use "http" or "https" for WebHDFS. If no schema is provided, the CLI assumes
native "rpc". If no port is provided, the default is 8020 for RPC, 9870 for
HTTP, and 9871 for HTTPS. For example, the input "my-namenode" becomes
"rpc://my-namenode:8020".

**--hdfs-username**:
Username for connecting to an HDFS cluster with simple auth.

**--hdfs-data-transfer-protection**:
Client-side quality of protection setting for Kerberized clusters. Client-side
QOP value cannot be more restrictive than the server-side QOP value.
`HDFS_DATA_TRANSFER_PROTECTION` must be one of:
`authentication`, `integrity`, `privacy`.

**Kerberos FLAGS**

: **--kerberos-config-file**:
Path to Kerberos config file.

**--kerberos-keytab-file**:
Path to a Keytab file containing the user principal specified with the
--kerberos-user-principal flag.

**--kerberos-user-principal**:
Kerberos user principal to use when connecting to an HDFS cluster via Kerberos
auth.

**--kerberos-service-principal**:
Kerberos service principal to use, of the form
"<primary>/<instance>". Realm is mapped from your Kerberos config.
Any supplied realm is ignored. If not passed in, it will default to
"hdfs/<namenode_fqdn>" (fqdn = fully qualified domain name).

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
gcloud alpha transfer agents install
```