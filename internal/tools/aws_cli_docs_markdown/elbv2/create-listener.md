# create-listenerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/create-listener.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/create-listener.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elbv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/index.html#cli-aws-elbv2) ]

# create-listener

## Description

Creates a listener for the specified Application Load Balancer, Network Load Balancer, or Gateway Load Balancer.

For more information, see the following:

- [Listeners for your Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-listeners.html)
- [Listeners for your Network Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-listeners.html)
- [Listeners for your Gateway Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/gateway-listeners.html)

This operation is idempotent, which means that it completes at most one time. If you attempt to create multiple listeners with the same settings, each call succeeds.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/CreateListener)

## Synopsis

```
create-listener
--load-balancer-arn <value>
[--protocol <value>]
[--port <value>]
[--ssl-policy <value>]
[--certificates <value>]
--default-actions <value>
[--alpn-policy <value>]
[--tags <value>]
[--mutual-authentication <value>]
[--cli-input-json | --cli-input-yaml]
[--generate-cli-skeleton <value>]
[--debug]
[--endpoint-url <value>]
[--no-verify-ssl]
[--no-paginate]
[--output <value>]
[--query <value>]
[--profile <value>]
[--region <value>]
[--version <value>]
[--color <value>]
[--no-sign-request]
[--ca-bundle <value>]
[--cli-read-timeout <value>]
[--cli-connect-timeout <value>]
[--cli-binary-format <value>]
[--no-cli-pager]
[--cli-auto-prompt]
[--no-cli-auto-prompt]
```

## Options

`--load-balancer-arn` (string)

The Amazon Resource Name (ARN) of the load balancer.

`--protocol` (string)

The protocol for connections from clients to the load balancer. For Application Load Balancers, the supported protocols are HTTP and HTTPS. For Network Load Balancers, the supported protocols are TCP, TLS, UDP, and TCP_UDP. You canât specify the UDP or TCP_UDP protocol if dual-stack mode is enabled. You canât specify a protocol for a Gateway Load Balancer.

Possible values:

- `HTTP`
- `HTTPS`
- `TCP`
- `TLS`
- `UDP`
- `TCP_UDP`
- `GENEVE`

`--port` (integer)

The port on which the load balancer is listening. You canât specify a port for a Gateway Load Balancer.

`--ssl-policy` (string)

[HTTPS and TLS listeners] The security policy that defines which protocols and ciphers are supported.

For more information, see [Security policies](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/create-https-listener.html#describe-ssl-policies) in the *Application Load Balancers Guide* and [Security policies](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-tls-listener.html#describe-ssl-policies) in the *Network Load Balancers Guide* .

`--certificates` (list)

[HTTPS and TLS listeners] The default certificate for the listener. You must provide exactly one certificate. Set `CertificateArn` to the certificate ARN but do not set `IsDefault` .

(structure)

Information about an SSL server certificate.

CertificateArn -> (string)

The Amazon Resource Name (ARN) of the certificate.

IsDefault -> (boolean)

Indicates whether the certificate is the default certificate. Do not set this value when specifying a certificate as an input. This value is not included in the output when describing a listener, but is included when describing listener certificates.

Shorthand Syntax:

```
CertificateArn=string,IsDefault=boolean ...
```

JSON Syntax:

```
[
  {
    "CertificateArn": "string",
    "IsDefault": true|false
  }
  ...
]
```

`--default-actions` (list)

The actions for the default rule.

(structure)

Information about an action.

Each rule must include exactly one of the following types of actions: `forward` , `fixed-response` , or `redirect` , and it must be the last action to be performed.

Type -> (string)

The type of action.

TargetGroupArn -> (string)

The Amazon Resource Name (ARN) of the target group. Specify only when `Type` is `forward` and you want to route to a single target group. To route to one or more target groups, use `ForwardConfig` instead.

AuthenticateOidcConfig -> (structure)

[HTTPS listeners] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when `Type` is `authenticate-oidc` .

Issuer -> (string)

The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

AuthorizationEndpoint -> (string)

The authorization endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

TokenEndpoint -> (string)

The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

UserInfoEndpoint -> (string)

The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

ClientId -> (string)

The OAuth 2.0 client identifier.

ClientSecret -> (string)

The OAuth 2.0 client secret. This parameter is required if you are creating a rule. If you are modifying a rule, you can omit this parameter if you set `UseExistingClientSecret` to true.

SessionCookieName -> (string)

The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.

Scope -> (string)

The set of user claims to be requested from the IdP. The default is `openid` .

To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.

SessionTimeout -> (long)

The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).

