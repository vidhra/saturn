# gcloud compute security-policies rules create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create)*

**NAME**

: **gcloud compute security-policies rules create - create a Compute Engine security policy rule**

**SYNOPSIS**

: **`gcloud compute security-policies rules create` `[PRIORITY](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#PRIORITY)` `[--action](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--action)`=`ACTION` (`[--expression](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--expression)`=`EXPRESSION` `[--network-dest-ip-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--network-dest-ip-ranges)`=[`DEST_IP_RANGE`,…] `[--network-dest-ports](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--network-dest-ports)`=[`DEST_PORT`,…] `[--network-ip-protocols](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--network-ip-protocols)`=[`IP_PROTOCOL`,…] `[--network-src-asns](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--network-src-asns)`=[`SRC_ASN`,…] `[--network-src-ip-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--network-src-ip-ranges)`=[`SRC_IP_RANGE`,…] `[--network-src-ports](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--network-src-ports)`=[`SRC_PORT`,…] `[--network-src-region-codes](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--network-src-region-codes)`=[`SRC_REGION_CODE`,…] `[--network-user-defined-fields](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--network-user-defined-fields)`=[`NAME`;`[VALUE](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#VALUE)`:`[VALUE](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#VALUE)`:…,…] `[--src-ip-ranges](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--src-ip-ranges)`=[`SRC_IP_RANGE`,…]) [`[--ban-duration-sec](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--ban-duration-sec)`=`BAN_DURATION_SEC`] [`[--ban-threshold-count](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--ban-threshold-count)`=`BAN_THRESHOLD_COUNT`] [`[--ban-threshold-interval-sec](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--ban-threshold-interval-sec)`=`BAN_THRESHOLD_INTERVAL_SEC`] [`[--conform-action](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--conform-action)`=`CONFORM_ACTION`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--description)`=`DESCRIPTION`] [`[--enforce-on-key](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--enforce-on-key)`=`ENFORCE_ON_KEY`] [`[--enforce-on-key-configs](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--enforce-on-key-configs)`=[[`all`],[`ip`],[`xff-ip`],[`http-cookie`=`HTTP_COOKIE`],[`http-header`=`HTTP_HEADER`],[`http-path`],[`sni`],[`region-code`],[`tls-ja3-fingerprint`],[`user-ip`],[`tls-ja4-fingerprint`]],[…]] [`[--enforce-on-key-name](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--enforce-on-key-name)`=`ENFORCE_ON_KEY_NAME`] [`[--exceed-action](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--exceed-action)`=`EXCEED_ACTION`] [`[--exceed-redirect-target](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--exceed-redirect-target)`=`EXCEED_REDIRECT_TARGET`] [`[--exceed-redirect-type](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--exceed-redirect-type)`=`EXCEED_REDIRECT_TYPE`] [`[--preview](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--preview)`] [`[--rate-limit-threshold-count](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--rate-limit-threshold-count)`=`RATE_LIMIT_THRESHOLD_COUNT`] [`[--rate-limit-threshold-interval-sec](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--rate-limit-threshold-interval-sec)`=`RATE_LIMIT_THRESHOLD_INTERVAL_SEC`] [`[--recaptcha-action-site-keys](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--recaptcha-action-site-keys)`=[`SITE_KEY`,…]] [`[--recaptcha-session-site-keys](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--recaptcha-session-site-keys)`=[`SITE_KEY`,…]] [`[--redirect-target](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--redirect-target)`=`REDIRECT_TARGET`] [`[--redirect-type](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--redirect-type)`=`REDIRECT_TYPE`] [`[--region](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--region)`=`REGION`] [`[--request-headers-to-add](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--request-headers-to-add)`=[`REQUEST_HEADERS_TO_ADD`,…]] [`[--security-policy](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#--security-policy)`=`SECURITY_POLICY`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/security-policies/rules/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `gcloud compute security-policies rules create` is used to create
security policy rules.

**EXAMPLES**

: To create a rule at priority 1000 to block the IP range 1.2.3.0/24, run:

```
gcloud compute security-policies rules create 1000 --action=deny-403 --security-policy=my-policy --description="block 1.2.3.0/24" --src-ip-ranges=1.2.3.0/24
```

**POSITIONAL ARGUMENTS**

: **`PRIORITY`**:
The priority of the rule to add. Rules are evaluated in order from highest
priority to lowest priority where 0 is the highest priority and 2147483647 is
the lowest priority.

**REQUIRED FLAGS**

: **--action**:
The action to take if the request matches the match condition.
`ACTION` must be one of:

**`allow`**:
Allows the request from HTTP(S) Load Balancing.

**`deny`**:
Denies the request from TCP/SSL Proxy and Network Load Balancing.

**`deny-403`**:
Denies the request from HTTP(S) Load Balancing, with an HTTP response status
code of 403.

**`deny-404`**:
Denies the request from HTTP(S) Load Balancing, with an HTTP response status
code of 404.

**`deny-502`**:
Denies the request from HTTP(S) Load Balancing, with an HTTP response status
code of 502.

**`rate-based-ban`**:
Enforces rate-based ban action from HTTP(S) Load Balancing, based on rate limit
options.

**`redirect`**:
Redirects the request from HTTP(S) Load Balancing, based on redirect options.

**`redirect-to-recaptcha`**:
(DEPRECATED) Redirects the request from HTTP(S) Load Balancing, for reCAPTCHA
Enterprise assessment. This flag choice is deprecated. Use --action=redirect and
--redirect-type=google-recaptcha instead.

**`throttle`**:
Enforces throttle action from HTTP(S) Load Balancing, based on rate limit
options.

**--expression**

**OPTIONAL FLAGS**

: **--ban-duration-sec**:
Can only be specified if the action for the rule is
``rate-based-ban``. If specified, determines
the time (in seconds) the traffic will continue to be banned by the rate limit
after the rate falls below the threshold.

**--ban-threshold-count**:
Number of HTTP(S) requests for calculating the threshold for banning requests.
Can only be specified if the action for the rule is
``rate-based-ban``. If specified, the key will
be banned for the configured
``BAN_DURATION_SEC`` when the number of
requests that exceed the
``RATE_LIMIT_THRESHOLD_COUNT`` also exceed this
``BAN_THRESHOLD_COUNT``.

**--ban-threshold-interval-sec**:
Interval over which the threshold for banning requests is computed. Can only be
specified if the action for the rule is
``rate-based-ban``. If specified, the key will
be banned for the configured
``BAN_DURATION_SEC`` when the number of
requests that exceed the
``RATE_LIMIT_THRESHOLD_COUNT`` also exceed this
``BAN_THRESHOLD_COUNT``.

**--conform-action**:
Action to take when requests are under the given threshold. When requests are
throttled, this is also the action for all requests which are not dropped.
`CONFORM_ACTION` must be (only one value is supported):
`allow`.

**--description**:
An optional, textual description for the rule.

**--enforce-on-key**:
Different key types available to enforce the rate limit threshold limit on:

- ``ip``: each client IP address has this limit
enforced separately
- ``all``: a single limit is applied to all
requests matching this rule
- ``http-header``: key type takes the value of
the HTTP header configured in enforce-on-key-name as the key value
- ``xff-ip``: takes the original IP address
specified in the X-Forwarded-For header as the key
- ``http-cookie``: key type takes the value of
the HTTP cookie configured in enforce-on-key-name as the key value
- ``http-path``: key type takes the value of the
URL path in the request
- ``sni``: key type takes the value of the server
name indication from the TLS session of the HTTPS request
- ``region-code``: key type takes the value of
the region code from which the request originates
- ``tls-ja3-fingerprint``: key type takes the
value of JA3 TLS/SSL fingerprint if the client connects using HTTPS, HTTP/2 or
HTTP/3
- ``user-ip``: key type takes the IP address of
the originating client, which is resolved based on user-ip-request-headers
configured with the security policy
- ``tls-ja4-fingerprint``: key type takes the
value of JA4 TLS/SSL fingerprint if the client connects using HTTPS, HTTP/2 or
HTTP/3

`ENFORCE_ON_KEY` must be one of: `ip`,
`all`, `http-header`, `xff-ip`,
`http-cookie`, `http-path`, `sni`,
`region-code`, `tls-ja3-fingerprint`,
`user-ip`, `tls-ja4-fingerprint`.

**--enforce-on-key-configs**:
Specify up to 3 key type/name pairs to rate limit. Valid key types are:

- ``ip``: each client IP address has this limit
enforced separately
- ``all``: a single limit is applied to all
requests matching this rule
- ``http-header``: key type takes the value of
the HTTP header configured in enforce-on-key-name as the key value
- ``xff-ip``: takes the original IP address
specified in the X-Forwarded-For header as the key
- ``http-cookie``: key type takes the value of
the HTTP cookie configured in enforce-on-key-name as the key value
- ``http-path``: key type takes the value of the
URL path in the request
- ``sni``: key type takes the value of the server
name indication from the TLS session of the HTTPS request
- ``region-code``: key type takes the value of
the region code from which the request originates
- ``tls-ja3-fingerprint``: key type takes the
value of JA3 TLS/SSL fingerprint if the client connects using HTTPS, HTTP/2 or
HTTP/3
- ``user-ip``: key type takes the IP address of
the originating client, which is resolved based on user-ip-request-headers
configured with the security policy
- ``tls-ja4-fingerprint``: key type takes the
value of JA4 TLS/SSL fingerprint if the client connects using HTTPS, HTTP/2 or
HTTP/3

Key names are only applicable to the following key types:

- http-header: The name of the HTTP header whose value is taken as the key value.
- http-cookie: The name of the HTTP cookie whose value is taken as the key value.

**--enforce-on-key-name**:
Determines the key name for the rate limit key. Applicable only for the
following rate limit key types:

- http-header: The name of the HTTP header whose value is taken as the key value.
- http-cookie: The name of the HTTP cookie whose value is taken as the key value.

**--exceed-action**:
Action to take when requests are above the given threshold. When a request is
denied, return the specified HTTP response code. When a request is redirected,
use the redirect options based on --exceed-redirect-type and
--exceed-redirect-target below. `EXCEED_ACTION` must be
one of: `deny-403`, `deny-404`, `deny-429`,
`deny-502`, `deny`, `redirect`.

**--exceed-redirect-target**:
URL target for the redirect action that is configured as the exceed action when
the redirect type is ``external-302``.

**--exceed-redirect-type**:
Type for the redirect action that is configured as the exceed action.
`EXCEED_REDIRECT_TYPE` must be one of:
`google-recaptcha`, `external-302`.

**--preview**:
If specified, the action will not be enforced.

**--rate-limit-threshold-count**:
Number of HTTP(S) requests for calculating the threshold for rate limiting
requests.

**--rate-limit-threshold-interval-sec**:
Interval over which the threshold for rate limiting requests is computed.

**--recaptcha-action-site-keys**:
A comma-separated list of site keys to be used during the validation of
reCAPTCHA action-tokens. The provided site keys need to be created from the
reCAPTCHA API under the same project where the security policy is created.

**--recaptcha-session-site-keys**:
A comma-separated list of site keys to be used during the validation of
reCAPTCHA session-tokens. The provided site keys need to be created from the
reCAPTCHA API under the same project where the security policy is created.

**--redirect-target**:
URL target for the redirect action. Must be specified if the redirect type is
``external-302``. Cannot be specified if the
redirect type is ``google-recaptcha``.

**--redirect-type**:
Type for the redirect action. Default to
``external-302`` if unspecified while
--redirect-target is given. `REDIRECT_TYPE` must be one
of: `google-recaptcha`, `external-302`.

**--region**:
Region of the security policy to add. If not specified, you might be prompted to
select a region (interactive mode only).
A list of regions can be fetched by running:

```
gcloud compute regions list
```

Overrides the default `compute/region` property value for this
command invocation.

**--request-headers-to-add**:
A comma-separated list of header names and header values to add to requests that
match this rule.

**--security-policy**:
The security policy that this rule belongs to.

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
gcloud alpha compute security-policies rules create
```

```
gcloud beta compute security-policies rules create
```