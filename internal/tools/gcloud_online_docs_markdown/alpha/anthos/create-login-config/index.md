# gcloud alpha anthos create-login-config  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/create-login-config](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/create-login-config)*

**NAME**

: **gcloud alpha anthos create-login-config - generates a login configuration file**

**SYNOPSIS**

: **`gcloud alpha anthos create-login-config` `[--kubeconfig](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/create-login-config#--kubeconfig)`=`KUBECONFIG` [`[--merge-from](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/create-login-config#--merge-from)`=`MERGE_FROM`] [`[--output](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/create-login-config#--output)`=`OUTPUT`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/anthos/create-login-config#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Generates the file containing configuration information
developers will use to authenticate to an AWS Anthos cluster.

**EXAMPLES**

: To generate the default login config file (kubectl-anthos-config.yaml) using the
kubeconfig file 'my-kube-config.yaml':

```
gcloud alpha anthos create-login-config --kubeconfig 'my-kube-config.yaml'
```

To generate a config named 'myconfg.yaml' the --kubeconfig file
'my-kube-config.yaml':

```
gcloud alpha anthos create-login-config --kubeconfig 'my-kube-config.yaml' --output 'myconfg.yaml'
```

**REQUIRED FLAGS**

: **--kubeconfig**:
Specifies the input kubeconfig file to access user cluster for login
configuration data.

**OPTIONAL FLAGS**

: **--merge-from**:
Specifies the file path of an existing login configuration file to merge with.

**--output**:
Destination to write login configuration file. Defaults to
"kubectl-anthos-config.yaml".

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

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud anthos create-login-config
```

```
gcloud beta anthos create-login-config
```