AuthenticationRequestExtraParams -> (map)

The query parameters (up to 10) to include in the redirect request to the authorization endpoint.

key -> (string)

value -> (string)

OnUnauthenticatedRequest -> (string)

The behavior if the user is not authenticated. The following are possible values:

- deny- Return an HTTP 401 Unauthorized error.
- allow- Allow the request to be forwarded to the target.
- authenticate- Redirect the request to the IdP authorization endpoint. This is the default value.

UseExistingClientSecret -> (boolean)

Indicates whether to use the existing client secret when modifying a rule. If you are creating a rule, you can omit this parameter or set it to false.

AuthenticateCognitoConfig -> (structure)

[HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify only when `Type` is `authenticate-cognito` .

UserPoolArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

UserPoolClientId -> (string)

The ID of the Amazon Cognito user pool client.

UserPoolDomain -> (string)

The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

SessionCookieName -> (string)

The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.

Scope -> (string)

The set of user claims to be requested from the IdP. The default is `openid` .

To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.

SessionTimeout -> (long)

The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).

AuthenticationRequestExtraParams -> (map)

The query parameters (up to 10) to include in the redirect request to the authorization endpoint.

key -> (string)

value -> (string)

OnUnauthenticatedRequest -> (string)

The behavior if the user is not authenticated. The following are possible values:

- deny- Return an HTTP 401 Unauthorized error.
- allow- Allow the request to be forwarded to the target.
- authenticate- Redirect the request to the IdP authorization endpoint. This is the default value.

Order -> (integer)

The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first.

RedirectConfig -> (structure)

[Application Load Balancer] Information for creating a redirect action. Specify only when `Type` is `redirect` .

Protocol -> (string)

The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You canât redirect HTTPS to HTTP.

Port -> (string)

The port. You can specify a value from 1 to 65535 or #{port}.

Host -> (string)

The hostname. This component is not percent-encoded. The hostname can contain #{host}.

Path -> (string)

The absolute path, starting with the leading â/â. This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}.

Query -> (string)

The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading â?â, as it is automatically added. You can specify any of the reserved keywords.

StatusCode -> (string)

The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).

FixedResponseConfig -> (structure)

[Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when `Type` is `fixed-response` .

MessageBody -> (string)

The message.

StatusCode -> (string)

The HTTP response code (2XX, 4XX, or 5XX).

ContentType -> (string)

The content type.

Valid Values: text/plain | text/css | text/html | application/javascript | application/json

ForwardConfig -> (structure)

Information for creating an action that distributes requests among one or more target groups. For Network Load Balancers, you can specify a single target group. Specify only when `Type` is `forward` . If you specify both `ForwardConfig` and `TargetGroupArn` , you can specify only one target group using `ForwardConfig` and it must be the same target group specified in `TargetGroupArn` .

TargetGroups -> (list)

The target groups. For Network Load Balancers, you can specify a single target group.

(structure)

Information about how traffic will be distributed between multiple target groups in a forward rule.

TargetGroupArn -> (string)

The Amazon Resource Name (ARN) of the target group.

Weight -> (integer)

The weight. The range is 0 to 999.

TargetGroupStickinessConfig -> (structure)

The target group stickiness for the rule.

Enabled -> (boolean)

Indicates whether target group stickiness is enabled.

DurationSeconds -> (integer)

The time period, in seconds, during which requests from a client should be routed to the same target group. The range is 1-604800 seconds (7 days).

JSON Syntax:

```
[
  {
    "Type": "forward"|"authenticate-oidc"|"authenticate-cognito"|"redirect"|"fixed-response",
    "TargetGroupArn": "string",
    "AuthenticateOidcConfig": {
      "Issuer": "string",
      "AuthorizationEndpoint": "string",
      "TokenEndpoint": "string",
      "UserInfoEndpoint": "string",
      "ClientId": "string",
      "ClientSecret": "string",
      "SessionCookieName": "string",
      "Scope": "string",
      "SessionTimeout": long,
      "AuthenticationRequestExtraParams": {"string": "string"
        ...},
      "OnUnauthenticatedRequest": "deny"|"allow"|"authenticate",
      "UseExistingClientSecret": true|false
    },
    "AuthenticateCognitoConfig": {
      "UserPoolArn": "string",
      "UserPoolClientId": "string",
      "UserPoolDomain": "string",
      "SessionCookieName": "string",
      "Scope": "string",
      "SessionTimeout": long,
      "AuthenticationRequestExtraParams": {"string": "string"
        ...},
      "OnUnauthenticatedRequest": "deny"|"allow"|"authenticate"
    },
    "Order": integer,
    "RedirectConfig": {
      "Protocol": "string",
      "Port": "string",
      "Host": "string",
      "Path": "string",
      "Query": "string",
      "StatusCode": "HTTP_301"|"HTTP_302"
    },
    "FixedResponseConfig": {
      "MessageBody": "string",
      "StatusCode": "string",
      "ContentType": "string"
    },
    "ForwardConfig": {
      "TargetGroups": [
        {
          "TargetGroupArn": "string",
          "Weight": integer
        }
        ...
      ],
      "TargetGroupStickinessConfig": {
        "Enabled": true|false,
        "DurationSeconds": integer
      }
    }
  }
  ...
]
```

`--alpn-policy` (list)

[TLS listeners] The name of the Application-Layer Protocol Negotiation (ALPN) policy. You can specify one policy name. The following are the possible values:

- `HTTP1Only`
- `HTTP2Only`
- `HTTP2Optional`
- `HTTP2Preferred`
- `None`

For more information, see [ALPN policies](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-tls-listener.html#alpn-policies) in the *Network Load Balancers Guide* .

(string)

Syntax:

```
"string" "string" ...
```

`--tags` (list)

The tags to assign to the listener.

(structure)

Information about a tag.

Key -> (string)

The key of the tag.

Value -> (string)

The value of the tag.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--mutual-authentication` (structure)

The mutual authentication configuration information.

Mode -> (string)

The client certificate handling method. Options are `off` , `passthrough` or `verify` . The default value is `off` .

TrustStoreArn -> (string)

The Amazon Resource Name (ARN) of the trust store.

IgnoreClientCertificateExpiry -> (boolean)

Indicates whether expired client certificates are ignored.

TrustStoreAssociationStatus -> (string)

Indicates a shared trust stores association status.

AdvertiseTrustStoreCaNames -> (string)

Indicates whether trust store CA certificate names are advertised.

Shorthand Syntax:

```
Mode=string,TrustStoreArn=string,IgnoreClientCertificateExpiry=boolean,TrustStoreAssociationStatus=string,AdvertiseTrustStoreCaNames=string
```

JSON Syntax:

```
{
  "Mode": "string",
  "TrustStoreArn": "string",
  "IgnoreClientCertificateExpiry": true|false,
  "TrustStoreAssociationStatus": "active"|"removed",
  "AdvertiseTrustStoreCaNames": "on"|"off"
}
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--generate-cli-skeleton` (string)
Prints a JSON skeleton to standard output without sending an API request. If provided with no value or the value `input`, prints a sample input JSON that can be used as an argument for `--cli-input-json`. Similarly, if provided `yaml-input` it will print a sample input YAML that can be used with `--cli-input-yaml`. If provided with the value `output`, it validates the command inputs and returns a sample output JSON for that command. The generated JSON skeleton is not stable between versions of the AWS CLI and there are no backwards compatibility guarantees in the JSON skeleton generated.

## Global Options

`--debug` (boolean)

Turn on debug logging.

`--endpoint-url` (string)

Override commandâs default URL with the given URL.

`--no-verify-ssl` (boolean)

By default, the AWS CLI uses SSL when communicating with AWS services. For each SSL connection, the AWS CLI will verify SSL certificates. This option overrides the default behavior of verifying SSL certificates.

`--no-paginate` (boolean)

Disable automatic pagination. If automatic pagination is disabled, the AWS CLI will only make one call, for the first page of results.

`--output` (string)

The formatting style for command output.

- json
- text
- table
- yaml
- yaml-stream

`--query` (string)

A JMESPath query to use in filtering the response data.

`--profile` (string)

Use a specific profile from your credential file.

`--region` (string)

The region to use. Overrides config/env settings.

`--version` (string)

Display the version of this tool.

`--color` (string)

Turn on/off color output.

- on
- off
- auto

`--no-sign-request` (boolean)

Do not sign requests. Credentials will not be loaded if this argument is provided.

`--ca-bundle` (string)

The CA certificate bundle to use when verifying SSL certificates. Overrides config/env settings.

`--cli-read-timeout` (int)

The maximum socket read time in seconds. If the value is set to 0, the socket read will be blocking and not timeout. The default value is 60 seconds.

`--cli-connect-timeout` (int)

The maximum socket connect time in seconds. If the value is set to 0, the socket connect will be blocking and not timeout. The default value is 60 seconds.

`--cli-binary-format` (string)

The formatting style to be used for binary blobs. The default format is base64. The base64 format expects binary blobs to be provided as a base64 encoded string. The raw-in-base64-out format preserves compatibility with AWS CLI V1 behavior and binary values must be passed literally. When providing contents from a file that map to a binary blob `fileb://` will always be treated as binary and use the file contents directly regardless of the `cli-binary-format` setting. When using `file://` the file contents will need to properly formatted for the configured `cli-binary-format`.

- base64
- raw-in-base64-out

`--no-cli-pager` (boolean)

Disable cli pager for output.

`--cli-auto-prompt` (boolean)

Automatically prompt for CLI input parameters.

`--no-cli-auto-prompt` (boolean)

Disable automatically prompt for CLI input parameters.

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**Example 1: To create an HTTP listener**

The following `create-listener` example creates an HTTP listener for the specified Application Load Balancer that forwards requests to the specified target group.

```
aws elbv2 create-listener \
    --load-balancer-arn arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188 \
    --protocol HTTP \
    --port 80 \
    --default-actions Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067
```

For more information, see [Tutorial: Create an Application Load Balancer using the AWS CLI](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/tutorial-application-load-balancer-cli.html#create-load-balancer-aws-cli) in the *User Guide for Application Load Balancers*.

**Example 2: To create an HTTPS listener**

The following `create-listener` example creates an HTTPS listener for the specified Application Load Balancer that forwards requests to the specified target group. You must specify an SSL certificate for an HTTPS listener. You can create and manage certificates using AWS Certificate Manager (ACM). Alternatively, you can create a certificate using SSL/TLS tools, get the certificate signed by a certificate authority (CA), and upload the certificate to AWS Identity and Access Management (IAM).

```
aws elbv2 create-listener \
    --load-balancer-arn arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188 \
    --protocol HTTPS \
    --port 443 \
    --certificates CertificateArn=arn:aws:acm:us-west-2:123456789012:certificate/3dcb0a41-bd72-4774-9ad9-756919c40557 \
    --ssl-policy ELBSecurityPolicy-2016-08 \
    --default-actions Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067
```

For more information, see [Add an HTTPS listener](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/tutorial-application-load-balancer-cli.html#https-listener-aws-cli) in the *User Guide for Application Load Balancers*.

**Example 3: To create a TCP listener**

The following `create-listener` example creates a TCP listener for the specified Network Load Balancer that forwards requests to the specified target group.

```
aws elbv2 create-listener \
    --load-balancer-arn arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/net/my-network-load-balancer/5d1b75f4f1cee11e \
    --protocol TCP \
    --port 80 \
    --default-actions Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-tcp-targets/b6bba954d1361c78
```

For more information, see [Tutorial: Create a Network Load Balancer using the AWS CLI](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancer-cli.html#create-load-balancer-aws-cli) in the *User Guide for Network Load Balancers*.

**Example 4: To create a TLS listener**

The following `create-listener` example creates a TLS listener for the specified Network Load Balancer that forwards requests to the specified target group. You must specify an SSL certificate for a TLS listener.

```
aws elbv2 create-listener \
    --load-balancer-arn arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188 \
    --protocol TLS \
    --port 443 \
    --certificates CertificateArn=arn:aws:acm:us-west-2:123456789012:certificate/3dcb0a41-bd72-4774-9ad9-756919c40557 \
    --ssl-policy ELBSecurityPolicy-2016-08 \
    --default-actions Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067
```

For more information, see [TLS listeners for your Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/create-tls-listener.html) in the *User Guide for Network Load Balancers*.

**Example 5: To create a UDP listener**

The following `create-listener` example creates a UDP listener for the specified Network Load Balancer that forwards requests to the specified target group.

```
aws elbv2 create-listener \
    --load-balancer-arn arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/net/my-network-load-balancer/5d1b75f4f1cee11e \
    --protocol UDP \
    --port 53 \
    --default-actions Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-tcp-targets/b6bba954d1361c78
```

For more information, see [Tutorial: Create a Network Load Balancer using the AWS CLI](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancer-cli.html#create-load-balancer-aws-cli) in the *User Guide for Network Load Balancers*.

**Example 6: To create a listener for the specified gateway and forwarding**

The following `create-listener` example creates a listener for the specified Gateway Load Balancer that forwards requests to the specified target group.

```
aws elbv2 create-listener \
    --load-balancer-arn arn:aws:elasticloadbalancing:us-east-1:850631746142:loadbalancer/gwy/my-gateway-load-balancer/e0f9b3d5c7f7d3d6 \
    --default-actions Type=forward,TargetGroupArn=arn:aws:elasticloadbalancing:us-east-1:850631746142:targetgroup/my-glb-targets/007ca469fae3bb1615
```

Output:

```
{
    "Listeners": [
        {
            "ListenerArn": "arn:aws:elasticloadbalancing:us-east-1:850631746142:listener/gwy/my-agw-lb-example2/e0f9b3d5c7f7d3d6/afc127db15f925de",
            "LoadBalancerArn": "arn:aws:elasticloadbalancing:us-east-1:850631746142:loadbalancer/gwy/my-agw-lb-example2/e0f9b3d5c7f7d3d6",
            "DefaultActions": [
                {
                    "Type": "forward",
                    "TargetGroupArn": "arn:aws:elasticloadbalancing:us-east-1:850631746142:targetgroup/test-tg-agw-2/007ca469fae3bb1615",
                    "ForwardConfig": {
                        "TargetGroups": [
                            {
                                "TargetGroupArn": "arn:aws:elasticloadbalancing:us-east-1:850631746142:targetgroup/test-tg-agw-2/007ca469fae3bb1615"
                            }
                        ]
                    }
                }
            ]
        }
    ]
}
```

For more information, see [Getting started with Gateway Load Balancers using the AWS CLI](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/getting-started-cli.html) in the *User Guide for Gateway Load Balancers*.

## Output

Listeners -> (list)

Information about the listener.

(structure)

Information about a listener.

ListenerArn -> (string)

The Amazon Resource Name (ARN) of the listener.

LoadBalancerArn -> (string)

The Amazon Resource Name (ARN) of the load balancer.

Port -> (integer)

The port on which the load balancer is listening.

Protocol -> (string)

The protocol for connections from clients to the load balancer.

Certificates -> (list)

[HTTPS or TLS listener] The default certificate for the listener.

(structure)

Information about an SSL server certificate.

CertificateArn -> (string)

The Amazon Resource Name (ARN) of the certificate.

IsDefault -> (boolean)

Indicates whether the certificate is the default certificate. Do not set this value when specifying a certificate as an input. This value is not included in the output when describing a listener, but is included when describing listener certificates.

SslPolicy -> (string)

[HTTPS or TLS listener] The security policy that defines which protocols and ciphers are supported.

DefaultActions -> (list)

The default actions for the listener.

(structure)

Information about an action.

Each rule must include exactly one of the following types of actions: `forward` , `fixed-response` , or `redirect` , and it must be the last action to be performed.

Type -> (string)

The type of action.

TargetGroupArn -> (string)

The Amazon Resource Name (ARN) of the target group. Specify only when `Type` is `forward` and you want to route to a single target group. To route to one or more target groups, use `ForwardConfig` instead.

AuthenticateOidcConfig -> (structure)

[HTTPS listeners] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when `Type` is `authenticate-oidc` .

Issuer -> (string)

The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

AuthorizationEndpoint -> (string)

The authorization endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

TokenEndpoint -> (string)

The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

UserInfoEndpoint -> (string)

The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

ClientId -> (string)

The OAuth 2.0 client identifier.

ClientSecret -> (string)

The OAuth 2.0 client secret. This parameter is required if you are creating a rule. If you are modifying a rule, you can omit this parameter if you set `UseExistingClientSecret` to true.

SessionCookieName -> (string)

The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.

Scope -> (string)

The set of user claims to be requested from the IdP. The default is `openid` .

To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.

SessionTimeout -> (long)

The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).

AuthenticationRequestExtraParams -> (map)

The query parameters (up to 10) to include in the redirect request to the authorization endpoint.

key -> (string)

value -> (string)

OnUnauthenticatedRequest -> (string)

The behavior if the user is not authenticated. The following are possible values:

- deny- Return an HTTP 401 Unauthorized error.
- allow- Allow the request to be forwarded to the target.
- authenticate- Redirect the request to the IdP authorization endpoint. This is the default value.

UseExistingClientSecret -> (boolean)

Indicates whether to use the existing client secret when modifying a rule. If you are creating a rule, you can omit this parameter or set it to false.

AuthenticateCognitoConfig -> (structure)

[HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify only when `Type` is `authenticate-cognito` .

UserPoolArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

UserPoolClientId -> (string)

The ID of the Amazon Cognito user pool client.

UserPoolDomain -> (string)

The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

SessionCookieName -> (string)

The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.

Scope -> (string)

The set of user claims to be requested from the IdP. The default is `openid` .

To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.

SessionTimeout -> (long)

The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).

AuthenticationRequestExtraParams -> (map)

The query parameters (up to 10) to include in the redirect request to the authorization endpoint.

key -> (string)

value -> (string)

OnUnauthenticatedRequest -> (string)

The behavior if the user is not authenticated. The following are possible values:

- deny- Return an HTTP 401 Unauthorized error.
- allow- Allow the request to be forwarded to the target.
- authenticate- Redirect the request to the IdP authorization endpoint. This is the default value.

Order -> (integer)

The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first.

RedirectConfig -> (structure)

[Application Load Balancer] Information for creating a redirect action. Specify only when `Type` is `redirect` .

Protocol -> (string)

The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You canât redirect HTTPS to HTTP.

Port -> (string)

The port. You can specify a value from 1 to 65535 or #{port}.

Host -> (string)

The hostname. This component is not percent-encoded. The hostname can contain #{host}.

Path -> (string)

The absolute path, starting with the leading â/â. This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}.

Query -> (string)

The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading â?â, as it is automatically added. You can specify any of the reserved keywords.

StatusCode -> (string)

The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).

FixedResponseConfig -> (structure)

[Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when `Type` is `fixed-response` .

MessageBody -> (string)

The message.

StatusCode -> (string)

The HTTP response code (2XX, 4XX, or 5XX).

ContentType -> (string)

The content type.

Valid Values: text/plain | text/css | text/html | application/javascript | application/json

ForwardConfig -> (structure)

Information for creating an action that distributes requests among one or more target groups. For Network Load Balancers, you can specify a single target group. Specify only when `Type` is `forward` . If you specify both `ForwardConfig` and `TargetGroupArn` , you can specify only one target group using `ForwardConfig` and it must be the same target group specified in `TargetGroupArn` .

TargetGroups -> (list)

The target groups. For Network Load Balancers, you can specify a single target group.

(structure)

Information about how traffic will be distributed between multiple target groups in a forward rule.

TargetGroupArn -> (string)

The Amazon Resource Name (ARN) of the target group.

Weight -> (integer)

The weight. The range is 0 to 999.

TargetGroupStickinessConfig -> (structure)

The target group stickiness for the rule.

Enabled -> (boolean)

Indicates whether target group stickiness is enabled.

DurationSeconds -> (integer)

The time period, in seconds, during which requests from a client should be routed to the same target group. The range is 1-604800 seconds (7 days).

AlpnPolicy -> (list)

[TLS listener] The name of the Application-Layer Protocol Negotiation (ALPN) policy.

(string)

MutualAuthentication -> (structure)

The mutual authentication configuration information.

Mode -> (string)

The client certificate handling method. Options are `off` , `passthrough` or `verify` . The default value is `off` .

TrustStoreArn -> (string)

The Amazon Resource Name (ARN) of the trust store.

IgnoreClientCertificateExpiry -> (boolean)

Indicates whether expired client certificates are ignored.

TrustStoreAssociationStatus -> (string)

Indicates a shared trust stores association status.

AdvertiseTrustStoreCaNames -> (string)

Indicates whether trust store CA certificate names are advertised.