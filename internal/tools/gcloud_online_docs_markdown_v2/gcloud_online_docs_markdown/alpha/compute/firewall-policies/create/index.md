# gcloud alpha compute firewall-policies create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/create](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/create)*

**NAME**

: **gcloud alpha compute firewall-policies create - create a Compute Engine organization firewall policy**

**SYNOPSIS**

: **`gcloud alpha compute firewall-policies create` `[--short-name](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/create#--short-name)`=`SHORT_NAME` (`[--folder](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/create#--folder)`=`FOLDER`     | `[--organization](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/create#--organization)`=`ORGANIZATION`) [`[--description](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/create#--description)`=`DESCRIPTION`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/compute/firewall-policies/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` `gcloud alpha compute firewall-policies create`
is used to create organization firewall policies. An organization firewall
policy is a set of rules that controls access to various resources.

**EXAMPLES**

: To create an organization firewall policy under folder with ID ``123456789",
run:

```
gcloud alpha compute firewall-policies create --short-name=my-policy --folder=123456789
```

**REQUIRED FLAGS**

: **--short-name**:
A textual name of the firewall policy. The name must be 1-63 characters long,
and comply with RFC 1035.

**--folder**

**OPTIONAL FLAGS**

: **--description**:
An optional, textual description for the organization security policy.

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

**IAM PERMISSIONS**

: To create rules to a firewall policy, the user must have the following
permission: ``compute.firewallPolicies.create`.
To find predefined roles that contain those permissions, see the [Compute Engine IAM
roles](https://cloud.google.com/compute/docs/access/iam).`

**NOTES**

: This command is currently in alpha and might change without notice. If this
command fails with API permission errors despite specifying the correct project,
you might be trying to access an API with an invitation-only early access
allowlist. These variants are also available:

```
gcloud compute firewall-policies create
```

```
gcloud beta compute firewall-policies create
```