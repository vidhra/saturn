# gcloud anthos auth login  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/anthos/auth/login](https://cloud.google.com/sdk/gcloud/reference/anthos/auth/login)*

**NAME**

: **gcloud anthos auth login - authenticate clusters using the Anthos client**

**SYNOPSIS**

: **`gcloud anthos auth login` [`[--no-browser](https://cloud.google.com/sdk/gcloud/reference/anthos/auth/login#--browser)`] [`[--cluster](https://cloud.google.com/sdk/gcloud/reference/anthos/auth/login#--cluster)`=`CLUSTER`] [`[--dry-run](https://cloud.google.com/sdk/gcloud/reference/anthos/auth/login#--dry-run)`] [`[--kubeconfig](https://cloud.google.com/sdk/gcloud/reference/anthos/auth/login#--kubeconfig)`=`KUBECONFIG`] [`[--login-config](https://cloud.google.com/sdk/gcloud/reference/anthos/auth/login#--login-config)`=`LOGIN_CONFIG`] [`[--login-config-cert](https://cloud.google.com/sdk/gcloud/reference/anthos/auth/login#--login-config-cert)`=`LOGIN_CONFIG_CERT`] [`[--remote-bootstrap](https://cloud.google.com/sdk/gcloud/reference/anthos/auth/login#--remote-bootstrap)`=`REMOTE_BOOTSTRAP`] [`[--server](https://cloud.google.com/sdk/gcloud/reference/anthos/auth/login#--server)`=`SERVER`] [`[--set-preferred-auth](https://cloud.google.com/sdk/gcloud/reference/anthos/auth/login#--set-preferred-auth)`] [`[--user](https://cloud.google.com/sdk/gcloud/reference/anthos/auth/login#--user)`=`USER`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/anthos/auth/login#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Authenticate clusters using the Anthos client.

**EXAMPLES**

: To add credentials to default kubeconfig file:

```
gcloud anthos auth login --cluster=testcluster --login-config=kubectl-anthos-config.yaml
```

To add credentials to custom kubeconfig file:

```
gcloud anthos auth login --cluster=testcluster --login-config=kubectl-anthos-config.yaml --kubeconfig=my.kubeconfig
```

To generate the commands without executing them:

```
gcloud anthos auth login --cluster=testcluster --login-config=kubectl-anthos-config.yaml --dry-run
```

To add credentials to default kubeconfig file using server side login:

```
gcloud anthos auth login --cluster=testcluster --server=<server-url>
```

To add credentials to custom kubeconfig file using server side login:

```
gcloud anthos auth login --cluster=testcluster --server=<server-url> --kubeconfig=my.kubeconfig
```

To add credentials to custom kubeconfig file with server side login using a
remote-device for login:

```
gcloud anthos auth login --cluster=testcluster --server=<server-url> --kubeconfig=my.kubeconfig --no-browser
```

**FLAGS**

: **--no-browser**:
Option to indicate login completion on a second device with browser.Used with
`server` option.

**--cluster**:
Cluster to authenticate against. If no cluster is specified, the command will
print a list of available options.

**--dry-run**:
Print out the generated kubectl commands but do not execute them.

**--kubeconfig**:
Specifies the destination kubeconfig file where credentials will be stored.

**--login-config**:
Specifies the configuration yaml file for login. Can be a file path or a URL.

**--login-config-cert**:
Specifies the CA certificate file to be added to trusted pool for making HTTPS
connections to a `--login-config` URL.

**--remote-bootstrap**:
Option to complete login that was started using `no-browser` optionon
a remote device that does not have a browser.

**--server**:
Specifies the URL of API server of the cluster to authenticate against.

**--set-preferred-auth**:
If set, forces update of preferred authentication for given cluster

**--user**:
If configuring multiple user accounts in the same kubecconfig file, you can
specify a user to differentiate between them.

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
gcloud alpha anthos auth login
```

```
gcloud beta anthos auth login
```