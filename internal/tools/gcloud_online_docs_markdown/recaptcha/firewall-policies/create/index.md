# gcloud recaptcha firewall-policies create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/recaptcha/firewall-policies/create](https://cloud.google.com/sdk/gcloud/reference/recaptcha/firewall-policies/create)*

**NAME**

: **gcloud recaptcha firewall-policies create - create a Firewall Policy**

**SYNOPSIS**

: **`gcloud recaptcha firewall-policies create` [`[--actions](https://cloud.google.com/sdk/gcloud/reference/recaptcha/firewall-policies/create#--actions)`=`ACTIONS`] [`[--condition](https://cloud.google.com/sdk/gcloud/reference/recaptcha/firewall-policies/create#--condition)`=`CONDITION`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/recaptcha/firewall-policies/create#--description)`=`DESCRIPTION`] [`[--path](https://cloud.google.com/sdk/gcloud/reference/recaptcha/firewall-policies/create#--path)`=`PATH`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/recaptcha/firewall-policies/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a reCAPTCHA Firewall Policy.

**EXAMPLES**

: To create a new reCAPTCHA firewall policy covering the path "/login/`" for
all requests with a reCAPTCHA Lite score of >= 0.5 to allow the requests and
set the header 'foo' to the value 'bar':

```
gcloud recaptcha firewall-policies create --path='/login/*' --condition='recaptcha.assessment_type == AssessmentType.LITE
&& recaptcha.score >= 0.5' --actions=allow,set_header=foo=bar
````

**FLAGS**

: **--actions**:
The actions that the caller should take regarding the user. There should be at
most 1 terminal action. A terminal action is any action that forces a response,
such as Allow, Block or Substitute. If it makes sense for it to happen multple
times, such as SetHeader, the action is non-terminal.
Examples:

- Block and set the header with key foo to value bar

- --actions=block,set_header=foo=bar
- Substitute with path google.com and set two headers, one with key key1 to value
value1 and one with key key2 to value value2

- --actions=substitute=google.com,set_header=key1=value1,set_header=key2=value2

**--condition**:
A CEL (Common Expression Language) conditional expression that specifies if this
policy applies to an incoming user request. If this condition evaluates to true
and the requested path matched the path pattern, the associated actions should
be executed by the caller. The condition string is checked for CEL syntax
correctness on creation. For more information, see the CEL spec: [https://github.com/google/cel-spec](https://github.com/google/cel-spec)
and its language definition: [https://github.com/google/cel-spec/blob/master/doc/langdef.md](https://github.com/google/cel-spec/blob/master/doc/langdef.md)

**--description**:
A description of what this policy aims to achieve, for convenience purposes. The
description can at most include 256 UTF-8 characters.

**--path**:
The path for which this policy applies, specified as a glob pattern. For more
information on glob, see the manual page: [https://man7.org/linux/man-pages/man7/glob.7.html](https://man7.org/linux/man-pages/man7/glob.7.html).

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

: This command uses the `recaptchaenterprise/v1` API. The full
documentation for this API can be found at: [https://cloud.google.com/recaptcha-enterprise/](https://cloud.google.com/recaptcha-enterprise/)

**NOTES**

: This variant is also available:

```
gcloud alpha recaptcha firewall-policies create
```